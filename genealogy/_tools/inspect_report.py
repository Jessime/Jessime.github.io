"""Inspect the source layout before making relationship decisions."""
import json
import re
from pathlib import Path
import fitz

START = re.compile(r"^(?P<dots>[.\u2026]*)\s*(?P<generation>[1-9])\s+(?P<text>.+)")


def extract(path):
    records, excluded = [], []
    with fitz.open(path) as doc:
        for page_number, page in enumerate(doc, 1):
            for block in page.get_text("rawdict")["blocks"]:
                for line in block.get("lines", []):
                    chars = [c for s in line["spans"] for c in s["chars"]]
                    text = "".join(c["c"] for c in chars).strip()
                    x, y, _, _ = line["bbox"]
                    if not text:
                        continue
                    x = next(c["bbox"][0] for c in chars if not c["c"].isspace())
                    if (text == str(page_number) and y > 755) or text.startswith("Outline Descendant Report") or text == "THE END":
                        excluded.append((page_number, text))
                        continue
                    match = START.match(text)
                    if match or text.startswith("+"):
                        records.append({
                            "id": f"p{len(records) + 1:04d}",
                            "generation": int(match["generation"]) if match else None,
                            "kind": "descendant" if match else "partner",
                            "text": match["text"] if match else text[1:].strip(),
                            "lines": [], "x": round(x, 2),
                        })
                    else:
                        if not records:
                            raise ValueError(f"Unattached text on page {page_number}: {text}")
                        records[-1]["text"] += " " + text
                    records[-1]["lines"].append({"page": page_number, "text": text, "x": round(x, 2), "y": round(y, 2)})
    return records, excluded


if __name__ == "__main__":
    records, excluded = extract(Path(__file__).with_name("genealogy.pdf"))
    Path("records-inspection.json").write_text(json.dumps(records, indent=2, ensure_ascii=False))
    stack = {}
    for i, r in enumerate(records):
        if r["generation"]:
            g = r["generation"]
            if g > 1 and g-1 not in stack:
                print("GENERATION GAP", r)
            stack = {k: v for k, v in stack.items() if k < g}
            stack[g] = r
            dots = len(re.match(r"^\.*", r["lines"][0]["text"])[0])
            if dots and dots != 3*(g-1):
                print("DOT MISMATCH", r["id"], r["text"], dots)
        else:
            g = max(stack)
            expected = 82.8 + (g-1)*8.65
            if abs(expected-r["x"]) > 3:
                print("\nSPOUSE INDENT", r["id"], "PAGE", r["lines"][0]["page"], "x",r["x"], "expected",round(expected,1))
                for prev in records[max(0,i-2):i+2]:
                    print(prev["id"],prev["generation"],prev["text"])
                print("ACTIVE", {k:v["text"].split(' b:')[0] for k,v in stack.items()})
    print("\nTOTAL", len(records), "EXCLUDED", len(excluded), "DESCENDANTS", sum(r['kind']=='descendant' for r in records))
