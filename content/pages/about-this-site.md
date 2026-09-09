---
title: "About This Site"
slug: "about-this-site"
---

<div class="page-intro">
  <p>
    <strong>About This Site</strong> outlines the technical architecture, infrastructure, tooling, and design principles behind <code>jimcollinsworth.github.io</code>. It is built as a fast, durable, zero-JavaScript static site designed for long-term reading comfort and low-maintenance longevity.
  </p>
</div>

## DevOps & Infrastructure Dashboard

<div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">CI/CD Pipeline</div>
    <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem;">
      <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/actions" target="_blank" rel="noopener">
        <img src="https://github.com/jimcollinsworth/jimcollinsworth.github.io/actions/workflows/deploy.yml/badge.svg" alt="Deploy Status" style="vertical-align: middle; display: inline-block;">
      </a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">GitHub Actions (Tests + Build)</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Site Version</div>
    <div style="font-size: 1.2rem; font-weight: 600; color: var(--accent); margin-top: 0.4rem;">v0.5.5</div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Active Pre-Release (Targeting v1.0)</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">JavaScript Payload</div>
    <div style="font-size: 1.2rem; font-weight: 600; margin-top: 0.4rem;">0 KB (Zero-JS)</div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">0 scripts, 0 cookies, 0 trackers</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Hosting &amp; Delivery</div>
    <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem;">GitHub Pages</div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Global CDN + HTTPS</div>
  </div>
</div>

---

## The Technology Stack

- **Static Site Generator**: [Pelican](https://getpelican.com/) (Python static generator) compiling Markdown into clean HTML5.
- **Python Environment & Package Manager**: [uv](https://astral.sh/uv) fast Python package resolver and runner with Python 3.13.
- **Templating**: Jinja2 semantic templates in `theme/templates/`.
- **Styling**: Single pure CSS stylesheet (`theme/static/css/style.css`) featuring modern CSS Grid, fluid container scaling (1080px / 1380px), orientation adaptation, and automatic dark/light mode switching (`@media (prefers-color-scheme: dark)`).
- **Test Automation**: [pytest](https://docs.pytest.org/) automated end-to-end test suite (`tests/test_pelican_e2e.py`) validating build output, zero-JS compliance, title deduplication, and link/asset integrity on every push.

---

## Antigravity AI & Pair Programming Model

Site development and infrastructure management are conducted through collaborative pair programming with **Google Antigravity** (agentic AI coding assistant).

### Roles & Boundaries
- **Content Authorship (100% Jim)**: Jim authors all notes, essays, book reflections, and personal thoughts in Obsidian. Jim personally selects and transfers all photos. The AI agent is strictly prohibited from ghostwriting or fabricating personal opinions, articles, or prose.
- **Infrastructure & Maintenance (Antigravity Agent)**: Antigravity manages static site generator configuration (`pelicanconf.py`), Jinja2 theme blueprints, CSS grid layouts, test suite maintenance (`test_pelican_e2e.py`), CI/CD workflows, and link auditing.
- **Governance (The 3-Document Rule)**: Project context is strictly bounded to three root files:
  1. `README.md` &mdash; System architecture, setup instructions, and standard commands.
  2. `PLANNING.md` &mdash; Active milestones, backlog, and technical roadmap.
  3. `JOURNAL.md` &mdash; Chronological decision log and change records.

---

## Authoring & Publishing Workflow

```text
[ Obsidian Vault (Jim's Notes & Frontmatter) ]
                    │
                    ▼
[ Content Drop: content/posts/ & content/pages/ ]
                    │
                    ▼
[ Pelican + ObsidianMarkdownReader (pelicanconf.py) ]
                    │
                    ▼
[ Automated Validation (pytest -v) ]
                    │
                    ▼
[ Git Push -> GitHub Actions CI/CD -> GitHub Pages CDN ]
```

All commands use standard CLI tools executable on any machine:

```bash
# Sync dependencies
uv sync

# Build static site
uv run pelican content -s pelicanconf.py -o output -d

# Run local preview server
uv run pelican --listen -p 8000

# Execute end-to-end test suite
uv run pytest -v
```
