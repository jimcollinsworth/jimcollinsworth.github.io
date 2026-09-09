---
name: pelican-obsidian-bridge
description: >-
  Configure and maintain the Markdown bridge between an Obsidian vault and the
  Pelican static site generator. Use when handling Obsidian YAML frontmatter,
  wikilinks, image embeds, callouts, and vault folder mappings for Pelican.
---

# Pelican-Obsidian Bridge

This skill guides how to connect an **Obsidian** vault directly with the **Pelican** static site pipeline so Jim can author notes in Obsidian and have them compile cleanly into semantic, zero-JavaScript HTML.

---

## 1. Vault Setup & Folder Mapping

To publish notes seamlessly from Obsidian to Pelican:

### Direct Vault Method (Recommended)
Point Obsidian directly at this repository's `content/` directory:
1. In Obsidian, select **Open folder as vault**.
2. Select `d:\projects\jimcollinsworth.github.io\content`.
3. Configure Obsidian settings for web compatibility:
   - **Files & links → Default location for new attachments**: `In the folder specified below` &rarr; set to `attachments`.
   - **Files & links → New link format**: `Relative path to file`.
   - **Files & links → Use [[Wikilinks]]**: Can be left **ON** if using Pelican's wikilink extension/plugin, or turned **OFF** to write standard Markdown links `[Label](note.md)`.

---

## 2. Handling Obsidian Syntax in Pelican

> [!IMPORTANT]
> **Jim authors 100% pure Markdown in Obsidian.** He never writes raw HTML or HTML file links.
> The arrows (`→`) below represent what the **Pelican compiler automatically converts behind the scenes** when generating the static website.

### A. Frontmatter (YAML Headers)
Obsidian notes typically begin with standard YAML metadata:
```markdown
---
Title: Cordoba Stage Guitar Setup
Date: 2026-09-07
Category: Music
Tags: guitar, nylon-string, gear
Slug: cordoba-stage-guitar
Summary: Action adjustments, string choices, and piezo equalization notes.
---
```
Pelican automatically parses this YAML frontmatter using Python-Markdown's `meta` extension.

### B. Internal Links
In Obsidian, Jim writes Markdown links:
- Standard Markdown: `[Cordoba Guitar](cordoba-stage-guitar.md)`
- Or Obsidian Wikilinks: `[[cordoba-stage-guitar|Cordoba Guitar]]`

**Neither of these mentions `.html`.**
During the build, Pelican's parser automatically resolves the link destination to the published page (`posts/cordoba-stage-guitar.html`).

### C. Media Embeds & Images
In Obsidian, Jim simply drags and drops an image into his note, writing standard Markdown:
- Standard Markdown: `![Cordoba bridge detail](attachments/cordoba-bridge.jpg)`
- Or Obsidian Embed: `![[cordoba-bridge.jpg]]`

**Jim never writes `<figure>` or `<img>` tags.**
The compiler automatically wraps the image in clean, semantic HTML `<figure>` and `<figcaption>` tags on the published site.
When compiling Obsidian notes, transform `![[filename.ext]]` into semantic HTML figures:
```html
<figure>
  <img src="/assets/images/filename.ext" alt="filename" loading="lazy">
  <figcaption>filename.ext</figcaption>
</figure>
```

### D. Callouts (`> [!note]`)
Obsidian callouts:
```markdown
> [!note]
> Acoustic nylon guitars require careful piezo EQ adjustment to avoid harsh attack transients.
```
Configure Python-Markdown with the `admonition` extension in `pelicanconf.py`:
```python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}
```
This renders semantic HTML blockquotes with appropriate CSS classes that match `assets/css/style.css`.

---

## 3. Author-to-Publish Workflow

1. **Authoring (Jim in Obsidian)**:
   - Jim creates or edits notes in `content/posts/`.
   - Adds title, date, category (one of the 12 Lanes), and summary in the frontmatter.
   - Attaches any images into `content/attachments/`.

2. **Compilation**:
   - Run standard Pelican command:
     ```bash
     pelican content -s pelicanconf.py
     ```

3. **Preview & Audit**:
   - Preview locally: `pelican --listen` at `http://localhost:8000`.
   - Verify link integrity and confirm zero `<script>` tags were introduced.

4. **Publish**:
   - Git commit locally:
     ```bash
     git add content/ output/
     git commit -m "Publish new post from Obsidian"
     ```
   - **Push to Remote**: Per Agent Rule 9, **never push without Jim's explicit request or confirmation**:
     ```bash
     git push origin main
     ```

---

## 4. Official Authoring Baseline Reference

For complete metadata schema specifications, intra-site linking syntax (`{filename}`, `{static}`, `{category}`), and Pygments syntax highlighting conventions, consult:
- [`docs/content_authoring.md`](file:///d:/projects/jimcollinsworth.github.io/docs/content_authoring.md)
- [`references/pelican_content_spec.md`](file:///d:/projects/jimcollinsworth.github.io/.agents/skills/pelican-site-manager/references/pelican_content_spec.md)

