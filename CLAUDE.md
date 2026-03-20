# Project Overview

Trophy Case is a Next.js portfolio/showcase web application for Trending Up Digital, run by Nate Williams. It appears to be a project management and research-heavy initiative with multiple worktrees and research documentation.

**Business/Client:** Trending Up Digital (internal project)

**Tech Stack:**
- Framework: Next.js 16.1.6 with App Router
- Language: TypeScript 5
- Styling: Tailwind CSS 4 with PostCSS
- UI Components: Radix UI, shadcn, Lucide React icons
- Utilities: clsx, tailwind-merge, class-variance-authority

# Key Files & Structure

- **package.json** - Project dependencies and scripts (dev, build, start, lint)
- **tsconfig.json** - TypeScript configuration with path aliases (@/* â ./src/*)
- **next.config.ts** - Next.js configuration (currently minimal)
- **components.json** - shadcn component configuration
- **eslint.config.mjs** - ESLint rules
- **postcss.config.mjs** - PostCSS/Tailwind configuration
- **.claude/settings.json** - Claude AI workspace settings
- **.claude/worktrees/elastic-easley/** - Research branch with site audit, keyword analysis, and parsed research files
- **PROPOSAL.md** - Project proposal documentation
- **CODEBASE.md** - Codebase documentation

# Development Notes

**Local Setup:**
```bash
npm run dev
# Opens http://localhost:3000
```

**Build & Deploy:**
```bash
npm run build
npm start
npm run lint
```

**Key Patterns & Conventions:**
- Uses TypeScript strict mode
- App Router structure (edit `app/page.tsx` for homepage)
- Component-based architecture with Radix UI + shadcn
- Tailwind CSS for all styling
- Path aliases configured (@/* points to ./src/*)
- Research-driven development with phase-1-site-audit.md documenting findings

**Git Conventions:**
- Use descriptive commit messages
- Follow standard Next.js/React patterns

# MCP Servers Available

- notion
- figma
- atlassian
- linear
- monday
- asana
- hubspot
- canva
- box
- intercom
- gsc (Google Search Console)

# Nate's Preferences

- â Always use TypeScript (strict mode enabled)
- â Prefer Next.js App Router (currently configured)
- â Use Tailwind CSS for styling (v4 with PostCSS)
- â Keep components small and reusable (Radix UI + shadcn pattern)
- â Always commit with descriptive messages


---

## Shared Data Library

Nate's shared SEO dataset lives at `C:\Users\Nateman\SharedData\`

Before fetching any external data, check here first:
- **FAQs / PAA questions** → `faqs.json` (keyed by keyword)
- **Keyword data** → `keywords.json` (keyed by keyword)
- **SERP snapshots** → `serp-data.json`
- **Schema blocks** → `schema-templates\`
- **Content outlines** → `content-templates\`

Use cached data if `fetched_at` is within 60 days. Only fetch fresh data if the keyword is missing or the cache is expired.
