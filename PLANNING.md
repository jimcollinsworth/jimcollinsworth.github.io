# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

- [x] **Milestone 10: Multi-Lane Taxonomy & Post-Type Lifecycle Evolution (Completed)**
  - **Multi-Lane Post Assignment**: Extended `pelicanconf.py` and `ObsidianMarkdownReader` to parse multiple pursuit lanes per post (`lanes: [Music, Making]`). Connected `assign_multi_lane_categories` hook to `signals.article_generator_finalized` so articles appear across all assigned lane archive pages (`lanes/music.html`, `lanes/making.html`).
  - **Post-Type Evolution Lineage**: Modeled post lifecycle with a single active `type:` (e.g. `PROJ`) and an optional list of `previous_types:` (e.g. `[IDEA, WIP]`), rendering subtle typographic evolution lineage (`[PROJ] (evolved from IDEA → WIP)`) in post headers.
  - **Strict Lane Taxonomy & Retirement of Ideas/Projects**: Established `AI` as a canonical pursuit lane (`lanes/ai.html`), assigned `M.E.` to `AI`, and permanently retired `Ideas` and `Projects` as lanes since they represent post formats (`[IDEA]`, `[PROJ]`).
  - **Multi-Lane Rendering Across Templates**: Updated `index.html`, `archives.html`, `category.html`, and `article.html` to render all assigned lane links.
  - **Automated Verification**: Updated test suite to verify the existence of `ai.html`, non-existence of `ideas.html` and `projects.html`, multi-lane membership of `digital-piano-enhancements.html`, and post-type evolution rendering.

- [x] **Milestone 9: Post Type Taxonomy & Listing Metadata Display (Completed)**
  - **Curated 28-Type Taxonomy**: Codified short-code post formats across Core & Tech (`TIL`, `WIP`, `URL`, `PROJ`, `APP`, `LOG`, `POST`, `SPEC`, `IDEA`, `OPS`), Media & Sensory (`READ`, `WATCH`, `LISTEN`, `VIEW`), Data & Science (`DATA`, `VIZ`, `PERF`, `ASK`), Outdoors (`HIKE`, `TRIP`, `TOUR`, `WALK`), and Arts (`ART`, `GIG`, `TALK`, `FILM`, `FOOD`, `PIX`).
  - **Content Assignment**: Assigned frontmatter `type:` metadata across all existing posts (`[SPEC]`, `[IDEA]`, `[WIP]`, `[PROJ]`).
  - **Template & CSS Integration**: Rendered `[TYPE] • Date • Lane` across home featured/stream listings, post archives (`posts.html`), category archives, and individual article headers with zero-pills typography.
  - **Automated Verification**: Added `test_post_types_displayed_in_listings` to `tests/test_pelican_e2e.py` (32 of 32 tests passing).

- [x] **Milestone 8: Pelican 4.12.0 Official Content Authoring Baseline & Specification (Completed)**
  - **Canonical Authoring Guide (`docs/content_authoring.md`)**: Codified official Pelican 4.12.0 rules for Articles (`content/posts/`) vs. Pages (`content/pages/`) vs. Static files (`content/images/`), complete YAML frontmatter metadata keywords (`Title`, `Date`, `Category`, `Tags`, `Slug`, `Summary`, `Modified`, `Authors`, `Status`), and internal linking syntax (`{filename}`, `{static}`, `{category}`).
  - **Technical Reference Specification (`.agents/skills/pelican-site-manager/references/pelican_content_spec.md`)**: Authored technical reference covering generator lifecycles, metadata precedence, directive translation, and `ObsidianMarkdownReader` architecture.
  - **Agent Skills Alignment**: Updated `.agents/skills/pelican-site-manager/SKILL.md` and `.agents/skills/pelican-obsidian-bridge/SKILL.md` to reference the canonical guide and reinforced Rule #9 (no push without explicit confirmation).
  - **Repository Documentation**: Linked authoring guidelines directly in `README.md`.

- [x] **Milestone 7: Embedded Applications & DevOps Workbench Integration (Completed)**
  - **Dedicated Embedded Page (`devops.html` & `pipeline-tools.html`)**: Created clean, responsive wrapper embedding the local Gradio + Pixeltable workbench (`http://127.0.0.1:7860`) within the site design system, accessible as both `/devops.html` and `/pipeline-tools.html`.
  - **Status Header & Resilient Fallbacks**: Integrated target status indicators and helpful fallback launch instructions (`cd d:\projects\pipeline-tools; uv run gradio app.py`) for visitors or when the local daemon is offline.
  - **Footer Navigation**: Added explicit `DevOps` navigation link in the site footer (`theme/templates/base.html`).
  - **Automated Test Coverage**: Added `test_devops_and_pipeline_tools_page_structure` to `tests/test_pelican_e2e.py` validating page outputs, iframe target, fallback card, and footer links. Full test suite expanded to 31 passing tests.

- [x] **Milestone 6: Comprehensive Web Accessibility (WCAG 2.1/2.2 AA & AAA, Section 508, ADA) (Completed)**
  - **Skip-to-Content Navigation**: Added `<a href="#main-content" class="skip-link">Skip to main content</a>` that becomes visible on keyboard focus, navigating directly to `<main id="main-content" tabindex="-1">`.
  - **Semantic Landmarks & ARIA**: Implemented standard landmark roles (`role="banner"`, `role="contentinfo"`), unambiguous navigation labels (`aria-label="Main Navigation"`, `aria-label="Footer Navigation"`, `aria-label="Filter posts by lane"`), and screen reader indicators (`aria-current="page"`, `.sr-only`).
  - **High-Contrast Modes & Color Systems**: Built native CSS `@media (prefers-contrast: more)` and `@media (prefers-color-scheme: dark) and (prefers-contrast: more)` modes delivering 7:1+ AAA contrast ratios, forced underline links, and enhanced focus indicators. Added `@media (forced-colors: active)` support for Windows High Contrast Mode.
  - **Fluid Typography & Text Scaling**: Enforced relative percentage base sizing (`html { font-size: 100%; }`) preserving user browser font scaling up to 200%+ for low-vision and elderly users (WCAG 1.4.4).
  - **Reduced Motion**: Added `@media (prefers-reduced-motion: reduce)` disabling non-essential transitions and animations for users with vestibular disorders.
  - **Touch Targets**: Guaranteed interactive targets conform to WCAG 2.5.8 target size criteria (`min-height: 38px`, ample padding).
  - **Zero-JS Preservation**: All accessibility behaviors operate with pure semantic HTML5 and modern CSS media queries without client-side JavaScript.
  - **Automated Accessibility Test Suite (`tests/test_accessibility.py`)**: Added 9 dedicated automated tests validating lang attributes, skip links, ARIA landmarks, active page attributes, image alt tags, CSS rules, touch targets, and zero-JS policy. Total test suite expanded to 28 passing tests.

- [x] **Milestone 5: Playwright Testing & Multi-Resolution Responsive Suite (Completed)**
  - **Pure Python Testing Ecosystem**: Installed `playwright` and `pytest-playwright` managed strictly via `uv` with zero Node.js / npm dependencies.
  - **Multi-Resolution Screenshot Utility (`tools/screenshots.py`)**: Built an automated screenshot generator capturing any page across 4 screen sizes and 2 orientations (Phone, Tablet, Laptop, Desktop/TV in Portrait and Landscape = 8 viewports), supporting light/dark theme emulation and interactive HTML previews.
  - **Automated Responsive Tests (`tests/test_playwright_responsive.py`)**: Added test coverage verifying that pages load in headless Chromium across mobile and desktop without unhandled console errors or layout breaks.
  - **CI/CD Integration**: Configured GitHub Actions workflow (`.github/workflows/deploy.yml`) to provision the Playwright Chromium binary and run the complete 19-test test suite on every commit to `main`.
  - **Developer Tooling Inventory**: Documented utilities table and standard CLI workflows in `README.md`.

- [x] **Milestone 4: Magazine Multi-Column Layout, Orientation Modes & Progressive Density (Completed)**
  - Expanded desktop/laptop container scale eliminating excessive empty gutters (`--max-width: 1080px` laptop, `1380px` ultra-wide).
  - Built pure CSS 2-column magazine grid (`.desktop-two-col`) pairing Featured Post + Recent Reads on the left with Recent Stream + Photo spotlight on the right.
  - Implemented distinct orientation modes: single-column reading flow in portrait; 2-column split layout in landscape.
  - Implemented progressive density rules (`.post-teaser` / `.post-detail`) giving full excerpts on desktop/laptop and concise single-line teasers on mobile (`< 640px`) with zero JavaScript.
  - Multi-viewport visual verification completed across ultra-wide desktop, laptop, tablet landscape, tablet portrait, and mobile portrait.

- [x] **Milestone 3: Pelican Static Site Generator Integration (Completed)**
  - Reorganized site source into structured `content/` drop folders (`content/posts/`, `content/pages/`, `content/images/`).
  - Created custom Jinja2 Pelican theme (`theme/`) preserving zero-JavaScript policy and editorial design system.
  - **Title Deduplication**: Removed redundant `<h1>` page titles on standalone pages (`about.html`, `reads.html`, `gallery.html`); the highlighted menu item serves as the title.
  - **Lane Formatting**: Removed pill/badge styling; pursuit lanes are styled as understated, clean text links.
  - **Obsidian Frontmatter Support**: Integrated `ObsidianMarkdownReader` into `pelicanconf.py` to seamlessly parse YAML frontmatter.
  - **End-to-End Test Suite**: Implemented `tests/test_pelican_e2e.py` verifying Pelican build execution, core page outputs, title deduplication, zero-pills styling, content flow, and link/asset integrity.
  - **Automated CI/CD**: Updated `.github/workflows/deploy.yml` to install dependencies via `uv`, run tests, build with Pelican, and deploy `output/` to GitHub Pages.

- [x] **Milestone 2: Calvin/MacWright UI Overhaul & Bookshelf (Completed)**
  - Redesigned typography and post listing rhythm inspired by Calvin French-Owen (`calv.info`).
  - Implemented dedicated Bookshelf page (`reads.html`) with reading synthesis and mental models.
  - Implemented MacWright-style clean photo stream (`gallery.html`).
  - Refactored `index.html` into a clean dashboard of recent posts, reads, and photo spotlight.
  - Consolidated full bio and "Lanes" taxonomy into `about.html`.
  - Streamlined main navigation: `Home`, `About`, `Posts`, `Reads`, `Gallery`.

- [x] **Milestone 1: Clean Foundation (Completed)**
  - Safely archived legacy Nikola compiler assets, drafts, notes, and photo galleries into `archive/`.
  - Established `.agents/agent_rules.md` with the mandatory 3-document rule and strict content boundary (agent never drafts content).
  - Implemented zero-JavaScript, pure HTML5 + modern CSS design system.

---

## Core Content & Image Curation Policies

### Manual Image Transfer & Zero AI Content Generation
- **100% Human Curated**: Jim explicitly selects and manually transfers every photo into `content/images/` before referencing it in blog posts.
- **Strict Role Boundary**: AI agents are strictly restricted to **content management** (templates, CSS, build configuration, link auditing). AI agents **never generate, draft, or edit post content or images**.
- **Rule 12 Mandatory AI Attribution**: Whenever an AI model creates, co-authors, or is suspected of contributing to content or summaries, it must be credited in the frontmatter `Authors:` field with its explicit model ID (e.g. `LLM-Gemini3.8`, `LLM-Qwen3.5`).
- **External Photo Galleries**: Blog posts include selected key photos directly in `<figure>` tags, with links out to full, high-resolution albums on Google Photos (e.g. [OutOfMyLane Google Photos album](https://photos.app.goo.gl/yGTTSd3hnw1pqCPo8)).
- **Future Custom Applications**: Roadmap item for custom project applications dedicated to photo search, indexing, and navigation.

---

## The 12 Lanes

1. Music making
2. Software
3. Life sciences
4. Engineering
5. Photography
6. Making
7. Law
8. Art
9. Politics
10. Data
11. Exercise
12. Anatomy

---

## Technical & Design Backlog (Nice to Have / Optional)

- [ ] **Zero-JS Google Sheets + Apps Script Commenting Pipeline with LLM Summarization (GitHub Issue #9)**: Deploy private spam-quarantined reader interaction pipeline. Plain HTML form POSTs to Google Apps Script web app, records all raw submissions to a private Google Sheet ("garbage and good stuff"), pre-build script syncs entries, Gemini / `pipeline-tools` triages spam and synthesizes editorial discussion digest, Pelican renders static HTML. Includes dedicated agent skill (`comment-pipeline-manager`).
- [ ] **Build-Time LLM Synthesizer & "My Odyssey in Haiku" (GitHub Issue #7)**: Connect local `pipeline-tools` (Pixeltable / Ollama / Gemini) to Pelican build hooks (`pelicanconf.py` / `tools/synthesizer.py`) to generate poetic haiku chronicles and prompt progression narratives from `JOURNAL.md` with Zero-JS static output.
- [ ] **Custom Photo Navigation & Search Mini-App**: Client-side interactive explorer for high-volume photo archives and tags.
- [ ] **Interactive Projects Showcase**: Standalone mini-apps (e.g. Circle of Fifths music visualizer, USGS live earthquakes monitor).
- [ ] **Pure CSS Tag Filtering**: Explore CSS `:target` or radio-state filtering for journal entries without JavaScript.
- [ ] **Pure CSS Image Modal**: Lightweight lightbox using CSS `:target` for high-res photo inspection.
- [ ] **Print Stylesheet**: Add `@media print` rules for clean hard-copy printing.

