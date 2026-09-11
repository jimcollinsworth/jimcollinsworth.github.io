---
Title: DevOps
Slug: devops
---

<header class="post-header" style="margin-bottom: 1.5rem;">
  <h1 class="post-title" style="font-size: 2rem; margin-bottom: 0.5rem;">DevOps Workbench</h1>
  <p class="post-meta" style="color: var(--text-muted); font-size: 0.95rem;">
    Local developer operations, multimodal pipeline tools, and background services.
  </p>
</header>

<div class="page-intro">
  <p>
    An interactive multimodal workbench and ETL engine powered by <strong>Pixeltable</strong> and <strong>Gradio</strong>. Ingest local directories, scan media assets, test sample-first prompts with local Ollama or Google Gemini, and export enriched metadata and Markdown sidecars.
  </p>
  <p style="margin-top: 0.5rem; display: flex; gap: 0.75rem; flex-wrap: wrap;">
    <a href="https://huggingface.co/spaces/jimcollinsworth/pipeline-tools" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.35rem 0.75rem; border-radius: 6px; background: var(--bg-card); border: 1px solid var(--border); font-size: 0.85rem; text-decoration: none; color: var(--text);">
      <span>🤗</span> <strong>Hugging Face Space</strong>
    </a>
    <a href="https://github.com/jimcollinsworth/pipeline-tools" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.35rem 0.75rem; border-radius: 6px; background: var(--bg-card); border: 1px solid var(--border); font-size: 0.85rem; text-decoration: none; color: var(--text);">
      <span>🐙</span> <strong>GitHub Repository</strong>
    </a>
    <a href="http://127.0.0.1:7860" target="_blank" rel="noopener" style="display: inline-flex; align-items: center; gap: 0.35rem; padding: 0.35rem 0.75rem; border-radius: 6px; background: var(--bg-card); border: 1px solid var(--border); font-size: 0.85rem; text-decoration: none; color: var(--text);">
      <span>💻</span> <strong>Local Dev (127.0.0.1:7860)</strong>
    </a>
  </p>
</div>

<div class="app-container" style="margin: 2rem 0;">
  <!-- Status Bar -->
  <div class="app-status-bar" style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 1rem; background: var(--bg-card); border: 1px solid var(--border); border-bottom: none; border-radius: 8px 8px 0 0; font-family: var(--font-sans); font-size: 0.85rem; color: var(--text-muted); flex-wrap: wrap; gap: 0.5rem;">
    <span><strong>Live Cloud App:</strong> <a href="https://huggingface.co/spaces/jimcollinsworth/pipeline-tools" target="_blank" rel="noopener" style="color: var(--text); text-decoration: underline;">jimcollinsworth/pipeline-tools</a></span>
    <div style="display: flex; align-items: center; gap: 1rem;">
      <span><strong>Engine:</strong> Pixeltable + Gradio</span>
      <a href="https://jimcollinsworth-pipeline-tools.hf.space" target="_blank" rel="noopener" style="color: #2563eb; font-weight: 500; text-decoration: none;">
        ↗ Open Fullscreen
      </a>
    </div>
  </div>

  <!-- Embedded Application Frame -->
  <iframe 
    id="devops-workbench-frame"
    src="https://jimcollinsworth-pipeline-tools.hf.space" 
    width="100%" 
    height="950" 
    style="width: 100%; height: 950px; border: 1px solid var(--border); border-radius: 0 0 8px 8px; background: var(--bg-card); display: block;"
    allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking; clipboard-write"
    sandbox="allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads"
    title="DevOps &amp; Pipeline Tools Workbench">
  </iframe>

  <!-- Usage & Fallback Notes -->
  <div class="app-fallback-card" style="margin-top: 1.5rem; padding: 1.25rem 1.5rem; background: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: 8px; font-family: var(--font-sans); font-size: 0.9rem; line-height: 1.6;">
    <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.05rem; color: var(--text);">Cloud vs. Local Execution</h3>
    <p style="margin-bottom: 0.75rem;">
      <strong>☁️ Cloud Space:</strong> Hosted live on Hugging Face Spaces. In cloud mode, multimodal prompts and evaluations use Google Gemini via Space secrets.<br>
      <strong>💻 Local Workbench:</strong> Connects to your local machine at <a href="http://127.0.0.1:7860" target="_blank" rel="noopener">http://127.0.0.1:7860</a> with full access to local disk folders, raw media files, and local Ollama models.
    </p>
    <p style="margin-bottom: 0.5rem; font-size: 0.85rem; color: var(--text-muted);">
      To run the local workbench in PowerShell:
    </p>
    <pre style="background: var(--code-bg); padding: 0.75rem 1rem; border-radius: 6px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.85rem; color: var(--text); margin-bottom: 0.75rem;"><code>cd d:\projects\pipeline-tools
uv run gradio app.py</code></pre>
  </div>
</div>
