---
title: "About This Site"
slug: "about-this-site"
template: "about-this-site"
---

[Mine] **About This Site** outlines the technical architecture and infrastructure behind `jimcollinsworth.github.io`. This website is built through pair programming with artificial intelligence under my direct architectural guidance &mdash; with the AI assistant managing static site generation, Jinja2 theme templates, responsive CSS layouts, and comprehensive test automation. The site serves pure HTML and CSS with zero client-side JavaScript on reading pages. All steering prompts, technical decisions, and course corrections are logged on [Development Prompts](prompt-history.md).

## [Mine] Content Streams & Provenance

Content is organized by authorship origin and perspective rather than subject silos:

- **Me**: Direct autobiographical notes, biodata (sleep, health, activity), and reflections written by Jim.
- **Mine**: Original essays, technical notes, software, and physical making authored by Jim.
- **AI**: Codebases, tools, and explorations co-authored or generated with artificial intelligence.
- **Ours**: Joint works and shared experiences created with family, peers, and collaborators.
- **Theirs**: Curated external references, quotes, and third-party works.

Raw seedling concepts across all streams are collected in the high-density [Ideas](ideas.md) stream.

---

## [Mine] Technology Stack

- **Static Site Engine**: [Pelican](https://getpelican.com/) (Python) compiling Markdown with custom YAML frontmatter into static HTML5.
- **Styling & Layout**: Single CSS stylesheet (`theme/static/css/style.css`) featuring modern CSS Grid, container scaling, dark/light modes, and zero-JS display controls.
- **Interactive Apps**: Standalone mini-apps in `content/apps/` querying static JSON datasets in `content/data/`.
- **Environment & Runner**: [uv](https://astral.sh/uv) package manager with Python 3.13.
- **Test Automation**: [pytest](https://docs.pytest.org/) and [Playwright](https://playwright.dev/) test suite auditing HTML markup, zero-JS compliance, and 8 responsive viewports.
