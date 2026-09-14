---
title: "About This Site"
slug: "about-this-site"
---

<div class="page-intro">
  <p>
    <strong>About This Site</strong> outlines the technical architecture, infrastructure, tooling, and design principles behind <code>jimcollinsworth.github.io</code>. It is built with Pelican, HTML5, and CSS, containing zero client-side JavaScript on content pages.
  </p>
</div>

## Content Streams & Provenance

This is about provenance and my desire to attempt to separate and identify AI or others' contributions from my small writings on the site. Behind the scenes, content is organized by origin and perspective rather than rigid subject silos:

- <span class="category-badge" title="Category: Me" aria-label="Category: Me"><svg class="category-icon icon-me" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span> **Me**: Notes about myself, personal biodata (activity, sleep, health tracking), personal bookmarks, and things written about me by me.
- <span class="category-badge" title="Category: Mine" aria-label="Category: Mine"><svg class="category-icon icon-mine" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span> **Mine**: Original essays, technical notes, software, and physical making projects authored directly by me.
- <span class="category-badge" title="Category: AI" aria-label="Category: AI"><svg class="category-icon icon-ai" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg></span> **AI**: Explorations and code generated or co-authored with artificial intelligence.
- <span class="category-badge" title="Category: Ours" aria-label="Category: Ours"><svg class="category-icon icon-ours" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-3-3.87"></path><path d="M7 21v-2a4 4 0 0 1 3-3.87"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></span> **Ours**: Collaborative works and shared experiences created or documented jointly with family, peers, and friends &mdash; such as hikes, events, museum visits, tours, and joint projects (or human and AI collaboration).
- <span class="category-badge" title="Category: Theirs" aria-label="Category: Theirs"><svg class="category-icon icon-theirs" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.75-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 2-2 3-3 4"></path><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.75-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 2-2 3-3 4"></path></svg></span> **Theirs**: Curated external references, exhibitions, events, museum tours, quotes, and third-party works.

Unpolished concepts, seedlings, and prompts across these streams are collected in the high-density [Ideas](ideas.html) stream.

---

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
      <a href="prompt-history.html">v0.7.6 &bull; Release Notes &rarr;</a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Chronological milestones v0.1 &ndash; v0.7.6 &bull; <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/tags" target="_blank" rel="noopener">GitHub Tags</a></div>
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

  <div class="dashboard-card" style="border: 1px solid var(--border-color); padding: 1rem; border-radius: 4px;">
    <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted);">Steering Prompts</div>
    <div style="font-size: 1.2rem; font-weight: 600; color: var(--accent); margin-top: 0.4rem;">
      <a href="prompt-history.html">102 Prompts &rarr;</a>
    </div>
    <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.25rem;">Direct human guidance &amp; remediation</div>
  </div>
</div>

---

## The Technology Stack

- **LLM &amp; Agent Harness**: [Google Antigravity](https://deepmind.google/) agentic coding platform running Google DeepMind models with tool integration, test execution, and governance constraints.
- **Static Site Generator**: [Pelican](https://getpelican.com/) (Python static generator) compiling Markdown with custom YAML frontmatter into HTML5.
- **Tabular &amp; Info Data Architecture**: Centralized static data directory (`content/data/`) housing structured JSON, CSV, and tabular data feeds for applications and site indexing.
- **Interactive Application Sandbox**: Standalone mini-applications (`content/apps/`) built with HTML5, CSS, and JavaScript, querying static datasets in `content/data/` while preserving zero client-side JavaScript on reading pages.
- **Python Environment &amp; Package Manager**: [uv](https://astral.sh/uv) Python package resolver and runner with Python 3.13.
- **Templating**: Jinja2 semantic templates in `theme/templates/`.
- **Styling**: Single CSS stylesheet (`theme/static/css/style.css`) featuring CSS Grid, container scaling (1080px / 1380px), responsive orientation modes, and CSS theme switchers (`body:has(:checked)`).
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
Every architectural transition, design system rule, and convention on this site was directed through human instructions and course corrections from Jim.
- [**Explore the Prompt History &amp; Instruction Timeline &rarr;**](prompt-history.html) &mdash; Timeline of Jim's instructions, error remediations, and resulting architectural pivots synced to each version release.

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
[ Automated Validation (pytest -v: 51 Tests) ]
                    │
                    ▼
[ Git Push -> GitHub Actions CI/CD -> GitHub Pages CDN ]
```
