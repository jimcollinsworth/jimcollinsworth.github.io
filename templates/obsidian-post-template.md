---
# ==============================================================================
# Obsidian & Pelican Post Template
# Personal Website & Blog — Jim Collinsworth (jimcollinsworth.github.io)
# ==============================================================================

# 1. CORE METADATA (Required)
# ------------------------------------------------------------------------------
# Title of the post or essay. Wrap in quotes if it contains colons or special chars.
title: "Title of Your Post"

# Publication date in YYYY-MM-DD or YYYY-MM-DD HH:MM format.
date: 2026-09-13

# Clean URL identifier (e.g., 'posts/my-post-slug.html').
# If omitted, Pelican auto-derives the slug from the title.
slug: "my-post-slug"

# 2. PROVENANCE & AUTHORSHIP STREAM (Required)
# ------------------------------------------------------------------------------
# Defines origin and authorship stream (mutually exclusive):
#   - Mine   : Original human writing, technical notes, software, physical making authored by Jim (Default)
#   - Me     : Autobiographical notes, personal biodata (sleep, health, activity), personal reflections
#   - AI     : Material and code generated or co-authored with AI / LLMs
#   - Ours   : Collaborative works created jointly (Jim + collaborators or Jim + AI)
#   - Theirs : External works, curated references, quotes, or third-party highlights
category: "Mine"

# 3. CONTENT FORMAT & EVOLUTION LIFECYCLE (Required)
# ------------------------------------------------------------------------------
# Single active uppercase format/stage code:
#   - NOTE  : General thought note, observation, journal entry, quick discovery
#   - ESSAY : Long-form structured narrative or analytical deep dive
#   - PROJ  : Active multi-step engineering or fabrication build with milestones
#   - VIEW  : Review, critique, photographic study, exhibition reflection
#   - BOOK  : Book synthesis, structured reading notes, literary critique
#   - TIL   : "Today I Learned" — short 1–3 paragraph insight or CLI fix
#   - SPEC  : Engineering/hardware specifications, architecture blueprints
#   - IDEA  : Concept seedling, raw hypothesis, unexecuted prompt
#   - WIP   : Active work-in-progress draft
type: "NOTE"

# (Optional) Prior evolution stages showing thought maturation across time.
# Example: [IDEA, TIL] or [NOTE, PROJ]
previous_types:
  - IDEA

# 4. TOPIC TAGS & KEYWORDS (Recommended)
# ------------------------------------------------------------------------------
# List of lowercase topical keywords for cross-post thematic discovery.
# Examples: [woodworking, guitar, music, ai, pelican, photography, chicago, health]
tags:
  - general
  - writing

# 5. PUBLISHING STATUS & SUMMARY (Required)
# ------------------------------------------------------------------------------
# Publishing workflow state:
#   - published : Normal public visibility, included in chronological lists & archives
#   - draft     : In-progress draft; kept local or excluded from production feeds
#   - hidden    : Rendered to HTML but excluded from public post listings
status: published

# Concise 1–2 sentence summary / teaser for post cards, index feeds, and meta tags.
summary: "A concise 1–2 sentence summary of this post for index listings and search snippets."

# 6. REVISION & HERO MEDIA (Optional)
# ------------------------------------------------------------------------------
# Last modification date (YYYY-MM-DD). If updated later, set this date:
# modified: 2026-09-15

# (Optional) Hero or preview image path relative to content/ or output/:
# image: images/example-photo.jpg
# image_alt: "Detailed accessible description of the image"
# image_caption: "Descriptive caption rendered beneath the figure"

# 7. STANDALONE PAGE MENU SETTINGS (Pages Only — Leave commented for posts)
# ------------------------------------------------------------------------------
# If this file is placed in content/pages/ and you want it in the site nav bar:
# menu: true
# menu_order: 10
# menu_title: "My Page"
---

<div class="page-intro">
  <p>
    Opening lede or thesis paragraph introducing the topic with slightly enlarged editorial type.
  </p>
</div>

## Section Heading

Body prose goes here. Write clean, distraction-free markdown. Paragraphs are capped at comfortable reading line lengths with precise vertical rhythm.

### Subsection Heading

Further details, observations, or technical analysis.

<!-- Image with context caption (supports lazy loading & high-contrast mode) -->
<figure>
  <img src="../images/example.jpg" alt="Descriptive visual content description" loading="lazy">
  <figcaption>Contextual description of the photograph or diagram.</figcaption>
</figure>

<!-- Obsidian / GitHub style callout quote -->
> [!NOTE]
> Key principle, mental model, or takeaway note to highlight for the reader.

### Code Snippet Example

```bash
# Clean, reproducible CLI commands
uv run pelican content -s pelicanconf.py -o output
uv run pytest -v
```

### Key Takeaways

- First key observation or milestone.
- Second key observation or milestone.
- Next steps or open questions for future exploration.
