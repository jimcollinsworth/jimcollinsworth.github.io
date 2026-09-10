# Site Journal & Decision Log: jimcollinsworth.github.io

> Chronological log of architectural decisions, site milestones, and design changes. Maintained under the 3-document agent rule.

---

## 2026-09-09 — Accessibility Toggles Overhaul: High-Contrast Low-Complexity Mode & Large Text Scaling

### Context & Need
Jim requested that the accessibility toggles deliver much more obvious and significant visual transformations:
- **Text Size Toggle**: Dramatically bigger text across all elements, expanded line-height, and generous margins so content has comfortable breathing space.
- **High-Contrast Toggle**: Low-complexity assistive mode tailored for readers needing maximum clarity: fewer lines (stripping decorative boxes, borders, and card outlines), no graphics (hiding photos and decorative images, replaced by structured text summaries), no tabs (serializing navigation into a clear linear list), flattening multi-column grids into a single serial column, and adding explicit data labels (`Date: `, `Category: `, `Author: `, `Read: `, `[Active Page]`) for text and assistive readers.

### Decisions & Actions Taken
1. **Dramatic Text Scaling (`body:has(#text-size-toggle:checked)`)**:
   - Scaled base body font size to `1.65rem` (~26.4px) with `2.0` line-height.
   - Scaled headings (`h1` to `2.85rem`, `h2` to `2.3rem`, `h3` to `1.9rem`, `.site-title` to `2.4rem`, `.post-title` to `2.05rem`).
   - Expanded paragraph spacing (`margin-bottom: 1.75rem`), post separation (`margin-bottom: 3.5rem`), container padding, and control buttons (`44px`).
2. **High-Contrast Low-Complexity Assistive Mode (`body:has(#contrast-toggle:checked)`)**:
   - **Contrast**: Stark 21:1 pure contrast in both Light (`#ffffff` bg / `#000000` text) and Dark (`#000000` bg / `#ffffff` text / `#ffff33` links) with 3px thick link underlines.
   - **Fewer Lines**: Stripped decorative card borders, timeline boxes, and shadows from `.dashboard-card`, `.timeline-milestone`, `.exhibit-card`, `blockquote`, and `.post-item`.
   - **No Graphics**: Hidden `img`, `picture`, and decorative gallery previews; styled `<figcaption>` into high-clarity descriptive assistive text blocks (`[Visual Content Description: ...]`).
   - **No Tabs / Serial Layout**: Serialized `.site-nav` and `.footer-nav` into a clear linear vertical list with active page indicators (`[Active Page]`); flattened `.desktop-two-col`, `.dashboard-grid`, and `.photo-preview-row` into a unified sequential reading column.
   - **Explicit Data Labels**: Injected bold visual prefixes via CSS pseudo-elements for dates, categories, authors, reading dates, and external link indicators.
   - Preserved control buttons clickability by keeping `.control-btn .sr-only` scoped.
3. **Automated Testing & Visual Verification**:
   - Enhanced `test_in_page_mode_switchers_interactive` in `tests/test_playwright_responsive.py` to assert font size enlargement (>= 24px), column nav direction, and image suppression.
   - Verified all 40/40 tests pass cleanly in `pytest`.
   - Generated and visually checked full-page screenshot artifacts across light, dark, large text, and combined high-contrast + large-text modes.

---

## 2026-09-09 — Prompt History & Instruction Timeline Subpage

### Context & Need
Jim requested a dedicated timeline subpage under *About This Site* focusing entirely on his direct instructions (summarized in his voice) and especially critical course corrections, error remediations, and design decisions, synced directly to the release milestones (`v0.1` through current development).

### Decisions & Actions Taken
1. **Created Prompt History Page (`content/pages/prompt-history.md` &rarr; `output/prompt-history.html`)**:
   - Structured chronologically across all milestones: Milestone 8 (Apps Hub, Views lane, static data directory), v0.5.5 (DevOps dashboard, Continuous Learning protocol, glossary cancellation, Mermaid syntax fixes), v0.5 & Accessibility (CSS `:has` switchers, orientation layout, progressive density), v0.3 & v0.4 (Pelican SSG migration, title deduplication, zero-pills mandate, Jekyll trap bypass), and v0.1 & v0.2 (human authorship boundary Rule 1, AI placeholder purge, 3-document governance rule).
   - Clean, high-contrast timeline layout using site CSS variables (`--accent`, `--border-color`, `--card-bg`, `--text-muted`), blockquotes of Jim's guidance, and bullet points of error remediations.
   - Strictly 100% Zero-JS with semantic HTML5 elements.
2. **Linked Prominently from `about-this-site.md`**:
   - Added dedicated section "Prompt & Instruction Timeline" with a direct link to `prompt-history.html`.
3. **Automated Testing & Browser Verification**:
   - Added `prompt-history.html` and `about-this-site.html` to both `tests/test_pelican_e2e.py` and `tests/test_playwright_responsive.py`.
   - Verified 40/40 tests pass cleanly with zero console errors or accessibility violations.
   - Captured multi-viewport screenshots via `tools/screenshots.py` and visually verified rendering quality.

---

## 2026-09-09 — Milestone 8: About-This-Site Overhaul, Visual Exhibits ("Views") Lane, Apps Hub & Example Interactive Tools

### Decisions & Actions Taken
1. **Overhauled `about-this-site.md`**:
   - Removed the local CLI install/run commands section.
   - Prominently positioned the **Google Antigravity & LLM Agent Harness** at the very top of the Technology Stack.
   - Added direct links and dashboard cards for the **GitHub Repository** (`https://github.com/jimcollinsworth/jimcollinsworth.github.io`) and **Release Notes** (`releases/` / GitHub releases).
2. **Main Navigation Expansion & "Views" Visual Lane**:
   - Added **`Views`** and **`Apps`** to both `site-nav` and `footer-nav` in `theme/templates/base.html`.
   - Created **Views** (`content/pages/views.md`) dedicated to museum visits, art exhibits, gallery tours, and opinionated visual critiques with photo figures and observations.
   - Added sample art post `content/posts/art-institute-chicago-modern-wing.md` (`origin: review`, `stage: inquiry`, category `Art`).
3. **Centralized Static Data Directory (`content/data/`)**:
   - Configured `STATIC_PATHS = ['images', 'extra', 'apps', 'data']` in `pelicanconf.py`.
   - Created `content/data/photos.json` and `content/data/photos.md` containing image metadata, dates, locations, and direct Google Drive links.
   - Created `content/data/site-index.json` containing complete multi-facet content index spanning categories, stages, origins, and tags.
4. **Built Two Full-Screen Example Interactive Applications**:
   - `content/apps/photo-viewer/index.html`: Responsive full-screen photo viewer parsing manifest data, with filmstrip sidebar, keyboard navigation, camera telemetry, dark/light toggle, and direct Google Drive RAW links.
   - `content/apps/keyword-search/index.html`: Full-screen interactive taxonomy, keyword, category, and thought stage visual discovery explorer with live fuzzy search and clickable filter chips.
   - Created Apps Hub page `content/pages/apps.md` (`apps.html`) introducing the sandbox.
5. **Architectural Boundary: Zero-JS vs. Standalone Apps**:
   - Preserved 100% Zero-JS guarantee for all editorial reading content (`index.html`, `posts/*.html`, `reads.html`, `views.html`, `about.html`, etc.).
   - Interactive applications operate in isolated standalone subpaths (`output/apps/**`).
6. **Automated Test Suite Expansion**:
   - Expanded test suite from 30 to 36 automated tests (`tests/test_accessibility.py`, `tests/test_pelican_e2e.py`, `tests/test_playwright_responsive.py`), validating all pages and apps across viewports.

---

## 2026-09-09 — Milestone 7: Versioning v0.5.5, DevOps Dashboard, Cheat Sheet PDFs & Release History

### Decisions & Actions Taken
1. **Created Visual Cheat Sheets & Automated PDF Generator**:
   - Designed two comprehensive visual cheat sheets featuring rich Mermaid diagrams and print-optimized typography:
     - `docs/cheatsheets/architecture_flow.pdf` &bull; `.md` &bull; `.html` &mdash; End-to-end publishing pipeline, source topography, interactive apps & static data architecture, Antigravity AI sequence diagram, governance matrix, and CLI commands.
     - `docs/cheatsheets/content_authoring.pdf` &bull; `.md` &bull; `.html` &mdash; Thought evolution lifecycle state diagram, authorship/origin boundary flow, Pelican YAML frontmatter template, semantic layout component mapping table, and responsive orientation modes.
   - Built `tools/generate_cheatsheet_pdfs.py` utilizing Playwright headless Chromium to render vector-sharp, letter-format PDFs on demand with built-in diagram validation that catches any Mermaid syntax parsing issues.
   - Resolved Mermaid syntax error in box 5 ("Responsive Layout & Orientation Rules") by escaping angle brackets in edge labels.
   - Added reference section in `README.md`.
2. **Bumped Project Version to `v0.5.5` & Created Structured Release History**:
   - Set version to `0.5.5` across `pyproject.toml` and `about-this-site.md`.
   - Created standardized GitHub-style release documents under `releases/`:
     - `releases/v0.1.md` &mdash; Clean Foundation, Zero-JS, and 3-Document Governance.
     - `releases/v0.2.md` &mdash; Calvin/MacWright Editorial Redesign, Bookshelf, and Gallery.
     - `releases/v0.3.md` &mdash; Pelican SSG Integration, Obsidian Frontmatter Reader, and E2E Testing.
     - `releases/v0.4.md` &mdash; GitHub Pages Root Deployment Alignment & Custom "JC" Favicon.
     - `releases/v0.5.md` &mdash; Magazine 2-Column Desktop Grid, Orientation Modes, and Progressive Density.
     - `releases/v0.5.5.md` &mdash; DevOps Dashboard, Continuous Learning Protocol, and Semantic Component Guide.
   - Published Git tags and official GitHub Releases (`v0.1` through `v0.5.5`).
3. **Formalized Continuous Learning Protocol (`/learn`) in Agent Governance**:
   - Integrated learning procedures into `.agents/agent_rules.md`: when new debugging solutions, user corrections, or workflow preferences are established, the agent records structured entries in `JOURNAL.md` and permanently updates `.agents/agent_rules.md` and `.agents/skills/`.
4. **Created `about-this-site.md` & DevOps Dashboard**:
   - Built standalone meta page at `content/pages/about-this-site.md` (compiled to `about-this-site.html`).
   - Integrated live GitHub Actions deployment badge, release version metric (`v0.5.5`), zero-JS guarantee (0 KB JS, 0 cookies, 0 tracking), and hosting architecture (GitHub Pages + HTTPS).
   - Formally documented the **Antigravity AI Assistant & Pair Programming Model** detailing the strict separation of concerns (Jim owns 100% of prose/content; Antigravity manages templates, CSS, build tools, tests, and CI/CD).
   - Integrated page into site footer navigation in `theme/templates/base.html`.
5. **Consolidated Content Types & Semantic Terminology Directly into Docs**:
   - Consolidated clear content format definitions (*Post/Essay, Project, TIL, Idea, Read, Comment*) directly into the **Semantic Component Guide** in `README.md`.
6. **Automated Test Suite Validation**:
   - Verified 30/30 automated tests passing across accessibility, Playwright browser rendering, and Pelican E2E integrity.

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

## 2026-09-09 — Troubleshooting & Resolution: Pixeltable Embedded PostgreSQL Test Runner

### Problem & Diagnostic Analysis
- **Symptom**: `uv run python -m tests` in the `pipeline-tools` workspace experienced 27 test failures with `AssertionError: assert self._postmaster_info is not None`.
- **Root Cause**: On Windows, abruptly terminating Python / test runners left orphaned background `postgres.exe` child processes holding open file handles to `C:\Users\jimco\.pixeltable\pgdata\log` and `postmaster.pid`. When subsequent test runs initialized, PostgreSQL entered crash recovery, hit a Windows sharing violation (`could not open file "./log": sharing violation`), and timed out after 30 seconds.
- **Clarification**: `pxt service ...` commands only apply to remote/cloud Pixeltable microservices, not the local embedded PostgreSQL instance managed by `pixeltable_pgserver`.

### Solution & Recovery Procedure
1. Terminated lingering background PostgreSQL processes: `taskkill /F /IM postgres.exe /T 2>nul`.
2. Cleaned corrupted database state directory: `rmdir /s /q "%USERPROFILE%\.pixeltable\pgdata"`.
3. Verified test suite: `uv run python -m tests` cleanly reinitialized a fresh cluster and executed successfully.
>>>>>>> ed02d16 (feat(release): v0.5.5 with DevOps dashboard, learning protocol, semantic guide, and release history)

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
