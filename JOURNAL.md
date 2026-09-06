# Site Journal & Decision Log: jimcollinsworth.github.io

> Chronological log of architectural decisions, site milestones, and design changes. Maintained under the 3-document agent rule.

---

## 2026-09-06 — Content Reversion to Archive & 12 Lanes Setup

### Decisions & Actions Taken
1. **Reverted All Content to Archive Text**:
   - Replaced all prose on `about.html` and `index.html` strictly with Jim's original text from `pages/about.md` and `README.md`. Removed all AI-generated commentary.
   - Simplified `gallery.html` to minimalist titles and direct link to the Google Photos album.
2. **Configured 12 Requested Lanes**:
   - Updated `lanes.html` and `index.html` with the 12 explicit lanes: *Music making, Software, Life sciences, Engineering, Photography, Making, Law, Art, Politics, Data, Exercise, Anatomy*.
3. **Dummy Entries for Layout Preview**:
   - Inserted placeholder `Lorem ipsum` entries on `journal.html` and `index.html` solely to preview page layout without authoring posts.
4. **CI Workflow Streamlining**:
   - Refined `.github/workflows/deploy.yml` with a lightweight Zero-JS audit step and GitHub's official Pages deployment action.

---

## 2026-09-06 — Architectural Transformation: Pure HTML/CSS & Agent Governance

### Context & Problem
The site previously relied on Nikola, a Python-based static site generator with configuration files (`conf.py`), theme directories (`themes/hyde`), virtual environments (`pyproject.toml`, `uv.lock`), and compiler build workflows (`nikola.yml`). This introduced unnecessary build friction, compilation fragility, and opaque templating layers for what should be an authentic, durable personal website.

### Decisions & Actions Taken

1. **Complete Decommissioning of Compiler Toolchain**:
   - Removed `conf.py`, `themes/`, `plugins/`, `pyproject.toml`, `uv.lock`, and legacy build workflows.
   - Preserved all historical notes, draft essays, category definitions, and SEO verification tokens safely in `archive/content/`.
   - Relocated original full-resolution photo collections into `archive/original_photos/`.

2. **Mandatory 3-Document Rule & Content Boundaries**:
   - Created `.agents/agent_rules.md`.
   - Strict governance: the agent may maintain **only three** root system design documents (`README.md`, `PLANNING.md`, `JOURNAL.md`). Any walkthroughs or additional meta documents are unauthorized.
   - Strict content policy: the agent must **never** draft content documents, create content files, or write articles for Jim. All content authoring belongs 100% to Jim.

3. **Pure Semantic HTML5 & Modern CSS Architecture**:
   - Committed to 99.9% pure HTML5 and **zero client-side JavaScript**.
   - Crafted `assets/css/style.css` focusing on editorial typography (Charter / Sitka Text / Georgia serif body, clean sans headers and navigation, monospace code/data), comfortable line length (~70ch), fluid responsive grid, and native `@media (prefers-color-scheme: dark)` styling.
   - Design restraint inspired by Bear Blog (`pinewind.bearblog.dev`) and Mark Boulton (`markboulton.co.uk/journal/anewcanon/`).

4. **Core Structural Pages Created**:
   - `index.html`: Central home featuring tagline ("Out of My Lane"), bio overview, active lanes grid, and lakefront photography.
   - `about.html`: Personal profile covering Jim's 50-year career (Arthur Andersen, guitarist, tech startups, data science) and retirement philosophy.
   - `lanes.html`: Structured index of active pursuit lanes.
   - `journal.html`: Chronological journal index container with sample entries.
   - `gallery.html`: Photographic showcase with Chicago sky and botanical studies.
   - `.github/workflows/deploy.yml`: Automated Zero-JS audit, link integrity test, and direct GitHub Pages deployment.

5. **Automated Verification & CI Guardrails**:
   - Integrated `.github/workflows/deploy.yml` to run automated quality audits on every push before publishing.
   - Verified that all HTML files contain 0 `<script>` tags.
   - Verified that all internal page and image links resolve cleanly to existing local files.
   - Validated standard `<!DOCTYPE html>` structure and closed tags.
