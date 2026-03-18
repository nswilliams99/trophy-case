# CODEBASE - trophy-case

## Project Overview
- **Type:** Next.js 16 web application
- **Purpose:** Digital storefront and SEO-optimized website for The Trophy Case (local trophy shop in Fremont, NE) to increase business value and online visibility before potential sale
- **Tech Stack:** Next.js 16, React 19, TypeScript 5, Tailwind CSS 4, Radix UI, shadcn/ui components, Lucide icons

## Directory Structure

```
src/
âââ app/                    # Next.js app directory (pages, layout, globals)
âââ components/            # Reusable React components (from shadcn)
âââ lib/                    # Utility functions (classname merging, helpers)
âââ styles/               # Global CSS and theme configuration
```

**Root-level files:**
- `components.json` - shadcn/ui configuration
- `next.config.ts` - Next.js configuration
- `tsconfig.json` - TypeScript configuration with path aliases (@/*)
- `postcss.config.mjs` - PostCSS/Tailwind pipeline
- `eslint.config.mjs` - ESLint rules

## Key Patterns

- **Path Aliases:** Use `@/*` to import from src/ (e.g., `@/lib/utils`)
- **Component Library:** shadcn/ui + Radix UI for accessible, composable components with Tailwind styling
- **Styling:** Tailwind CSS v4 with class-variance-authority (CVA) for variant-based component patterns
- **Type Safety:** Strict TypeScript enabled; all React components must be typed
- **Dark Mode:** Built-in support via Tailwind dark: variant (see globals.css)

## Dev Commands

```bash
npm run dev      # Start development server (http://localhost:3000)
npm run build    # Production build
npm run start    # Run production server
npm run lint     # Run ESLint
```

## Environment Variables

None configured. Create `.env.local` if needed for API keys or database connections.
