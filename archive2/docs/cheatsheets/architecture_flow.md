# Site Architecture & Publishing Flow — Cheat Sheet

> Quick reference guide for static site compilation, data flows, pair programming governance, and CI/CD operations.
> Printable PDF: [`architecture_flow.pdf`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/docs/cheatsheets/architecture_flow.pdf)

---

## 1. End-to-End Publishing Pipeline

```mermaid
flowchart LR
  subgraph Authoring ["1. Human Authoring"]
    OV["Obsidian Vault<br/>(Markdown Notes)"]
    CP["content/posts/<br/>content/pages/"]
    IM["content/images/<br/>(Jim's Curated Photos)"]
    OV -->|Direct Save / Drop| CP
    OV -->|Manual Selection| IM
  end

  subgraph Compilation ["2. Pelican Static Generator"]
    CONF["pelicanconf.py<br/>(Obsidian Reader)"]
    TH["theme/templates/<br/>(Jinja2 Semantic HTML)"]
    OUT["output/<br/>(Pure HTML5 + CSS)"]
    CP --> CONF
    IM --> CONF
    TH --> CONF
    CONF -->|Compile Under 0.2s| OUT
  end

  subgraph Testing ["3. Automated Quality Gate"]
    PY["uv run pytest -v<br/>(30 Automated Tests)"]
    A11Y["Accessibility<br/>(WCAG AAA / ARIA)"]
    PW["Playwright Headless<br/>(8 Viewports / Light+Dark)"]
    OUT --> PY
    PY --> A11Y
    PY --> PW
  end

  subgraph Deployment ["4. GitHub Pages CDN"]
    GA["GitHub Actions<br/>(.github/workflows/deploy.yml)"]
    GP["GitHub Pages CDN<br/>(100% Zero-JS HTTPS)"]
    PY -->|git push origin main| GA
    GA -->|Deploy output/| GP
  end
```

---

## 2. Interactive Apps & Static Data Architecture

```mermaid
flowchart TD
  DATA["content/data/<br/>(JSON, CSV, SQLite Datasets)"]
  APP["content/apps/name/<br/>(Standalone App Code: Python/WASM/JS/Ruby)"]
  POST["content/posts/name.md<br/>(stage: app, app_url: /apps/name/)"]
  PAGE["HTML Output<br/>(Embedded iframe or Full Page Link)"]

  DATA -->|Fetch / Query Local Static Data| APP
  APP -->|Linked / Embedded in| POST
  POST -->|Compiled via Pelican| PAGE
```

*Every interactive app is paired with a companion post (`stage: app`) documenting its architecture, rationale, and evolution.*

---

## 3. Antigravity AI Pair Programming Governance

```mermaid
sequenceDiagram
  autonumber
  actor Jim as Jim (Author & Architect)
  participant Obsidian as Obsidian Vault
  participant Agent as Antigravity AI Agent
  participant Tests as Pytest / Playwright
  participant GitHub as GitHub (Repo & Pages)

  Jim->>Obsidian: Authors posts, notes, book reflections, and selects photos
  Note over Jim,Obsidian: 100% Human Content Ownership (Agent Never Writes Content)
  Jim->>Agent: Requests layout, styling, tool, or build modification
  Agent->>Agent: Implements Jinja2 templates, CSS grids, or CLI tools
  Agent->>Tests: Executes automated test suite (Zero-JS + Viewport verification)
  Tests-->>Agent: 30/30 Tests Pass
  Agent->>Agent: Updates 4 Governance Docs (JOURNAL, PLANNING, ROADMAP, README)
  Agent->>Jim: Presents changes, test output & requests push confirmation
  Jim->>Agent: Confirms push
  Agent->>GitHub: git push origin main & creates Git release tags
  GitHub-->>Jim: Deploys live to GitHub Pages CDN via Actions
```

---

## 4. Core Governance Documents Matrix

| Document | Role & Primary Purpose | Update Trigger |
| :--- | :--- | :--- |
| **[`README.md`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/README.md)** | Architecture overview, CLI guide & component lexicon. | New tools, syntax, or commands. |
| **[`PLANNING.md`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/PLANNING.md)** | Active sprint tasks, near-term milestones & statuses. | Every milestone completion. |
| **[`ROADMAP.md`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/ROADMAP.md)** | Long-term creative sandbox, wishlists & concept specs. | New exploratory concepts. |
| **[`JOURNAL.md`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/JOURNAL.md)** | Chronological technical decision log & troubleshooting. | Every commit / session. |

---

## 5. Essential CLI Commands

```bash
# 1. Dependency Sync
uv sync

# 2. Build Pelican Static Site
uv run pelican content -s pelicanconf.py -o output -d

# 3. Local Development Preview Server
uv run pelican --listen -p 8000

# 4. Run Full Test Suite (Accessibility + E2E + Playwright)
uv run pytest -v

# 5. Generate Multi-Resolution Screenshots (8 Viewports)
uv run python tools/screenshots.py --page index.html

# 6. Generate PDF Cheat Sheets
uv run python tools/generate_cheatsheet_pdfs.py
```
