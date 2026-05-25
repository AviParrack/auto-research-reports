// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import mdx from '@astrojs/mdx';
import pagefind from 'astro-pagefind';

// Tailwind v4 wired via PostCSS — avoids @tailwindcss/vite × rolldown-vite
// binding incompatibility. See postcss.config.mjs.
//
// astro-pagefind runs `pagefind` after astro build, indexing the dist/
// folder. Provides client-side search via /pagefind/pagefind-ui.js.
export default defineConfig({
  integrations: [react(), mdx(), pagefind()],
});
