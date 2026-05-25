// @ts-check
import { defineConfig } from 'astro/config';

import react from '@astrojs/react';
import mdx from '@astrojs/mdx';

// Tailwind v4 wired via PostCSS — avoids @tailwindcss/vite × rolldown-vite
// binding incompatibility. See postcss.config.mjs.
export default defineConfig({
  integrations: [react(), mdx()],
});
