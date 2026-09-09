# Content Authoring & Pelican Metadata Guide

This document establishes the canonical content authoring standards, metadata keywords, intra-site linking conventions, and file organization for **Out of My Lane** (`jimcollinsworth.github.io`). It aligns official Pelican static generator conventions with Jim's Obsidian authoring workflow.

---

## 1. Core Distinction: Articles vs. Pages

Pelican separates content into two distinct types:

| Concept | Purpose | Location | Characteristics |
| :--- | :--- | :--- | :--- |
| **Articles** | Temporal, chronological posts | `content/posts/*.md` | Has publication `Date`, categorized into a **Pursuit Lane**, indexed in archives (`posts.html`), RSS feeds, and featured lists. |
| **Pages** | Non-temporal, standalone documents | `content/pages/*.md` | Standalone reference or dashboard pages (`about.md`, `reads.md`, `gallery.md`, `pipeline-tools.md`). Does not belong to a category feed. |
| **Static Files** | Raw media and static assets | `content/images/`, `content/extra/` | Copied as-is to `output/` without Markdown/template parsing. |

---

## 2. File Metadata Specification

All Markdown files author metadata using standard YAML frontmatter (`---` delimiters) parsed by `ObsidianMarkdownReader`:

```markdown
---
Title: Cordoba Stage Guitar Setup & Piezo EQ
Date: 2026-09-07 10:30
Modified: 2026-09-08 14:15
Category: Music
Tags: guitar, nylon-string, lutherie, audio
Slug: cordoba-stage-guitar
Authors: Jim Collinsworth
Summary: Action adjustments, string tension choices, and acoustic preamp equalization notes.
Status: published
---
```

### Metadata Reference Table

| Keyword | Required? | Format / Values | Description |
| :--- | :--- | :--- | :--- |
| **`Title`** | **Yes** | Text string | Title of the article or page. Used in `<title>`, `<h1>`, and cards. |
| **`Date`** | **Yes** (Articles) | `YYYY-MM-DD` or `YYYY-MM-DD HH:MM` | Publication timestamp. Governs chronological ordering. |
| **`Category`** | **Yes** (Articles) | Single string (One of the Pursuit Lanes) | Primary domain (`Music`, `Health`, `Software`, `Making`, `Reads`, `Ideas`, `Projects`). |
| **`Slug`** | Optional | Lowercase URL slug (e.g., `cordoba-stage-guitar`) | Determines the output URL (`posts/{slug}.html`). Auto-generated from Title if omitted. |
| **`Summary`** | Recommended | 1–2 plain text sentences | Explicit teaser description displayed in article lists and index cards. |
| **`Tags`** | Optional | Comma-separated list | Specific subject keywords (e.g. `guitar, piezo, acoustic`). |
| **`Modified`** | Optional | `YYYY-MM-DD HH:MM` | Timestamp of last revision or update. |
| **`Authors`** | Optional | Text string | Author name (defaults to `Jim Collinsworth` via `pelicanconf.py`). |
| **`Status`** | Optional | `published`, `draft`, `hidden` | `draft` excludes from feeds; `hidden` builds page without listing it in menus. |
| **`Save_as`** | Optional | Relative output path | Custom output destination override. |
| **`Template`** | Optional | Template name (e.g., `page`, `article`) | Custom Jinja2 template override if needed. |

---

## 3. Linking to Internal Content & Assets

Pelican provides built-in link directives that resolve paths at compile time regardless of where the final files are deployed:

### A. Linking to Another Article or Page (`{filename}`)
Use `{filename}` followed by the source path (using forward slashes `/`):
```markdown
[Read about sleep health]({filename}/posts/sleep-movement-evaluation-plan.md)
[View the bookshelf]({filename}/pages/reads.md)
[Relative post link]({filename}ulu-knife-handle.md)
```
*At build time, Pelican converts this directly into the published URL (e.g. `./posts/sleep-movement-evaluation-plan.html`).*

### B. Linking to Static Assets & Images (`{static}`)
Use `{static}` to link to images and documents without relocating them:
```markdown
![Lake Michigan horizon]({static}/images/sky-lakefront.jpg)
[Download Diagram]({static}/extra/schematic.pdf)
```

### C. Attaching Static Files to an Article (`{attach}`)
Use `{attach}` when you want an asset stored next to an article to be copied directly into the article's output directory:
```markdown
![Wiring Diagram]({attach}diagram.png)
```

### D. Linking to Pursuit Lanes (`{category}`)
Link directly to a pursuit lane archive:
```markdown
[Browse all Music notes]({category}music)
[Browse all Health notes]({category}health)
```

---

## 4. Syntax Highlighting

For code snippets, use standard Markdown fenced code blocks with language identifiers. Pelican's `codehilite` extension formats them with Pygments:

````markdown
```python
def calculate_tempo(bpm: float) -> float:
    """Calculate quarter-note duration in seconds."""
    return 60.0 / bpm
```
````

For code blocks with line numbers, use the triple-colon or shebang syntax supported by Python-Markdown:
```python
:::python
print("Syntax highlighted with Pygments")
```

---

## 5. Obsidian Authoring Integration

When authoring in Obsidian:
1. **Frontmatter**: Keep standard `---` YAML frontmatter at the top of your `.md` files.
2. **Images**: Images stored in `content/images/` can be linked via standard Markdown `![Caption]({static}/images/filename.jpg)` or Obsidian drag-and-drop.
3. **Internal Links**: Write `{filename}/posts/slug.md` for foolproof cross-note links that compile cleanly on the web.
