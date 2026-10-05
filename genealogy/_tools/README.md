# Rebuild the family archive

Run these commands from the `genealogy/` folder. The website itself needs no dependencies.

```sh
python3 -m venv _tools/.venv
_tools/.venv/bin/python -m pip install -r _tools/requirements.txt
_tools/.venv/bin/python _tools/build_genealogy.py
(cd _tools && .venv/bin/python -m unittest -v test_genealogy)
_tools/.venv/bin/python _tools/check_browser.py
```

The browser check uses a locally installed Google Chrome. It starts and stops its own local HTTP server. The parser reads `source.pdf` and rewrites `data.js`, `data.json`, and `_tools/validation-report.json`. To convert another location, pass `--pdf PATH --output DIRECTORY` to the builder.

The report contains 2,144 records across 49 pages (1,492 numbered descendants and 652 partners). Names repeated in the source are kept as separate records. Every extracted nonempty line is accounted for; only the title, footers, and THE END are excluded.

Generation numbers determine the primary outline. The builder documents 36 manually reviewed spouse returns by exact source-name prefix, and deliberately fails if a future report changes those names or their context. Consecutive partners before children leave the other parent unresolved. 35 records have visible review notes, covering possible relationships, unlabeled dates, and questionable parent ages. Details are in `validation-report.json`. Al Leo's connection to Janine and Clara W Bussan-Tesmer's connection to Francis Louis Steffen are marked for verification, and Rebekah Avery's partner is not asserted.

No dates or spellings are corrected. Connections reflect the family report, not independently verified biological parentage. The original extracted entry is available on every profile, alongside the exact PDF page.

The files in this directory are excluded from the published site by Jekyll's default treatment of underscore-prefixed folders. Publish the parent `genealogy/` folder through the repository's usual GitHub Pages workflow to serve `/genealogy/`. No Jekyll configuration changes are necessary. Nothing has been pushed automatically.

Record IDs use source order; a new report with inserted records will need an ID migration if existing shared links must be retained.
