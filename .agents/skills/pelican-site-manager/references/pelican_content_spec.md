# Pelican Technical Content Specification & Reader Architecture

Reference documentation for Pelican static site generation, metadata extraction, link directive resolution, and reader behavior.

---

## 1. Content Generation Lifecycle

```text
content/
  ├── posts/*.md       -->  Article Generator  -->  theme/templates/article.html  -->  output/posts/{slug}.html
  ├── pages/*.md       -->  Page Generator     -->  theme/templates/page.html     -->  output/{slug}.html
  ├── images/*         -->  Static Generator   -->  (copied as-is)                -->  output/images/*
  └── extra/*          -->  Static Generator   -->  (EXTRA_PATH_METADATA map)     -->  output/*
```

---

## 2. Metadata Processing & Precedence

1. **In-File Metadata**: Markdown YAML frontmatter / headers take highest precedence.
2. **Path / Directory Inferred**: If `USE_FOLDER_AS_CATEGORY = True` (default in Pelican), the parent directory of an article can define its category. In this repository, `USE_FOLDER_AS_CATEGORY = False` to allow explicit YAML categorization into Pursuit Lanes.
3. **Filesystem Timestamps**: If `date` is omitted and `DEFAULT_DATE = 'fs'`, file `mtime` is used.
4. **Filename Regular Expressions**: Configured via `FILENAME_METADATA`.

---

## 3. Link Directive Translation Rules

Pelican preprocesses link URLs matching `{directive}path`:

| Directive | Resolution Target | Example Input | Build Output |
| :--- | :--- | :--- | :--- |
| `{filename}` | Path to source article/page | `{filename}/posts/guitar.md` | `./posts/guitar.html` |
| `{static}` | Path to static file | `{static}/images/photo.jpg` | `./images/photo.jpg` |
| `{attach}` | Attached asset copied into article dir | `{attach}notes.pdf` | `./posts/notes.pdf` |
| `{category}` | Slug of category archive | `{category}music` | `./lanes/music.html` |
| `{tag}` | Slug of tag archive | `{tag}guitar` | `./tag/guitar.html` |

*Path separator must always be forward slash `/`, even on Windows hosts.*

---

## 4. Custom Reader Implementation (`ObsidianMarkdownReader`)

Defined in `pelicanconf.py`:
- Inherits from `pelican.readers.MarkdownReader`.
- Parses YAML frontmatter enclosed between `---` delimiters using `yaml.safe_load`.
- Passes sanitized metadata dictionary to Pelican's content processor.
- Retains compatibility with standard Pelican metadata fields.
