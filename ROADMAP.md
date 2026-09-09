# Long-Term Roadmap & Creative Brainstorming: jimcollinsworth.github.io

> **The Living Vision Canvas for *Out of My Lane***  
> Maintained under the core governance rules authorized by Jim Collinsworth.  
> This document serves as a persistent, open space for long-term architectural vision, creative brainstorming, speculative features, and exploratory projects across Jim's 12 pursuit lanes.

---

## 1. Vision & Architectural Philosophy

### The "Out of My Lane" Philosophy
After a 50-year career spanning Arthur Andersen, professional guitar performance, software startups, and data science, retirement is an invitation to explore freely without professional silos or arbitrary boundaries. *"How does that work?"* is the core question guiding every note, essay, and technical experiment.

### Foundational Tenets (Non-Negotiable)
1. **100% Human-Authored Content & Image Curation**:
   - Jim explicitly authors every essay in Obsidian and manually transfers every photo into the site repository.
   - AI agents are strictly restricted to technical infrastructure, build maintenance, layout styling, and validation tools.
2. **Zero Client-Side JavaScript on Content Pages**:
   - The published reading experience is built entirely on semantic HTML5 and modern CSS. Zero `<script>` tags, zero trackers, zero runtime bloat.
3. **Pure Python Tooling Ecosystem**:
   - All tools, build pipelines, and testing suites are 100% Python-based (managed via `uv`).
   - Strictly **no Node.js or npm** ever for applications or toolchains (the sole current exception is `npx skills` for agent skills).
4. **Editorial Typography & Reading Comfort**:
   - Mobile-first, distraction-free typography inspired by Mark Boulton and Calvin French-Owen, with automatic dark/light mode switching via `prefers-color-scheme`.
5. **Durable Digital Longevity**:
   - Built to last decades. Pure static HTML deployed to GitHub Pages with continuous automated regression testing.

---

## 2. Current Requirements & Proven Foundation

The core platform has reached a robust, automated state:

- **Static Site Generator**: Pelican with custom Jinja2 theme (`theme/`) and YAML frontmatter parsing via `ObsidianMarkdownReader`.
- **Content Pipeline**: Structured drop directories in `content/` (`posts/`, `pages/`, `images/`, `extra/`) designed to mirror an Obsidian vault.
- **UI Design System**: Zero pills, clean text links for lanes, deduplicated page headers, and fluid responsive reading layouts.
- **Testing & Quality Assurance**:
  - Full automated pytest suite with 19 passing tests (`uv run pytest -v`).
  - Headless Chromium browser automation via Playwright (`tests/test_playwright_responsive.py`) auditing layout, 404 links, and zero console errors.
  - Multi-resolution screenshot capture tool (`tools/screenshots.py`) covering 4 device form factors in both portrait and landscape (8 viewports) with interactive HTML gallery previews (`preview.html`).
- **CI/CD Automation**: GitHub Actions workflow (`.github/workflows/deploy.yml`) builds with Pelican, runs the full test suite in Playwright Chromium, and publishes to GitHub Pages.

---

## 3. Jim's "Crazy Ideas" & Creative Sparks

These are high-potential concepts, experiments, and passion projects raised in discussions, journal entries, and brainstorming sessions:

### A. Circle of Fifths Interactive Music Visualizer
- **Concept**: An interactive harmonic visualizer exploring the Circle of Fifths, key signatures, relative minors, modal interchange, and chord progressions.
- **Instrument Mapping**:
  - Classical and fingerstyle guitar fretboard chord maps (CAGED system, dropped tunings, triad inversions).
  - Piano keyboard voicings (integrating Jim's Kawai ES-8 keyboard studies).
- **Architecture Options**:
  - *Zero-JS Exploration*: Pure SVG with CSS `:hover` / `:focus` / `:target` state transitions.
  - *Standalone Mini-App*: An isolated HTML5/Canvas/WebGL application living in a dedicated `/projects/circle-of-fifths/` folder that does not compromise the zero-JS rule of the core editorial pages.

### B. USGS Real-Time Earthquake & Geophysical Tracker
- **Concept**: A live seismic and tectonic visualizer querying the USGS Earthquake API (GeoJSON feed).
- **Features**:
  - Real-time mapping of global seismic activity with magnitude filtering.
  - Regional focus on midwestern micro-quakes, the New Madrid Seismic Zone, and tectonic fault lines.
  - Historical comparison of significant seismic events.
- **Architecture Options**:
  - Build-time static snapshot generator (Python cron job generating pure SVG/GeoJSON maps daily).
  - Standalone interactive app in `/projects/earthquakes/`.

### C. High-Volume Photo Navigation & Archive Explorer
- **Concept**: Jim captures dozens to hundreds of photographs across Lake Michigan morning walks, Chicago skies, botanical macros, woodworking projects, and sunsets.
- **Current State**: Curated key photos are placed in `content/images/` and embedded in `<figure>` tags, with links out to full Google Photos albums (e.g. [OutOfMyLane Google Photos album](https://photos.app.goo.gl/yGTTSd3hnw1pqCPo8)).
- **Future Vision**:
  - A dedicated photo navigation mini-app capable of indexing high-resolution archives.
  - EXIF metadata extraction (camera settings, lens, exposure, timestamp, sunrise/sunset alignment).
  - Faceted visual filtering by pursuit lane, season, lighting conditions, and tags without bloating the git repo (using cloud storage or external static asset hosting).

### D. M.E. (Mental Entity / My Essence) Companion Integration
- **Concept**: A completely local, offline personal AI companion carried on your person with an adaptive memory architecture (documented in Jim's post *M.E. (Mental Entity / My Essence)*).
- **Synergies with Site**:
  - Offline bidirectional sync: M.E. can read Jim's Obsidian notes and site archive locally while traveling.
  - Autonomous synthesis: M.E. can maintain private research indices and suggest connections across Jim's 12 pursuit lanes without touching public content.
  - Long-term memory logs: Curated reflections exported by Jim from M.E. into public journal entries.

### E. Sleep Health & Periodic Limb Movement Somatic Analysis
- **Concept**: Deep exploration of sleep health, periodic limb twitching, RLSRS scores, and non-pharmacological clinical assessment pathways (working with Dr. James Runke).
- **Data Visualizations**:
  - Longitudinal sleep movement frequency charts and sleep architecture breakdowns.
  - Sensor-driven time series data from wearable accelerometers / sleep trackers.
  - Correlation studies between somatic practices (Tai Chi, Alexander Technique) and motor quiescence during sleep.

### F. Model Context Protocol (MCP) Interface for Static Site Management
- **Concept**: A specialized Python MCP server (`mcp-pelican-tools`) allowing LLM coding agents to interact with the static site through structured tools rather than raw shell commands.
- **Tool Capabilities**:
  - Content inventory and YAML frontmatter schema validation.
  - Automated link auditing and image reference verification.
  - Pelican build execution and test status reporting.
  - Visual regression inspection via Playwright screenshots.

### G. Pipeline Tools Embedded Cockpit & Hugging Face Hosting
- **Concept**: Integrate Jim's multimodal ETL and prompt workbench (`pipeline-tools`) as an interactive application reachable directly within the site (`pipeline-tools.html`).
- **Deployment & PostgreSQL Architectures**:
  - *Local Cockpit (Zero-Cost / Native Disk Access)*: The Python backend runs locally on Jim's machine (`uv run gradio app.py` at `127.0.0.1:7860`), maintaining fast access to local folders (`d:\projects\...`), local Ollama models, and self-healing embedded PostgreSQL locks without network overhead or storage fees.
  - *Hosted Hugging Face Space (Cloud Access)*: Deploy the Gradio application to a public or private Hugging Face Space.
  - *PostgreSQL on Hugging Face Considerations*:
    - **Ephemeral Storage as a Demo Sandbox Feature**: For a public-facing demo or interactive playground, ephemeral container storage is an intentional architectural advantage. Every visitor or session gets an isolated, self-cleaning sandbox. Visitors can upload sample documents, run prompt tests, and inspect tables without data leakage, privacy concerns between visitors, or disk bloat. The embedded PostgreSQL instance spins up automatically on Space boot, operates in-container, and cleanly resets on sleep/restart.
    - **Persistent Options (If Long-Term Retention Needed)**: If production data retention is desired, pair with external serverless PostgreSQL (Neon / Supabase free tier) or attach a Hugging Face persistent SSD volume ($5/mo).

---

## 4. Medium-Term Possibilities & Technical Enhancements

### A. Pure CSS Zero-JS Interactivity
- **Pure CSS Image Lightbox / Modal**:
  - Using CSS `:target` on `<figure id="photo-1">` so clicking an image enlarges it into a full-screen overlay with caption, and clicking a close link (`#_`) dismisses it — 100% zero JavaScript.
- **Pure CSS Tag & Lane Filtering**:
  - Exploring CSS radio-button or `:target` tricks to filter articles on `posts.html` without client-side scripts.
- **Collapsible Reading Notes**:
  - Native `<details>` and `<summary>` styling for extended quotes, bibliographic citations, and mental model breakdowns.

### B. Obsidian-to-Web Bridge Deepening
- **Internal Wikilink Resolution**:
  - Python Markdown extension translating Obsidian `[[slug|label]]` and `[[slug]]` syntax directly to `<a href="/posts/slug.html">label</a>`.
- **Obsidian Callout Blocks**:
  - Rendering Obsidian-style callouts (`> [!note]`, `> [!quote]`, `> [!tip]`, `> [!warning]`) into styled semantic blockquotes with corresponding CSS accents.
- **Bidirectional Backlinks**:
  - Pelican build plugin generating a static "Referenced By" backlink index at the footer of each article.

### C. Media & Performance Optimization
- **Responsive Picture Formats**:
  - Build-time image pipeline (using pure Python Pillow) to generate modern AVIF and WebP variants with responsive `srcset` markup.
- **Native HTML5 Audio Player**:
  - Embedding clean `<audio controls>` elements for Jim's fingerstyle guitar and piano study recordings, offering lossless FLAC and compressed MP3 downloads.
- **Print Stylesheets**:
  - Refined `@media print` rules ensuring clean, beautifully margined paper printouts of essays, articles, and music charts.

---

## 5. "To Heart's Desire" — Speculative Sandbox & Future Wishlist

*A collection of creative possibilities, technical experiments, and inventive ideas to inspire future building:*

### 1. Lake Michigan Sky & Weather Chronicle
- A semi-automated weather annotation script that queries NOAA / NWS API for historical weather data (temperature, wind direction, wave height, cloud cover) corresponding to the exact timestamp of Jim's lakefront photographs, adding atmospheric context to the gallery.

### 2. Pure SVG Fretboard & Chord Diagram Generator
- A pure Python CLI script that parses ASCII or YAML chord definitions and outputs pixel-perfect, scalable SVG chord boxes and fretboard scale runs for classical guitar studies, fully styled for dark and light modes.

### 3. Statically Pre-Indexed Subject Concordance (Zero-JS Search)
- Instead of client-side search scripts, Pelican compiles an automated alphabetical Subject Index (`index-concordance.html`) mapping key concepts, authors, books, and musical terms to their occurrences across all published posts.

### 4. Tai Chi & Alexander Technique Movement Vectors
- Vector-based skeletal and alignment diagrams illustrating Tai Chi form transitions, centerline grounding, and Alexander Technique head-neck release mechanics.

### 5. Static Micro-Zines / Annual Print Edition
- A Python build utility using WeasyPrint to compile Jim's annual articles, photo highlights, and bookshelf notes into a beautifully typeset, printable PDF book or personal zine.

### 6. Offline-First PWA Archive (Offline Reading Mode)
- An optional service-worker manifest allowing the entire site (HTML + CSS + compressed images) to be cached locally on a phone or tablet for distraction-free reading while camping, traveling, or off the grid.

### 7. Clean RSS & Fediverse Synergies
- Statically generated RSS 2.0 and Atom feeds for each lane (`/lanes/music.xml`, `/lanes/software.xml`), plus static IndieWeb Webmention discovery tags.

---

## 6. How Ideas Move from Roadmap to Production

```text
[ROADMAP.md]                  [PLANNING.md]                 [BUILD & TEST]              [JOURNAL.md]
Creative Brainstorming   -->  Active Sprint Backlog    -->  Pelican + Playwright   -->  Documented Milestones
Ideas & Possibilities         Near-Term Milestones          19 Automated Tests          Permanent Decision Log
```

1. **Ideation**: Discussed freely in `ROADMAP.md`.
2. **Prioritization**: Jim selects an initiative to move into `PLANNING.md` as an active milestone.
3. **Implementation & Testing**: Built using standard Python CLI tools (`uv`), validated by the test suite and Playwright visual audits.
4. **Permanent Record**: Archived into `JOURNAL.md` as a completed milestone with lessons learned.
