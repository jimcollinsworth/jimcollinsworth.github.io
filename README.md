# jimcollinsworth.github.io

> Personal website, journal, and exploration lanes of **Jim Collinsworth** — *Out of My Lane*.

---

## Overview & Philosophy

jimcollinsworth.github.io is Jim Collinsworth's personal website and journal, built using the Pelican static site generator with HTML5 and CSS, containing zero client-side JavaScript:

- **Static Site Generation via Pelican**: Python static site compilation from Markdown notes.
- **Zero Client-Side JavaScript**: Semantic HTML5 and CSS on content pages. Zero `<script>` tags, tracking, or runtime dependencies.
- **Responsive CSS**: Fluid layouts and automatic dark/light theme switching via `@media (prefers-color-scheme: dark)`.
- **Editorial Layout**: Layout inspired by [Pine Wind (Bear Blog)](https://pinewind.bearblog.dev/) and [Mark Boulton](https://markboulton.co.uk/journal/anewcanon/).
- **Human-Curated Content & Images**: Jim authors all posts in Obsidian and transfers all photos shown on the site. AI agents are restricted to technical management (infrastructure, build configuration, layout styling, and link validation).

---

## The Concept: "Out of My Lane"

After a 50-year career spanning Arthur Andersen, professional guitar playing, software startups, and data science, retirement is an invitation to explore without professional boundaries. *"How does that work?"* is the core question guiding this site across various interest lanes:

- **Music**: Classical and fingerstyle guitar, piano studies (Kawai ES-8), music theory.
- **STEM & Computing**: Local offline AI (M.E.), Python tools, data analysis, weather observation, electronics.
- **Health & Somatics**: Tai Chi, Alexander Technique, sleep health & periodic limb movement analysis.
- **Craft & Physical Making**: Woodworking, Ulu knife crafting, instrument maintenance.
- **Photography**: Chicago skies, lakefront weather, sunsets, and botanical studies.

---

## Repository Structure

```text
jimcollinsworth.github.io/
├── .agents/
│   ├── agent_rules.md            # LLM agent governance, 3-doc rule & CLI reproducibility
│   └── skills/                   # Project skills (pelican-site-manager, pelican-obsidian-bridge)
├── .github/
│   └── workflows/
│       └── deploy.yml            # Automated CI/CD (pytest audit + Pelican build + Pages deployment)
├── content/                      # Source Markdown (Obsidian Vault drop folder)
│   ├── posts/                    # Long-form posts (Health, Projects, Software, Ideas, Music, Art)
│   ├── pages/                    # Standalone pages (about, ai, links, photos, apps, about-this-site, contact)
│   ├── apps/                     # Standalone interactive mini-apps (photo-viewer, keyword-search)
│   ├── data/                     # Tabular & info static datasets (JSON, CSV, markdown manifests)
│   ├── images/                   # Manually curated photos referenced by posts
│   └── extra/                    # Favicons and verification tokens
├── theme/                        # Custom Pelican Jinja2 theme
│   ├── templates/                # base.html, index.html, article.html, page.html, etc.
│   └── static/css/style.css      # Central stylesheet (zero pills, dark/light mode)
├── archive/                      # Historical Nikola archives, original full-resolution photos, drafts
├── docs/
│   └── cheatsheets/              # Architecture & Content Authoring Cheat Sheets (PDF & Markdown)
│       ├── architecture_flow.pdf # Printable PDF: Publishing pipeline & data flows
│       ├── architecture_flow.md  # Markdown: Architecture diagrams & governance
│       ├── content_authoring.pdf # Printable PDF: Frontmatter & thought evolution
│       └── content_authoring.md  # Markdown: Semantic layout & component mapping
├── releases/                     # Historical release documents (v0.1 to v0.6.11)
├── templates/                    # Authoring templates for Obsidian & editors
│   └── obsidian-post-template.md # Comprehensive post template with commented YAML
├── tests/
│   ├── test_pelican_e2e.py       # End-to-end test suite (build, links, zero-JS, formatting)
│   ├── test_accessibility.py     # WCAG AAA / ARIA / high-contrast audit
│   └── test_playwright_responsive.py # Playwright headless browser & responsive audit
├── tools/
│   ├── screenshots.py            # Multi-resolution screenshot generator (8 viewports)
│   └── generate_cheatsheet_pdfs.py # PDF compiler for cheat sheets via Playwright
├── pelicanconf.py                # Pelican configuration (with Obsidian YAML frontmatter reader)
├── pyproject.toml                # Project dependencies (pelican, markdown, playwright, pytest)
├── output/                       # Generated static HTML (deployed to GitHub Pages)
├── README.md                     # Core document 1: Site overview & guide
├── PLANNING.md                   # Core document 2: Active roadmap & backlog
├── ROADMAP.md                    # Core document 3: Long-term vision & brainstormed ideas
└── JOURNAL.md                    # Core document 4: Chronological changelog
```

---

## Architecture & Authoring Cheat Sheets (Printable PDFs)

Quick-reference visual cheat sheets with Mermaid diagrams are located in [`docs/cheatsheets/`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/):

| Cheat Sheet | Format | Highlights & Contents |
| :--- | :--- | :--- |
| **Site Architecture & Publishing Flow** | [**PDF**](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/architecture_flow.pdf) &bull; [Markdown](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/architecture_flow.md) | End-to-end publishing pipeline, repository map, interactive apps & static data architecture, Antigravity AI pair programming governance, and CLI reference. |
| **Content Authoring & Layout Relationship** | [**PDF**](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/content_authoring.pdf) &bull; [Markdown](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/content_authoring.md) | Thought evolution lifecycle, origin/authorship boundary (Jim's original vs. external works), Pelican YAML frontmatter template, Markdown-to-CSS component mapping, and responsive orientation modes. |

*To regenerate the PDFs at any time: `uv run python tools/generate_cheatsheet_pdfs.py`.*

---

## Developer Utilities & Command Reference

All developer tools and test suites are Python managed via `uv`. Strictly **no Node.js or npm** ever for applications or toolchains (sole exception: `npx skills` for agent skills).

| Utility / Command | Purpose | Example CLI Invocations |
| :--- | :--- | :--- |
| `gh` | Official GitHub CLI for issues, PRs, and native agent skills (`gh skill`) | `gh issue list`<br>`gh issue create --title "..." --body "..."`<br>`gh skill list` |
| `tools/screenshots.py` | Multi-resolution responsive capture across 4 devices & 2 orientations (8 viewports) | `uv run python tools/screenshots.py --page index.html`<br>`uv run python tools/screenshots.py --page about.html --color-scheme dark` |
| `pytest` | End-to-end audit (Pelican build, zero-JS policy, link validation, Playwright browser test) | `uv run pytest -v` |
| `pelican` (build) | Static site compiler | `uv run pelican content -s pelicanconf.py -o output -d` |
| `pelican --listen` | Local live development web server | `uv run pelican --listen -p 8000` |
| `playwright install` | Install headless Chromium browser binary | `uv run playwright install chromium` |


---

## Multi-Resolution Screenshot Utility (`tools/screenshots.py`)

A Playwright utility in Python that captures site pages across **4 device form factors** in both **Portrait and Landscape** orientations (8 viewports total):

| Device Form Factor | Portrait Viewport | Landscape Viewport | Target Device Class |
| :--- | :--- | :--- | :--- |
| **Phone** | 390 × 844 | 844 × 390 | iPhone / Mobile Viewports |
| **Tablet** | 820 × 1180 | 1180 × 820 | iPad / Tablet |
| **Laptop** | 768 × 1366 | 1366 × 768 | 13–15" Laptop Display |
| **Large Desktop / TV** | 1080 × 1920 | 1920 × 1080 | 1080p Desktop Monitor or TV |

### Usage & Examples

```bash
# Capture home page (output/index.html) across all 8 viewports in light mode
uv run python tools/screenshots.py

# Capture any specific page
uv run python tools/screenshots.py --page about.html
uv run python tools/screenshots.py --page posts.html
uv run python tools/screenshots.py --page posts/sleep-movement-evaluation-plan.html

# Emulate dark mode
uv run python tools/screenshots.py --page about.html --color-scheme dark

# Emulate both light and dark modes (16 screenshots total)
uv run python tools/screenshots.py --page index.html --color-scheme both

# Capture above-the-fold viewport only (instead of full page)
uv run python tools/screenshots.py --viewport-only

# Filter to a specific device or orientation
uv run python tools/screenshots.py --device phone --orientation portrait
```

> [!TIP]
> The script automatically creates an interactive visual gallery at `screenshots/<page>/preview.html` where you can inspect all viewports side-by-side or open high-resolution captures in separate tabs.

---

## GitHub CLI (`gh`)

The portable official GitHub CLI is installed at `C:\Users\jimco\bin\gh.exe` and configured in the User `PATH` (no administrator privileges required).

### One-Time Authentication
Run this once from PowerShell or any terminal:
```powershell
gh auth login
```
Select:
1. **GitHub.com**
2. **HTTPS**
3. **Login with a web browser** (opens a one-click confirmation in your browser).

### Common Workflows

```powershell
# List open issues for this repository
gh issue list

# Create a new issue / plan proposal
gh issue create --title "Feature Title" --body "Issue description..."

# View an issue and discussion comments
gh issue view <issue-number>

# Manage agent skills natively (no Node / npm needed)
gh skill list
gh skill search <topic>
gh skill install <repo/skill>
```

---

## Standard CLI Commands


Commands can be run directly in Command Prompt or PowerShell:

### Install Dependencies
```bash
uv sync
```

### Install Playwright Browser Binary
```bash
uv run playwright install chromium
```

### Build Static Site
```bash
uv run pelican content -s pelicanconf.py -o output -d
```

### Local Development Preview
Start Pelican's local web server:
```bash
uv run pelican --listen -p 8000
```
Open `http://localhost:8000` in your browser.

### Run End-to-End Test Suite
```bash
uv run pytest -v
```


---

## Agent Governance: Core Documents & Content Rules

Per `.agents/agent_rules.md`:
1. **Mandatory 4 Governance Documents**: The agent may maintain **only four** root system and planning documents:
   - `README.md` (System overview, architecture, developer utilities, and instructions)
   - `PLANNING.md` (Active backlog, sprint tasks, and near-term milestones)
   - `ROADMAP.md` (Long-term vision, brainstorming, creative ideas, and future possibilities)
   - `JOURNAL.md` (Chronological decision log and technical change records)
2. **Content Ownership**: The agent must **never draft content documents, create content files, or write articles** for Jim. All content authoring and image curation belongs exclusively to Jim.
3. **Agent Rule Authorization**: The agent must **never add or modify rules in `.agents/`** without explicit permission from Jim.
4. **Command Line Standards**: All agent commands must be standard CLI invocations that Jim can run manually.
5. **Toolchain Constraints**: Strictly **no Node.js or npm** ever for applications or toolchains (only exception: `npx skills`).

---

## Web & Markdown Authoring: Semantic Component Guide

This guide defines content formats, Markdown syntax, and how elements map to the site's semantic styling classes in `theme/static/css/style.css`:

### 1. Metadata Mapping: Pelican Engine vs. Obsidian Authoring vs. Site Concept

| Level | Site Concept | Pelican Keyword | Obsidian Property | Multiplicity | Native Pelican Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Provenance** | **Stream** (Mine, AI, Ours, Theirs, Me) | `category` | `category` | **Strictly One** | Generates `/category/{slug}.html`, drives category icons, and maps authorship origin. |
| **Format** | **Post Type** (ESSAY, PROJ, APP, TIL, IDEA) | `type` *(custom)* | `type` (dropdown/text) | **One** | Uppercased shortcode in Jinja2 (`article.type`) altering layout, styling, and navigation without plugins. |
| **Topics** | **Keywords / Topics** (python, audio, tai-chi) | `tags` | `tags` (list) | **Multiple** | Generates `article.tags` list in Jinja2; powers topical indexing and Obsidian tag graph. |
| **Lifecycle** | **Publishing State** (Draft vs. Live) | `status` | `status` | **One** | `published` &rarr; live site; `draft` &rarr; isolated in `output/drafts/` (hidden from live index). |

### 2. Content Formats & Writing Types

| Format | Definition & Characteristics | Location |
| :--- | :--- | :--- |
| **Post / Essay** | Long-form, deep-dive exploration with full context, narrative analysis, and takeaways. | `content/posts/` |
| **Project** | Active, multi-step engineering, coding, or physical build with milestones and deliverables. | `content/posts/` |
| **TIL ("Today I Learned")** | Concise, 1–3 paragraph technical nugget, CLI fix, or quick realization. | Short post in `content/posts/` |
| **Idea / Seedling** | Raw backlog item, question (*"How does that work?"*), or untested hypothesis. | `content/posts/` (Ideas stream) |
| **Shelf / Book Synthesis** | Curated book reflection with core mental models and takeaways. | `content/pages/shelf.md` |
| **Comment / Annotation** | Brief personal reaction or footnote attached to a quote, book, or photo. | Inline callouts (`> Blockquote`) |

### 3. Document Structure & Typography

| Element / Component | Markdown / HTML Syntax | CSS Class / Selector | Visual & Styling Behavior |
| :--- | :--- | :--- | :--- |
| **Site Header** | Generated by template | `.site-header`, `.site-nav` | Top navigation bar with active tab indicator and responsive mobile wrapping. |
| **Document Title** | `# Title` or YAML `title:` | `h1`, `.page-title` | Large serif/sans heading. (Omitted on standalone pages where nav tab indicates location). |
| **Lead / Summary Intro** | `<div class="page-intro">...</div>` | `.page-intro` | Introductory paragraph with slightly larger font (`1.15rem`) and distinct vertical spacing. |
| **Section Headings** | `## Heading 2`, `### Heading 3` | `h2`, `h3`, `h4` | Semantic outline with proportional margins and visual hierarchy. |
| **Body Paragraphs** | Regular text separated by blank lines | `p`, `main p` | Reading measure capped at `max-width: 76ch` with `1.65` line height. |
| **Quotes & Callouts** | `> Blockquote text` | `blockquote` | Warm left accent border (`3px solid var(--accent)`), indented margins, and italicized text. |
| **Post Metadata** | Template-generated from YAML | `.post-meta`, `.post-category`, `.post-date`, `.post-type` | Secondary metadata line displaying the publication date, provenance stream, and post type. |
| **Footer** | Generated by template | `.site-footer`, `.footer-nav` | Bottom section containing site navigation links, license, and copyright. |

### 2. Media, Data & Technical Components

| Element / Component | Markdown / HTML Syntax | CSS Class / Selector | Visual & Styling Behavior |
| :--- | :--- | :--- | :--- |
| **Figures & Captions** | `![Caption text](images/photo.jpg)` | `figure`, `figcaption` | Image container with an italicized, muted caption directly below. |
| **Data Tables** | Standard Markdown pipe tables (`\| Col \|`) | `table`, `th`, `td` | Bordered table with padded cells and shaded header row. |
| **Code Blocks** | ` ```python ... ``` ` | `pre`, `code`, `.highlight` | Monospace code block with syntax highlighting and subtle card background. |
| **Dashboard Cards** | `<div class="dashboard-grid">...</div>` | `.dashboard-grid`, `.dashboard-card` | CSS Grid card layout for metrics, status badges, and telemetry. |
| **Stream Navigation** | `<nav class="stream-nav">` | `.stream-nav`, `.stream-link` | Horizontal navigation across provenance categories (`All`, `Mine`, `Ours`). |

### 3. Responsive Layout & Density Rules

- **Container Scale**: Container width expands from `1080px` on laptops to `1380px` on screens `>= 1360px`.
- **2-Column Magazine Grid (`.desktop-two-col`)**: Two-column layout pairing primary reading streams on the left with secondary spotlights/feeds on the right.
- **Progressive Density**:
  - Desktop/Laptop: Full excerpts, detailed metadata (`.post-detail`).
  - Mobile (`< 640px`): Collapses supplementary details into single-line teasers (`.post-teaser`) with zero JavaScript.
- **Orientation Modes**:
  - **Portrait**: Single-column vertical reading stream.
  - **Landscape**: Side-by-side multi-column presentation.
- **Zero-JS Policy**: HTML5 + CSS. Zero client-side scripts, zero cookies, zero trackers on reading pages.

### 4. Photo Asset Size Management & Sizing Tiers

- **Zero RAW in Repo**: Camera RAW captures and full-resolution original files (> 500 KB) are never stored in the Git repository. Full resolution resolves externally via direct Google Photos / Drive URLs.
- **Two Local Display Tiers**:
  1. **Thumbnail**: ~400px width (~30–50 KB) for filmstrips, grid cards, and mobile views.
  2. **Medium Web**: ~1200–1600px width (~150–300 KB) for post reading measure, homepage spotlight, and photo detail pages.
- **Automated Ingestion**: New photo assets pass through an automated build or optimization step to strip unneeded EXIF bloat and constrain dimensions prior to repo commit.

---

## License

Content and essays &copy; Jim Collinsworth, licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
