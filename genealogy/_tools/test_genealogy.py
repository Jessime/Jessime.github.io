"""Regression checks for the actual report's difficult layout cases."""
from collections import Counter
import unittest
import fitz
from build_genealogy import SOURCE, build


class ReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.audit = build(SOURCE)
        cls.people = cls.data['people']
        cls.by_id = {p['id']: p for p in cls.people}

    def person(self, prefix):
        matches = [p for p in self.people if p['name'].startswith(prefix)]
        self.assertEqual(len(matches), 1, prefix)
        return matches[0]

    def test_every_nonempty_pdf_line_is_preserved_once(self):
        original = Counter()
        with fitz.open(SOURCE) as doc:
            for n, page in enumerate(doc, 1):
                for block in page.get_text('dict')['blocks']:
                    for line in block.get('lines', []):
                        text = ''.join(s['text'] for s in line['spans']).strip()
                        if text:
                            original[(n, text)] += 1
        preserved = Counter((l['page'], l['text']) for p in self.people for l in p['source']['lines'])
        preserved.update(tuple(l) for l in self.data['meta']['excludedLines'])
        self.assertEqual(original, preserved)
        self.assertEqual(self.data['meta']['people'], 2144)
        self.assertEqual(self.data['meta']['descendants'], 1492)
        self.assertEqual(self.data['meta']['partners'], 652)
        self.assertEqual(len(self.audit), 36)

    def test_unicode_ellipses_are_people_not_continuations(self):
        for prefix in ['Agnes Marie Thi Huong Gillen', 'Shelby Rose Bell-Myers', 'Hope Marie Hansen', 'Emme Louise Van Wyngarden', 'Natalee Esa Mageo', 'Bennett James Deckert', 'Harper Mary Jacobs', 'Oliver Bennett White']:
            self.assertEqual(self.person(prefix)['kind'], 'descendant')
        self.assertEqual(self.person('RyLee Hollis Bell')['outlineParent'], self.person('Shelby Rose Bell-Myers')['id'])

    def test_returns_to_previous_generations_and_parent_groups(self):
        for a, b in [('Rhonda Jo Ginsbach-Richards', 'Jerome "Jerry" Ginsbach'), ('Charles Richard Kirk', 'Linda Kay Murray-Kirk'), ('Rita Kay VanderWal', 'Stephen Wayne Rogers'), ('Cory Van Wyngarden', 'Sara Anne Sparks Van Wyngarden'), ('Will Edward Chenoweth', 'Dolores Erlynn Kennedy-Johnson')]:
            self.assertEqual(self.person(a)['partners'], [self.person(b)['id']])
        for child, parents in [('Jessime Murray Kirk', ['Linda Kay Murray-Kirk', 'Jilani E. Trabelsi']), ('Mahlon Murray Kirk', ['Linda Kay Murray-Kirk', 'Charles Richard Kirk']), ('Connor Jacob Singrey', ['Shirley Jean Geraets-Thompson', 'Joel Edwin Singrey']), ('Max Michael Thompson', ['Shirley Jean Geraets-Thompson', 'David Andrew Thompson'])]:
            self.assertEqual(self.person(child)['parents'], [self.person(p)['id'] for p in parents])

    def test_page_breaks_and_year_only_continuations(self):
        p = self.person('Joseph E Geraets')
        self.assertEqual(p['source']['pages'], [2, 3])
        self.assertIn('07 Sep 2009', next(e['text'] for e in p['events'] if e['type'] == 'Death'))
        matches = [p for p in self.people if any(l['page'] == 22 and l['text'] == '1964' for l in p['source']['lines'])]
        self.assertEqual(len(matches), 1)
        self.assertIn('1964', matches[0]['source']['text'])

    def test_uncertainty_is_not_silently_resolved(self):
        self.assertIn('Adoption noted', self.person('Jerome "Jerry" Ginsbach')['tags'])
        p = self.person('Rebekah Avery')
        self.assertFalse(p['partners'])
        self.assertEqual(len(p['possiblePartners']), 2)
        p = self.person('Jeffrey King Barrows')
        self.assertEqual(len(p['parents']), 1)
        self.assertEqual(len(p['possibleParents']), 2)
        p = self.person('Kyler Levi Klein')
        self.assertIn('1968', p['events'][0]['text'])
        self.assertTrue(any(i['code'] == 'parent-age' for i in p['issues']))
        self.assertEqual(self.person('Agnes Marie Thi Huong Gillen')['events'][0]['type'], 'Unlabeled detail')
        p = self.person('Clara W Bussan-Tesmer')
        self.assertEqual(p['partners'], [self.person('Francis Louis "Frank" Steffen')['id']])
        self.assertTrue(p['issues'])
        self.assertTrue(any(i['code'] == 'marriage-date' for i in self.person('Wanda Overstreet-Barrows')['issues']))

    def test_duplicate_names_remain_separate(self):
        self.assertGreaterEqual(len([p for p in self.people if p['name'] == 'Maria Steffen']), 2)


if __name__ == '__main__':
    unittest.main()
