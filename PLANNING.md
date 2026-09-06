# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

- [x] **Milestone 1: Clean Foundation (Completed)**
  - Safely archived legacy Nikola compiler assets, drafts, notes, and high-resolution photo galleries into `archive/`.
  - Established `.agents/agent_rules.md` with the mandatory 3-document rule and strict content ownership policy (agent never drafts content).
  - Implemented zero-JavaScript, pure HTML5 + modern CSS design system inspired by Bear Blog and Mark Boulton.
  - Established core 3 documents: `README.md`, `PLANNING.md`, `JOURNAL.md`.
  - Built core structural pages: `index.html`, `about.html`, `lanes.html`, `journal.html`, and `gallery.html`.
  - Automated verification: 0 scripts detected, all internal links and images resolved.
  - Configured zero-build GitHub Pages deployment workflow (`.github/workflows/pages.yml`).

---

## Content Notes in Archive (For Jim's Writing)

The following subject areas have research notes and ideas safely stored in `archive/content/ideas_and_drafts.md` for when Jim chooses to write:
- **M.E. (Mental Entity / My Essence)**: Personal offline AI companion concept.
- **Sleep Movement Evaluation**: Standardized rating scales (RLSRS, PSQI, ESS, GAD-7) and lifestyle factors.
- **Instrument Studies**: Kawai ES-8 piano modifications and Cordoba Stage nylon guitar notes.
- **Craft**: Handcrafting custom Ulu knife handles.
- **Bookmarks Analysis**: Parsing browser bookmarks into a structured internet directory.

---

## Technical & Design Backlog

- [ ] **Pure CSS Tag Filtering**: Explore CSS `:target` or radio-state filtering for journal entries without JavaScript.
- [ ] **Pure CSS Image Modal**: Lightweight lightbox using CSS `:target` for high-res photo inspection.
- [ ] **Print Stylesheet**: Add `@media print` rules for clean hard-copy printing.
- [ ] **Additional Photo Showcases**: Prepare web-optimized selections from `archive/original_photos/` (Lakefront Twilight and Macro Garden series).
