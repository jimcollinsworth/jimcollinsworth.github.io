---
title: "Pipeline Tools"
slug: "pipeline-tools"
---

<div class="page-intro">
  <p>
    An interactive multimodal workbench and ETL engine powered by <strong>Pixeltable</strong> and <strong>Gradio</strong>. Ingest local directories, scan media assets, test sample-first prompts with local Ollama or Google Gemini, and export enriched metadata and Markdown sidecars.
  </p>
</div>

<div class="app-container" style="margin: 2rem 0;">
  <div class="app-status-bar" style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 1rem; background: var(--bg-card); border: 1px solid var(--border); border-bottom: none; border-radius: 8px 8px 0 0; font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted);">
    <span><strong>Target:</strong> Local Workbench (<code>http://127.0.0.1:7860</code>)</span>
    <span><strong>Engine:</strong> Pixeltable + Gradio</span>
  </div>

  <iframe 
    id="pipeline-tools-frame"
    src="http://127.0.0.1:7860" 
    width="100%" 
    height="950" 
    style="width: 100%; height: 950px; border: 1px solid var(--border); border-radius: 0 0 8px 8px; background: var(--bg-card); display: block;"
    title="Pipeline Tools Multimodal Workbench">
  </iframe>

  <div class="app-fallback-card" style="margin-top: 1.5rem; padding: 1.25rem 1.5rem; background: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: 8px; font-family: var(--font-sans); font-size: 0.9rem; line-height: 1.6;">
    <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.05rem; color: var(--text);">Workbench Status &amp; Launch Instructions</h3>
    <p style="margin-bottom: 0.75rem;">
      If the workbench above appears blank or unavailable, start the local Python server in PowerShell:
    </p>
    <pre style="background: var(--code-bg); padding: 0.75rem 1rem; border-radius: 6px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.85rem; color: var(--text); margin-bottom: 0.75rem;"><code>cd d:\projects\pipeline-tools
uv run gradio app.py</code></pre>
    <p style="margin-bottom: 0; color: var(--text-muted); font-size: 0.85rem;">
      Once started, refresh this page or open <a href="http://127.0.0.1:7860" target="_blank" rel="noopener">http://127.0.0.1:7860</a> directly in a new tab.
    </p>
  </div>
</div>
