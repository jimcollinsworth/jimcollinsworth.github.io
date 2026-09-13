---
title: "Apps"
slug: "apps"
---

<div class="page-intro">
  <p>
    <strong>Apps</strong> contains standalone mini-applications on <code>jimcollinsworth.github.io</code>. While essays, notes, and reading pages contain zero client-side JavaScript, these standalone applications run client-side JavaScript to query static datasets in <code>content/data/</code>.
  </p>
</div>

<div class="dashboard-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
  
  <div class="dashboard-card" style="border: 1px solid var(--border-color); border-radius: 6px; padding: 1.5rem; background: var(--card-bg); display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="display: flex; align-items: baseline; gap: 0.45rem; margin-bottom: 0.75rem;">
        <span class="category-badge dual-badge" title="Provenance: AI Codebase &bull; Jim Collinsworth Stewardship" aria-label="Category: AI and Mine"><svg class="category-icon icon-ai" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg><svg class="category-icon icon-mine" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="margin-left: 2px;"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span>
        <h3 style="font-size: 1.05rem; font-weight: 600; font-family: var(--font-sans); margin: 0; line-height: 1.35;">
          Photo Viewer &amp; Drive Manifest Explorer
        </h3>
      </div>
      <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;">
        A full-screen, responsive photo viewer designed to parse tabular markdown and JSON manifests from <code>content/data/photos.json</code>. Features filmstrip sidebar navigation, keyboard shortcuts, camera telemetry inspector (Sony A7 IV specs), and direct one-click resolution into original RAW photos hosted in Google Drive.
      </p>
    </div>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="apps/photo-viewer/index.html" class="app-launch-btn" target="_blank" rel="noopener">
        Launch Full-Screen App &rarr;
      </a>
      <a href="posts/photo-viewer-drive-manifest-explorer.html" class="app-data-btn">
        Read App Post &rarr;
      </a>
      <a href="data/photos.json" class="app-data-btn" target="_blank" rel="noopener">
        View Data JSON &nearr;
      </a>
    </div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); border-radius: 6px; padding: 1.5rem; background: var(--card-bg); display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="display: flex; align-items: baseline; gap: 0.45rem; margin-bottom: 0.75rem;">
        <span class="category-badge dual-badge" title="Provenance: AI Codebase &bull; Jim Collinsworth Stewardship" aria-label="Category: AI and Mine"><svg class="category-icon icon-ai" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg><svg class="category-icon icon-mine" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="margin-left: 2px;"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span>
        <h3 style="font-size: 1.05rem; font-weight: 600; font-family: var(--font-sans); margin: 0; line-height: 1.35;">
          Content Taxonomy &amp; Keyword Explorer
        </h3>
      </div>
      <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;">
        A visual discovery widget that cross-filters site content across all dimensions: the 12 core domains, thought evolution stages (<code>idea</code> &rarr; <code>inquiry</code> &rarr; <code>project</code> &rarr; <code>app</code> &rarr; <code>article</code>), authorship origins (<code>original</code>, <code>study</code>, <code>review</code>, <code>curation</code>), and multi-label keyword tags with real-time fuzzy filtering.
      </p>
    </div>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="apps/keyword-search/index.html" class="app-launch-btn" target="_blank" rel="noopener">
        Launch Full-Screen App &rarr;
      </a>
      <a href="posts/keyword-explorer-taxonomy.html" class="app-data-btn">
        Read App Post &rarr;
      </a>
      <a href="data/site-index.json" class="app-data-btn" target="_blank" rel="noopener">
        View Index JSON &nearr;
      </a>
    </div>
  </div>

  <div class="dashboard-card" style="border: 1px solid var(--border-color); border-radius: 6px; padding: 1.5rem; background: var(--card-bg); display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="display: flex; align-items: baseline; gap: 0.45rem; margin-bottom: 0.75rem;">
        <span class="category-badge dual-badge" title="Provenance: AI Codebase &bull; Jim Collinsworth Stewardship" aria-label="Category: AI and Mine"><svg class="category-icon icon-ai" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg><svg class="category-icon icon-mine" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="margin-left: 2px;"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span>
        <h3 style="font-size: 1.05rem; font-weight: 600; font-family: var(--font-sans); margin: 0; line-height: 1.35;">
          Pipeline Tools (Hugging Face)
        </h3>
      </div>
      <p style="font-size: 0.92rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;">
        A web-based data pipeline and transformation workbench deployed to Hugging Face Spaces. Ingests data files, executes validation and enhancement models, inspects contextual schemas, and exports structured datasets.
      </p>
    </div>
    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--border-color);">
      <a href="apps/pipeline-tools/index.html" class="app-launch-btn" target="_blank" rel="noopener">
        Launch Full-Screen App &rarr;
      </a>
      <a href="posts/pipeline-tools-workbench.html" class="app-data-btn">
        Read App Post &rarr;
      </a>
      <a href="pipeline-tools.html" class="app-data-btn">
        Embedded View &rarr;
      </a>
      <a href="https://huggingface.co/spaces/jimcollinsworth/pipeline-tools" class="app-data-btn" target="_blank" rel="noopener">
        Hugging Face Space &nearr;
      </a>
      <a href="https://github.com/jimcollinsworth/pipeline-tools" class="app-data-btn" target="_blank" rel="noopener">
        GitHub Source &nearr;
      </a>
    </div>
  </div>

</div>

---

## Static Data & Deployment Architecture

All mini-apps are backed by centralized static data sources housed in `content/data/` or external cloud services:

| Data Source / Deployment | Format / Host | Consumer Application | Purpose |
| :--- | :--- | :--- | :--- |
| `jimcollinsworth/pipeline-tools` | Hugging Face Spaces | Pipeline Tools | Interactive data pipeline, quality inspection, and enhancement workbench. |
| `content/data/photos.json` | JSON | Photo Viewer | Indexed photo manifest with dates, locations, Google Drive URLs, and camera telemetry. |
| `content/data/photos.md` | Markdown | Static Reader | Tabular markdown version of photo index for human review and Obsidian linking. |
| `content/data/site-index.json` | JSON | Keyword Explorer | Multi-facet content index spanning categories, stages, origins, and tags. |
