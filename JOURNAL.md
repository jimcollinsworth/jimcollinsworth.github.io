# Site Journal & Decision Log: jimcollinsworth.github.io

> Chronological log of architectural decisions, site milestones, and design changes. Maintained under the 3-document agent rule.

---

## 2026-09-11 — Rule 12 AI Author Attribution & Zero-JS Google Sheets Commenting Pipeline Architecture

### Context & Need
- Jim directed formalizing an explicit agent rule mandating transparent attribution whenever AI authors, co-authors, or is suspected of contributing to content, including specific model IDs (`LLM-Gemini3.8`, `LLM-Qwen3.5`).
- Jim evaluated reader interaction architectures: rejected public GitHub Issues due to vulnerability to automated spam flooding and manual cleanup burdens; evaluated Formspree/Gmail; selected **Google Apps Script + Google Sheets** as the ideal zero-JS private submission buffer where all raw input ("garbage and good stuff") can be reviewed in a tabular dashboard.
- Needed a comprehensive GitHub Issue detailing the complete architecture, test plan, LLM summarization pipeline, and agent skills.

### Decisions & Actions Taken
1. **Rule 12 Codified in `.agents/agent_rules.md`**:
   - Added Rule 12: Mandatory AI & LLM Author Attribution.
   - Mandated specific model IDs prefixed with `LLM-` (e.g. `LLM-Gemini3.8`, `LLM-Qwen3.5`, `LLM-Claude3.7`) in `Authors:` frontmatter.
   - Distinguished primary vs. supporting author placement and prohibited deceptive masking.
   - Documented in `docs/content_authoring.md` and `PLANNING.md`.
2. **GitHub Issue #9 Created**:
   - Filed [Issue #9 on `jimcollinsworth.github.io`](https://github.com/jimcollinsworth/jimcollinsworth.github.io/issues/9) via authenticated `antigravity-jc-bot`: *Architecture: Zero-JS Google Sheets + Apps Script Commenting Pipeline with LLM Summarization*.
   - Outlined trade-off analysis across GitHub Issues, Gmail, Formspree, and Google Sheets.
   - Detailed specifications for:
     - Client-side semantic HTML5 form with hidden honeypot.
     - Google Apps Script web app endpoint (`doPost(e)`).
     - Google Sheets 9-column schema.
     - Pre-build ingestion utility (`tools/sync_sheet_comments.py`).
     - Multi-stage LLM triage and editorial synthesis pipeline (Gemini / `pipeline-tools`).
     - Pelican static HTML integration.
     - Planned agent skill (`comment-pipeline-manager`) and end-to-end test suite.
3. **Site & Documentation Updates**:
   - Updated `content/pages/about.md` with a "Contact & Reader Feedback" section explaining the zero-JS Google Sheets interaction architecture and linking to Issue #9.
   - Documented pipeline in Section 6 of `docs/content_authoring.md`.
   - Verified that all 33 automated tests pass.

---

## 2026-09-10 — Multi-Lane Taxonomy & Post-Type Lifecycle Evolution (Zero-Pills Typography)

### Context & Need
- Jim established crucial requirements for content modeling:
  1. **Post-Type Evolution Lifecycle**: Posts possess a single active `type` (e.g. `PROJ`), but may have an evolutionary lineage of `previous_types` (e.g. `[IDEA, WIP]`).
  2. **Multi-Lane Support**: Posts can belong to multiple pursuit lanes simultaneously (e.g. `lanes: [Music, Making]`).
  3. **Lane Taxonomy Corrections**: `M.E.` belongs to the `AI` pursuit lane. `Ideas` and `Projects` are permanently retired as lanes because they are post types (`[IDEA]`, `[PROJ]`).

### Decisions & Actions Taken
1. **Pelican Reader & Generator Hooks (`pelicanconf.py`)**:
   - Extended `ObsidianMarkdownReader` to parse `lanes` frontmatter (supporting YAML lists or comma-separated strings), set the primary category for Pelican's native internals, and instantiate `Category` objects for each assigned lane.
   - Parsed `previous_types` and exposed evolution lineage to templates.
   - Connected `assign_multi_lane_categories` callback to `signals.article_generator_finalized` to dynamically append multi-lane posts to each corresponding lane's category list and sort chronologically.
2. **Frontmatter Refactoring**:
   - `m-e-offline-ai-companion.md`: Assigned to `AI` lane as `IDEA` (eliminated `Ideas`).
   - `digital-piano-enhancements.md`: Assigned to both `Music` and `Making` lanes, with type `PROJ` and previous types `[IDEA, WIP]` (eliminated `Projects`).
   - `cordoba-stage-guitar.md`: Assigned to `Music` lane, type `WIP`, previous types `[IDEA]`.
   - `sleep-movement-evaluation-plan.md`: Assigned to `Health` lane, type `SPEC`, previous types `[IDEA, LOG]`.
   - `ulu-knife-handle.md`: Assigned to `Making` lane, type `PROJ`, previous types `[WIP]`.
3. **Template & Design System Updates**:
   - Updated `index.html`, `archives.html` (`posts.html`), `category.html`, and `article.html` to render all assigned lanes.
   - In `article.html`, rendered the post's evolution lineage (`[PROJ] (evolved from IDEA → WIP)`) in subtle monospace typography (`.post-type-evolution`).
   - Synced CSS classes across `theme/static/css/style.css`, `theme/css/style.css`, and `assets/css/style.css`.
4. **Repository Cleanup**:
   - Deleted legacy root-level archive files `lanes/ideas.html` and `lanes/projects.html`.
   - Synced root and generated `lanes/ai.html`.

---

## 2026-09-10 — Post Type Taxonomy & Listing Metadata Display (Zero-Pills Typography)

### Context & Need
- Jim directed creating a concise, acronym-focused post type classification to expose post formats (TIL, WIP, Project, Read, etc.) alongside dates and pursuit lanes on post lists and titles.
- Filtered a proposed 30-type taxonomy down to 28 curated types: retained `WIP`, removed `REV`, and added four sensory/media consumption channels (`READ`, `WATCH`, `LISTEN`, `VIEW`).

### Decisions & Actions Taken
1. **Curated 28-Type Taxonomy**:
   - Codified in `docs/content_authoring.md`:
     - **Core & Tech**: `TIL`, `WIP`, `URL`, `PROJ`, `APP`, `LOG`, `POST`, `SPEC`, `IDEA`, `OPS`.
     - **Media & Sensory**: `READ`, `WATCH`, `LISTEN`, `VIEW`.
     - **Data & Science**: `DATA`, `VIZ`, `PERF`, `ASK`.
     - **Outdoors & Life**: `HIKE`, `TRIP`, `TOUR`, `WALK`.
     - **Arts & Culture**: `ART`, `GIG`, `TALK`, `FILM`, `FOOD`, `PIX`.
2. **Content Frontmatter Assignment**:
   - Assigned `type:` across all existing posts in `content/posts/`: `[SPEC]` for sleep evaluation plan, `[IDEA]` for M.E. companion, `[WIP]` for Cordoba guitar setup, `[PROJ]` for digital piano and ulu knife handle.
3. **Template & CSS Integration**:
   - Updated `index.html`, `archives.html` (`posts.html`), `category.html`, and `article.html` to render `[TYPE] • Date • Lane`.
   - Added `.post-type` CSS styling using monospace font and subtle muted color preserving the zero-pills editorial design.
4. **Automated Verification**:
   - Added `test_post_types_displayed_in_listings` to `tests/test_pelican_e2e.py`. Total test suite expanded to 32 passing tests.

---

## 2026-09-10 — Governance Rules 10 & 11: Anti-Tunneling and Strict Workspace Isolation

### Context & Need
- Jim directed adding strong, explicit rules prohibiting any use of Tailscale, tunneling, or unauthorized network access techniques, as well as strict isolation to the current project directory.
- Codified that only Jim modifies permissions, access, or network configuration. Agents must stay inside `d:\projects\jimcollinsworth.github.io` and ask with explicit reasoning before ever searching or working outside.

### Decisions & Actions Taken
1. **Rule 10: Prohibition of Network Tunneling & Privilege Alteration**:
   - Strictly forbids Tailscale, ngrok, Cloudflare tunnels, reverse SSH tunnels, frpc, Gradio `share=True` tunneling, and any proxy workarounds.
   - Forbids backdoor routing, firewall bypasses, or attempting privilege escalation.
   - Enforces an ask-first policy: only Jim manages access and permissions.
2. **Rule 11: Workspace Isolation & Project Boundary**:
   - Mandates that agents remain strictly within the project directory (`d:\projects\jimcollinsworth.github.io`).
   - Forbids searching parent folders, user profiles, or system directories without first stating clear reasoning and receiving Jim's explicit approval.
3. **Updated `.agents/agent_rules.md`**:
   - Added Sections 10 and 11 directly to the authoritative rule file.

---

## 2026-09-09 — Adoption of Pelican 4.12.0 Official Content Authoring & Metadata Standards

### Context & Need
- Jim established official Pelican 4.12.0 documentation as the project-wide baseline standard for content authoring, metadata keywords, intra-site linking syntax, and reader behavior.
- Clear alignment was needed between Jim's Obsidian note-taking environment and Pelican's compiler model, along with agent skills and references to maintain consistency.

### Decisions & Actions Taken
1. **Canonical Content Authoring Guide (`docs/content_authoring.md`)**:
   - Codified the distinction between **Articles** (`content/posts/*.md`), **Pages** (`content/pages/*.md`), and **Static Files** (`content/images/`, `content/extra/`).
   - Documented the full metadata keyword specification (`Title`, `Date`, `Category`, `Tags`, `Slug`, `Authors`, `Summary`, `Modified`, `Status`).
   - Defined intra-site compile-time linking directives: `{filename}` for articles/pages, `{static}` for unmanaged assets, `{attach}` for article-attached media, and `{category}` for Pursuit Lane archives.
   - Documented Pygments code highlighting via Pelican's `codehilite` extension.
2. **Technical Reference Specification (`.agents/skills/pelican-site-manager/references/pelican_content_spec.md`)**:
   - Documented the generator lifecycle pipeline, metadata precedence rules, URL rewrite behavior, and the `ObsidianMarkdownReader` architecture.
3. **Agent Skills & Governance Updates**:
   - Updated `.agents/skills/pelican-site-manager/SKILL.md` with Section 6 referencing the canonical specifications.
   - Updated `.agents/skills/pelican-obsidian-bridge/SKILL.md` with Section 4 linking to authoring guides and reinforcing Rule #9 (no push without explicit confirmation).
   - Documented the authoring baseline in `README.md` and added Milestone 8 to `PLANNING.md`.

---

## 2026-09-09 — Embedded Applications & Pipeline Tools Workbench Integration

### Context & Need
- Jim directed adding the embedded application architecture to `PLANNING.md`, `ROADMAP.md`, and automated test suites, connecting the personal static site with the local `pipeline-tools` multimodal workbench (`d:\projects\pipeline-tools`).
- Evaluated options for running embedded PostgreSQL on hosted Hugging Face Spaces vs. local embedded instances vs. external serverless PostgreSQL.

### Decisions & Actions Taken
1. **Dedicated Cockpit Page (`content/pages/devops.md` -> `devops.html` & `pipeline-tools.html`)**:
   - Created clean, responsive page embedding the local Gradio workbench (`http://127.0.0.1:7860`) inside an `<iframe>` styled with site borders, card background, status bar, and clear `<h1>DevOps Workbench</h1>` title.
   - Built a clear offline fallback card documenting the PowerShell command (`cd d:\projects\pipeline-tools; uv run gradio app.py`) and direct link.
   - Added explicit **DevOps** link to the site footer navigation (`theme/templates/base.html`).
2. **PostgreSQL & Hugging Face Spaces Architectural Analysis**:
   - Documented in `ROADMAP.md`: Free-tier Hugging Face Spaces have ephemeral storage, causing embedded PostgreSQL databases to wipe on container sleep/restart unless persistent SSD storage ($5/mo) is provisioned.
   - Recommended pairing Hugging Face with free-tier serverless PostgreSQL (**Neon.tech** or **Supabase**) to persist Pixeltable tables indefinitely across container restarts at zero cost.
3. **Automated E2E Tests**:
   - Added `test_devops_and_pipeline_tools_page_structure` to `tests/test_pelican_e2e.py` validating output existence of `devops.html`, iframe URL, fallback commands, and footer link integrity. Total test suite expanded to 31 passing tests.

---

## 2026-09-09 — In-Page Accessibility & Theme Switchers (Zero-JS CSS :has)

### Context & Need
- Jim requested in-page, icon-based switchers to toggle light/dark theme, high-contrast mode, and text size directly on the site, while clarifying how dark-mode screenshots had been generated previously.
- Previous dark mode operated via OS media queries (`prefers-color-scheme: dark`) emulated by Playwright. Adding manual on-page controls required a solution that strictly preserved the Zero-JS architecture without requiring client-side `<script>` tags.

### Decisions & Actions Taken
1. **Pure CSS `:has()` Switcher Architecture**:
   - Added semantic `<input type="checkbox">` toggles at the top of `<body>` (`#theme-toggle`, `#contrast-toggle`, `#text-size-toggle`) with `.sr-only` accessibility styling.
   - Built a `.site-controls` button group in the header with 3 accessible icon labels:
     - **Theme Switcher** (`for="theme-toggle"`): Displays SVG Moon in light mode (to trigger dark) and SVG Sun in dark mode (to trigger light). Flips `--bg`, `--text`, `--link`, and cards via `body:has(#theme-toggle:checked)`.
     - **High-Contrast Switcher** (`for="contrast-toggle"`): SVG Contrast symbol (`◐`). Triggers pure black/white high-contrast palettes, forced link underlines, and heavy borders.
     - **Text Size Switcher** (`for="text-size-toggle"`): SVG Typography symbol (`aA`). Scales font sizing up to `1.32rem` with comfortable line height across body and headings.
2. **Accessible Interaction & Visual Feedback**:
   - Each button has minimum 38x38px touch targets, hover transitions, active pressed background states when toggled, and keyboard `:focus-visible` rings.
3. **Automated Testing & Interactive Verification**:
   - Added `test_mode_switchers_present_and_accessible` to `tests/test_accessibility.py`.
   - Added `test_in_page_mode_switchers_interactive` to `tests/test_playwright_responsive.py` verifying real browser clicks on the toggles successfully transition colors and font sizes.
   - Total test suite now stands at 30 passing tests.

---

## 2026-09-09 — Governance Rule: Remote Push Confirmation Requirement

### Context & Decision
- Jim established a strict operational rule prohibiting automated or autonomous `git push` commands.
- **Decision**: Added Section 9 to `.agents/agent_rules.md`. Pushes to remote mutate shared repository state, trigger GitHub Actions CI/CD workflows, and deploy live artifacts to GitHub Pages. The agent may build, test, and commit locally, but must always pause and request explicit confirmation from Jim before executing any `git push`.

---

## 2026-09-09 — Comprehensive Web Accessibility Implementation (WCAG 2.1/2.2 AAA & Zero-JS)

### Context & Need
- Jim requested addressing GitHub Issue #1 ("add accessibility to the site") filed on `jimcollinsworth/jimcollinsworth.github.io`.
- Site required full compliance with accessibility standards (WCAG 2.1/2.2 AA and AAA, Section 508, ADA) across keyboard navigation, screen reader semantic structure, high-contrast modes, fluid typography scaling, and vestibular motion reduction while strictly maintaining the zero client-side JavaScript architecture.

### Decisions & Actions Taken
1. **Semantic HTML5 & ARIA Landmarks**:
   - Added skip-to-content navigation (`<a href="#main-content" class="skip-link">Skip to main content</a>`) on every page, with immediate focus shifting to `<main id="main-content" tabindex="-1">`.
   - Added landmark roles (`role="banner"`, `role="contentinfo"`), unambiguous ARIA navigation labels (`aria-label="Main Navigation"`, `aria-label="Footer Navigation"`, `aria-label="Filter posts by lane"`), and screen reader indicators (`aria-current="page"`, `.sr-only`).
2. **WCAG AAA Contrast Palette & Accessible Focus Rings**:
   - Upgraded link and text contrast ratios to exceed 7:1 (light link `#8a3710` at 7.2:1, dark link `#e2955a` at 7.3:1).
   - Implemented high-visibility 3px `:focus-visible` outline rings with 3px offsets across all interactive elements.
3. **Adaptive Accessibility Modes (Native CSS)**:
   - Added `@media (prefers-contrast: more)` and `@media (prefers-color-scheme: dark) and (prefers-contrast: more)` for pure black/white high-contrast themes and forced link underlines.
   - Added `@media (forced-colors: active)` for Windows High Contrast Mode system color compatibility.
   - Added `@media (prefers-reduced-motion: reduce)` to disable transitions and animations for users with vestibular sensitivities.
4. **Fluid Typography & Touch Sizing**:
   - Replaced fixed mobile pixel root sizing with relative percentages (`html { font-size: 100%; }` and mobile `97%`), ensuring seamless browser text zoom up to 200%+ without layout clipping (WCAG 1.4.4).
   - Applied minimum 38px touch targets and padding on navigation items.
5. **Automated Accessibility Test Suite (`tests/test_accessibility.py`)**:
   - Created 9 automated pytest tests covering lang attributes, skip links, landmarks, active nav tabs, image alt attributes, zero-JS policy, CSS accessibility rules, and touch targets.
   - Total test suite now stands at 28 passing tests.

---

## 2026-09-09 — Long-Term Roadmap Creation, Governance Alignment, & Visual Verification Report

### Context & Decisions
1. **Created `ROADMAP.md`**:
   - Established a dedicated long-term vision, brainstorming, and creative sandbox document.
   - Synthesized Jim's foundational tenets with creative concepts (Circle of Fifths music visualizer, USGS live earthquake tracker, high-volume photo archive navigation mini-app, M.E. local AI companion, and sleep/somatic movement tracking).
   - Added speculative technical wishlists (zero-JS search index, pure SVG fretboard charts, Lake Michigan weather chronicles, offline PWA archive, micro-zines).
2. **Strict Agent Governance Rule in `.agents/agent_rules.md`**:
   - **Removed 8-viewport rule** from agent guidelines; confirmed it is a specific tool option on `tools/screenshots.py`.
   - **Added strict rule**: The agent must **never add, modify, or append rules or files in `.agents/` without explicit permission from Jim**. Jim will explicitly request specific rules to be added.
   - **Added strict Node/npm rule**: No Node.js or npm ever for applications or toolchains; the only current exception is `npx skills`.
   - Updated governance docs to recognize `ROADMAP.md` alongside `README.md`, `PLANNING.md`, and `JOURNAL.md`.
3. **Generated Visual Verification Report (`reports/responsive_screenshots_report.md`)**:
   - Embedded 24 multi-resolution screenshot captures across 3 core pages (`index.html`, `about.html`, `posts.html`) covering all 8 viewports in light and dark modes.
   - Staged all assets and submitted to GitHub for Jim's review.

---

## 2026-09-09 — Playwright Testing & Multi-Resolution Responsive Tooling

### Context & Need
- Jim requested visual verification across all display sizes and orientations: Phone, Tablet, Laptop, and Large Desktop / TV, in both Portrait and Landscape (8 viewports total).
- Jim mandated 100% Python-based tooling (via `uv`) and strictly **no Node.js / npm**.
- Formalized testing standards to ensure continuous multi-resolution visual sanity, zero-JS policy enforcement, and CLI command transparency.

### Decisions & Actions Taken
1. **Installed Python Playwright & Pytest Suite**:
   - Added `playwright>=1.62.0` and `pytest-playwright>=0.9.0` to `pyproject.toml` dev group using `uv`.
   - Installed headless Chromium browser binary (`uv run playwright install chromium`).
2. **Built Multi-Resolution Screenshot Utility (`tools/screenshots.py`)**:
   - Automated 4 device form factors x 2 orientations (8 viewports):
     - **Phone**: 390x844 (portrait) / 844x390 (landscape)
     - **Tablet**: 820x1180 (portrait) / 1180x820 (landscape)
     - **Laptop**: 768x1366 (portrait) / 1366x768 (landscape)
     - **Large Desktop / TV**: 1080x1920 (portrait) / 1920x1080 (landscape)
   - Added CLI support for `--page` (defaults to `index.html`), `--color-scheme` (`light`, `dark`, `both`), `--viewport-only`, `--device`, and `--orientation`.
   - Generates an interactive visual inspection HTML gallery (`screenshots/<page>/preview.html`).
3. **Automated Playwright Responsive Tests (`tests/test_playwright_responsive.py`)**:
   - Created headless Chromium tests verifying that core pages (`index.html`, `about.html`, `posts.html`, `reads.html`, `gallery.html`) render cleanly across mobile and desktop without uncaught console errors, 404 assets, or layout exceptions.
   - Verified that `tools/screenshots.py` executes successfully in automated testing.
   - Full test suite now contains 19 passing tests (`uv run pytest -v`).
4. **CI/CD Alignment (`.github/workflows/deploy.yml`)**:
   - Added Playwright Chromium installation step (`uv run playwright install --with-deps chromium`) to GitHub Actions workflow so full browser audits run automatically on every push.
5. **Documentation & Utilities Inventory**:
   - Added "Developer Utilities & Command Reference" to `README.md` and updated `PLANNING.md`.

---

## 2026-09-08 — Magazine Multi-Column Desktop Grid, Orientation Adaptation & Progressive Density

### Decisions & Actions Taken
1. **Container Scale Expansion & Ultra-Wide Magazine Grid**:
   - Expanded container width scale from narrow `720px` to fluid `1080px` (standard desktop/laptop) and `1380px` (supersize desktop `>= 1360px`).
   - Implemented `.desktop-two-col` CSS grid (1.25fr/1fr on laptops/landscape, 1.3fr/1fr on wide desktop) structuring `index.html` with Featured Post + Recent Reads in the primary column and Recent Posts stream + Photo spotlight in the secondary column.
   - Constrained all body paragraphs to `max-width: 76ch` to guarantee optimal reading measure and typographic rhythm regardless of viewport width.
2. **Orientation-Driven Adaptations**:
   - Built pure CSS media queries combining width and orientation: `@media (min-width: 960px), (min-width: 720px) and (orientation: landscape)`.
   - Portrait orientation displays as a focused single-column reading mode, while landscape orientation leverages screen width with side-by-side reading and spotlight streams.
3. **Progressive Information Density**:
   - Added semantic markup classes `.post-teaser` and `.post-detail`.
   - On desktops/laptops, full excerpts and metadata are displayed; on mobile viewports (`< 640px`), secondary detail blocks are automatically hidden to keep feeds concise and scannable without requiring client-side JavaScript.
4. **Visual, Pelican SSG, & Zero-JS Verification**:
   - Integrated changes into Pelican theme templates (`theme/templates/index.html`) and static CSS (`theme/static/css/style.css`).
   - Verified 100% Zero-JS compliance (0 `<script>` tags across compiled output).
   - Validated all 8 end-to-end automated tests with `uv run pytest -v`.
   - Captured and verified multi-viewport visual screenshots (1600x1000 ultra-wide, 1200x800 laptop, 1024x768 tablet landscape, 768x1024 tablet portrait, 500x880 mobile portrait).

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
