---
name: pelican-site-manager
description: >-
  Manage, configure, build, and maintain a static site using the Pelican Python
  static site generator. Use when setting up or modifying pelicanconf.py,
  building HTML from content/, configuring themes, testing builds, or publishing to GitHub Pages.
---

# Pelican Site Manager

This skill guides the setup, configuration, local testing, and maintenance of static websites powered by **Pelican**, the mature Python-based static site generator.

---

## 1. Architecture & Directory Layout

A standard, clean Pelican layout for this repository:

```text
├── content/                    # Source Markdown files (Obsidian vault drop)
│   ├── posts/                  # Blog posts and deep dives
│   ├── pages/                  # Static pages (about, reads, gallery)
│   └── attachments/            # Images and media referenced by notes
├── theme/                      # Custom Jinja2 theme templates
│   ├── templates/
│   │   ├── base.html           # Site shell: header, site-nav, footer
│   │   ├── index.html          # Recent posts, reads highlight, photo spotlight
│   │   ├── article.html        # Individual post template
│   │   ├── category.html       # Posts by pursuit lane
│   │   └── page.html           # Standalone pages (About, Reads)
│   └── static/css/             # Assets (assets/css/style.css)
├── pelicanconf.py              # Local development configuration
├── publishconf.py              # Production / GitHub Pages configuration
└── output/                     # Generated static HTML (or deployed directly)
```

---

## 2. Core Pelican Configuration (`pelicanconf.py`)

When configuring Pelican, always adhere to the site's **Zero-JS policy** and **pure HTML5/CSS design system**:

```python
AUTHOR = 'Jim Collinsworth'
SITENAME = 'Jim Collinsworth'
SITESUBTITLE = 'Out of My Lane'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# URL structure
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'lanes/{slug}.html'
CATEGORY_SAVE_AS = 'lanes/{slug}.html'

# Content paths
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['attachments', 'assets']

# Theme
THEME = 'theme'

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.toc': {'permalink': False},
    },
    'output_format': 'html5',
}

# Feeds & Extra Pages
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pagination
DEFAULT_PAGINATION = 10
```

---

## 3. Standard CLI Commands (Reproducible)

Per the project's **Command Line Standards**, always use clean, standard commands that can be run directly in the terminal:

### Install Dependencies
```bash
uv pip install pelican markdown pyyaml jinja2
```

### Build the Site (Development)
```bash
pelican content -s pelicanconf.py
```

### Local Live Preview
Start Pelican's built-in local web server with auto-regeneration:
```bash
pelican --listen
```
Open `http://localhost:8000` in the browser.

### Production Build for GitHub Pages
```bash
pelican content -s publishconf.py -o output
```

---

## 4. Strict Content Boundary & Source Markdown Rules

> [!CAUTION]
> **The agent must never author content posts for Jim.**
> - **100% Human Content in `content/`**: Everything in `content/` is templated Markdown with metadata, photos, and media authored exclusively by Jim.
> - **Zero AI-Generated Content or Source Badges in `content/`**: No file in `content/` contains AI-generated prose or source-level provenance shortcuts (`[Mine]`, `[AI]`). Everything originating in `content/` is intrinsically Jim's.
> - **Scaffolding Only**: If asked to scaffold a new post, the agent must ONLY create clean YAML front-matter metadata and standard `Lorem ipsum` placeholder text.

### Scaffolding Template
```markdown
---
Title: Post Title
Date: 2026-09-08
Category: Software
Tags: python, static-site
Slug: post-title
Summary: One-line takeaway summary.
---

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
```

---

## 5. Discovered Pelican Patterns, Tips & Tricks

1. **Resilient Jinja2 Logic for Empty Article Lists**:
   - Always guard article indexing in templates with `{% if standard_articles %}` to prevent `UndefinedError: list object has no element 0` on newly initialized sites or sites with 0 articles:
     ```jinja2
     {% set standard_articles = articles|rejectattr('type', 'equalto', 'IDEA')|list %}
     {% set featured_matches = standard_articles|selectattr('featured', 'defined')|selectattr('featured')|list %}
     {% if featured_matches %}
       {% set featured = featured_matches[0] %}
     {% elif standard_articles %}
       {% set featured = standard_articles[0] %}
     {% else %}
       {% set featured = none %}
     {% endif %}
     {% set stream_articles = standard_articles|rejectattr('slug', 'equalto', featured.slug)|list if featured else [] %}
     ```

2. **Automated Intra-Site Link & Wikilink Resolution (`pelicanconf.py`)**:
   - Inheriting from `pelican.readers.MarkdownReader` allows automatic translation of Obsidian `[[wikilinks]]` and relative `.md` links into Pelican `{filename}` references (`{filename}/pages/about.md` or `{filename}/posts/...`), preventing broken links on static output pages.

3. **Pure CSS Zero-JS Sticky Slide-Cover**:
   - Stack pinned background header (`position: sticky; top: 0; z-index: 1`) behind scrolling body container (`position: relative; z-index: 2; background-color: var(--bg); box-shadow: ...`). Use `@media (max-height: 500px) and (orientation: landscape)` to automatically hide the sticky header on small landscape smartphones.

4. **Dynamic Image Src Resolution & HTML5 Figure Wrapping**:
   - Standardize `![alt](attachments/photo.jpg)` into semantic `<figure><img ...><figcaption>alt</figcaption></figure>`. Automatically adjust `src` depth (`../attachments/photo.jpg` for nested post pages vs `attachments/photo.jpg` for top-level pages).

5. **Responsive Mobile Table Scroll Containers**:
   - AST post-processing of `<table>` elements into `<div class="table-container" style="overflow-x: auto;">` prevents narrow mobile viewports from breaking layout alignment.

6. **Pure Markdown Provenance Shortcuts**:
   - Translate inline shortcuts (`[Mine]`, `[AI]`, `[Me]`, `[Ours]`, `[Theirs]`, `[AI+Mine]`) into accessible inline SVG badges with tooltips and ARIA attributes at build time.

7. **Theme Reusability & Modular Pathing**:
   - Configure modular theme paths via `THEME = 'themes/lakefront'` (or `THEME = 'theme'`) for instant deployment across multiple sites.

---

## 6. Verification Checklist

After running a build:
1. **Zero-JS Check**: Verify no `<script>` tags were introduced into content pages.
2. **Link Verification**: Ensure relative links between `index.html`, `about.html`, `posts.html`, and `reads.html` resolve correctly.
3. **Asset Verification**: Ensure all images referenced in `<figure>` tags exist in `output/assets/` or `output/images/`.
4. **Clean Git State**: Verify only intended HTML/markdown files are modified.
