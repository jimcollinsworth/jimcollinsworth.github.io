# Agent Guidelines & Rules: jimcollinsworth.github.io

This document outlines the strict operational principles, technical constraints, design philosophy, authoring boundaries, and procedures for any LLM coding agent maintaining Jim Collinsworth's personal site and blog.

---

## 1. Mandatory 3-Document Rule

> [!IMPORTANT]
> The agent is authorized and permitted to maintain **only three** system design / meta documents in the root directory:
> 1. `README.md` – Site overview, architecture, publishing instructions, and directory map.
> 2. `PLANNING.md` – Active backlog, upcoming lanes, and technical roadmap.
> 3. `JOURNAL.md` – Chronological project log recording milestones, technical decisions, and changes.
>
> **NO other system design, architecture, walkthrough, or meta documents may be created anywhere in this repository or workspace without first explicitly proposing them to Jim and receiving approval.**

---

## 2. Content Authoring Boundaries (Strict)

> [!CAUTION]
> **Content Belongs Exclusively to Jim**:
> - The agent must **NEVER draft content documents, essays, articles, posts, or personal notes** for Jim.
> - The agent must **NEVER create new content files** on its own initiative.
> - The agent must **NEVER assist with or write content** unless Jim explicitly and directly asks for that specific assistance.
> - The agent's role is strictly technical stewardship: maintaining clean HTML/CSS infrastructure, ensuring responsive layouts, verifying link integrity, managing assets, and maintaining the three governance documents.

---

## 3. Technical Philosophy & Constraints

1. **99.9% Pure HTML5 & Modern CSS**:
   - Zero dynamic web page compilers (no Nikola, Jekyll, Hugo, Astro, Next.js).
   - Zero Node.js / npm dependencies.
   - Zero Python build dependencies.
   - Pages are published directly by pushing standard static files to GitHub Pages (`main` branch).
2. **Zero JavaScript**:
   - The site operates completely with zero client-side JavaScript (`<script>` tags are strictly disallowed on content pages).
   - Interactivity is achieved through semantic HTML (e.g., `<details>`, `<summary>`, anchor links) and modern CSS.
3. **Responsive & Accessible by Default**:
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

## 6. Maintenance Procedures for the 3 Core Documents

Whenever technical changes, layout updates, or infrastructure features are implemented:
1. **`JOURNAL.md`**: Append a concise entry under the current date detailing what technical changes were made and why.
2. **`PLANNING.md`**: Update technical task statuses, roadmap milestones, and capture ideas discussed with Jim.
3. **`README.md`**: Keep directory structures, stats, and high-level descriptions accurate as the site evolves.
