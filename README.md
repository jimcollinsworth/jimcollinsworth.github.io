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


## UX

Simple 2 pane focus for navigation/browsing, left/right or up/down depending on orientation. Could be for metadata/photo, article/comments, article/image. image/image 

Full screen for content reading/viewing, with a color frame but otherwise text and images should always appropriatly fill up the screen. The color frame should match to a photo, like sunsets, or other nature. Maybe a color theme change would allow configuration.

Small menu button on all screens. Would be great to have a zoom in/out, drill down/up.. button on every page. Can't we have pinch zoom text size? or maybe just a text 'density' button. 

### Categories


1. Projects
    - Data Analysis & Visualization
    - Site Development & Operations
    - Home Automation
    - No Commercials
    - Music & Art - My studies, work, and others work.
        - Piano
        - Guitar
        - Photos
        - Drawing

2. Lanes (Areas/Interests) - each lane is a post, with links to everything about that lane - TILs, links, photos, comments. more like a personal wiki.
    - Finance
    - Politics
    - Health
        - Tai Chi
        - Anatomy (Said, M. Alexander..)
    - Family
    - STEM
        - Anatomy
        - Weather (can post observations)

   - Music
        - Guitar
        - Piano
    - Art 
        - Photos
        - Drawing

3. References (data file, with optional annotation). References can be linked to from posts, like a review. 
   - Books: refs/books/nanotechnology-godsell.md
   - Research Papers:
   - Urls
   - Quotes

### Content Types
- short: blog entries, observation, TIL (thing i learned).. with metadata-based categorization and taging. Maybe TIL is like a daily journal of the things I did, learned, saw, improved, book review, thoughtof/realized, learned about, anything, text, knowledge, visual, physical (all good tag possibilities). Short text, maybe daily, static they dont change.
- Explorations: Ideas, Interests (guitar, photography), focus area (arthritis, anatomy), code/diy/household project - ie piano, M. Alexander Tech, earthquake viz, Tai Chi. These all have a main page with overview, photos, text (or anything else), and then links to sub pages or related ones. These also change over time, just going to edit them randomly and continuously unless explicitely closed/finalized.
- Pages: Static content (About, Meta, Documentation)
- Images: my photos

## Technical Features
- Responsive design with fullscreen image overlays
- Hierarchical category system, post can only have one category but it can be hierarchical. Use for lanes: computer science, music, music/guitar, music/piano, music/drum, photography, science, woodworking, art, history, DIY, all-else 
- Tag-based content organization (TIL, book review, idea, python utility....spark,venture, endeavor, exploration, jouney, pursuits - journal, note, spark, bits, glipses, message), biochemistry, nosql
- blog metadata for draft/publish and such
- Image galleries with EXIF data preservation
- RSS feed support
- No React, No node/npm for building or serving. 
- Simple, inline Javascript as much as possible.
- Meta information page with site management links
- A Mosaic/Bricks approach could be great, simply self adjusting blocks for everything - nav, structure, lists, documents...
- A pure text only view too - accessible view that anyone can use.
- How about pure image option too, no text at all, just LLM generated images from the blog text (and images)
- Everything is in github so we have great versioning. Ideally we can see this in the output, so users see what is new (maybe just color/highlight it based on age, newest is clearest/darkest) ?any nikola git github plugins?
- External discussion system if any, open source discourse?, X, Instagram

### photo/video management
 Google Photos is the source for all photo assets, anything from the [OutOfMyLane](https://photos.app.goo.gl/yGTTSd3hnw1pqCPo8) photos album. could have a build steps that create metadata and summaries for all the photos, stored as --photo-name.md files in a directory, maybe added as a long description in google photos as allowed. This meta data can be searched by the galleries to find photos and used for descriptions. Turns out google photos is hard to integrate, it is possible to get an image url but they don't seem to work embedded. Photos can be downloaded in a zip, and served other ways too. I think I'll have a few topic related galleries like sunrise, flowers, art that could be large, can't do those just in Nikola. Using LLM would be nice too for automatic categorzation and avoid file names, but second step. 

 [x] Use native Nikola to create some galleries, copy some images into repo 
 [] Provide link to public google photos galleries for users to see more.
 [] Update template to for nice 2 pane view
 [] Plugins or custom code to use better gallery/lightbox
 [] File management/LLM utilities to scan images, discover links from google photos. Takeout might be best source, don't bother with google apis at all, maybe takeout will provide the url to images.

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



Create a new post:

nikola new_post -f markdown -t "Your Post Title" --tags="journal" -d short


## License
Content is licensed under [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).