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

<div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Source Repository</div>
    <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem;">
      <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io" target="_blank" rel="noopener">GitHub Repository &rarr;</a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">jimcollinsworth.github.io</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Site Version &amp; Releases</div>
    <div style="font-size: 1.2rem; font-weight: 600; color: var(--accent); margin-top: 0.4rem;">
      <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases" target="_blank" rel="noopener">v0.5.6.01 &bull; Release Notes &rarr;</a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Full historical release notes v0.1 &ndash; v0.5.6.01</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">CI/CD Pipeline</div>
    <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem;">
      <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/actions" target="_blank" rel="noopener">
        <img src="https://github.com/jimcollinsworth/jimcollinsworth.github.io/actions/workflows/deploy.yml/badge.svg" alt="Deploy Status" style="vertical-align: middle; display: inline-block; max-width: 100%;">
      </a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">GitHub Actions (Tests + Build)</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Reading Payload</div>
    <div style="font-size: 1.2rem; font-weight: 600; margin-top: 0.4rem;">0 KB (Zero-JS)</div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">0 scripts, 0 cookies, 0 trackers on reading pages</div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Hosting &amp; Delivery</div>
    <div style="font-size: 1.1rem; font-weight: 600; margin-top: 0.4rem;">GitHub Pages</div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Global CDN + Custom Domain HTTPS</div>
  </div>
</div>

---

## The Technology Stack

- **LLM &amp; Agent Harness**: [Google Antigravity](https://deepmind.google/) advanced agentic AI pair programming platform running Google DeepMind models with autonomous tool integration, proactive test execution, and strict governance constraints.
- **Static Site Generator**: [Pelican](https://getpelican.com/) (Python static generator) compiling Markdown with custom YAML frontmatter into clean HTML5.
- **Tabular &amp; Info Data Architecture**: Centralized static data directory (`content/data/`) housing structured JSON, CSV, and tabular data feeds for applications and site indexing.
- **Interactive Application Sandbox**: Dedicated standalone mini-applications (`content/apps/`) built with standards-compliant HTML5/CSS/JS, querying local static datasets and external APIs while preserving a 100% Zero-JS guarantee for all editorial reading content.
- **Python Environment &amp; Package Manager**: [uv](https://astral.sh/uv) fast Python package resolver and runner with Python 3.13.
- **Templating**: Jinja2 semantic templates in `theme/templates/`.
- **Styling**: Single pure CSS stylesheet (`theme/static/css/style.css`) featuring modern CSS Grid, fluid container scaling (1080px / 1380px), responsive orientation modes, and pure-CSS theme switchers (`body:has(:checked)`).
- **Test Automation**: [pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/) headless browser test suite (`tests/`) validating build output, zero-JS compliance, WCAG AAA accessibility, and 8 responsive viewports.

---

## Antigravity AI &amp; Pair Programming Model

Site development and infrastructure management are conducted through collaborative pair programming with **Google Antigravity** (agentic AI coding assistant).

### Roles &amp; Boundaries
- **Content Authorship (100% Jim)**: Jim authors all notes, essays, book reflections, museum critiques, and personal thoughts in Obsidian. Jim personally selects and curates all photos. The AI agent is strictly prohibited from ghostwriting or fabricating personal opinions, articles, or prose.
- **Infrastructure &amp; Maintenance (Antigravity Agent)**: Antigravity manages static site generator configuration (`pelicanconf.py`), Jinja2 theme blueprints, CSS grid layouts, test suite maintenance (`test_pelican_e2e.py`, `test_accessibility.py`), CI/CD workflows, and link auditing.
- **Governance (The 3-Document Rule)**: Project context is strictly bounded to three root files:
  1. `README.md` &mdash; System architecture, setup instructions, and standard commands.
  2. `PLANNING.md` &mdash; Active milestones, backlog, and technical roadmap.
  3. `JOURNAL.md` &mdash; Chronological decision log and change records.

### Prompt &amp; Instruction Timeline
Every architectural transition, design system rule, and convention on this site was directed through human instructions and critical course corrections from Jim.
- [**Explore the Prompt History &amp; Instruction Timeline &rarr;**](prompt-history.html) &mdash; Detailed timeline of Jim's instructions, error remediations, and resulting architectural pivots synced to each version release.

---

## Authoring &amp; Publishing Workflow

```text
[ Obsidian Vault (Jim's Notes & Frontmatter) ]
                    │
                    ▼
[ Content Drop: content/posts/, content/pages/, content/data/ ]
                    │
                    ▼
[ Pelican + ObsidianMarkdownReader (pelicanconf.py) ]
                    │
                    ▼
[ Automated Validation (pytest -v: 30+ Tests) ]
                    │
                    ▼
[ Git Push -> GitHub Actions CI/CD -> GitHub Pages CDN ]
```
