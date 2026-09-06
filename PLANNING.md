# Site Planning & Roadmap: jimcollinsworth.github.io

> Active development roadmap and technical backlog for Jim Collinsworth's personal site. Maintained under the 3-document agent rule.

---

## Active Status & Milestones

- [x] **Milestone 1: Clean Foundation (Completed)**
  - Safely archived legacy Nikola compiler assets, drafts, notes, and photo galleries into `archive/`.
  - Established `.agents/agent_rules.md` with the mandatory 3-document rule and strict content boundary (agent never drafts content).
  - Implemented zero-JavaScript, pure HTML5 + modern CSS design system.
  - Reverted all page content strictly to original archive text with zero additions.
  - Configured the 12 lanes: Music making, Software, Life sciences, Engineering, Photography, Making, Law, Art, Politics, Data, Exercise, Anatomy.
  - Added dummy `Lorem ipsum` journal entries to preview layout.
  - Verified 0 scripts, all links and images valid.
  - Integrated `.github/workflows/deploy.yml` with automated Zero-JS audit and direct Pages deployment.

---

## The 12 Lanes

1. Music making
2. Software
3. Life sciences
4. Engineering
5. Photography
6. Making
7. Law
8. Art
9. Politics
10. Data
11. Exercise
12. Anatomy

---

## Content Notes in Archive (For Jim's Writing)

Research notes and raw materials are preserved in `archive/content/` for Jim's reference when authoring posts.

---

## Technical & Design Backlog

- [ ] **Pure CSS Tag Filtering**: Explore CSS `:target` or radio-state filtering for journal entries without JavaScript.
- [ ] **Pure CSS Image Modal**: Lightweight lightbox using CSS `:target` for high-res photo inspection.
- [ ] **Print Stylesheet**: Add `@media print` rules for clean hard-copy printing.
