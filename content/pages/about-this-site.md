---
title: "About This Site"
slug: "about-this-site"
template: "about-this-site"
---

**About This Site** outlines the technical architecture, infrastructure, tooling, and design principles behind `jimcollinsworth.github.io`. I built this site using Markdown, Pelican, HTML5, and CSS, containing zero client-side JavaScript on content pages. All my steering prompts and remediation instructions for building this site are recorded on [Development Prompts](prompt-history.md).

## Content Streams & Provenance

This is about provenance and my desire to attempt to separate and identify AI or others' contributions from my small writings on the site. Behind the scenes, content is organized by origin and perspective rather than rigid subject silos:

- **Me**: Notes about myself, personal biodata (activity, sleep, health tracking), personal bookmarks, and things written about me by me.
- **Mine**: Original essays, technical notes, software, and physical making projects authored directly by me.
- **AI**: Explorations and code generated or co-authored with artificial intelligence.
- **Ours**: Collaborative works and shared experiences created or documented jointly with family, peers, and friends &mdash; such as hikes, events, museum visits, tours, and joint projects (or human and AI collaboration).
- **Theirs**: Curated external references, exhibitions, events, museum tours, quotes, and third-party works.

Unpolished concepts, seedlings, and prompts across these streams are collected in the high-density [Ideas](ideas.md) stream.

---

## The Technology Stack

- **LLM & Agent Harness**: [Google Antigravity](https://deepmind.google/) agentic coding platform running Google DeepMind models with tool integration, test execution, and governance constraints.
- **Static Site Generator**: [Pelican](https://getpelican.com/) (Python static generator) compiling Markdown with custom YAML frontmatter into HTML5.
- **Tabular & Info Data Architecture**: Centralized static data directory (`content/data/`) housing structured JSON, CSV, and tabular data feeds for applications and site indexing.
- **Interactive Application Sandbox**: Standalone mini-applications (`content/apps/`) built with HTML5, CSS, and JavaScript, querying static datasets in `content/data/` while preserving zero client-side JavaScript on reading pages.
- **Python Environment & Package Manager**: [uv](https://astral.sh/uv) Python package resolver and runner with Python 3.13.
- **Templating**: Jinja2 semantic templates in `theme/templates/`.
- **Styling**: Single CSS stylesheet (`theme/static/css/style.css`) featuring CSS Grid, container scaling (1080px / 1380px), responsive orientation modes, and CSS theme switchers (`body:has(:checked)`).
- **Test Automation**: [pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/) headless browser test suite (`tests/`) validating build output, zero-JS compliance, WCAG AAA accessibility, and 8 responsive viewports.

---

## Antigravity AI & Pair Programming Model

Site development and infrastructure management are conducted through collaborative pair programming with **Google Antigravity** (agentic AI coding assistant).

### Roles & Boundaries
- **Content Authorship (100% Jim)**: Jim authors all notes, essays, book reflections, museum critiques, and personal thoughts in Obsidian. Jim personally selects and curates all photos. The AI agent is strictly prohibited from ghostwriting or fabricating personal opinions, articles, or prose.
- **Infrastructure & Maintenance (Antigravity Agent)**: Antigravity manages static site generator configuration (`pelicanconf.py`), Jinja2 theme blueprints, CSS grid layouts, test suite maintenance (`test_pelican_e2e.py`, `test_accessibility.py`), CI/CD workflows, and link auditing.
- **Governance (The 3-Document Rule)**: Project context is strictly bounded to three root files:
  1. `README.md` &mdash; System architecture, setup instructions, and standard commands.
  2. `PLANNING.md` &mdash; Active milestones, backlog, and technical roadmap.
  3. `JOURNAL.md` &mdash; Chronological decision log and change records.

### Prompt & Instruction Timeline
Every architectural transition, design system rule, and convention on this site was directed through human instructions and course corrections from Jim.
- [**Explore the Prompt History & Instruction Timeline &rarr;**](prompt-history.md) &mdash; Timeline of Jim's instructions, error remediations, and resulting architectural pivots synced to each version release.

---

## Authoring & Publishing Workflow

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
[ Automated Validation (pytest -v: 52 Tests) ]
                    │
                    ▼
[ Git Push -> GitHub Actions CI/CD -> GitHub Pages CDN ]
```

---

## License

Content and essays &copy; Jim Collinsworth, licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
