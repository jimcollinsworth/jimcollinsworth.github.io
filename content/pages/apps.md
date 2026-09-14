---
title: "Apps"
slug: "apps"
template: "apps"
---

**Apps** contains standalone mini-applications on jimcollinsworth.github.io. While essays, notes, and reading pages contain zero client-side JavaScript, these standalone applications run client-side JavaScript to query static datasets in content/data/.

---

## Static Data & Deployment Architecture

All mini-apps are backed by centralized static data sources housed in content/data/ or external cloud services:

| Data Source / Deployment | Format / Host | Consumer Application | Purpose |
| :--- | :--- | :--- | :--- |
| jimcollinsworth/pipeline-tools | Hugging Face Spaces | Pipeline Tools | Interactive data pipeline, quality inspection, and enhancement workbench. |
| content/data/photos.json | JSON | Photo Viewer | Indexed photo manifest with dates, locations, Google Drive URLs, and camera telemetry. |
| content/data/photos.md | Markdown | Static Reader | Tabular markdown version of photo index for human review and Obsidian linking. |
| content/data/site-index.json | JSON | Keyword Explorer | Multi-facet content index spanning categories, stages, origins, and tags. |
