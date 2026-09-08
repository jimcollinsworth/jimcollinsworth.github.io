# Site Journal & Decision Log: jimcollinsworth.github.io

> Chronological log of architectural decisions, site milestones, and design changes. Maintained under the 3-document agent rule.

---

## 2026-09-08 — GitHub Pages Deployment Alignment & Root HTML Synchronization

### Problem & Analysis
- When viewing the live site on mobile, legacy pill navigation (`.pill`, `.pill-nav`) and duplicate titles (`<h1>Posts & Notes</h1>`, `<h1>About Jim Collinsworth</h1>`) were still appearing.
- Root Cause: GitHub Pages was configured to build and deploy from the `main` branch root (`/`), which still contained pre-Pelican static HTML files from Milestone 2. Pelican's build output in `output/` was gitignored, causing branch deployment to serve the obsolete root files.

### Decisions & Actions Taken
1. **Bypassed Jekyll**:
   - Added `.nojekyll` to `content/extra/` and registered it in `pelicanconf.py` (`EXTRA_PATH_METADATA`).
2. **Synchronized Root HTML with Pelican Build**:
   - Replaced root `index.html`, `about.html`, `posts.html`, `reads.html`, `gallery.html`, `lanes.html`, `posts/`, and `lanes/` with Pelican's compiled output.
   - Synchronized `theme/css/style.css` and updated `assets/css/style.css` so legacy or cached CSS references also render without pills.
3. **Hardened Automated Tests (`tests/test_pelican_e2e.py`)**:
   - Updated `test_zero_pills_lane_formatting` to scan both `output/` and repository root HTML files, ensuring neither ever contains `.pill` or `.pill-nav`.
   - Updated `test_no_duplicate_page_titles` to verify `posts.html` contains no redundant `<h1>Posts` header.
4. **Verified Build & Tests**:
   - All 8 end-to-end tests passing (`uv run pytest -v`).

---

## 2026-09-08 — Pelican SSG Integration, Manual Image Workflow, & UI Refinements

### Decisions & Actions Taken
1. **Configured Pelican Static Site Generator**:
   - Created `pyproject.toml` and `pelicanconf.py` configured for zero-JS, pure HTML5, and relative URLs.
   - Implemented `ObsidianMarkdownReader` in `pelicanconf.py` to seamlessly parse YAML frontmatter headers (`---`).
2. **Content Reorganization**:
   - Migrated markdown files to `content/posts/` (`cordoba-stage-guitar.md`, `digital-piano-enhancements.md`, `m-e-offline-ai-companion.md`, `sleep-movement-evaluation-plan.md`, `ulu-knife-handle.md`).
   - Created `content/pages/` for standalone pages (`about.md`, `reads.md`, `gallery.md`).
   - Created `content/images/` for manually curated photo assets and `content/extra/` for root metadata files.
3. **Custom Pelican Theme (`theme/`) & UI Cleanup**:
   - Recreated site templates in Jinja2 (`base.html`, `index.html`, `article.html`, `page.html`, `archives.html`, `category.html`, `categories.html`).
   - **Title Deduplication**: Removed redundant `<h1>` headings from standalone pages (`About`, `Reads`, `Gallery`); the active menu tab serves as the title.
   - **Lane Styling**: Removed pill/badge formatting (`.pill`, `.pill-nav`); pursuit lanes are styled as clean, simple text links (`.post-lane`, `.lane-link`).
4. **Manual Image Transfer & Zero-AI Content Policy**:
   - Formalized policy: Jim manually selects and transfers all photos to `content/images/`. AI is strictly restricted to content management, never content generation.
   - External gallery integration: Posts include selected photo figures and link to full albums on Google Photos.
5. **End-to-End Test Suite (`tests/test_pelican_e2e.py`)**:
   - Implemented automated E2E tests validating build execution, page generation, title deduplication, zero-pills styling, content flow from Markdown, zero-JS policy, and link/asset integrity (all 8 tests passing).
6. **Automated CI/CD**:
   - Updated `.github/workflows/deploy.yml` to install dependencies via `uv`, run tests, build with Pelican, and deploy `output/` to GitHub Pages.

---

## 2026-09-08 — Scope Realignment: Rollback Custom Tools & Focus on Obsidian Flow

### Decisions & Actions Taken
1. **Rolled Back Custom Build & Tool Pipeline**:
   - Reverted all working tree modifications and cleaned untracked directories (`tools/`, `tests/`, `projects/`, virtual environment, etc.) to return repository to clean `origin/main` state.
   - Preserved pure static site structure and strict content boundaries.
2. **Backlog Realignment in `PLANNING.md`**:
   - Transferred custom static site builder, MCP server, Pytest suite, and interactive tools (`circle-of-fifths`, `earthquakes`) to the backlog as optional "nice to have" enhancements.
3. **Refocused Active Priority**:
   - Established primary exploration: clarifying how Markdown authored in Obsidian is placed into a directory and flows into published HTML.
   - Selected Pelican as the preferred static site generator foundation.
4. **Installed Project Skills in `.agents/skills/`**:
   - Created [`pelican-site-manager`](file:///d:/projects/jimcollinsworth.github.io/.agents/skills/pelican-site-manager/SKILL.md): Complete runbook for Pelican configuration, development server, zero-JS preservation, and build verification.
   - Created [`pelican-obsidian-bridge`](file:///d:/projects/jimcollinsworth.github.io/.agents/skills/pelican-obsidian-bridge/SKILL.md): Guidelines for mapping an Obsidian vault to Pelican's content folder, handling YAML frontmatter, wikilinks, image embeds, and callouts.
   - Added Rule 7 (Command Line Standards & Reproducibility) to [`.agents/agent_rules.md`](file:///d:/projects/jimcollinsworth.github.io/.agents/agent_rules.md).

---

## 2026-09-07 — Custom "JC" Favicon Update

### Decisions & Actions Taken
1. **Designed Minimalist "JC" Favicon**:
   - Created vector [`favicon.svg`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/favicon.svg) featuring "JC" monogram with rounded geometry and built-in CSS `@media (prefers-color-scheme: dark)` color-switching (rust in light mode, amber in dark mode).
   - Generated multi-resolution [`favicon.ico`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/favicon.ico) (16x16, 32x32, 48x48, 64x64) with matching warm rust background and white lettering.
   - Linked both SVG and ICO fallback across all 11 site and post pages.

---

## 2026-09-07 — Content Boundary Remediation & Post Page Linking

### Decisions & Actions Taken
1. **Strict Content Boundary Remediation**:
   - Audited every page and deleted all agent-authored text and fabricated summaries.
   - Replaced placeholder entries in `reads.html` and `index.html` strictly with standard `Lorem ipsum` holding text.
   - Replaced all post descriptions across `index.html`, `posts.html`, and `posts/*.html` strictly with Jim's original archived text from `archive/content/`.
2. **Individual Post Page Generation & Linking**:
   - Generated dedicated static post pages in `posts/` containing Jim's exact archived text:
     - [`posts/sleep-movement-evaluation-plan.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/sleep-movement-evaluation-plan.html)
     - [`posts/m-e-offline-ai-companion.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/m-e-offline-ai-companion.html)
     - [`posts/cordoba-stage-guitar.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/cordoba-stage-guitar.html)
     - [`posts/digital-piano-enhancements.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/digital-piano-enhancements.html)
     - [`posts/ulu-knife-handle.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/ulu-knife-handle.html)
   - Linked all post titles from `index.html` and `posts.html` directly to their respective post pages.
3. **Pure Photo Gallery**:
   - Removed all captions and extra text from `gallery.html`, presenting clean unencumbered photography with only the Google Photos album link at the top.

---

## 2026-09-07 — Calvin & MacWright UI Overhaul, Bookshelf, & Content Pipeline

### Decisions & Actions Taken
1. **Adopted Calvin French-Owen Typography & Listing Rhythm**:
   - Implemented post listings with prominent rust titles (`var(--link)`), right-aligned uppercase dates, category pill badges, and concise takeaway descriptions.
   - Created secondary level filter pill navigation bar on `posts.html`.
2. **Added Bookshelf / Reads (`reads.html`)**:
   - Dedicated reading synthesis page inspired by Calvin's bookshelf with titles, authors, dates read, favorite indicators (`*`), and mental model notes.
3. **MacWright-Style Photo Stream (`gallery.html`)**:
   - Replaced boxed card grid with a clean, full-width photo stream with left-aligned captions and zero distracting card borders.
4. **Streamlined Navigation & Page Roles**:
   - Primary navigation streamlined to: `Home`, `About`, `Posts`, `Reads`, `Gallery`.
   - Retired `lanes.html`; integrated the Lanes taxonomy into `about.html` and as single-category badges across posts.
   - Removed duplicated biography text on `index.html`, refocusing the home page on current activity, recent posts, bookshelf highlights, and photo spotlight.
5. **New Content Drop Directory (`content/`)**:
   - Established `content/posts/`, `content/notes/`, and `content/reads/` for dropping Markdown source files with clean YAML front-matter (`title`, `date`, `category`, `description`).

---

## 2026-09-07 — Header Branding Single-Line Alignment

### Decisions & Actions Taken
1. **Unified Title and Tagline Row**:
   - Updated header structure to place "Jim Collinsworth" and "Out of My Lane" on the same horizontal row using `.site-branding` with flex `justify-content: space-between`.
   - Set matching font size (`1.35rem`) and font family (`var(--font-sans)`) across title and tagline while maintaining subtle text mute for the tagline.
   - Updated across all 5 site pages (`index.html`, `about.html`, `lanes.html`, `journal.html`, `gallery.html`) and `assets/css/style.css`.

---

## 2026-09-06 — Content Reversion to Archive & 12 Lanes Setup

### Decisions & Actions Taken
1. **Reverted All Content to Archive Text**:
   - Replaced all prose on `about.html` and `index.html` strictly with Jim's original text from `pages/about.md` and `README.md`. Removed all AI-generated commentary.
   - Simplified `gallery.html` to minimalist titles and direct link to the Google Photos album.
2. **Configured 12 Requested Lanes**:
   - Updated `lanes.html` and `index.html` with the 12 explicit lanes: *Music making, Software, Life sciences, Engineering, Photography, Making, Law, Art, Politics, Data, Exercise, Anatomy*.
3. **Dummy Entries for Layout Preview**:
   - Inserted placeholder `Lorem ipsum` entries on `journal.html` and `index.html` solely to preview page layout without authoring posts.
4. **CI Workflow Streamlining**:
   - Refined `.github/workflows/deploy.yml` with a lightweight Zero-JS audit step and GitHub's official Pages deployment action.

---

## 2026-09-06 — Architectural Transformation: Pure HTML/CSS & Agent Governance

### Context & Problem
The site previously relied on Nikola, a Python-based static site generator with configuration files (`conf.py`), theme directories (`themes/hyde`), virtual environments (`pyproject.toml`, `uv.lock`), and compiler build workflows (`nikola.yml`). This introduced unnecessary build friction, compilation fragility, and opaque templating layers for what should be an authentic, durable personal website.

### Decisions & Actions Taken

1. **Complete Decommissioning of Compiler Toolchain**:
   - Removed `conf.py`, `themes/`, `plugins/`, `pyproject.toml`, `uv.lock`, and legacy build workflows.
   - Preserved all historical notes, draft essays, category definitions, and SEO verification tokens safely in `archive/content/`.
   - Relocated original full-resolution photo collections into `archive/original_photos/`.

2. **Mandatory 3-Document Rule & Content Boundaries**:
   - Created `.agents/agent_rules.md`.
   - Strict governance: the agent may maintain **only three** root system design documents (`README.md`, `PLANNING.md`, `JOURNAL.md`). Any walkthroughs or additional meta documents are unauthorized.
   - Strict content policy: the agent must **never** draft content documents, create content files, or write articles for Jim. All content authoring belongs 100% to Jim.

3. **Pure Semantic HTML5 & Modern CSS Architecture**:
   - Committed to 99.9% pure HTML5 and **zero client-side JavaScript**.
   - Crafted `assets/css/style.css` focusing on editorial typography (Charter / Sitka Text / Georgia serif body, clean sans headers and navigation, monospace code/data), comfortable line length (~70ch), fluid responsive grid, and native `@media (prefers-color-scheme: dark)` styling.
   - Design restraint inspired by Bear Blog (`pinewind.bearblog.dev`) and Mark Boulton (`markboulton.co.uk/journal/anewcanon/`).

4. **Core Structural Pages Created**:
   - `index.html`: Central home featuring tagline ("Out of My Lane"), bio overview, active lanes grid, and lakefront photography.
   - `about.html`: Personal profile covering Jim's 50-year career (Arthur Andersen, guitarist, tech startups, data science) and retirement philosophy.
   - `lanes.html`: Structured index of active pursuit lanes.
   - `journal.html`: Chronological journal index container with sample entries.
   - `gallery.html`: Photographic showcase with Chicago sky and botanical studies.
   - `.github/workflows/deploy.yml`: Automated Zero-JS audit, link integrity test, and direct GitHub Pages deployment.

5. **Automated Verification & CI Guardrails**:
   - Integrated `.github/workflows/deploy.yml` to run automated quality audits on every push before publishing.
   - Verified that all HTML files contain 0 `<script>` tags.
   - Verified that all internal page and image links resolve cleanly to existing local files.
   - Validated standard `<!DOCTYPE html>` structure and closed tags.
