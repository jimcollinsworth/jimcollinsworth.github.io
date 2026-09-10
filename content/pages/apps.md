---
title: "Apps"
slug: "apps"
---

<div class="page-intro">
  <p>
    <strong>Apps</strong> is the interactive laboratory of <code>jimcollinsworth.github.io</code>. While all essays, reads, and visual critique pages adhere to a strict 100% Zero-JavaScript guarantee for durable reading longevity, these standalone mini-applications use modern browser standards to query local static datasets (from <code>content/data/</code>) and provide rich visual interaction.
  </p>
</div>

<div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  
  <div class="dashboard-card" style="border: 1px solid var(--border-color); border-radius: 6px; padding: 1.5rem; background: var(--card-bg); display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--accent); font-weight: 700;">
        Interactive Application &bull; Visual Media
      </div>
      <h2 style="font-size: 1.4rem; margin: 0.4rem 0 0.75rem;">
        Photo Viewer &amp; Drive Manifest Explorer
      </h2>
      <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;">
        A full-screen, responsive photo viewer designed to parse tabular markdown and JSON manifests from <code>content/data/photos.json</code>. Features filmstrip sidebar navigation, keyboard shortcuts, camera telemetry inspector (Sony A7 IV specs), and direct one-click resolution into original RAW photos hosted in Google Drive.
      </p>
    </div>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="apps/photo-viewer/index.html" class="app-launch-btn" target="_blank" rel="noopener">
        Launch Full-Screen App &rarr;
      </a>
      <a href="data/photos.json" class="app-data-btn" target="_blank" rel="noopener">
        View Data JSON &nearr;
      </a>
    </div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); border-radius: 6px; padding: 1.5rem; background: var(--card-bg); display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--accent); font-weight: 700;">
        Interactive Application &bull; Search &amp; Discovery
      </div>
      <h2 style="font-size: 1.4rem; margin: 0.4rem 0 0.75rem;">
        Content Taxonomy &amp; Keyword Explorer
      </h2>
      <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;">
        A visual discovery widget that cross-filters site content across all dimensions: the 12 core domains, thought evolution stages (<code>idea</code> &rarr; <code>inquiry</code> &rarr; <code>project</code> &rarr; <code>app</code> &rarr; <code>article</code>), authorship origins (<code>original</code>, <code>study</code>, <code>review</code>, <code>curation</code>), and multi-label keyword tags with real-time fuzzy filtering.
      </p>
    </div>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="apps/keyword-search/index.html" class="app-launch-btn" target="_blank" rel="noopener">
        Launch Full-Screen App &rarr;
      </a>
      <a href="data/site-index.json" class="app-data-btn" target="_blank" rel="noopener">
        View Index JSON &nearr;
      </a>
    </div>
  </div>

</div>

---

## Static Data Architecture (`content/data/`)

All mini-apps are backed by centralized static data sources housed in the `content/data/` directory:

| Data Source | Format | Consumer Application | Purpose |
| :--- | :--- | :--- | :--- |
| `content/data/photos.json` | JSON | Photo Viewer | Indexed photo manifest with dates, locations, Google Drive URLs, and camera telemetry. |
| `content/data/photos.md` | Markdown | Static Reader | Tabular markdown version of photo index for human review and Obsidian linking. |
| `content/data/site-index.json` | JSON | Keyword Explorer | Complete multi-facet content index spanning categories, stages, origins, and tags. |
