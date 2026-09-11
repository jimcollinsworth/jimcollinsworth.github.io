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
Title: Digital Piano Enhancements
Date: 2026-09-04
Lanes:
  - Music
  - Making
Type: PROJ
Previous_types:
  - IDEA
  - WIP
Slug: digital-piano-enhancements
Summary: Hardware and ergonomic modifications to Kawai-ES8 digital piano.
Status: published
---
```

### Metadata Reference Table

| Keyword | Required? | Format / Values | Description |
| :--- | :--- | :--- | :--- |
| **`Title`** | **Yes** | Text string | Title of the article or page. Used in `<title>`, `<h1>`, and cards. |
| **`Date`** | **Yes** (Articles) | `YYYY-MM-DD` or `YYYY-MM-DD HH:MM` | Publication timestamp. Governs chronological ordering. |
| **`Lanes`** | **Yes** (Articles) | YAML list or comma-separated string (e.g. `[Music, Making]`) | Pursuit Lanes for the post. A post can belong to **multiple lanes** (e.g., `AI`, `Health`, `Making`, `Music`). Pelican indexes the post in each assigned lane archive. |
| **`Category`** | Optional | Single string (fallback for `Lanes`) | Legacy single category fallback. `Lanes` is preferred. |
| **`Type`** | Optional | Uppercase short code (e.g., `PROJ`, `IDEA`, `WIP`, `SPEC`) | Single active post format indicator displayed alongside date and lane in lists. |
| **`Previous_types`** | Optional | YAML list or comma-separated short codes (e.g. `[IDEA, WIP]`) | Conceptual evolution lineage. Renders on the post as `(evolved from IDEA → WIP)`. |
| **`Slug`** | Optional | Lowercase URL slug (e.g., `digital-piano-enhancements`) | Determines the output URL (`posts/{slug}.html`). Auto-generated from Title if omitted. |
| **`Summary`** | Recommended | 1–2 plain text sentences | Explicit teaser description displayed in article lists and index cards. |
| **`Tags`** | Optional | Comma-separated list | Specific subject keywords (e.g. `piano, midi, ergonomics`). |
| **`Modified`** | Optional | `YYYY-MM-DD HH:MM` | Timestamp of last revision or update. |
| **`Authors`** | Optional | Text string or list (e.g. `Jim Collinsworth`, `Jim Collinsworth, LLM-Gemini3.8`) | Author credit. **Rule 14**: When AI is an author, co-author, or suspected contributor, credit the exact model ID prefixed with `LLM-` (e.g., `LLM-Gemini3.8`, `LLM-Qwen3.5`). |
| **`Status`** | Optional | `published`, `draft`, `hidden` | `draft` excludes from feeds; `hidden` builds page without listing it in menus. |
| **`Save_as`** | Optional | Relative output path | Custom output destination override. |
| **`Template`** | Optional | Template name (e.g., `page`, `article`) | Custom Jinja2 template override if needed. |

> [!IMPORTANT]
> **Lane vs. Type Distinction**:
> - **Pursuit Lanes** represent domains of human interest/pursuit: `AI`, `Art`, `Health`, `Making`, `Music`.
> - **`Ideas` and `Projects` are NOT pursuit lanes.** They are post types (`[IDEA]`, `[PROJ]`).
> - **`M.E.` (Mental Entity / My Essence) belongs to the `AI` pursuit lane** as an `[IDEA]`.

---

### Canonical 28 Post Types (Short Codes)

Post types decouple **content format & lifecycle** (`Type`) from **pursuit lane** (`Lanes`):

| Domain | Short Codes | Full Name & Description |
| :--- | :--- | :--- |
| **Core & Tech** | `TIL`<br>`WIP`<br>`URL`<br>`PROJ`<br>`APP`<br>`LOG`<br>`POST`<br>`SPEC`<br>`IDEA`<br>`OPS` | Today I Learned<br>Work In Progress (Workbench / In-flight)<br>Link / Bookmark<br>Project / Completed Build<br>Interactive App / Dashboard<br>Field Log / Journal<br>Essay / Long-form<br>Plan / Specification<br>Mental Model / Concept<br>DevOps / Build Meta |
| **Media & Sensory** | `READ`<br>`WATCH`<br>`LISTEN`<br>`VIEW` | Book / Essay / Paper Read<br>Video / Talk / Film Watched<br>Music Album / Audio Listened To<br>Art / Gallery / Vista Viewed |
| **Data & Science** | `DATA`<br>`VIZ`<br>`PERF`<br>`ASK` | Dataset / Data Drop<br>Data Visualization / Chart<br>Benchmark / Performance<br>Open Inquiry / Question |
| **Outdoors & Life** | `HIKE`<br>`TRIP`<br>`TOUR`<br>`WALK` | Nature Trail / Hike<br>Trip / Travelogue<br>Guided Tour / Workshop Visit<br>Urban / Lakefront Stroll |
| **Arts & Culture** | `ART`<br>`GIG`<br>`TALK`<br>`FILM`<br>`FOOD`<br>`PIX` | Art Exhibition<br>Live Concert / Music<br>Lecture / Seminar<br>Film / Theater<br>Culinary / Tasting<br>Photo Dispatch |

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

---

## 6. Feedback & Commenting Pipeline Architecture (Zero-JS)

*Under design (see [GitHub Issue #9](https://github.com/jimcollinsworth/jimcollinsworth.github.io/issues/9) for implementation roadmap).*

To preserve the strict **Zero-JS policy** while providing reader interaction without exposing the site or GitHub repository to public issue spam:

```
[Reader Browser] --(HTML Form POST / Zero-JS)--> [Google Apps Script Web App]
                                                             │
                                                             ▼
                                                    [Google Sheet Database]
                                                    (All submissions: spam + legit)
                                                             │
                                            (Pre-Build Extraction & Sync)
                                                             ▼
                                                    [LLM Triage & Digest]
                                                    (Gemini / Pipeline Tools)
                                                             │
                                                             ▼
                                                    [content/comments/*.md]
                                                             │
                                                    [Pelican HTML Compile]
```

### Architecture Specifications:
1. **Zero-JS Form**: Plain semantic HTML5 `<form>` with hidden honeypot, post slug, email, and limited text input at the bottom of posts and contact pages. Submits natively via standard HTTP POST to a Google Apps Script Web App endpoint.
2. **Google Apps Script & Sheet**:
   - `doPost(e)` appends all incoming entries directly to a private Google Sheet.
   - Jim sees **all raw submissions** ("both garbage and good stuff") in one central dashboard.
   - Zero public issue tracker defacement; zero GitHub spam ticket cleanup.
3. **Ingestion & LLM Summarization**:
   - Pre-build script reads entries from the Google Sheet (via CSV export or API).
   - Feeds batches through an LLM triage prompt (evaluates spam, toxicity, prompt injection) and synthesizes community themes into an editorial digest.
   - Saves structured summary to `content/comments/<slug>.md`.
4. **Static Compilation**:
   - Pelican compiles the approved, synthesized feedback directly into semantic HTML at the bottom of the post.

