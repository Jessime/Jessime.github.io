"""Rebuild the static family browser's data from the original PDF.

No OCR, date guessing, spelling correction, or identity deduplication is used.
The numbered outline establishes the primary family line; partners require
layout review because the author sometimes returned to an earlier generation.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil

from inspect_report import extract

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE.parent if HERE.name == '_tools' else Path('/Users/jessime/Code/me/Jessime.github.io/genealogy')
SOURCE = HERE/'genealogy.pdf' if (HERE/'genealogy.pdf').exists() else HERE.parent/'source.pdf'
FIELD = re.compile(r'\b([bmd]):\s*')

# Reviewed against the outline's position, generation, names, and dates.
# Exact name prefixes deliberately fail if a revised PDF makes them ambiguous.
RETURNING_PARTNERS = {
    'Rhonda Jo Ginsbach-Richards': 'Jerome "Jerry" Ginsbach',
    'David Andrew Thompson': 'Shirley Jean Geraets-Thompson',
    'Kelly Jean Beede-Redenius': 'John Roger Redenius Sr',
    'Adrienne Sullivan-Clark': 'Zachary Steffen Clark',
    'Susan Pieria-Steffen': 'John Wayne "Jack" Steffen Jr',
    'Will Edward Chenoweth': 'Dolores Erlynn Kennedy-Johnson',
    'John J Merrifeld': 'Katie Marie Matulonis',
    'Bradin Robert Dockall b:': 'Michelle Rene Young',
    'Mark LaValle': 'Monica Suzanne Young',
    'Cory Van Wyngarden': 'Sara Anne Sparks Van Wyngarden',
    'Gretchen Iris "Iris" Martin-Steffen': 'Francis Aloysious "Frank" Steffen',
    'Fred Hilley': 'Miriam “Coleen” Steffen-Hilley-Turgeon',
    'Al Leo': 'Janine Hilley-Speiler-Leo',
    'Wanda Overstreet-Barrows': 'Jeffrey King Barrows',
    'Gregory Morgan Vetter': 'Patricia Ann "Pam" Murray-Vetter',
    'Charles Richard Kirk': 'Linda Kay Murray-Kirk',
    'Angela Rae Chiasson-Murray': 'Andrew James "Andy" Murray',
    'Cindy Lou Hohn-Pulver': 'Shawn Michael Pulver',
    'Heather Forbes-Metzger': 'William Charles Metzger',
    'Debbie (**) -Welter': 'Matthew James Welter',
    'Lana Marie Kitsch-Hood': 'Ronald Frederick Hood',
    'Rita Kay VanderWal': 'Stephen Wayne Rogers',
    'Laurie Williams-Rogers': 'Stephen Wayne Rogers',
    'Elizabeth Desiree LeVan-Rogers': 'Mark James Rogers',
    'Darin McWilliams-Cozad': 'Allan Ray Cozad',
    'Karen Michelle West-Biegger': 'James Alan Biegger',
    'Melissa (**) -Hein': 'Kevin Darnell Hein',
    'Danny Neil Branson': 'Donna Lee Roby -Branson',
    'Debra Crisp-Page': 'Richard Lee Page',
    'Mildred Jones-Page': 'Richard Lee Page',
    'Sally Neal-Barclay': 'Michael Allan Barclay Sr',
    'Debra McPeak': 'Michael Allan Barclay Sr',
    'William Lester Schwartz': 'Molly Jane McAreavy-Schwartz',
    'Chris White b:': 'June Marie Steffen-Winske',
    'Stacy Tod Butson': 'Jona Marie Withrow-Austin',
    'Clara W Bussan-Tesmer': 'Francis Louis "Frank" Steffen',
}


def warn(person, code, message):
    person['issues'].append({'code': code, 'message': message})


def parse_fields(record):
    text = re.sub(r'\s+', ' ', record['text']).strip()
    markers = list(FIELD.finditer(text))
    heading = text[:markers[0].start()].rstrip(' ,') if markers else text
    # Relationship labels are retained as badges, with exact wording in source.
    name = re.split(r'/divorced|\s*\((?:not married|stepchild|stepson|stepdaughter|adopted)\)|\s*[“"]adopted[”"]', heading, maxsplit=1)[0].strip()
    if '(adopted)' in heading:
        name = re.sub(r'\s*\(adopted\)\s*', ' ', heading).strip()
    events = []
    for i, marker in enumerate(markers):
        end = markers[i+1].start() if i+1 < len(markers) else len(text)
        events.append({'type': {'b': 'Birth', 'm': 'Marriage', 'd': 'Death'}[marker[1]], 'text': text[marker.end():end].strip(' ,')})
    person = {
        'id': record['id'], 'name': name, 'kind': record['kind'],
        'generation': record['generation'], 'events': events,
        'parents': [], 'partners': [], 'children': [], 'outlineParent': None,
        'possibleParents': [], 'possiblePartners': [], 'issues': [], 'interpretation': [],
        'tags': [label for pattern, label in [(r'\badopted\b', 'Adoption noted'), (r'\bstep(?:child|son|daughter)\b', 'Stepchild'), (r'\bdivorced\b', 'Divorce noted'), (r'\bannulled\b', 'Annulment noted'), (r'not married', 'Not married')] if re.search(pattern, text, re.I)],
        'source': {'pages': sorted({l['page'] for l in record['lines']}), 'text': '\n'.join(l['text'] for l in record['lines']), 'lines': record['lines']},
    }
    if not markers and re.search(r'\d{4}', text):
        if text.startswith('Agnes Marie Thi Huong Gillen'):
            person['name'] = 'Agnes Marie Thi Huong Gillen'
            person['events'] = [{'type': 'Unlabeled detail', 'text': text[len(person['name']):].strip()}]
        elif text.startswith('Elizabeth in 2018'):
            person['name'] = 'Elizabeth'
            person['events'] = [{'type': 'Unlabeled detail', 'text': text[len('Elizabeth'):].strip()}]
        warn(person, 'unlabeled-detail', 'The report gives a date without an event label; its meaning has not been assumed.')
    return person


def year(person, event):
    value = next((e['text'] for e in person['events'] if e['type'] == event), '')
    match = re.match(r'(?:(?:\d{1,2}\s+)?[A-Za-z]+\s+)?((?:17|18|19|20)\d{2})\b', value)
    return int(match[1]) if match else None


def build(source):
    records, excluded = extract(source)
    people = [parse_fields(r) for r in records]
    by_id = {p['id']: p for p in people}

    def unique(prefix):
        matches = [r for r in records if r['text'].startswith(prefix)]
        assert len(matches) == 1, (prefix, len(matches))
        return matches[0]['id']

    overrides = {unique(a): unique(b) for a, b in RETURNING_PARTNERS.items()}
    stack, active_partners, last_partner_owner = {}, {}, None
    audit = []
    for r, p in zip(records, people):
        if p['kind'] == 'descendant':
            g = p['generation']
            if g > 1:
                assert g-1 in stack, f"Missing generation before {p['name']}"
                parent = by_id[stack[g-1]]
                p['outlineParent'] = parent['id']
                p['parents'].append(parent['id'])
                partners = active_partners.get(g-1, [])
                if len(partners) == 1:
                    p['parents'].extend(partners)
                elif len(partners) > 1:
                    p['possibleParents'] = partners[:]
                    warn(p, 'ambiguous-parent', 'Multiple partners precede this child in the report. The other parent is unresolved; possible connections are listed separately.')
                for parent_id in p['parents']:
                    by_id[parent_id]['children'].append(p['id'])
            stack = {k: v for k, v in stack.items() if k < g}
            active_partners = {k: v for k, v in active_partners.items() if k < g}
            stack[g] = p['id']
            active_partners[g] = []
            last_partner_owner = None
        else:
            owner_id = overrides.get(p['id'], stack[max(stack)])
            if p['name'] == 'Rebekah Avery':
                # The end of this branch contains no dates or identifying text.
                p['possiblePartners'] = [stack[7], stack[8]]
                p['generation'] = None
                warn(p, 'ambiguous-partner', 'The position could refer to Michael David Severson or Andrew Michael Severson. No partner link has been asserted.')
                for candidate in p['possiblePartners']:
                    by_id[candidate]['possiblePartners'].append(p['id'])
                    warn(by_id[candidate], 'ambiguous-partner', 'Rebekah Avery appears at the end of this branch, but the report does not clearly identify her partner.')
                last_partner_owner = None
                continue
            owner = by_id[owner_id]
            g = owner['generation']
            assert stack.get(g) == owner_id, f"Override not in active lineage: {p['name']}"
            p['generation'] = g
            p['partners'].append(owner_id)
            owner['partners'].append(p['id'])
            if last_partner_owner == owner_id:
                active_partners[g].append(p['id'])
            else:
                active_partners[g] = [p['id']]
            last_partner_owner = owner_id
            stack = {k: v for k, v in stack.items() if k <= g}
            active_partners = {k: v for k, v in active_partners.items() if k <= g}
            if p['id'] in overrides:
                note = f"Partner linked to {owner['name']} by review of the surrounding branch; this entry returns to an earlier generation."
                p['interpretation'].append(note)
                audit.append({'person': p['id'], 'partner': owner_id, 'page': p['source']['pages'][0], 'reason': note})
                if p['name'] == 'Al Leo':
                    warn(p, 'inconsistent-indent', 'The indentation points one generation too high. The connection to Janine follows her listed surname (Hilley-Speiler-Leo) and the surrounding branch; please verify with family records.')
                    warn(owner, 'inconsistent-indent', 'Al Leo is linked here from the surname and surrounding branch; his indentation is inconsistent. Please verify with family records.')
                if p['name'] == 'Clara W Bussan-Tesmer':
                    note = 'Clara’s entry is indented beside a descendant born in 2013, although her marriage is dated 1948. The branch ending and dates suggest Francis Louis "Frank" Steffen (1897–1988), whose first listed wife died in 1943. This interpreted connection needs verification.'
                    warn(p, 'inconsistent-indent', note)
                    warn(owner, 'inconsistent-indent', note)
    # Preserve questionable dates, but surface them instead of silently fixing.
    for p in people:
        birth, death = year(p, 'Birth'), year(p, 'Death')
        if birth and death and death < birth:
            warn(p, 'date-order', 'The reported death year precedes the birth year. Both are preserved as printed.')
        for parent_id in p['parents']:
            parent = by_id[parent_id]
            py = year(parent, 'Birth')
            if birth and py and not 12 <= birth-py <= 70:
                warn(p, 'parent-age', f"The reported birth years put {parent['name']} at age {birth-py} when this person was born. This may be a date error or a step/adoptive relationship; the report is preserved.")
        if p['kind'] == 'partner' and p['partners']:
            partner = by_id[p['partners'][0]]
            marriage = year(p, 'Marriage')
            for member in (p, partner):
                born, died = year(member, 'Birth'), year(member, 'Death')
                if marriage and born and marriage-born < 13:
                    warn(p, 'marriage-age', f"The reported dates put {member['name']} at age {marriage-born} at this marriage. The dates are preserved and need verification.")
                if marriage and died and marriage > died:
                    warn(p, 'marriage-date', f"The marriage year ({marriage}) follows the reported death of {member['name']} ({died}). The dates are preserved and need verification.")
    counts = Counter(p['kind'] for p in people)
    data = {
        'title': 'The Steffen family', 'root': people[0]['id'],
        'meta': {'people': len(people), 'descendants': counts['descendant'], 'partners': counts['partner'], 'generations': max(p['generation'] or 0 for p in people), 'pages': 49, 'sourceFile': 'source.pdf', 'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'reviewCount': sum(bool(p['issues']) for p in people), 'sourceLines': sum(len(p['source']['lines']) for p in people), 'excludedLines': excluded, 'reviewedPartnerReturns': len(audit)},
        'people': people,
    }
    validate(data)
    return data, audit


def validate(data):
    people = {p['id']: p for p in data['people']}
    assert len(people) == len(data['people'])
    for p in people.values():
        assert p['name'] and p['source']['text'] and p['source']['pages']
        assert not re.search(r'[.…]{3,}\s*[1-9]\s', p['name']), p['name']
        for pid in p['parents']:
            assert p['id'] in people[pid]['children']
            assert people[pid]['generation'] + 1 == p['generation']
        for pid in p['partners']:
            assert p['id'] in people[pid]['partners']
            assert people[pid]['generation'] == p['generation']
        chain, current = set(), p
        while current['outlineParent']:
            assert current['id'] not in chain
            chain.add(current['id'])
            current = people[current['outlineParent']]
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', type=Path, default=SOURCE)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data, audit = build(args.pdf)
    args.output.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    (args.output/'data.json').write_text(payload + '\n')
    (args.output/'data.js').write_text('window.GENEALOGY = ' + payload + ';\n')
    if args.pdf.resolve() != (args.output/'source.pdf').resolve():
        shutil.copy2(args.pdf, args.output/'source.pdf')
    report = {'summary': data['meta'], 'reviewedPartnerReturns': audit, 'issues': [{'id': p['id'], 'name': p['name'], 'pages': p['source']['pages'], 'issues': p['issues']} for p in data['people'] if p['issues']]}
    (HERE/'validation-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(data['meta'], indent=2))


if __name__ == '__main__':
    main()
