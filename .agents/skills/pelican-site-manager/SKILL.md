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

## 4. Strict Content Boundary Rules

> [!CAUTION]
> **The agent must never author content posts for Jim.**
> If asked to scaffold a new post, the agent must ONLY create front-matter metadata and standard `Lorem ipsum` placeholder text.

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

## 5. Verification Checklist

After running a build:
1. **Zero-JS Check**: Verify no `<script>` tags were introduced into content pages.
2. **Link Verification**: Ensure relative links between `index.html`, `about.html`, `posts.html`, and `reads.html` resolve correctly.
3. **Asset Verification**: Ensure all images referenced in `<figure>` tags exist in `output/assets/` or `output/images/`.
4. **Clean Git State**: Verify only intended HTML/markdown files are modified.
