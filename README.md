# jimcollinsworth.github.io

> Personal website, journal, and exploration lanes of **Jim Collinsworth** — *Out of My Lane*.

---

## Overview & Philosophy

This site is an intentionally simple, durable personal web space. It has been built with an uncompromising commitment to long-term digital sustainability, reading comfort, and zero maintenance overhead:

- **99.9% Pure Semantic HTML5**: No dynamic web compilers, static site generators, complex build toolchains, or node/npm pipelines.
- **Zero Client-Side JavaScript**: Fast, private, and durable. Navigation and structure rely solely on native web standards and semantic markup.
- **Modern Responsive CSS**: Clean typography, fluid layouts, and automatic dark/light theme switching via `@media (prefers-color-scheme: dark)`.
- **Content-Out Editorial Design**: Inspired by [Pine Wind (Bear Blog)](https://pinewind.bearblog.dev/) and [Mark Boulton](https://markboulton.co.uk/journal/anewcanon/).
- **Maintained by an LLM-Based Coding Agent**: Kept lightweight, disciplined, and consistent over time with strict agent governance.

---

## The Concept: "Out of My Lane"

After a 50-year career spanning Arthur Andersen, professional guitar playing, software startups, and data science, retirement is an invitation to explore without professional boundaries. *"How does that work?"* is the core question guiding this site across various interest lanes:

- **Music**: Classical and fingerstyle guitar, piano studies (Kawai ES-8), music theory.
- **STEM & Computing**: Local offline AI (M.E.), Python tools, data analysis, weather observation, electronics.
- **Health & Somatics**: Tai Chi, Alexander Technique, sleep health & periodic limb movement analysis.
- **Craft & Physical Making**: Woodworking, Ulu knife crafting, instrument maintenance.
- **Photography**: Chicago skies, lakefront weather, sunsets, and botanical studies.

---

## Repository Structure

```
jimcollinsworth.github.io/
├── .agents/
│   └── agent_rules.md            # LLM agent governance, 3-doc rule & content boundary
├── .github/
│   └── workflows/
│       └── deploy.yml            # Automated audit (Zero-JS & link check) + GitHub Pages deployment
├── archive/
│   ├── content/                  # Extracted legacy notes, drafts, and taxonomy
│   ├── original_photos/          # Full-resolution photographic archives
│   └── legacy_split_screen_experiment.html
├── assets/
│   ├── css/
│   │   └── style.css             # Unified modern stylesheet (light/dark mode)
│   └── images/                   # Curated web-optimized imagery
├── index.html                    # Homepage (tagline, intro, active lanes, recent posts)
├── about.html                    # Biography, career background, and personal ethos
├── lanes.html                    # Overview of active areas of interest and projects
├── journal.html                  # Chronological journal index
├── gallery.html                  # Photographic study & sky series showcase
├── favicon.ico                   # Browser favicon
├── googledaf3f946832f8abf.html   # Google Search Console verification token
├── README.md                     # Core document 1: Site overview & guide
├── PLANNING.md                   # Core document 2: Active roadmap & backlog
└── JOURNAL.md                    # Core document 3: Chronological changelog
```

---

## Agent Governance: The 3-Document & Content Rules

Per `.agents/agent_rules.md`:
1. **Mandatory 3-Document Rule**: The agent may maintain **only three** root system design documents:
   - `README.md` (System overview, architecture, and instructions)
   - `PLANNING.md` (Active roadmap and technical backlog)
   - `JOURNAL.md` (Chronological decision log and change records)
   *Walkthroughs or additional meta documents are strictly unauthorized without prior proposal and approval.*
2. **Content Ownership**: The agent must **never draft content documents, create content files, or write articles** for Jim. All content authoring belongs exclusively to Jim.

---

## Quality & Verification Standards

All pages are verified via automated GitHub Actions auditing on every push (`.github/workflows/deploy.yml`):
- **Zero-JS Enforcement**: Fails the build if any unauthorized `<script>` tag is detected in content files.
- **Link & Asset Integrity**: Fails the build if any internal `href` link or image `src` fails to resolve.
- **Accessibility & Contrast**: Legible typography (Charter/Sitka Text serif body, system sans headers), compliant contrast ratios in both light and dark modes.

---

## Publishing & Deployment

Deploying is as simple as pushing standard static files to GitHub:
1. The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs the audit suite on every push to `main`.
2. Upon passing, it deploys the raw static assets directly to GitHub Pages with zero dynamic compilation.
3. Custom domain mapping is maintained via GitHub Pages DNS.

---

## License

Content and essays © Jim Collinsworth, licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
