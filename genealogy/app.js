/* A dependency-free browser: works on GitHub Pages and directly from disk. */
(() => {
  'use strict';
  const data = window.GENEALOGY;
  if (!data) {
    document.getElementById('profile').textContent = 'The family data could not be loaded. Please reload, or open the original report above.';
    return;
  }
  const $ = id => document.getElementById(id);
  const people = new Map(data.people.map(p => [p.id, p]));
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
  const normalize = text => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, ' ').trim();
  const searchable = new Map(data.people.map(p => [p.id, normalize(p.name + ' ' + p.source.text)]));
  const children = new Map(data.people.filter(p => p.kind === 'descendant').map(p => [p.id, p.children.filter(id => people.get(id).outlineParent === p.id)]));
  const possibleChildren = new Map(data.people.map(p => [p.id, []]));
  data.people.forEach(p => p.possibleParents.forEach(id => possibleChildren.get(id).push(p.id)));
  const state = {selected: data.root, view: 'directory', limit: 60, query: '', generation: '', review: false, sort: 'name'};
  let treeBuilt = false;
  const birthYear = p => {
    const birth = p.events.find(e => e.type === 'Birth')?.text || '';
    return birth.match(/^(?:(?:\d{1,2}\s+)?[A-Za-z]+\s+)?((?:17|18|19|20)\d{2})\b/)?.[1] || '';
  };
  const eventYear = (p, type) => (p.events.find(e => e.type === type)?.text || '').match(/^(?:(?:\d{1,2}\s+)?[A-Za-z]+\s+)?((?:17|18|19|20)\d{2})\b/)?.[1] || '';
  function lifespan(p) {
    const b = birthYear(p), d = eventYear(p, 'Death');
    if (b && d) return `${b}–${d}`;
    if (b) return `Born ${b}`;
    if (d) return `Died ${d}`;
    return 'Dates not recorded';
  }
  const pageLabel = p => `Page${p.source.pages.length > 1 ? 's' : ''} ${p.source.pages.join('–')}`;
  const link = (p, label = p.name) => `<a href="#${esc(p.id)}" data-person="${esc(p.id)}">${esc(label)}</a>`;
  function cards(ids) {
    return `<div class="relatives">${ids.map(id => {
      const p = people.get(id);
      return `<a class="relative-card" href="#${p.id}" data-person="${p.id}"><span class="relative-name">${esc(p.name)}${p.issues.length ? '<span class="review-dot" aria-label="Has a review note"></span>' : ''}</span><span class="relative-meta">${esc(lifespan(p))}${p.tags.includes('Adoption noted') ? ' · Adoption noted' : ''}${p.tags.includes('Stepchild') ? ' · Stepchild' : ''}</span></a>`;
    }).join('')}</div>`;
  }
  function section(title, ids, empty = '') {
    return `<section class="record-section"><div class="section-heading"><h3>${title}</h3>${ids.length ? `<span>${ids.length}</span>` : ''}</div>${ids.length ? cards(ids) : `<p class="missing">${empty}</p>`}</section>`;
  }
  function ancestors(p) {
    const result = [];
    let node = p.kind === 'partner' && p.partners.length ? people.get(p.partners[0]) : p;
    if (node !== p) result.unshift(node);
    while (node.outlineParent) {
      node = people.get(node.outlineParent);
      result.unshift(node);
    }
    return result;
  }
  function renderProfile() {
    const p = people.get(state.selected);
    document.title = `${p.name} · Steffen family archive`;
    const chain = ancestors(p);
    const siblings = p.outlineParent ? people.get(p.outlineParent).children.filter(id => id !== p.id) : [];
    const tags = [...p.tags.map(t => `<span class="tag">${esc(t)}</span>`), ...(p.issues.length ? ['<span class="tag review">Review note</span>'] : [])].join('');
    const generationLabel = p.generation ? `Generation ${p.generation} · ${p.kind === 'partner' ? 'Partner' : 'Descendant'}` : 'Partner · Connection unresolved';
    $('profile').innerHTML = `<header class="profile-top"><div class="profile-label"><p class="eyebrow">${generationLabel}</p><button class="copy-link" id="copy-link" type="button">Copy link ↗</button></div><h2>${esc(p.name)}</h2><p class="lifespan">${esc(lifespan(p))} <span aria-hidden="true">·</span> ${esc(pageLabel(p))}</p>${tags ? `<div class="tag-row">${tags}</div>` : ''}</header>
      <div class="profile-body">
        ${chain.length ? `<p class="lineage-label">${p.kind === 'partner' ? 'Connected through' : 'Family line'}</p><nav class="lineage" aria-label="Family line">${chain.map(a => link(a)).join('<span aria-hidden="true">›</span>')}</nav>` : ''}
        ${p.issues.length ? `<aside class="review-notes"><h3>Review note</h3>${p.issues.map(i => `<p>${esc(i.message)}</p>`).join('')}</aside>` : ''}
        <section class="record-section"><div class="section-heading"><h3>Events</h3></div>${p.events.length ? `<dl class="events">${p.events.map(e => `<div class="event"><dt>${esc(e.type)}</dt><dd>${esc(e.text || 'Not specified')}</dd></div>`).join('')}</dl>` : '<p class="missing">No events recorded.</p>'}</section>
        ${section('Parents in the report', p.parents, p.id === data.root ? 'Report starts here.' : 'Not recorded.')}
        ${p.possibleParents.length ? section('Other parent · unresolved', p.possibleParents) : ''}
        ${section('Partners', p.partners, p.possiblePartners.length ? 'Unresolved; see possible connections below.' : 'Not recorded.')}
        ${p.possiblePartners.length ? section('Possible partner connections', p.possiblePartners) : ''}
        ${section('Children in the report', p.children, possibleChildren.get(p.id).length ? 'Parentage unresolved; see possible children below.' : 'Not recorded.')}
        ${possibleChildren.get(p.id).length ? section('Possible children · unresolved', possibleChildren.get(p.id)) : ''}
        ${siblings.length ? `<details class="siblings"><summary>Siblings in this branch (${siblings.length})</summary>${cards(siblings)}</details>` : ''}
        <section class="source-section"><div class="source-head"><h3>Source</h3><a href="source.pdf#page=${p.source.pages[0]}" target="_blank" rel="noopener">${esc(pageLabel(p))} in the PDF ↗</a></div><details id="original-entry"><summary>Original entry</summary><pre>${esc(p.source.text)}</pre></details>${p.interpretation.map(t => `<p class="interpretation">${esc(t)}</p>`).join('')}</section>
      </div>`;
    $('copy-link').addEventListener('click', async () => {
      const url = new URL(location.href); url.search = ''; url.hash = p.id;
      try {
        await navigator.clipboard.writeText(url.href);
        $('copy-link').textContent = 'Link copied ✓';
        $('announcement').textContent = 'Link copied to clipboard.';
      } catch {
        let input = $('copy-fallback');
        if (!input) {
          input = document.createElement('input'); input.id = 'copy-fallback'; input.className = 'copy-fallback'; input.readOnly = true; input.setAttribute('aria-label', 'Shareable link — select and copy');
          document.querySelector('.profile-top').append(input);
        }
        input.value = url.href; input.focus(); input.select();
        $('announcement').textContent = 'Copy the selected link.';
      }
    });
    $('announcement').textContent = `Showing ${p.name}.`;
    document.querySelectorAll('.tree-node.is-selected').forEach(el => el.classList.remove('is-selected'));
    document.querySelector(`[data-tree-id="${p.id}"]`)?.classList.add('is-selected');
  }
  function updateURL() {
    const url = new URL(location.href);
    for (const [key, value] of Object.entries({q:state.query, gen:state.generation, review:state.review?'1':'', sort:state.sort==='name'?'':state.sort})) {
      if (value) url.searchParams.set(key, value); else url.searchParams.delete(key);
    }
    history.replaceState(null, '', url);
  }
  function renderResults() {
    const tokens = normalize(state.query).split(' ').filter(Boolean);
    const filtered = data.people.filter(p => (!state.generation || p.generation === Number(state.generation)) && (!state.review || p.issues.length) && tokens.every(t => searchable.get(p.id).includes(t)));
    filtered.sort((a, b) => {
      if (state.sort === 'report') return a.id.localeCompare(b.id);
      if (state.sort === 'birth') return Number(birthYear(a) || 9999) - Number(birthYear(b) || 9999) || a.name.localeCompare(b.name);
      return a.name.localeCompare(b.name);
    });
    $('result-count').textContent = `${filtered.length.toLocaleString()} ${filtered.length === 1 ? 'person' : 'people'}${state.query || state.generation || state.review ? ' found' : ' in the archive'}`;
    $('results').innerHTML = filtered.length ? filtered.slice(0, state.limit).map(p => `<button type="button" class="result${p.id === state.selected ? ' selected' : ''}" data-person="${p.id}"${p.id === state.selected ? ' aria-current="true"' : ''}><span class="result-name">${esc(p.name)}${p.issues.length ? '<span class="review-dot" aria-label="Has a review note"></span>' : ''}</span><span class="result-meta">${esc(lifespan(p))} · ${p.generation ? `Gen ${p.generation}` : 'Unresolved'} · p. ${p.source.pages[0]}</span></button>`).join('') : '<p class="empty">No matching records.<br>Try a shorter name, another spelling, or reset the filters.</p>';
    $('load-more').hidden = filtered.length <= state.limit;
    $('load-more').textContent = `Show ${Math.min(60, filtered.length-state.limit)} more people`;
    $('clear-search').hidden = !state.query;
  }
  function select(id, navigate = true, focus = false) {
    if (!people.has(id)) return;
    state.selected = id;
    if (navigate && location.hash !== '#' + id) history.pushState(null, '', '#' + id);
    renderProfile(); renderResults();
    if (focus) {
      $('profile').focus({preventScroll:true});
      if (matchMedia('(max-width:760px)').matches || $('profile').getBoundingClientRect().top < 0) $('profile').scrollIntoView({block:'start'});
    }
  }
  function buildTreeNode(id) {
    const p = people.get(id), childIds = children.get(id) || [];
    const node = document.createElement('details'); node.className = 'tree-node'; node.dataset.treeId = id;
    node.innerHTML = `<summary>${link(p)}<span>${childIds.length ? childIds.length + ' children' : 'Gen ' + p.generation}</span></summary><div class="tree-contents"></div>`;
    node.addEventListener('toggle', () => { if (node.open) populateTreeNode(node); });
    return node;
  }
  function populateTreeNode(node) {
    if (node.dataset.loaded) return;
    node.dataset.loaded = 'true';
    const p = people.get(node.dataset.treeId), content = node.querySelector('.tree-contents');
    if (p.partners.length) content.innerHTML = p.partners.map(id => `<p class="tree-partner">+ ${link(people.get(id))}</p>`).join('');
    for (const id of children.get(p.id) || []) content.append(buildTreeNode(id));
    if (!(children.get(p.id) || []).length) content.insertAdjacentHTML('beforeend', '<p class="tree-partner">No children listed.</p>');
  }
  function initTree() {
    if (treeBuilt) return;
    treeBuilt = true;
    const root = buildTreeNode(data.root); $('family-tree').append(root); populateTreeNode(root); root.open = true;
  }
  function locateInTree(scroll = true) {
    initTree();
    let p = people.get(state.selected);
    if (p.kind === 'partner') p = people.get(p.partners[0] || p.possiblePartners[0]);
    if (!p) return;
    for (const a of [...ancestors(p), p]) {
      const node = document.querySelector(`[data-tree-id="${a.id}"]`);
      if (node) { populateTreeNode(node); node.open = true; }
    }
    document.querySelectorAll('.tree-node.is-selected').forEach(el => el.classList.remove('is-selected'));
    const node = document.querySelector(`[data-tree-id="${p.id}"]`);
    node?.classList.add('is-selected');
    if (scroll && node) {
      const box = $('family-tree'); box.scrollTop += node.getBoundingClientRect().top - box.getBoundingClientRect().top - 20;
    }
  }
  function setView(view) {
    state.view = view;
    document.querySelectorAll('[data-view]').forEach(button => {
      button.classList.toggle('active', button.dataset.view === view);
      button.setAttribute('aria-pressed', String(button.dataset.view === view));
    });
    $('workspace').hidden = view === 'about'; $('about-panel').hidden = view !== 'about';
    $('directory').hidden = view !== 'directory'; $('outline-panel').hidden = view !== 'outline';
    $('workspace').classList.toggle('outline-view', view === 'outline');
    if (view === 'outline') locateInTree(false);
  }
  function restore() {
    const params = new URLSearchParams(location.search);
    state.query = params.get('q') || ''; state.generation = /^[1-9]$/.test(params.get('gen') || '') ? params.get('gen') : '';
    state.review = params.get('review') === '1'; state.sort = ['birth','report'].includes(params.get('sort')) ? params.get('sort') : 'name';
    $('search').value = state.query; $('generation').value = state.generation; $('sort').value = state.sort; $('review-only').checked = state.review;
    const id = location.hash.slice(1);
    select(people.has(id) ? id : data.root, false);
    if (id && !people.has(id)) $('announcement').textContent = 'That record was not found. Showing the first generation.';
  }
  $('people-count').textContent = data.meta.people.toLocaleString();
  $('generation-count').textContent = data.meta.generations;
  $('review-total').textContent = `(${data.meta.reviewCount})`;
  $('review-explanation').textContent = `${data.meta.reviewCount} records have ambiguous relationships, unlabeled details, or questionable dates. Select “Needs review” in “Find a person” to see them.`;
  for (let g=1; g<=data.meta.generations; g++) $('generation').add(new Option(`Generation ${g}`, g));
  for (const [id, field, event] of [['search','query','input'], ['generation','generation','change'], ['sort','sort','change'], ['review-only','review','change']]) {
    $(id).addEventListener(event, e => { state[field] = field === 'review' ? e.target.checked : e.target.value; state.limit = 60; renderResults(); $('results').scrollTop = 0; updateURL(); });
  }
  $('clear-search').addEventListener('click', () => { $('search').value = ''; $('search').dispatchEvent(new Event('input')); $('search').focus(); });
  $('reset').addEventListener('click', () => { Object.assign(state, {query:'',generation:'',review:false,sort:'name',limit:60}); updateURL(); restore(); $('results').scrollTop = 0; });
  $('load-more').addEventListener('click', () => { const scroll = $('results').scrollTop; state.limit += 60; renderResults(); $('results').scrollTop = scroll; });
  $('show-lineage').addEventListener('click', () => locateInTree());
  $('collapse-tree').addEventListener('click', () => document.querySelectorAll('.tree-node').forEach(el => { el.open = false; }));
  document.addEventListener('click', e => {
    const target = e.target.closest('[data-person]');
    if (target && !e.ctrlKey && !e.metaKey && !e.shiftKey && !e.altKey) { e.preventDefault(); if (state.view === 'about') setView('directory'); select(target.dataset.person, true, true); }
    const viewButton = e.target.closest('[data-view]'); if (viewButton) setView(viewButton.dataset.view);
  });
  window.addEventListener('popstate', restore);
  window.addEventListener('hashchange', restore);
  restore();
})();
