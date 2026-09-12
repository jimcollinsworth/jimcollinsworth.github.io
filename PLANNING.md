# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

- [x] **Milestone 19: Dynamic Mobile Dropdown Menu in Portrait Mode (Completed - Release v0.6.5)**
  - Implemented dynamic hiding dropdown menu in mobile portrait mode using 100% pure HTML5 `<details>` and `<summary>` (Zero-JS).
  - Dynamic Jinja2 `namespace` logic identifies active section and displays it on the closed button (`[ Home ▾ ]`, `[ Posts ▾ ]`, `[ About ▾ ]`, `[ Site ▾ ]`, etc.).
  - Flattened mobile portrait header to strictly 1 row (~40px height), completely eliminating 3-4 row wrapping.
  - Floating dropdown card styled with subtle shadow, border, and active state highlights; meets WCAG 2.1 AAA touch targets (`min-height: 38px`).
  - Added automated Playwright tests `test_mobile_dynamic_dropdown_portrait` and `test_navigation_mode_switching_by_viewport` (51/51 passing).
  - Synchronized `pyproject.toml`, `about-this-site.md`, generated `releases/v0.6.5.md`.

- [x] **Milestone 18: Compact Mobile Header, Streamlined Dates & Dense Post Listings (Completed - Release v0.6.4)**
  - Flattened header on phone landscape (`@media (orientation: landscape) and (max-height: 500px)`) to strictly 1 line max under 45px total height (`Jim Collinsworth` | `nav links` | `controls`), freeing >150px of vertical reading space.
  - Hidden `.site-tagline` ("Out of My Lane") on mobile and landscape phones to conserve vertical reading space.
  - Re-architected mobile portrait header into a compact 2-row grid: Row 1 (`Jim Collinsworth` + `site-controls`) and Row 2 (`site-nav` across full width).
  - Streamlined dates across templates to concise Month Year format (`%b %y`, e.g. `Aug 26`, `Sep 23`).
  - Removed visual evolution lineage (`(evolved from ...)`) from post headers and listings.
  - Implemented dense mobile post listings: clamped post descriptions to 2 lines max with `-webkit-line-clamp: 2`, reduced vertical spacing to 0.75rem with clean separators.
  - Tabled dynamic hiding dropdown menu and `[VIEW]` vs `VIEW` discussion for future milestones.
  - Added automated Playwright tests `test_mobile_header_compact_and_landscape_single_line` and `test_streamlined_date_formats` (49/49 passing).
  - Synchronized `pyproject.toml`, `about-this-site.md`, generated `releases/v0.6.4.md`.

- [x] **Milestone 17: Responsive Image Containment & Edge-to-Edge Photo Stream (Completed - Release v0.6.3)**
  - Fixed layout blowout in posts (e.g. Modern Wing 2,108px images) by enforcing universal fluid media containment (`img, picture, video, canvas { max-width: 100%; height: auto; }`).
  - Added semantic editorial `<figure>` and `<figcaption>` base styling with subtle borders, border radiuses, and readable typography.
  - Implemented edge-to-edge zero-gutter display for photo albums (`.photo-stream`) on mobile (< 640px) and tablet (< 1024px) screens (`margin-left: -1rem; margin-right: -1rem; width: calc(100% + 2rem)`), while preserving caption padding.
  - Updated category icons to Jim's choices: feather quill (`feather`) for `Mine` and robot head (`bot`) for `AI`.
  - Added automated Playwright viewport containment tests (`test_images_fit_viewport_width`) verifying 0 horizontal scroll overflow and bounded image dimensions across viewports.
  - Updated test suite to 47/47 passing tests, synchronized `about-this-site.md`, `pyproject.toml`, and generated `releases/v0.6.3.md`.

- [x] **Milestone 16: 'Me' Category, Downlow Presentation, Post Iconography & Configurable Menu (Completed - Release v0.6.2)**
  - Added **`Me`** provenance category for autobiographical notes, personal biodata (Fitbit/sleep/health), bookmarks, and self-written reflections.
  - Renamed **`AI Generated`** &rarr; **`AI`**.
  - Kept categories "on the downlow": removed `.stream-nav` category lists from `posts.html` and `category/*.html`, and removed `.footer-categories` from the site footer.
  - Documented the 5 provenance categories (`Me`, `Mine`, `AI`, `Ours`, `Theirs`) on `content/pages/about.md`.
  - Introduced subtle 13×13px inline SVG category icons next to posts in archive listings, index feeds, and article headers (`Me`: 👤, `Mine`: 🖋️, `AI`: ✦, `Ours`: 👥, `Theirs`: ❝) with `<title>` tooltips and screen-reader `aria-label`s.
  - Implemented configurable top navigation menu via Pelican's `MENUITEMS` with permanent core items (`Home`, `About`, `Posts`) and page frontmatter opt-in (`menu: true`, `menu_order: ...`).
  - Resolved artifact screenshot preview rendering by standardizing URIs to `file:///C:/Users/...`.
  - Synchronized test suites, governance documents, and bumped version to `v0.6.2`.

- [x] **Milestone 15: Provenance Categories, Topic-Driven Decoupling & Streams Navigation (Completed - Release v0.6.1)**
  - Replaced rigid "lanes" taxonomy with 4 mutually-exclusive Provenance Categories: `Mine`, `AI Generated`, `Ours`, `Theirs`.
  - Re-aligned Pelican categories 1:1 with provenance streams, writing clean archives to `category/{slug}.html`.
  - Re-pointed header tagline *"Out of My Lane"* directly to `/posts.html` (All Posts).
  - Retired `lanes/` and `lanes.html`; replaced `.lane-nav` and `.footer-lanes` with subtle, unboxed `.stream-nav` and `.footer-categories` (`Streams: Mine • Ours`).
  - Switched post frontmatter to `Category: "Mine"` (or `Ours`, `Theirs`, `AI Generated`) with flexible topical keywords (`tags: [...]`) and format short codes (`type: PROJ`, `previous_types: [...]`).
  - Updated Section 5 of `AGENTS.md` and `.agents/agent_rules.md` to define Provenance Categories and Custom Topic Pages (e.g., Tai Chi, Music, Science, Big Projects to be authored by Jim).
  - Updated `docs/content_authoring.md` and `README.md` metadata guides.
  - Updated test suites (`tests/test_pelican_e2e.py` and `tests/test_accessibility.py`) with all 43/43 tests passing.
  - Bumped version to `v0.6.1`.

- [x] **Milestone 14: Multi-Lane Taxonomy, Post-Type Evolution & Rule 14 AI Attribution (Completed - Release v0.6.0)**
  - Decoupled content format/lifecycle (`type`, `previous_types`) from pursuit lanes (`lanes`).
  - Standardized canonical 5 pursuit lanes: `AI`, `Art`, `Health`, `Making`, `Music`.
  - Purged non-lanes `Ideas` and `Projects` from category archives; mapped them to post types `[IDEA]` and `[PROJ]`.
  - Enabled multi-lane post membership (e.g. `[Music, Making]` on Digital Piano) with dynamic generation in all assigned lane archives.
  - Implemented 28-code uppercase post-type short codes and conceptual evolution lineage (`(evolved from IDEA → WIP)`).
  - Designed Zero-JS Google Sheets + Apps Script commenting pipeline architecture ([GitHub Issue #9](https://github.com/jimcollinsworth/jimcollinsworth.github.io/issues/9)).
  - Codified Rule 14 (Mandatory AI & LLM Author Attribution) in `.agents/agent_rules.md` and `docs/content_authoring.md`.
  - Expanded automated test suite to 43/43 passing tests (`uv run pytest -v`).
  - Bumped release version to `v0.6.0`.

- [x] **Milestone 13: Tagline Lanes Link, Footer Lane Navigator, AI Promoted Lane, Links Rename & Homepage Bio (Completed)**
  - Linked header tagline *"Out of My Lane"* directly to `/lanes.html`.
  - Configured 7-item header menu: `Home`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`.
  - Added conversational personal intro blurb to homepage (`index.html`) with direct link to `about.html`.
  - Added global pursuit lane navigator (`.footer-lanes`) to site footer, listing all categories dynamically.
  - Created `content/pages/ai.md` (`slug: ai`, `title: AI`) as a promoted top-level lane.
  - Renamed `Shelf` &rarr; `Links` (`links.md` &rarr; `links.html`).
  - Removed `Events` page/menu item (`events.md` &rarr; deleted).
  - Documented "Me, Mine, Ours, Others" taxonomy and `macwright.com` layout inspirations in `ROADMAP.md`.
  - Synchronized test suites (all 42/42 tests passing), bumped version to `v0.5.8`.

- [x] **Milestone 12: Contact Page, Footer Navigation Links & UI Walkthrough Visual Protocol (Completed)**
  - Authored clean, zero-JS editorial Contact page (`content/pages/contact.md` &rarr; `output/contact.html`).
  - Updated `<nav class="footer-nav">` in `theme/templates/base.html` with direct links: `About Site`, `Dev Prompts`, `Contact`, and `Google Photos`.
  - Codified **Section 13 (Visual Evidence & UI Walkthrough Protocol)** in `AGENTS.md` and `.agents/agent_rules.md`: mandatory inline visual screenshots before pushing or merging UI changes.
  - Updated automated test suite (`tests/test_pelican_e2e.py` and `tests/test_playwright_responsive.py`) with all 42/42 tests passing.
  - Bumped version to `v0.5.7` across `pyproject.toml` and `about-this-site.md`.

- [x] **Milestone 11: Section Taxonomy Refinement (Reads &rarr; Shelf, Gallery &rarr; Photos, Views &rarr; Events) & Header Layout Optimization (Completed)**
  - Renamed content sections across Markdown sources, slugs, templates, navigation, and tests:
    - Reads &rarr; Shelf (`shelf.md` / `shelf.html`)
    - Gallery &rarr; Photos (`photos.md` / `photos.html`)
    - Views &rarr; Events (`events.md` / `events.html`)
  - Restructured site header layout into two clean, balanced rows:
    - Line 1: `Jim Collinsworth` on far left, `Out of My Lane` right-aligned on far right.
    - Line 2: Navigation menu left-aligned, theme and accessibility toggles right-aligned.
  - Refined theme/contrast/text-size control buttons: compact `28x28px` borderless transparent styling with `15px` SVG icons, eliminating white card boxes to visually harmonize with menu typography.
  - High-contrast mode refinement: eliminated extra line feeds on menu, constrained header to 2 lines, and reduced line-height across typography (`1.55`).
  - Footer deduplication: removed any menu items from the footer that appear on the header, leaving only `About This Site` and `Google Photos`.
  - Updated homepage "Recent Reads" section to "From the Shelf" and updated all internal reference links.
  - Synchronized test suite (40/40 tests passing), bumped version to `v0.5.6.01`.

- [x] **Milestone 10: Accessibility Toggles Overhaul: High-Contrast Low-Complexity Mode & Large Text Scaling (Completed)**
  - Dramatically enlarged text sizes across all pages when `#text-size-toggle` is checked (`font-size: 1.65rem`, headings to `2.85rem`, expanded line-height to `2.0`, and expanded margins/padding).
  - Overhauled `#contrast-toggle` into a low-complexity assistive reading mode:
    - Stark 21:1 pure contrast (white-on-black or black-on-white) with 3px thick link underlines.
    - Low complexity & fewer lines: stripped decorative card borders, timeline boxes, and shadows into unboxed clean reading streams.
    - No graphics: suppressed non-essential photos, images, and decorative media, replacing them with descriptive captions (`[Visual Content Description: ...]`).
    - No tabs & serial navigation: serialized navigation into a clean vertical list with `[Active Page]` indicators, flattening multi-column grids into single serial text.
    - Explicit data labels: added bold visual labels for dates, categories, authors, and external links.
  - Automated tests updated and passing (40/40 tests) with visual screenshot validation.

- [x] **Milestone 9: Prompt History & Instruction Timeline Subpage (Completed)**
  - Created `content/pages/prompt-history.md` compiling to `output/prompt-history.html`.
  - Chronicled Jim's summarized instructions and critical course corrections synced across each release milestone (`v0.1` through `Milestone 8`).
  - Linked directly from `content/pages/about-this-site.md`.
  - Expanded test coverage across Pelican E2E and Playwright responsive suites (40/40 tests passing).
  - Maintained 100% Zero-JS guarantee on reading pages.

- [x] **Milestone 8: About-This-Site Overhaul, Visual Exhibits ("Views") Lane, Apps Hub & Example Interactive Tools (Completed)**
  - Overhauled `about-this-site.md`: removed local install/run commands, positioned Google Antigravity & LLM Agent Harness prominently at the top of the Technology Stack, added direct links and dashboard cards for the GitHub Repository and Release Notes.
  - Added **`Apps`** and **`Views`** to main navigation and footer navigation in `theme/templates/base.html`.
  - Created **Views** (`content/pages/views.md`) dedicated to museum visits, art exhibits, gallery tours, and opinionated visual critiques with photo figures and observations.
  - Added sample art museum post `content/posts/art-institute-chicago-modern-wing.md` (`origin: review`, `stage: inquiry`).
  - Established centralized static tabular and info data directory (`content/data/`) with `photos.json`, `photos.md`, and `site-index.json`.
  - Built two full-screen, responsive, styled interactive applications in `content/apps/`:
    - `content/apps/photo-viewer/index.html` (Responsive photo viewer parsing manifest, camera telemetry, notes, and Google Drive RAW links).
    - `content/apps/keyword-search/index.html` (Full-screen interactive taxonomy, keyword, category, and thought stage visual explorer).
  - Created Apps Hub page (`content/pages/apps.md` -> `apps.html`).
  - Maintained strict 100% Zero-JS guarantee for all editorial reading content while configuring the standalone app sandbox in `output/apps/`.
  - Expanded automated test suite from 30 to 36 tests across Pelican E2E, accessibility, and Playwright responsive rendering (all 36 passing).

- [x] **Milestone 7: Versioning v0.5.5, DevOps Dashboard, Cheat Sheet PDFs & Release History (Completed)**
  - Initialized official project versioning targeting `v1.0` upon initial production content publishing, currently at `v0.5.5`.
  - Created high-resolution printable PDF & Markdown cheat sheets with creative Mermaid diagrams:
    - `docs/cheatsheets/architecture_flow.pdf` (Publishing pipeline, apps/data architecture, Antigravity pair programming sequence, governance matrix).
    - `docs/cheatsheets/content_authoring.pdf` (Thought evolution lifecycle, origin/authorship boundary, Pelican YAML frontmatter template, semantic CSS mapping).
    - `tools/generate_cheatsheet_pdfs.py` (Automated PDF generator via Playwright).
  - Created structured release documents under `releases/` (`v0.1.md` through `v0.5.5.md`) and published Git tags & GitHub Releases.
  - Formalized **Continuous Learning Protocol (`/learn`)** in `.agents/agent_rules.md` syncing debugging fixes, conventions, and rules directly into `JOURNAL.md`.
  - Created `content/pages/about-this-site.md` (DevOps dashboard, live GitHub status, Antigravity AI pair programming model).
  - Codified the practical **Web & Markdown Authoring: Semantic Component Guide** and content types directly in `README.md`.
  - Integrated `about-this-site.html` into base footer navigation and verified 30/30 automated tests with zero JavaScript.

- [x] **Milestone 6: Comprehensive Web Accessibility (WCAG 2.1/2.2 AA & AAA, Section 508, ADA) (Completed)**
  - **Skip-to-Content Navigation**: Added `<a href="#main-content" class="skip-link">Skip to main content</a>` that becomes visible on keyboard focus, navigating directly to `<main id="main-content" tabindex="-1">`.
  - **Semantic Landmarks & ARIA**: Implemented standard landmark roles (`role="banner"`, `role="contentinfo"`), unambiguous navigation labels (`aria-label="Main Navigation"`, `aria-label="Footer Navigation"`, `aria-label="Filter posts by lane"`), and screen reader indicators (`aria-current="page"`, `.sr-only`).
  - **High-Contrast Modes & Color Systems**: Built native CSS `@media (prefers-contrast: more)` and `@media (prefers-color-scheme: dark) and (prefers-contrast: more)` modes delivering 7:1+ AAA contrast ratios, forced underline links, and enhanced focus indicators. Added `@media (forced-colors: active)` support for Windows High Contrast Mode.
  - **Fluid Typography & Text Scaling**: Enforced relative percentage base sizing (`html { font-size: 100%; }`) preserving user browser font scaling up to 200%+ for low-vision and elderly users (WCAG 1.4.4).
  - **Reduced Motion**: Added `@media (prefers-reduced-motion: reduce)` disabling non-essential transitions and animations for users with vestibular disorders.
  - **Touch Targets**: Guaranteed interactive targets conform to WCAG 2.5.8 target size criteria (`min-height: 38px`, ample padding).
  - **Zero-JS Preservation**: All accessibility behaviors operate with pure semantic HTML5 and modern CSS media queries without client-side JavaScript.
  - **Automated Accessibility Test Suite (`tests/test_accessibility.py`)**: Added dedicated automated tests validating lang attributes, skip links, ARIA landmarks, active page attributes, image alt tags, CSS rules, touch targets, and zero-JS policy.

- [x] **Milestone 5: Playwright Testing & Multi-Resolution Responsive Suite (Completed)**
  - **Pure Python Testing Ecosystem**: Installed `playwright` and `pytest-playwright` managed strictly via `uv` with zero Node.js / npm dependencies.
  - **Multi-Resolution Screenshot Utility (`tools/screenshots.py`)**: Built an automated screenshot generator capturing any page across 4 screen sizes and 2 orientations (Phone, Tablet, Laptop, Desktop/TV in Portrait and Landscape = 8 viewports), supporting light/dark theme emulation and interactive HTML previews.
  - **Automated Responsive Tests (`tests/test_playwright_responsive.py`)**: Added test coverage verifying that pages load in headless Chromium across mobile and desktop without unhandled console errors or layout breaks.
  - **CI/CD Integration**: Configured GitHub Actions workflow (`.github/workflows/deploy.yml`) to provision the Playwright Chromium binary and run test suite on every commit to `main`.
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

- [ ] **Custom Photo Navigation & Search Mini-App**: Client-side interactive explorer for high-volume photo archives and tags.
- [ ] **Interactive Projects Showcase**: Standalone mini-apps (e.g. Circle of Fifths music visualizer, USGS live earthquakes monitor).
- [ ] **Pure CSS Tag Filtering**: Explore CSS `:target` or radio-state filtering for journal entries without JavaScript.
- [ ] **Pure CSS Image Modal**: Lightweight lightbox using CSS `:target` for high-res photo inspection.
- [ ] **Print Stylesheet**: Add `@media print` rules for clean hard-copy printing.
