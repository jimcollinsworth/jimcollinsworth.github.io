# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

- [x] **Milestone 52: Chicago Lakefront Sky Study Homepage Featured Post Selection (Completed - Release v0.7.23)**
  - Frontmatter Metadata: added `featured: true` to `content/posts/sample-photo-post.md` and removed from `pipeline-tools-workbench.md`.
  - Dynamic Homepage Selection: updated `theme/templates/index.html` fallback slug to `sample-photo-post`.
  - Release & Version: rebuilt static site, verified test suite, and bumped version to `v0.7.23`.

- [x] **Milestone 51: Multimodal Data Pipeline-Tool Homepage Featured Post Selection (Completed - Release v0.7.22)**
  - Frontmatter Metadata: added `featured: true` to `content/posts/pipeline-tools-workbench.md`.
  - Dynamic Homepage Selection: updated `theme/templates/index.html` to select the pipeline tool post as the featured post and filter recent stream items to prevent duplication.
  - Release & Version: built static output, verified minimal test suite, and bumped version to `v0.7.22`.

- [x] **Milestone 50: Scoped Pure CSS Sticky Hero Photo Cover & Responsive Visual Enhancements (Completed - Release v0.7.21)**
  - Template Restoration: restored clean header layout across non-photo pages (`index.html`, `about.html`, `posts.html`, `links.html`, `apps.html`, `ai.html`).
  - Scoped Photos Hero Cover: integrated sticky photo header strictly into `photos.html` with overlaid study title (`Chicago Lakefront & Sky`), summary subtitle, and Google Photos badge button.
  - Advanced CSS & Accessibility: applied `position: sticky; top: 0; z-index: 1`, `clamp()` fluid typography, `aspect-ratio: 16 / 7` CLS prevention, `min-height: 44px` touch target compliance, and `box-shadow: 0 -8px 24px rgba(0,0,0,0.18)` shadow elevation.
  - Landscape Phone Exclusion: hid hero photo header on small landscape smartphones (`@media (max-height: 500px) and (orientation: landscape)`).
  - Test Suite & Version: expanded test suite to 60 passing tests (`pytest -v`), captured multi-resolution screenshots, and synchronized version to `v0.7.21`.

- [x] **Milestone 49: Intra-Page Provenance Attribution, Pure Markdown Shortcuts & Rule Codification (Completed - Release v0.7.12)**
  - Granular Intra-Page Attribution: added `[Mine]` provenance badges to lead intros and section headings across `about-this-site.md`, `apps.md`, `about.md`, `links.md`, `ai.md`, and `contact.md`.
  - Photos & Ideas Template Badges: added `[Mine]` badge to `.photos-title` in `photos.html` and `.page-intro` in `ideas.html`.
  - AI Haiku Summary Heading: updated heading to `[AI] Site History Haiku` in `about-this-site.html` and `tools/generate_site_summary.py`.
  - Pure Markdown Shortcuts: upgraded `_decorate_provenance_badges` in `pelicanconf.py` to convert `[Mine]`, `[AI]`, `[Me]`, `[Ours]`, `[Theirs]`, `[AI+Mine]`, and `[Mine+AI]` into accessible SVG badges.
  - CSS Baseline Alignment: added styling for `.category-badge` and `.category-icon` in `h1`–`h3` headings and inline paragraphs in `theme/static/css/style.css`.
  - Rule Codification & Docs: added Section 20 to `AGENTS.md` and `.agents/agent_rules.md`, and updated `README.md`.
  - Automated Testing: added `test_intra_page_provenance_and_markdown_shortcuts` in `tests/test_pelican_e2e.py` (59/59 tests passing).

- [x] **Milestone 48: Margin Alignment, Edge-to-Edge Photo Bleed, Apps Table Removal, AI Props & About Site Restructuring (Completed - Release v0.7.11)**
  - Scoped Photo Bleed: removed `.photo-gallery-page` from negative margins, keeping `.photos-header` aligned with container and scoping edge-to-edge bleed strictly to `.photo-stream`.
  - Apps Hub Cleanup: removed obsolete `Static Data & Deployment Architecture` table from `content/pages/apps.md`.
  - Table Touch Scrolling: added `_wrap_tables` in `ObsidianMarkdownReader` to wrap `<table>` tags in `<div class="table-container">` with `overflow-x: auto`.
  - About Site Restructuring: added AI pair programming credit to lead intro, removed verbose sections, and placed the 8-stanza AI Haiku summary immediately after the lead paragraph.
  - Automated Testing & Version: added 3 new tests (58/58 passing) and bumped version to `v0.7.11`.

- [x] **Milestone 47: Chat Bubbles, AI Summary Generator, Mobile Header Streamlining & Timestamp Precision (Completed - Release v0.7.10)**
  - Conversational Chat Bubbles: updated `tools/sync_dev_prompts.py` to wrap turns in `.chat-thread`, styling user prompts in `.chat-user` with warm accent border and AI actions in `.chat-ai` with `LLM-Gemini3.8` attribution.
  - AI Summary Generator: created `tools/generate_site_summary.py` to compile an 8-stanza haiku summary from `JOURNAL.md` into `content/data/site-summary.json`, rendering on `about-this-site.html`.
  - Mobile Header & Footer Controls: moved `.site-controls` to `.site-footer`, scaled phone title font, simplified portrait nav, and expanded `.footer-nav` across all pages.
  - Modernized Dashboard Cards: styled `.btn-compact` buttons and added Recent Releases table with exact commit dates and times.
  - Home Page Featured Post: normalized title font to `1.05rem` / `600` weight and teaser markup to `<p class="post-teaser">`.
  - Testing & Version: passed 55/55 automated tests; bumped version to `v0.7.10`.

- [x] **Milestone 46: Date Architecture Simplification: Date as Real-World Occurrence (Completed - Release v0.7.9.01)**
  - Standardized on Pelican native `date` (real-world event occurrence) and `modified` (publication/update timestamp).
  - Updated `README.md`, `templates/obsidian-post-template.md`, and authoring cheatsheets.

- [x] **Milestone 45: Photos Header, Dedicated Ideas Directory & Pure Markdown Enforcement (Completed - Release v0.7.9)**
  - Photos Page Header: added `.photos-header` flex row with study title and Google Photos badge with official SVG icon.
  - Dedicated Ideas Directory: moved idea files to `content/ideas/` and routed to `output/ideas/{slug}.html`.
  - Pure Markdown Guard: added `test_idea_pages_exist` and expanded `test_pure_markdown_content_sources` to 55 passing tests.

- [x] **Milestone 44: Pure Markdown Content Migration, Automatic Link Resolution & Dedicated Blueprints (Completed - Release v0.7.8)**
  - Automated Link Resolution: upgraded `ObsidianMarkdownReader` in `pelicanconf.py` to automatically resolve Markdown `.md` links and Obsidian `[[wikilinks]]` to Pelican `{filename}` directives.
  - Automated Figure Wrapping: transformed Markdown images into semantic, responsive `<figure>` + `<figcaption>` elements with cross-directory path normalization.
  - Pure Markdown Content: removed all raw HTML wrappers (`<div class="page-intro">`), card containers, and SVG icons across `content/pages/` and `content/posts/`.
  - Dedicated Blueprints: created `about-this-site.html`, `apps.html`, `photos.html`, and `links.html` templates in `theme/templates/`.
  - CSS Lead Paragraphs: added `.page-body > p:first-of-type, .post-content > p:first-of-type` styling in `theme/static/css/style.css`.
  - Automated Testing: added 2 new tests verifying pure Markdown sources and link/figure resolution (54/54 tests passing).
  - Version Bump: updated to `v0.7.8` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.8.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 43: Photo Asset Size Management Policy & Zero Full-Resolution In-Repo Standards (Completed - Release v0.7.7.01)**
  - GitHub Issue #3 Update: documented zero full-resolution in-repo policy, two local display tiers (thumbnails & medium), direct Google Photos / Drive URL resolution, and automated build step pipeline.
  - Agent Rules Codified: added Section 19 to `AGENTS.md` and `.agents/agent_rules.md` prohibiting commit of files > 500 KB or camera RAWs and requiring automated optimization for incoming photos.
  - Architecture Documentation: updated `README.md` Section 4 and `ROADMAP.md` Section 3.C with photo asset sizing tiers and ingest pipeline details.
  - DevOps & Timeline: synchronized prompt history to 106 steering prompts across 32 milestones.
  - Bumped version to `v0.7.7.01` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.7.01.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 42: Homepage Layout: Photo Spotlight Reordered After Featured Post (Completed - Release v0.7.7)**
  - Homepage Grid Balance: moved `Photo Spotlight` from `.sidebar-column` into `.main-column` immediately following `Featured Post` in `theme/templates/index.html`.
  - Column Balance: created balanced vertical column heights on desktop (Featured Post + Photo Spotlight + Recent Links on left, Recent Stream on right).
  - Mobile Reading Flow: aligned mobile flow to Welcome Intro &rarr; Featured Post &rarr; Photo Spotlight &rarr; Recent Links &rarr; Recent Stream.
  - Automated Testing: verified static build and passed 52/52 automated tests (`pytest -v`).
  - Synchronized dev prompt timeline (`content/pages/prompt-history.md`) to 105 steering prompts across 31 milestones.
  - Bumped version to `v0.7.7` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.7.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 41: Ported Amateur Personas, Metadata Matrix & Vertical Density Standards (Completed - Release v0.7.6.01)**
  - Remote Branch Triage: audited `feature/mobile-1line-header-dense-layout`; determined mobile header code was already merged in `v0.6.4`–`v0.6.7`, while documentation concepts were valuable to preserve.
  - Amateur Pursuit Personas: added Section 8 to `ROADMAP.md` covering Jim's 6 exploration personas (*The Sunday Woodwright*, *The Lakefront Cyclist*, *The Amateur Instrumentalist*, *The Local Biome Naturalist*, *The Civic Transit Tracker*, *The Zero-JS Web Craftsman*).
  - Metadata Mapping Architecture: added matrix mapping Pelican engine keys to Obsidian authoring and site presentation in `README.md` and `docs/cheatsheets/content_authoring.md`.
  - Elimination of Redundant Action Links & Vertical Density: codified binding rule in Section 4 of `AGENTS.md` and `.agents/agent_rules.md`.
  - Automated Testing: verified static build and passed 52/52 automated tests (`pytest -v`).
  - Synchronized dev prompt timeline (`content/pages/prompt-history.md`) to 104 steering prompts across 30 milestones.
  - Bumped version to `v0.7.6.01` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.6.01.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 40: Condensed Ideas Stream & Provenance Filtering (Completed - Release v0.7.6)**
  - Ideas Stream: created `/ideas.html` with high-density, metadata-free title list and provenance badges.
  - Feed Isolation: excluded `type: IDEA` from homepage featured post, recent stream, and `posts.html` archive list.
  - Smart Navigation: configured back arrow in `theme/templates/article.html` to return to `/ideas.html` when viewing an idea post.
  - Initial Concepts: authored Jim's 3 ideas (*"I'm vibe coding now"*, *"I'm an AI doomsayer now"*, *"History book mapper"*) with `category: Mine`, and 2 AI ideas (*"Offline Cross-Reference Footnote Weaver"*, *"Lake Michigan Microclimate Correlator"*) with `category: AI` (`LLM-Gemini3.8`).
  - Automated Testing: added `test_ideas_stream_isolated_and_dense` verifying feed isolation across 52 automated tests.
  - Synchronized dev prompt timeline (`content/pages/prompt-history.md`) to 101 steering prompts across 29 milestones.
  - Bumped version to `v0.7.6` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.6.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 39: Content Refinements, Provenance Relocation & App Nomenclature (Completed - Release v0.7.5)**
  - Homepage bio: removed "local" from "local AI" blurb in `theme/templates/index.html` ("...woodworking, and AI.").
  - Multimodal Data Pipeline-Tool: updated post title in `content/posts/pipeline-tools-workbench.md` to `"Multimodal Data Pipeline-Tool"`.
  - About Me cleanup: removed `## Content Streams & Categorization` section and zero-JS comment pipeline paragraph from `content/pages/about.md`.
  - About This Site: added `## Content Streams & Provenance` to the top of `content/pages/about-this-site.md`, updated intro copy to highlight provenance and authorship transparency, and enriched stream descriptions with hikes, events, museums, and tours examples.
  - Synchronized dev prompt timeline (`content/pages/prompt-history.md`) to 99 steering prompts across 28 milestones.
  - Bumped version to `v0.7.5` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.5.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 38: Visual Evidence Path Standards Codification (Section 13) & Release v0.7.4.02 (Completed - Release v0.7.4.02)**
  - Diagnosed recurring "Preview not available" errors in artifact previews: relative paths fail in artifact viewer, and Windows backslashes break URL parsing.
  - Codified binding standards in Section 13 of `AGENTS.md` and `.agents/agent_rules.md`: zero relative paths, forward slashes only, artifact directory storage, and pre-flight verification.
  - Bumped version to `v0.7.4.02` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 37: Chronological Prompt History, On-Site Release Notes Linking & Version v0.7.4.01 (Completed - Release v0.7.4.01)**
  - Ordered Development Prompts (`prompt-history.html`) chronologically from earliest to latest via `tools/sync_dev_prompts.py`.
  - Linked Site Version card on `about-this-site.html` directly to `prompt-history.html` for native milestone review, and linked subtitle to `GitHub Tags`.
  - Synchronized Steering Prompts card to `91 Prompts →`.
  - Added missing release notes documents in `releases/`: `v0.7.1.md`, `v0.7.2.md`, `v0.7.3.md`, and `v0.7.4.md`.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).
  - Captured uncropped 1920x1080 visual evidence.
  - Bumped version to `v0.7.4.01` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 36: Custom Domain DNS Mapping & CNAME Configuration (Completed - Release v0.7.4)**
  - Diagnosed mobile resolution anomaly on `jimcollinsworth.com`: identified GoDaddy domain forwarding with masking serving an HTML 4 frameset lacking `<meta name="viewport">`.
  - Reconfigured GoDaddy DNS records: 4 apex `A` records to GitHub Pages IPs (`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`) and `www` `CNAME` pointing to `jimcollinsworth.github.io`.
  - Added `content/extra/CNAME` containing `jimcollinsworth.com` and mapped it in `pelicanconf.py` `EXTRA_PATH_METADATA` so Pelican outputs `output/CNAME`.
  - Added automated test in `tests/test_pelican_e2e.py` asserting `output/CNAME` existence and correct domain content.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).
  - Bumped version to `v0.7.4` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 35: Prompt History Visual Title, Full-Bleed Response Blocks, Provenance Icons & Release Links (Completed - Release v0.7.3)**
  - Added full post-style title row to `prompt-history.html`: back arrow, dual provenance badge (`[Mine]` `[AI]`), title `Development Prompts`, and right-justified unbolded date `Sept 13 2026`.
  - Scaled `.post-header-full .post-title` to smaller font size `1.15rem` (`font-weight: 600`), unifying blog lists, detail pages, and standalone pages.
  - Replaced text `(Mine)` on prompts with the feather/pen `[Mine]` provenance icon + `Jim:`.
  - Added chip/cpu `[AI]` provenance icon + `Response:` to response blocks.
  - Created full-bleed edge-to-edge response styling (`width: 100vw; margin-left: calc(50% - 50vw);`) with subtle grey background (`var(--bg-subtle)`), constrained inner container, and `overflow-x: clip;` on `html` and `body`.
  - Formatted release milestone titles in smaller font (`1.08rem`, `font-weight: 600`) as clickable links to relevant GitHub release tags.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).
  - Bumped version to `v0.7.3` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 34: Post Header Consolidation, Framed App Mockups, Full-Screen Photo Links & Zero-JS UI Streamlining (Completed - Release v0.7.2)**
  - Apps Hub: linked card titles directly to app posts; removed redundant "Read App Post &rarr;" buttons and removed "Embedded View &rarr;" button.
  - Decommissioned obsolete embedded page `pipeline-tools.md` via `git rm`.
  - Removed footer copyright notice line from `theme/templates/base.html`.
  - Unbolded post types (`font-weight: 400`) and tightened vertical spacing between main homepage sections.
  - Post header row consolidation: integrated inline `&larr;` back arrow, provenance category badge, title on left, and right-justified unbolded type/date on right, eliminating the standalone back link row.
  - App post layout: added top primary accent `Launch Full-Screen App &rarr;` button immediately after intro text; framed screenshot inside `figure.screenshot-frame` with accent border, rounded corners, and shadow.
  - Full-screen photo viewing: wrapped images with `a.photo-link` (with `cursor: zoom-in`) across gallery, homepage spotlight, article posts, and app screenshots.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).
  - Captured full-width uncropped screenshots (1920x1080) for visual verification.
  - Bumped version to `v0.7.2` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

- [x] **Milestone 33: Big Display Typography Scaling & Full-Screen App Header Unification (Completed - Release v0.7.1)**
  - Scaled site title ("Jim Collinsworth") to `1.95rem` and tagline ("Out of My Lane") to `1.45rem` on big displays (`@media (min-width: 1360px)`).
  - Scaled base desktop site title to `1.55rem` and tagline to `1.25rem`.
  - Scaled tagline in text-size toggle mode to `1.65rem`.
  - Harmonized top header bar markup and CSS in `content/apps/pipeline-tools/index.html` with `photo-viewer` and `keyword-search` (plain text accent `← Back to Apps` link, serif bold title, and `btn` action classes).
  - Added theme toggle and browser full-screen request buttons to `content/apps/pipeline-tools/index.html`.
  - Captured uncropped full-width (1920px) header evidence showing both left and right outer container margins and alignment.
  - Bumped version to `v0.7.1` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.
  - Passed all 51 automated tests in `pytest -v`.

- [x] **Milestone 32: Site v0.7.0: App Posts, Full-Screen App Container & Dual AI/Mine Provenance (Completed - Release v0.7.0)**
  - Bound Featured Post summary dynamically on `index.html` via `featured.summary`.
  - Promoted Pipeline Tools to active Featured Post (`content/posts/pipeline-tools-workbench.md`).
  - Created dedicated articles for Photo Viewer and Keyword Explorer in `content/posts/`.
  - Captured high-resolution application screenshots into `content/images/` and embedded them in posts with `<figure>` and `<figcaption>`.
  - Built full-screen standalone application wrapper `content/apps/pipeline-tools/index.html` with top app bar and 100% viewport iframe.
  - Added dual provenance icon support (`[AI]` + `[Mine]`) in `theme/templates/category_icon.html` and `theme/static/css/style.css`.
  - Streamlined `content/pages/apps.md` cards by removing uppercase eyebrow labels and matching `1.05rem` font-sans post titles.
  - Tightened navigation menu item spacing (`gap: 0.15rem;`, link padding `0.25rem;`, `margin-left: -0.25rem;`), bringing "About" close to "Home" while maintaining flush alignment with branding.
  - Bumped version to `v0.7.0` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.
  - Passed all 51 automated tests in `pytest -v`.

- [x] **Milestone 31: Pipeline Tools App Page & Hugging Face Spaces Integration (Completed - Release v0.6.16)**
  - Created dedicated application page `content/pages/pipeline-tools.md` with Stream `Mine` attribution (Jim Collinsworth).
  - Integrated direct iframe embed (`https://jimcollinsworth-pipeline-tools.hf.space`) with breadcrumbs back to the Apps hub.
  - Added responsive CSS embed container (`.app-embed-container` and `.app-embed-iframe`) in `theme/static/css/style.css` (850px height desktop, 650px mobile/tablet).
  - Added showcase card for Pipeline Tools in `content/pages/apps.md` and updated architecture table.
  - Configured navigation active state in `theme/templates/base.html` to highlight Apps tab when on `pipeline-tools.html`.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).

- [x] **Milestone 30: Desktop 2-Row/2-Column Layout & Menu Left Margin Alignment (Completed - Release v0.6.15)**
  - Applied `margin-left: -0.55rem;` to `nav.site-nav`, achieving flush vertical alignment between "Jim", the first menu label, the 4px horizontal bar, and body content.
  - Standardized `font-weight: 600;` across all navigation links to eliminate horizontal character width shifts when toggling active tabs.
  - Removed mobile `.intro-blurb` padding (`padding: 0;`), aligning the mobile lead paragraph with the site title and horizontal line.
  - Reorganized `content/pages/links.md` into a responsive 2-row / 2-column layout: Row 1 (70/30) with summary and collection stats/keywords; Row 2 (50/50) with Computing & AI on left, Arts, Health & Making on right.
  - Added responsive CSS grid rules for `.links-intro-row`, `.links-grid-row`, and `.links-meta-card`.
  - Configured realistic 1920x1080 resolution in screenshot capture script.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).

- [x] **Milestone 29: Provenance Icon Title Prefix & Intro Arrow Link (Completed - Release v0.6.14)**
  - Unified provenance icon positioning across `Recent Links` (`index.html` and `links.md`) so that the provenance icon prefixes the title, matching `Recent Stream` and `Featured Post`.
  - Added `.book-header-row`, `.book-header-left`, and `.book-header-right` flex styles to `theme/static/css/style.css` to align `[ICON] [TITLE]` on left and right-justified author (`AI`) and date on right.
  - Replaced `More about me →` in homepage intro blurb with compact arrow link to `about.html` (`&rarr;`) styled with `.about-arrow`.
  - Replaced inline `(→all)` header links with clean `(ALL)` links on `index.html`.
  - Removed redundant `Read full post →` from featured post block on `index.html`.
  - Synchronized `JOURNAL.md`, `pyproject.toml`, and `content/pages/about-this-site.md` to `0.6.14`.
  - Rebuilt static site with Pelican; passed all 51 automated tests (`pytest -v`).

- [x] **Milestone 28: Compact Blog Layout, Right-Justified Metadata & Header Refinements (Completed - Release v0.6.13)**
  - Increased compact navigation breakpoint from 640px to 768px in `theme/static/css/style.css`, eliminating 3-line header wrapping on medium portrait viewports.
  - Harmonized active navigation highlight in expanded line mode with the single-item dropdown button (`border: 1px solid var(--border)`, `background: var(--bg-subtle)`, rounded 6px).
  - Redesigned blog list entry layout to `[ICON] [TITLE]` on left and right-justified `[TYPE] [DATE]` on right, formatted in `var(--font-sans)` with unbracketed types and no bullet dots.
  - Scaled down post title font size to `1.05rem` (featured `1.15rem`).
  - Removed category text labels from `category_icon.html` to render pure accessible SVG icons.
  - Replaced placeholder authors in `links.md` and `index.html` with `AI` provenance stream attribution.
  - Converted bottom section links (`View all posts →`, `Explore all photos →`, `Browse all links →`) to inline `(→all)` header links.
  - Embedded SVG category icons next to `Me`, `Mine`, `AI`, `Ours`, and `Theirs` in `content/pages/about.md`.
  - Scrubbed ungrounded adjectives and evaluative modifiers across templates and content per Rule 18.
  - Rebuilt Pelican site, verified 51/51 automated tests passing, and bumped version to `v0.6.13`.

- [x] **Milestone 27: Prompt History Mine Attribution & Steering Dialog Streamlining (Completed - Release v0.6.12)**
  - Configured `Mine` stream and Jim Collinsworth author attribution on `content/pages/prompt-history.md` frontmatter and header.
  - Formatted steering prompts with `**Jim (Mine):**` dialog labels and concise responses.
  - Documented active zero-JS Google verification and filed Issue #10 for future tracking exploration.
  - Rebuilt Pelican static site and confirmed 51/51 test suites pass. Bumped version to `v0.6.12`.

- [x] **Milestone 26: Root Build Artifact Removal, Directory Organization & Nikola Cleanup (Completed - Release v0.6.11)**
  - Removed 37 obsolete build artifacts, root HTML files, duplicate directories (`category/`, `posts/`, `images/`, `assets/`), and intermediate files from the repository root.
  - Confirmed canonical source layout for Markdown (`content/posts/`, `content/pages/`) and historical archives (`archive/content/`).
  - Removed obsolete `nikola-baseline-build/` entry from `.gitignore`.
  - Rebuilt Pelican static site and verified all 51 automated unit, accessibility, and responsive tests pass. Bumped version to `v0.6.11`.

- [x] **Milestone 25: Prohibition of Ungrounded Adjectives & Fluff Removal (Completed - Release v0.6.10)**
  - Codified Section 18 in `AGENTS.md` and `.agents/agent_rules.md` prohibiting ungrounded adjectives, adverbs, superlatives, and marketing fluff without direct, verifiable empirical evidence.
  - Replaced flagged marketing text in `README.md` with factual Option 1A text: *"jimcollinsworth.github.io is Jim Collinsworth's personal website and journal, built using the Pelican static site generator with HTML5 and CSS, containing zero client-side JavaScript."*
  - Scrubbed ungrounded adjectives across `README.md`, `content/pages/about-this-site.md`, `content/pages/apps.md`, `content/pages/ai.md`, `tools/sync_dev_prompts.py`, `templates/obsidian-post-template.md`, and historical problem statements in `JOURNAL.md`.
  - Rebuilt static site and verified 51/51 pytest test suites pass. Bumped version to `v0.6.10`.

- [x] **Milestone 24: Tightened Header Spacing, Compact Active Nav & Segmented Controls (Completed - Release v0.6.9)**
  - Reduced excessive vertical padding above the header (`body` top padding reduced from 2.5rem to 1.25rem on desktop, 1.5rem on supersize, 1.25rem on tablets, 0.85rem on mobile).
  - Tightened vertical spacing between branding and navigation (`margin-bottom: 0.35rem;`).
  - Reduced desktop header padding above the grey horizon bar to `0.45rem`, and margin below the bar to `1.5rem`.
  - Tightened active navigation highlight pill on desktop (`padding: 0.12rem 0.55rem; line-height: 1.2;`, removed desktop `min-height: 38px`), creating a short, crisp pill that hugs navigation labels.
  - Integrated mobile portrait dropdown and theme/mode switcher icons with the horizon bar (`padding-bottom: 0.35rem`, `margin-bottom: 0.85rem`).
  - Grouped `.site-controls` into a cohesive, segmented capsule (`gap: 1px`, `background-color: var(--bg-subtle)`, `border: 1px solid var(--border-subtle)`, `border-radius: 6px`, `padding: 1px`) with square 25px buttons matching the height and visual weight of the mobile dropdown button.
  - Cleaned `templates/obsidian-post-template.md` by removing Section 7 (`STANDALONE PAGE MENU SETTINGS`) and removed redundant `p.menu` fallback loops from `theme/templates/base.html`.
  - Recompiled site and verified all 51 automated tests passing. Bumped version to `v0.6.9`.

- [x] **Milestone 23: Pelican Conventions Rule, Optional Summary & Menu Architecture (Completed - Release v0.6.8)**
  - Codified Section 17 in `AGENTS.md` and `.agents/agent_rules.md` requiring strict adherence to official Pelican conventions, standard metadata fields, and disallowing custom alias layers or metadata bloat.
  - Formulated optional summary policy: no requirement for manual `summary:` frontmatter; Pelican auto-derives the summary from body text when omitted.
  - Updated `templates/obsidian-post-template.md` to document `summary:` as optional per Pelican conventions.
  - Clarified menu architecture: custom pages (`about.md`, etc.) are configured via `MENUITEMS` in `pelicanconf.py`, while `menu: true` serves as an opt-in for additional pages. Verified that blog posts can also be placed into `MENUITEMS` directly.
  - Synchronized `pyproject.toml`, `about-this-site.md`, and bumped version to `v0.6.8`.

- [x] **Milestone 22: Header Horizon Bar, Reversed Active Nav & Obsidian Post Template (Completed - Release v0.6.7)**
  - Implemented 4px basic grey horizontal horizon bar (`--border-header: #b5b0a6` light / `#44494e` dark) beneath `header.site-header` on desktop, scaled to 3px on mobile and phone landscape.
  - Re-architected active navigation indicator from a conflicting bottom border to a high-contrast reversed pill (`background-color: var(--text); color: var(--bg) !important; font-weight: 600; border-radius: 4px; padding: 0.25rem 0.65rem; border-bottom: none;`).
  - Removed `border-bottom` on all navigation links to eliminate visual clash with the horizontal header bar and prevent hover jitter.
  - Aligned mobile dynamic dropdown menu active item styling with reversed pill treatment.
  - Created `templates/obsidian-post-template.md` at repo root with comprehensive commented YAML frontmatter (documenting `title`, `date`, `slug`, `category`, `type`, `previous_types`, `tags`, `status`, `summary`, `image`, `menu` settings) and an editorial Markdown starter layout.
  - Verified 100% parity between `assets/css/style.css` and `theme/static/css/style.css`.
  - Rebuilt static site and ran automated test suite (51/51 tests passing).
  - Captured 16 responsive screenshots across all 8 viewports in light and dark modes.
  - Synchronized `pyproject.toml`, `about-this-site.md`, and bumped version to `v0.6.7`.

- [x] **Milestone 21: Color Flair & Photo Border Architectural Design (Designed & Documented - Issue #6)**
  - Sampled color palettes directly from sky and Lake Michigan photography (`sky-twilight.jpg`, `sky-lakefront.jpg`, `sky-clouds.jpg`) using Playwright Canvas extraction.
  - Architected pure Zero-JS semantic 4-edge `<aside>` perimeter frame enabling click-to-view full-screen photo without interfering with reading canvas or scrolling.
  - Implemented responsive border scaling: 8px mobile, 14px–16px desktop, and matching link underlines (`text-decoration-color: var(--flair-color)`).
  - Designed neutral studio grey border (`#808387` light / `#323538` dark) for photo-rich pages (`photos.html`) to frame photos cleanly without color clashing.
  - Generated and inspected 7 visual prototype screenshots across viewports and color configurations.
  - Documented full architectural design proposal and findings in a detailed comment on GitHub Issue #6. Production code left clean pending Jim's review.

- [x] **Milestone 20: Verbatim Dev Prompts Timeline & Automated Milestone Sync (Completed - Issue #7)**
  - Replaced decorative cards and haiku synthesis with simple, unadorned plaintext quotes of Jim's authentic prompts on `content/pages/prompt-history.md`.
  - Created `tools/sync_dev_prompts.py` to parse `JOURNAL.md` on a per-milestone basis, extracting 29 steering prompts across 9 releases through `v0.6.5`.
  - Added 6th metric card to the DevOps dashboard on `content/pages/about-this-site.md` linking to `prompt-history.html`.
  - Posted full status update comment to GitHub Issue #7. All 51 automated tests passing.

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
