# Agent Guidelines & Rules: jimcollinsworth.github.io

This document outlines the strict operational principles, technical constraints, design philosophy, authoring boundaries, and procedures for any LLM coding agent maintaining Jim Collinsworth's personal site and blog.

---

## 1. Mandatory Governance Documents

> [!IMPORTANT]
> The agent is authorized and permitted to maintain **only four** core system and planning documents in the root directory:
> 1. `README.md` – Site overview, architecture, developer utilities, publishing instructions, and directory map.
> 2. `PLANNING.md` – Active backlog, sprint tasks, and near-term milestones.
> 3. `ROADMAP.md` – Long-term discussion of features, brainstorming, creative ideas, and future possibilities.
> 4. `JOURNAL.md` – Chronological project log recording milestones, technical decisions, and changes.
>
> **NO other system design, architecture, walkthrough, or meta documents may be created anywhere in this repository or workspace without first explicitly proposing them to Jim and receiving approval.**

---

## 2. Content Authoring Boundaries (Strict)

> [!CAUTION]
> **Content Belongs Exclusively to Jim**:
> - The agent must **NEVER draft content documents, essays, articles, posts, or personal notes** for Jim.
> - The agent must **NEVER create new content files** on its own initiative.
> - The agent must **NEVER assist with or write content** unless Jim explicitly and directly asks for that specific assistance.
> - The agent's role is strictly technical stewardship: maintaining clean HTML/CSS infrastructure, ensuring responsive layouts, verifying link integrity, managing assets, and maintaining the governance documents.

---

## 3. Technical Philosophy & Constraints

1. **Pure Static Generation via Pelican**:
   - Built with Pelican Python static site generator from clean Markdown sources in `content/`.
   - Pure Python ecosystem managed via `uv` (`.venv/`).
   - Output compiled to `output/` and deployed to GitHub Pages.
2. **Zero Node.js / npm Policy**:
   - Strictly **no Node.js or npm ever** for applications, site features, or development toolchains.
   - The **only current exception** at this time is `npx skills` (for installing or managing agent skills).
3. **Zero JavaScript Policy**:
   - The site operates completely with zero client-side JavaScript (`<script>` tags are strictly disallowed on published content pages).
   - Interactivity is achieved through semantic HTML (e.g., `<details>`, `<summary>`, anchor links) and modern CSS.
4. **Responsive & Accessible by Default**:
   - Mobile-first, fluid responsive layout.
   - High color contrast and legible type scaling.
   - Built-in automatic light and dark mode via CSS media query:
     ```css
     @media (prefers-color-scheme: dark) { ... }
     ```
   - Standard semantic markup: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<figure>`, `<figcaption>`, `<footer>`.

---

## 4. Visual & Typographic Design Principles

Inspired by:
- **[Pine Wind (Bear Blog)](https://pinewind.bearblog.dev/)**: Extreme minimalism, fast loading, distraction-free reading, generous whitespace.
- **[Mark Boulton (A New Canon)](https://markboulton.co.uk/journal/anewcanon/)**: Refined editorial typography, comfortable reading line length (60–75 characters, max width ~680px–740px), precise vertical rhythm, and elegant image handling with captions.

### Key CSS Standards
- Single central stylesheet: `assets/css/style.css`.
- High-quality system font stack with graceful fallbacks (e.g., Georgia / Charter / serif for editorial prose, system sans-serif for navigation and metadata, monospace for code snippets and data tables).
- Images formatted with `<figure>` and `<figcaption>` to celebrate photography with intentional context.

---

## 5. Content Organization & "Lanes"

- **Lanes (Areas of Interest)**: Jim's explorations and pursuits across different domains:
  - Music (Guitar, Piano, Theory)
  - STEM & Computing (Software, Data, AI, Electronics, Weather)
  - Health & Body (Tai Chi, Alexander Technique, Anatomy, Sleep)
  - Crafts & Making (Woodworking, Knife making, DIY)
- **Journal**: Chronological notes, observations, deep dives, and progress reports written by Jim.
- **Gallery**: Photographic essays and studies (Chicago sky, Lake Michigan, sunsets, botanical, craft).
- **Archive**: Historical notes, raw drafts, and original full-resolution photo assets in `archive/`.

---

## 6. Maintenance Procedures for the 4 Core Documents

Whenever technical changes, layout updates, or infrastructure features are implemented:
1. **`JOURNAL.md`**: Append a concise entry under the current date detailing what technical changes were made and why.
2. **`PLANNING.md`**: Update active technical task statuses, sprint items, and near-term milestones.
3. **`ROADMAP.md`**: Update long-term vision, capture brainstormed concepts, and refine technical exploration proposals.
4. **`README.md`**: Keep directory structures, stats, developer utility references, and high-level descriptions accurate as the site evolves.

---

## 7. Command Line Standards & Reproducibility

> [!IMPORTANT]
> - Always use clean, standard command-line invocations (e.g., `git status`, `pelican content -s pelicanconf.py`, `pytest`) that Jim can easily inspect, copy, and run manually in his own terminal.
> - Avoid opaque subshell wrappers, nested execution scripts, or obscure one-liners when standard commands exist.
> - Use standard command-line tools unless not possible.
> - If an operation cannot be run via standard, easily reproducible command-line syntax, stop and ask Jim before proceeding.

---

## 8. Agent Permissions & Rule Authorization (Strict)

> [!CAUTION]
> **Strict Boundary on Agent Rules & Permissions**:
> - The agent must **NEVER add, modify, or append rules or files in `.agents/` without explicit permission from Jim**.
> - Jim will explicitly request specific rules to be added.
> - The agent must never unilaterally codify tool options, personal habits, or arbitrary constraints into `.agents/`.

---

## 9. Git Remote Operations (Strict)

> [!CAUTION]
> **No Remote Pushes Without Explicit Confirmation**:
> - The agent must **NEVER push commits to any remote repository (`git push`) without Jim's explicit request or confirmation**.
> - Push is considered too large an action to take autonomously because pushing triggers automated CI/CD builds, deploys to GitHub Pages, and mutates public/shared repository state.
> - The agent may stage and commit changes locally for verification, but must always stop and wait for Jim to confirm before pushing.
