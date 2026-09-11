# jimcollinsworth.github.io

> Personal website, journal, and exploration lanes of **Jim Collinsworth** — *Out of My Lane*.

---

## Overview & Philosophy

This site is an intentionally simple, durable personal web space. It has been built with an uncompromising commitment to long-term digital sustainability, reading comfort, and clean engineering:

- **Static Site Generation via Pelican**: Fast, clean Python-based static site compilation from Markdown notes.
- **Zero Client-Side JavaScript**: 100% pure semantic HTML5 and modern CSS on content pages. Zero `<script>` tags, tracking, or runtime dependencies.
- **Modern Responsive CSS**: Clean typography, fluid layouts, and automatic dark/light theme switching via `@media (prefers-color-scheme: dark)`.
- **Content-Out Editorial Design**: Inspired by [Pine Wind (Bear Blog)](https://pinewind.bearblog.dev/) and [Mark Boulton](https://markboulton.co.uk/journal/anewcanon/).
- **Human-Curated Content & Images**: Jim explicitly and manually authors every post in Obsidian and manually transfers every photo shown on the site. AI agents are strictly restricted to content management (infrastructure, build configuration, layout styling, and link validation).

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
│   ├── posts/                    # Long-form posts (Health, Projects, Software, Ideas, Music)
│   ├── pages/                    # Standalone pages (about.md, reads.md, gallery.md)
│   ├── images/                   # Manually curated photos referenced by posts
│   └── extra/                    # Favicons and verification tokens
├── theme/                        # Custom Pelican Jinja2 theme
│   ├── templates/                # base.html, index.html, article.html, page.html, etc.
│   └── static/css/style.css      # Central stylesheet (zero pills, dark/light mode)
├── docs/
│   └── content_authoring.md      # Canonical Pelican 4.12.0 content authoring & metadata guide
├── tests/
│   ├── test_pelican_e2e.py       # End-to-end test suite (build, links, zero-JS, formatting)
│   └── test_playwright_responsive.py # Playwright headless browser & responsive audit
├── tools/
│   └── screenshots.py            # Multi-resolution screenshot generator (4 devices x 2 orientations)
├── pelicanconf.py                # Pelican configuration (with Obsidian YAML frontmatter reader)
├── pyproject.toml                # Project dependencies (pelican, markdown, playwright, pytest)
├── output/                       # Generated static HTML (deployed to GitHub Pages)
├── README.md                     # Core document 1: Site overview & guide
├── PLANNING.md                   # Core document 2: Active roadmap & backlog
├── ROADMAP.md                    # Core document 3: Long-term vision & brainstormed ideas
└── JOURNAL.md                    # Core document 4: Chronological changelog
```

---

## Content Authoring & Pelican Metadata (Official 4.12.0 Baseline)

All site content adheres strictly to official **Pelican 4.12.0** conventions combined with Jim's Obsidian workflow. See the full specification in [`docs/content_authoring.md`](docs/content_authoring.md).

- **Articles vs. Pages**:
  - **Articles** (`content/posts/*.md`): Temporal, chronological posts with publication dates, organized into Pursuit Lanes (`Category: Music`, `Health`, etc.), and syndicated into RSS feeds.
  - **Pages** (`content/pages/*.md`): Non-temporal standalone documents (`about.md`, `reads.md`, `gallery.md`, `pipeline-tools.md`).
- **YAML Frontmatter**: In-file metadata uses clean standard YAML headers (`---` delimiters) parsed by `ObsidianMarkdownReader`. Standard fields include `Title:`, `Date:`, `Category:`, `Summary:`, `Tags:`, and `Slug:`.
- **Intra-Site Link Directives (Compile-Time Resolution)**:
  - `{filename}`: Cross-references internal articles or pages (e.g., `[Sleep Plan]({filename}/posts/sleep-movement-evaluation-plan.md)`).
  - `{static}`: Links directly to static assets/images (e.g., `![Photo]({static}/images/lakefront.jpg)`).
  - `{category}`: Links to Pursuit Lane archive indexes (e.g., `[Music Lane]({category}music)`).
- **Code Highlighting**: Pure Markdown fenced blocks (`python`, `bash`, etc.) with Pygments syntax highlighting via Pelican's `codehilite` extension.

---

## Developer Utilities & Command Reference

All developer tools and test suites are 100% pure Python managed cleanly via `uv`. Strictly **no Node.js or npm** ever for applications or toolchains (sole exception: `npx skills` for agent skills).

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

A pure-Python Playwright utility that captures any site page across **4 device form factors** in both **Portrait and Landscape** orientations (8 viewports total):

| Device Form Factor | Portrait Viewport | Landscape Viewport | Target Device Class |
| :--- | :--- | :--- | :--- |
| **Phone** | 390 × 844 | 844 × 390 | iPhone 12–16 / Modern Mobile |
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


All operations use clean, standard commands that can be run directly in any terminal:

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
4. **Command Line Standards**: All agent commands must be standard, clean, reproducible CLI invocations that Jim can run manually.
5. **Toolchain Constraints**: Strictly **no Node.js or npm** ever for applications or toolchains (only exception: `npx skills`).
6. **Remote Git Push Protection**: The agent must **never execute `git push`** without Jim's explicit request or confirmation.
7. **No Tunneling or Privilege Escalation**: Strictly **no Tailscale, ngrok, tunnels, VPNs, or permission bypasses**. Only Jim configures access; always ask first.
8. **Workspace Isolation**: The agent must **stay strictly within the project directory**. Always explain reasoning and ask Jim for explicit permission before searching or working outside.


---

## License

Content and essays &copy; Jim Collinsworth, licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
