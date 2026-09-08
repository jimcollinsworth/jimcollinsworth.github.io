# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

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
