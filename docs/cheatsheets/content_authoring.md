# Content Authoring & Layout Relationship — Cheat Sheet

> Authoring reference for Pelican YAML metadata, thought evolution lifecycles, authorship boundaries, and semantic layout styling.
> Printable PDF: [`content_authoring.pdf`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/content_authoring.pdf)

---

## 1. Thought Evolution Lifecycle

```mermaid
stateDiagram-v2
  [*] --> Idea: Raw Prompt / Hypothesis
  [*] --> TIL: Quick Technical Discovery
  [*] --> Rant: Direct Commentary

  Idea --> Inquiry: Research & Deep Exploration
  TIL --> Inquiry: Expanding Insight
  Rant --> Inquiry: Structured Analysis

  Inquiry --> Project: Multi-step Build / Fabrication
  Inquiry --> App: Software Tool / Visualizer
  Inquiry --> Article: Long-form Synthesis

  Project --> Article: Mature Case Study
  App --> Article: Architecture & Rationale

  Project --> Inquiry: New Questions / Redesign
  Article --> Inquiry: Follow-up Exploration
```

*Posts are living thoughts that mature across stages over time using the `evolution:` audit log.*

---

## 2. Authorship & Origin Boundary

```mermaid
flowchart TD
  ITEM["Content Item (Post, Read, Photo, Exhibit)"]
  ORIG{"Is this Jim's Original Work?"}
  
  ITEM --> ORIG
  ORIG -->|YES| JIM["origin: original<br/>(Personal Woodworking, Photos, Software, Theory)"]
  ORIG -->|NO| EXT["External Reference"]

  EXT --> STUD["origin: study<br/>(Replicating a piece, exercise, practicing a score)"]
  EXT --> REV["origin: review<br/>(Critique of exhibit, book, film, software)"]
  EXT --> CUR["origin: curation<br/>(Reading note, bookmark, quote with short reflection)"]
```

---

## 3. Standard Pelican YAML Frontmatter Template

```yaml
---
title: "Cordoba Stage Classical Guitar Setup"
slug: "cordoba-stage-guitar"
date: 2026-03-24
modified: 2026-09-09

# 1. Primary Classification (The 12 Core Domains)
category: Music          # Music, Software, Health, Making, Art, Law,
                         # Politics, Data, Exercise, Anatomy, Engineering

# 2. Multi-Label Topics & Keywords
tags: [guitar, classical, pickups, acoustic-resonance]

# 3. Publishing Control & Summary Teaser
status: published        # published | draft | hidden
summary: "Evaluation and setup adjustments for nylon string tone."

# 4. Thought Evolution & Authorship
origin: original         # original | study | review | curation
stage: project           # idea | til | rant | inquiry | project | app | article
evolution: "2026-03-24:idea > 2026-06-10:inquiry > 2026-09-09:project"

# 5. Interactive Media & Apps (Optional)
app_url: ""              # e.g. /apps/circle-of-fifths/
gallery_url: ""          # e.g. Google Photos album URL
---
```

---

## 4. Markdown Syntax to Semantic CSS Component Mapping

| Component | Markdown / HTML Syntax | CSS Selector | Visual & Styling Behavior |
| :--- | :--- | :--- | :--- |
| **Site Header** | Template-driven | `.site-header`, `.site-nav` | Clean branding, active page highlight, and zero-JS accessibility controls. |
| **Lead Summary** | `<div class="page-intro">...</div>` | `.page-intro` | Slightly larger type (`1.15rem`) with generous margins for article ledes. |
| **Headings (H2-H4)** | `## Section`, `### Sub` | `h2`, `h3`, `h4` | Proportional margins, distinct serif/sans hierarchy, and clear section breaks. |
| **Body Prose** | Standard markdown paragraphs | `p`, `main p` | Readable measure capped at `max-width: 76ch` with `1.65` line-height. |
| **Quotes & Callouts** | `> Quote / mental model` | `blockquote` | Rust accent left border (`3px solid var(--accent)`), italicized, indented. |
| **Photo Figures** | `![Caption](images/photo.jpg)` | `figure`, `figcaption` | Bordered photo card with centered italicized caption below. |
| **Data Tables** | Pipe table: `\| Col 1 \| Col 2 \|` | `table`, `th`, `td` | Clean bordered table with shaded header row and horizontal row dividers. |
| **Code Snippets** | ` ```python ... ``` ` | `pre`, `code`, `.highlight` | Monospace block with card shading, dark mode support, and code syntax styles. |
| **Dashboard Grid** | `<div class="dashboard-grid">` | `.dashboard-grid` | Multi-column CSS Grid card layout for metrics, stats, and telemetry. |

---

## 5. Responsive Layout & Orientation Modes

```mermaid
flowchart TD
  DEV["Client Display Viewport"]
  DEV --> OR{"Orientation and Width"}

  OR -->|Portrait / Under 960px| PORT["Single-Column Reading Flow<br/>- Focused vertical prose stream<br/>- Maximum reading comfort"]
  OR -->|Landscape / 960px and Up| LAND["2-Column Magazine Grid (.desktop-two-col)<br/>- Left: Featured Article + Reads<br/>- Right: Recent Stream + Spotlight"]

  DEV --> DENS{"Viewport Width"}
  DENS -->|Desktop / 640px and Up| DET["Progressive Detail (.post-detail)<br/>- Full excerpts and complete metadata"]
  DENS -->|Mobile / Under 640px| TEAS["Progressive Teaser (.post-teaser)<br/>- Concise 1-line scannable feeds"]
```
