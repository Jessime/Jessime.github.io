# 2026 design previews

Open any of these files directly in a browser. No build, server, or internet connection is needed to render the previews.

- [02 — Working Library](working-library.html): Literata and Public Sans; ivory and oxblood by day, warm charcoal and rose by night.
- [04 — Clay & Paper](clay-and-paper.html): Source Sans 3; sand, cream, and terracotta by day, umber and peach by night.
- [05 — Under Glass](under-glass.html): Newsreader and Public Sans; pale sage and plum by day, deep forest, lichen, and lilac by night.

The top bar links between designs. Each page follows the system's color preference initially. Use the theme button to choose light or dark; the choice is saved when browser storage is available. When served from the same origin, the preference is shared between pages and tabs. Browsers may isolate storage per file when opening HTML directly.

The HTML is identical across all three previews except for the design stylesheet link. `shared.css` supplies fonts, common layout, responsive behavior, and accessibility styles; each named stylesheet supplies its visual treatment and paired light/dark color tokens. `theme.js` handles the reading preference and highlights the current preview. JavaScript is not needed to read the pages; without it, the system color preference still applies and the toggle is hidden.

The shared demo includes an adapted bioinformatics interview excerpt, code, a table, a Stockholm photograph, selected writing, and projects. The added demo prose and examples are identified on the page. Story and project links lead to the existing public website; section navigation stays within the preview.

All images and fonts are local under `assets/`. The fractal tree and Stockholm photo are copies of existing site assets. Fonts were downloaded from Google Fonts, with their SIL Open Font License files included in `assets/fonts/`.

The folder is an isolated static prototype. It does not change the Jekyll theme, templates, configuration, or existing posts.
