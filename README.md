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
├── tests/
│   └── test_pelican_e2e.py       # End-to-end test suite (build, links, zero-JS, formatting)
├── pelicanconf.py                # Pelican configuration (with Obsidian YAML frontmatter reader)
├── pyproject.toml                # Project dependencies (pelican, markdown, pyyaml, pytest)
├── output/                       # Generated static HTML (deployed to GitHub Pages)
├── README.md                     # Core document 1: Site overview & guide
├── PLANNING.md                   # Core document 2: Active roadmap & backlog
└── JOURNAL.md                    # Core document 3: Chronological changelog
```

---

## Standard CLI Commands

All operations use clean, standard commands that can be run directly in any terminal:

### Install Dependencies
```bash
uv sync
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

## Agent Governance: The 3-Document & Content Rules

Per `.agents/agent_rules.md`:
1. **Mandatory 3-Document Rule**: The agent may maintain **only three** root system design documents:
   - `README.md` (System overview, architecture, and instructions)
   - `PLANNING.md` (Active roadmap and technical backlog)
   - `JOURNAL.md` (Chronological decision log and change records)
2. **Content Ownership**: The agent must **never draft content documents, create content files, or write articles** for Jim. All content authoring and image curation belongs exclusively to Jim.
3. **Command Line Standards**: All agent commands must be standard, clean, reproducible CLI invocations that Jim can run manually.

---

## License

Content and essays &copy; Jim Collinsworth, licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
