# jimcollinsworth.github.io
Jim Collinsworth - Out of My Lane website/blog

## Overview
This repository contains my personal website and blog built using Nikola, a static site generator. The site features a clean, modern design with a focus on sharing thoughts, projects, and art related to computing and technology, along with other interests that extend beyond my core expertise.

The front page should have tagline/id, then some highlighted posts and my current 'lanes', like 'learning piano', 'photography', this list changing on activity/priority. Then links/tag/category clouds.


To create a new post with template

# TIL
nikola new_post -t "TIL: Git Rebase" -f markdown -1 --template=note.tmpl.md --meta="note_type=TIL" posts/notes/til-git-rebase.md

# Opinion
nikola new_post -t "Thoughts on Static Sites" -f markdown -1 --template=note.tmpl.md --meta="note_type=opinion" posts/notes/static-sites-opinion.md

# Goal
nikola new_post -t "Learn Python Testing" -f markdown -1 --template=note.tmpl.md --meta="note_type=goal" posts/notes/goal-python-testing.md


## Content Structure

### Categories


1. Projects
    - Data Analysis & Visualization
    - Site Development & Operations
    - Home Automation
    - No Commercials
    - Music & Art - My studies, work, and others work.
        - Piano
        - Guitar
        - Photography
        - Drawing

2. Lanes (Areas/Interests)
    - Finance
    - Politics
    - Health
        - Tai Chi
    - Family
    - STEM
        - Anatomy
        - Weather (can post observations)

   - Music
        - Guitar
        - Piano
    - Art 
        - Photography
        - Drawing

3. References (data file, with optional annotation). References can be linked to from posts, like a review. 
   - Books: refs/books/nanotechnology-godsell.md
   - Research Papers:
   - Urls
   - Quotes

### Content Types
- Posts: Blog entries, observation, TIL (thing i learned).. with metadata-based categorization and taging.
- Pages: Static content (About, Meta, Documentation)
- Images: my photos

## Technical Features
- Responsive design with fullscreen image overlays
- Hierarchical category system
- Tag-based content organization
- Image galleries with EXIF data preservation
- RSS feed support
- No React, No node/npm for building or serving. 
- Simple, inline Javascript as much as possible.
- Meta information page with site management links
- A Mosaic/Bricks approach could be great, simply self adjusting blocks for everything - nav, structure, lists, documents...
- A pure text only view too - accessible view that anyone can use
- Google Photos for all photo assets, anything from the [OutOfMyLane](https://photos.app.goo.gl/yGTTSd3hnw1pqCPo8) photos album. could have a build steps that create metadata and summaries for all the photos, stored as --photo-name.md files in a directory, maybe added as a long description in google photos as allowed. This meta data can be searched by the galleries to find photos and used for descriptions. 


## Management & Development
The site is automatically built and deployed via GitHub Actions.

### Key Management Links
- [GitHub Pages Status](https://github.com/jimcollinsworth/jimcollinsworth.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)
- [Google Search Console](https://search.google.com/search-console)
- [Google Analytics](https://analytics.google.com)
- [GoDaddy](https://godaddy.com)

### Local Development
1. Install Nikola
2. Clone this repository
3. Run `nikola build` to generate the site
4. Run `nikola serve` to preview locally

## License
Content is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).