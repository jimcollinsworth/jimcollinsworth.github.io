# Agent Guidelines & Rules: jimcollinsworth.github.io

This document outlines the strict operational principles, technical constraints, design philosophy, authoring boundaries, and procedures for any LLM coding agent maintaining Jim Collinsworth's personal site and blog.

---

## 1. Mandatory Governance Documents

> [!IMPORTANT]
> The agent is authorized and permitted to maintain the core system, governance, and planning documents:
> 1. `README.md` – Site overview, architecture, developer utilities, publishing instructions, and directory map.
> 2. `PLANNING.md` – Active backlog, sprint tasks, and near-term milestones.
> 3. `ROADMAP.md` – Long-term discussion of features, brainstorming, creative ideas, and future possibilities.
> 4. `JOURNAL.md` – Chronological project log recording milestones, technical decisions, and changes.
> 5. `AGENTS.md` (and `.agents/agent_rules.md`) – Operational principles, technical constraints, authoring boundaries, and small-team workflow rules.
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
- **Photos**: Photographic essays and studies (Chicago sky, Lake Michigan, sunsets, botanical, craft).
- **Archive**: Historical notes, raw drafts, and original full-resolution photo assets in `archive/`.

---

## 6. Maintenance Procedures for the 4 Core Documents & Continuous Learning

Whenever technical changes, troubleshooting resolutions, layout updates, or user corrections occur:
1. **`JOURNAL.md`**: Append a structured chronological entry detailing:
   - **Jim's Guidance & Direction**: Prominently highlight Jim's exact prompts, instructions, questions, corrections, and advice using callouts (`> [!NOTE] Jim's Instructions & Guidance:`).
   - **Problem & Diagnosis**: What issue or requirement occurred.
   - **Root Cause & Technical Analysis**: The underlying architectural or system reason.
   - **Solution & Standard Procedure**: The exact commands or steps taken to resolve it.
2. **`PLANNING.md`**: Update active task checkboxes, current milestone status, and sprint backlog items.
3. **`ROADMAP.md`**: Update long-term vision, capture brainstormed concepts, and refine technical exploration proposals.
4. **`README.md`**: Keep directory structures, stats, CLI commands, component guides, and developer utility references accurate.
5. **Persistent Agent Learning**: When a durable pattern, debugging fix, or user preference is established (e.g. via `/learn`), update persistent documentation and skills when explicitly approved by Jim.

---

## 7. Command Line Standards & Reproducibility

> [!IMPORTANT]
> - Always use clean, standard command-line invocations (e.g., `uv run pytest -v`, `uv run pelican content -s pelicanconf.py -o output -d`, `taskkill`, `rmdir`) that Jim can easily inspect, copy, and run manually in Windows Command Prompt (`cmd.exe`) or terminal.
> - Avoid requiring PowerShell when standard Command Prompt commands work cleanly.
> - Avoid opaque subshell wrappers, nested execution scripts, or obscure one-liners when standard commands exist.
> - If an operation cannot be run via standard, easily reproducible CLI syntax, stop and clarify with Jim before proceeding.

---

## 8. Continuous Commit-Level Versioning Protocol

Every commit and meaningful change set must increment the project version:
- **Major/Feature Changes (`0.5.01` $\rightarrow$ `0.5.02`)**: New pages, layout restructurings, architectural updates.
- **Incremental Refinements (`0.5.01.01` $\rightarrow$ `0.5.01.02`)**: Style tweaks, documentation updates, bugfixes, rule adjustments.
- **Synchronization**: Always keep `pyproject.toml` and the DevOps dashboard on `about-this-site.md` synchronized to the current version.

---

## 9. Content Taxonomy & Semantic Authoring Rules

- Follow the definitions documented directly in `README.md`.
- **Content Types**:
  - **Post / Essay**: Long-form structured narrative (`content/posts/`).
  - **Project**: Active, multi-step engineering or fabrication build with milestones.
  - **TIL ("Today I Learned") / Quick Note**: Short 1–3 paragraph insight or CLI fix.
  - **Idea / Seedling**: Unexecuted hypothesis or prompt (`Ideas` lane or backlog).
  - **Shelf / Book Synthesis**: Curated book reflections (`shelf.md`).
  - **Comment / Annotation**: Inline callout or marginalia.
- **No Newspaper Jargon**: Use clean, standard Web & Markdown terminology (*Site Header, Document Title, Lead Intro, Section Headings, Body Paragraphs, Quotes/Callouts, Figures/Captions, Data Tables, Code Blocks, Footer*).

---

## 10. Agent Permissions & Rule Authorization (Strict)

> [!CAUTION]
> **Strict Boundary on Agent Rules & Permissions**:
> - The agent must **NEVER add, modify, or append rules or files in `.agents/` without explicit permission from Jim**.
> - Jim will explicitly request specific rules to be added.
> - The agent must never unilaterally codify tool options, personal habits, or arbitrary constraints into `.agents/`.

---

## 11. Small-Team Git Branching & Remote Operations (Strict)

> [!CAUTION]
> **Branching & Deployment Invariants**:
> 1. **`main` is Production-Only**:
>    - `main` directly drives the live GitHub Pages site.
>    - The agent must **NEVER** commit directly to `main` or merge into `main` during feature development or experimentation.
>    - Merging to `main` and pushing to `origin main` is performed **ONLY** upon Jim's explicit instruction to "push", "publish", or "release".
> 2. **Feature & Bug Branches for All Work**:
>    - All active work, layout changes, and experiments must occur on dedicated working branches (`feature/*`, `bug/*`, or `dev`).
>    - When starting new work, use the in-place branch switch (`git checkout -b feature/<name>`) for small-team simplicity.
> 3. **Automated CI Testing on All Branches**:
>    - GitHub Actions CI must test (`uv run pelican` + `pytest -v`) across all working branches (`main`, `dev`, `feature/**`, `bug/**`).
>    - The `deploy` job to GitHub Pages is strictly gated to `main` pushes only (`if: github.ref == 'refs/heads/main' && github.event_name == 'push'`).
> 4. **No Remote Pushes Without Explicit Confirmation**:
>    - The agent must **NEVER push commits to any remote repository (`git push`) without Jim's explicit request or confirmation**.
>    - The agent may stage and commit changes locally on feature branches for verification, but must always stop and wait for Jim to confirm before pushing.

---

## 12. Stepwise Increments & Brainstorming Protocol

> [!IMPORTANT]
> - **Deliberate, Stepwise Progression**: The agent must **NEVER** implement expansive, multi-tier architectural changes (such as complex taxonomy schemes, multi-zone classification systems, or simultaneous multi-template refactors) in a single pass.
> - **Brainstorm First**: Always explore the simplest minimal viable solution in chat, discuss trade-offs, and obtain Jim's explicit approval before touching code.
> - **Deferral to GitHub Issues**: If an architectural concept is determined to be too complex, speculative, or in need of deeper rethinking, immediately capture it in a GitHub issue via `gh issue create` (or update an existing ticket) and defer implementation rather than pushing forward.

---

## 13. Visual Evidence & UI Walkthrough Protocol

> [!IMPORTANT]
> **Inline Visual Evidence Required for UI Changes**:
> - Whenever work involves user interface changes, layout restructurings, styling adjustments, or visual mode updates, the agent must **always provide one or two visual screenshots directly in the report / walkthrough** presented to Jim.
> - The agent must display this visual evidence before asking Jim for approval to push to remote branches or merge to `main`.
> - Never claim UI changes are ready for push or release without giving Jim immediate visual evidence to inspect.

