// Client-side tooltips for glossary terms + source citations.
// Runs after DOMContentLoaded + Tippy loaded.
// Reads window.__tooltipPayload (set by the layout) and window.__reportSlug.
//
// Scans .prose-leaf containers and:
//  (a) replaces [source-slug] inline citations with <a class="source-cite"> tags
//  (b) wraps glossary-term occurrences in <span class="glossary-term">
//  (c) initialises Tippy popovers on both with the relevant content.
//
// Avoids: code blocks, pre, KaTeX output, links, headings.

(function () {
  const SKIP_TAGS = new Set(['SCRIPT', 'STYLE', 'CODE', 'PRE', 'A', 'KATEX', 'TEXTAREA']);
  const SKIP_CLASS = /(katex|katex-display|tippy-)/;

  function ready(fn) {
    if (document.readyState !== 'loading') return fn();
    document.addEventListener('DOMContentLoaded', fn);
  }

  ready(() => {
    // Wait for Tippy to finish loading (it's deferred CDN script)
    const waitForTippy = (attempt = 0) => {
      if (typeof window.tippy !== 'function') {
        if (attempt > 40) return; // give up after ~4s
        return setTimeout(() => waitForTippy(attempt + 1), 100);
      }
      run();
    };
    waitForTippy();
  });

  function run() {
    const payload = window.__tooltipPayload;
    const slug = window.__reportSlug;
    if (!payload || !slug) return;

    const proseRoots = document.querySelectorAll('.prose-leaf');
    if (proseRoots.length === 0) return;

    // Build lookup maps
    const sourceBySlug = new Map();
    for (const s of payload.sources || []) sourceBySlug.set(s.slug, s);

    // Term match: each glossary entry contributes one or two matchable strings.
    // We match the `symbol` (case-sensitive — acronyms are usually caps) AND
    // the `term` (case-insensitive). Symbol match wins when ambiguous because
    // acronyms are more specific than the spelled-out form.
    const terms = [];
    for (const g of payload.glossary || []) {
      if (g.symbol) {
        terms.push({
          ...g,
          regex: new RegExp(`\\b(${escapeRegExp(g.symbol)})\\b`),
          priority: 100 + g.symbol.length,
        });
      }
      if (g.term) {
        terms.push({
          ...g,
          regex: new RegExp(`\\b(${escapeRegExp(g.term)}s?)\\b`, 'i'),
          priority: g.term.length,
        });
      }
    }
    // Longer / higher priority first so "production mass ratio" wins over "ratio"
    terms.sort((a, b) => b.priority - a.priority);

    proseRoots.forEach((root) => {
      processSourceCites(root, sourceBySlug, slug);
      processGlossary(root, terms);
    });

    // Initialise Tippy on all wrapped elements
    window.tippy('.source-cite', {
      allowHTML: true,
      theme: 'auto-research',
      interactive: true,
      maxWidth: 360,
      placement: 'top',
      delay: [120, 50],
      onShow(instance) {
        if (instance.props.content) return;
        const slug = instance.reference.dataset.sourceSlug;
        const s = sourceBySlug.get(slug);
        if (!s) {
          instance.setContent('<em>source not found</em>');
          return;
        }
        const titleHtml = s.title ? `<strong>${escapeHtml(s.title)}</strong>` : `<strong>${escapeHtml(s.slug)}</strong>`;
        const meta = [
          s.authors && s.authors.length ? escapeHtml(s.authors.join(', ')) : null,
          s.year ? String(s.year) : null,
        ].filter(Boolean).join(' &middot; ');
        const html = `${titleHtml}${meta ? `<br><span style="opacity:0.75">${meta}</span>` : ''}<div style="margin-top:0.55rem; font-size:0.85em; opacity:0.9">${escapeHtml(s.snippet)}</div>`;
        instance.setContent(html);
      },
    });

    window.tippy('.glossary-term', {
      allowHTML: true,
      theme: 'auto-research',
      maxWidth: 360,
      placement: 'top',
      delay: [200, 50],
      content: (ref) => ref.dataset.tippyContent || ref.dataset.def || '',
    });
  }

  // ---- source citation processing ----
  function processSourceCites(root, sourceBySlug, slug) {
    // Match [source-slug] or [source-slug#anchor] in text nodes
    const re = /\[([a-z0-9][a-z0-9-]*)(?:#([^\]]+))?\]/g;
    walkTextNodes(root, (node) => {
      const text = node.nodeValue;
      if (!re.test(text)) return;
      re.lastIndex = 0;
      const frag = document.createDocumentFragment();
      let lastIdx = 0;
      let m;
      while ((m = re.exec(text)) !== null) {
        const [full, srcSlug, anchor] = m;
        if (!sourceBySlug.has(srcSlug)) continue; // unknown slug -> leave as-is
        if (m.index > lastIdx) frag.appendChild(document.createTextNode(text.slice(lastIdx, m.index)));
        const a = document.createElement('a');
        a.className = 'source-cite';
        a.href = `/${slug}/sources/${srcSlug}/` + (anchor ? `#${anchor}` : '');
        a.dataset.sourceSlug = srcSlug;
        a.textContent = srcSlug + (anchor ? `#${anchor}` : '');
        frag.appendChild(a);
        lastIdx = m.index + full.length;
      }
      if (lastIdx > 0) {
        if (lastIdx < text.length) frag.appendChild(document.createTextNode(text.slice(lastIdx)));
        node.parentNode.replaceChild(frag, node);
      }
    });
  }

  // ---- glossary term processing ----
  function processGlossary(root, terms) {
    if (terms.length === 0) return;
    // Track which glossary entries have already been wrapped at least once in
    // this leaf to avoid spam: only mark the FIRST occurrence per term.
    const seenTerms = new Set();
    walkTextNodes(root, (node) => {
      const text = node.nodeValue;
      // Find leftmost match in this text node, scanning all entries
      let bestMatch = null;
      for (const t of terms) {
        // Skip if we've already wrapped this term elsewhere on the page
        const key = (t.symbol || t.term) + '::' + (bestMatch ? '' : '');
        if (seenTerms.has(t.term + (t.symbol || ''))) continue;
        t.regex.lastIndex = 0;
        const m = t.regex.exec(text);
        if (!m) continue;
        if (!bestMatch || m.index < bestMatch.match.index) {
          bestMatch = { ...t, match: m };
        }
      }
      if (!bestMatch) return;
      const m = bestMatch.match;
      const frag = document.createDocumentFragment();
      if (m.index > 0) frag.appendChild(document.createTextNode(text.slice(0, m.index)));
      const span = document.createElement('span');
      span.className = 'glossary-term';
      span.dataset.term = bestMatch.term;
      span.dataset.tippyContent = bestMatch.html;
      span.textContent = m[1];
      frag.appendChild(span);
      seenTerms.add(bestMatch.term + (bestMatch.symbol || ''));
      const after = text.slice(m.index + m[1].length);
      if (after) frag.appendChild(document.createTextNode(after));
      node.parentNode.replaceChild(frag, node);
    });
  }

  function walkTextNodes(root, fn) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode(node) {
        let p = node.parentNode;
        while (p && p !== root) {
          if (SKIP_TAGS.has(p.tagName)) return NodeFilter.FILTER_REJECT;
          if (p.className && typeof p.className === 'string' && SKIP_CLASS.test(p.className)) return NodeFilter.FILTER_REJECT;
          p = p.parentNode;
        }
        return node.nodeValue.trim() ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      },
    });
    const nodes = [];
    let n;
    while ((n = walker.nextNode())) nodes.push(n);
    nodes.forEach(fn);
  }

  function escapeRegExp(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }
})();
