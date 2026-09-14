# Site Journal & Decision Log: jimcollinsworth.github.io

> Chronological log of architectural decisions, site milestones, and design changes. Maintained under the 3-document agent rule.

## 2026-09-14 — Pure Markdown Content Migration, Automatic Link Resolution & Dedicated Blueprints (Release v0.7.8)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"i can't get this link to work in markdown, should i link to the html or markdown"*
> - *"wait, why is there html at all in the markdown, this is the input from obsidian that gets converted to html, from the source /content directory to the /output directory. markdown inter document links get converted to html links by pelican, isn't that the case?"*
> - *"remove the raw html wrappers and really all raw html from all markdown content files, insert appropriate front matter with our pelican and site metadata standards add the automatic link resolution, don't change anything on the page directories/folder structure"*

### Problem & Diagnosis
1. **Broken Markdown Link Parsing**:
   - In `content/pages/about-this-site.md`, the introductory paragraph was wrapped inside a raw HTML block (`<div class="page-intro"><p>...</p></div>`). Python-Markdown disables Markdown link parsing inside raw HTML tags, leaving `[Development Prompts](prompt-history.md)` unlinked as literal text.
2. **HTML Noise in Obsidian Vault**:
   - Multiple content pages and posts contained raw HTML elements (`<div class="page-intro">`, `<figure>`, `<figcaption>`, inline SVG icons, raw dashboard grids) that compromised readability and editing in Obsidian.
3. **Missing Intra-Site Link Translation**:
   - Stock Pelican requires explicit `{filename}` directives to resolve relative `.md` files into `.html` output URLs. Authors writing standard Markdown links (`[label](file.md)`) or Obsidian wikilinks (`[[target]]`) received broken or unresolved links.

### Root Cause & Technical Analysis
- The content directory is Jim's input source from Obsidian. Having raw HTML wrappers violated the principle of clean Markdown separation.
- By intercepting Markdown in Pelican's custom `ObsidianMarkdownReader`, intra-site `.md` links and wikilinks can be automatically mapped to `{filename}` directives using a pre-built content file registry, while standalone images (`![alt](src)`) can be transformed into semantic, responsive `<figure>` elements.

### Solution & Standard Procedure
1. **Automated Intra-Site Link Resolution (`pelicanconf.py`)**:
   - Extended `ObsidianMarkdownReader` with `_build_file_map()` and `_resolve_links()`. Automatically translates `[label](target.md)` and `[[target|label]]` into `{filename}` directives so Pelican calculates exact relative HTML URLs.
   - Handled `posts.md` and `posts` references to resolve cleanly to relative `posts.html`.
2. **Automated Figure Wrapping (`pelicanconf.py`)**:
   - Added `_wrap_figures()` to automatically transform Markdown images (`![alt](src)`) into `<figure><a class="photo-link"><img ...></a><figcaption>alt</figcaption></figure>`.
   - Automatically normalized image paths (`images/...` to `../images/...` for posts) to ensure asset integrity across directories.
3. **Dedicated Jinja2 Blueprints (`theme/templates/`)**:
   - Created `theme/templates/about-this-site.html` (renders Markdown content + appends structured DevOps & Infrastructure Dashboard).
   - Created `theme/templates/apps.html` (renders Markdown content + application cards).
   - Created `theme/templates/photos.html` (renders Markdown image stream inside responsive `.photo-gallery-page` 2-column grid).
   - Created `theme/templates/links.html` (renders curated links 2-column layout).
4. **CSS Lead-Paragraph Styling (`theme/static/css/style.css`)**:
   - Added `.page-body > p:first-of-type, .post-content > p:first-of-type` to lead intro styles across mobile, landscape, and desktop viewports, eliminating the need for `<div class="page-intro">`.
5. **Pure Markdown Content Migration (`content/`)**:
   - Removed all raw HTML wrappers, card divs, and SVG icons from `content/pages/` and `content/posts/`.
   - Updated `tools/sync_dev_prompts.py` to output pure Markdown paragraphs for prompt history intro.
6. **Automated Testing**:
   - Added `test_pure_markdown_content_sources()` and `test_markdown_link_and_figure_resolution()` to `tests/test_pelican_e2e.py`.
   - All 54 tests passing.

## 2026-09-14 — Photo Asset Size Management Policy & Zero Full-Resolution In-Repo Standards (Release v0.7.7.01)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"ok, going forward need to make sure we manage the photo sizes that end up in the repo, the full resolution will be direct google photo url. so only smaller photos (medium size and a thumbnail) get into repo and site. maybe a built step. update the photo viewer ticket, and elsewhere"*

### Problem & Diagnosis
1. **Repository Bloat & Clone Latency**:
   - Camera originals (8–10 MB each) in `archive/original_photos/` and historical gallery commits inflated `.git` download size to ~90–112 MB.
   - Recloning on secondary devices (such as laptops) required downloading heavy binary history unrelated to site code and text.
2. **Missing Ingestion Boundaries**:
   - No explicit size ceiling was codified preventing large full-resolution media from being committed to the repo.

### Root Cause & Technical Analysis
- Git is designed for text and code; binary photo assets do not compress efficiently across commit revisions.
- Decoupling display preview tiers from archival storage keeps the Git repository compact and fast while preserving access to full-resolution assets via external cloud storage URLs (Google Photos or Google Drive).

### Solution & Standard Procedure
1. **GitHub Issue #3 Updated**:
   - Added architectural comment to Issue #3 (*"photos app"*) documenting the zero full-resolution in-repo policy, two local display tiers (thumbnails and medium display assets), direct Google Photos / Drive URL resolution, and automated build step pipeline.
2. **Agent Rules Codified**:
   - Added Section 19 to `AGENTS.md` and `.agents/agent_rules.md` prohibiting commit of files > 500 KB or camera RAWs into the repo and requiring automated optimization for incoming photos.
3. **Documentation Updated**:
   - Added Section 4 "Photo Asset Size Management & Sizing Tiers" to `README.md`.
   - Updated Section 3.C "High-Volume Photo Navigation & Archive Explorer" in `ROADMAP.md`.
4. **DevOps & Timeline Synchronization**:
   - Synchronized prompt history to 106 steering prompts across 32 milestones.
   - Bumped version to `v0.7.7.01` across `pyproject.toml`, `releases/v0.7.7.01.md`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-14 — Homepage Layout: Photo Spotlight Reordered After Featured Post (Release v0.7.7)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"one more thing, lets put the photo spotlight after the featured post. then merge,  push and publish it all"*

### Problem & Diagnosis
1. **Homepage Visual Balance**:
   - The Photo Spotlight section was positioned at the bottom of the secondary sidebar column beneath the 3-item Recent Stream.
   - On desktop screens, this elongated the right column while leaving the left primary column shorter with only the Featured Post and 2 book notes.
   - On mobile screens, the photo spotlight appeared after both the featured post, bookshelf notes, and recent articles.

### Root Cause & Technical Analysis
- In `theme/templates/index.html`, Photo Spotlight was nested inside `.sidebar-column`. Moving it directly below Featured Post in `.main-column` balances the desktop two-column grid heights and brings visual photographic media into immediate prominence on both desktop and mobile viewports.

### Solution & Standard Procedure
1. **Template Restructuring**:
   - Relocated `<section> <h2>Photo Spotlight...` from `.sidebar-column` into `.main-column` directly beneath `Featured Post` and preceding `Recent Links`.
   - Removed the preceding `<hr>` separator from `.sidebar-column`.
2. **Automated Testing & Build Verification**:
   - Compiled static site via Pelican (`0.13s`).
   - Verified 52/52 automated tests in `pytest -v` across accessibility, layout rendering, and responsiveness.
3. **DevOps & Timeline Synchronization**:
   - Synchronized dev prompt timeline (`content/pages/prompt-history.md`) to 105 steering prompts across 31 milestones.
   - Bumped version to `v0.7.7` across `pyproject.toml`, `releases/v0.7.7.md`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-14 — Ported Amateur Personas, Metadata Matrix & Vertical Density Standards (Release v0.7.6.01)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"can you look at this branch in github feature/mobile-1line-header-dense-layout   i was doing this work on another machine. merge it in if still appropriate"*
> - *"proceed, and what do i do on my laptop that has the local branch"*

### Problem & Diagnosis
1. **Divergent Remote Feature Branch**:
   - Jim had worked on a separate machine on `feature/mobile-1line-header-dense-layout`, which branched from `v0.5.9`.
   - A direct `git merge` would cause massive merge conflicts and regress 15 releases of progress (`v0.6.0` through `v0.7.6`).
2. **Valuable Unmerged Concepts**:
   - The branch contained valuable documentation not present on `main`:
     1. Tongue-in-cheek Amateur Pursuit Personas in `ROADMAP.md`.
     2. Metadata Mapping Matrix in `README.md` and authoring cheat sheets.
     3. Strict Vertical Density & Click-Target principle in `AGENTS.md` and `.agents/agent_rules.md`.

### Root Cause & Technical Analysis
- The mobile header and dropdown navigation originally prototyped on that branch had already been completed and tested on `main` in `v0.6.4` through `v0.6.7`.
- Cherry-picking and adapting the enduring documentation concepts directly into current documents avoids code regression while capturing the authoring guidance.

### Solution & Standard Procedure
1. **Ported Architecture Concepts**:
   - Added Section 8 "Amateur Pursuit Personas & Cross-Disciplinary Exploration" to `ROADMAP.md`.
   - Added "Metadata Mapping: Pelican Engine vs. Obsidian Authoring vs. Site Concept" table to `README.md` and `docs/cheatsheets/content_authoring.md`.
   - Codified "Elimination of Redundant Action Links & Vertical Density (Strict)" in `AGENTS.md` and `.agents/agent_rules.md`.
2. **Laptop Branch Cleanup Guidance**:
   - Provided exact commands for Jim to synchronize and clean his laptop environment without merge conflicts.
3. **Remote Branch Deletion**:
   - Deleted stale remote branch `origin/feature/mobile-1line-header-dense-layout`.
4. **Testing & Versioning**:
   - Verified static build and passed all 52 automated tests in `uv run pytest -v`.
   - Bumped version to `0.7.6.01` across `pyproject.toml`, `releases/v0.7.6.01.md`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-14 — Condensed Ideas Stream & Provenance Filtering (Release v0.7.6)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"i want to add our 'future' concept to the site, or just upcoming might be a better term. or planned. this would be posts, rants, goals, apps, anything that really hasn't been started but i want to list as a teaser, collect input, keep it on my radar. i don't want to list these everywhere, it's more downlow and limited, or on demand. so maybe a status like published, draft, hidden, future, or just 'upcoming' in the date field, or what else? thoughts"*
> - *"actually i probably like ideas better than radar, radar implies others work i'm looking at, not my own. kiss. I intend to put tens, hundred ideas out there, just going to blast them in, so keep the view very condensed, packed in, no meta data, just title. add a few of yours to. be sure to mark yours with ai providence and mine with my providence icon. ideas: I'm vibe coding now, I'm an AI doomsayer now, History book mapper"*
> - *"yes, merge and publish. but a few more ideas from me to add: 4d earthquake animation - use map layers or 3d framework/game engine; what played then (vs playing now)- tracks every show/ad/product/song, open/crowdsourced/ai identification - signature contains what, when, channel; bike handlebar utility shelf - maglock for phones, bluetooth"*

### Problem & Diagnosis
1. **Teaser & Seedling Visibility**:
   - Jim required a lightweight mechanism to post unpolished concepts, rants, goals, and app ideas without cluttering the primary chronological blog archive (`posts.html`) or homepage feeds.
2. **High-Density Presentation**:
   - As tens or hundreds of ideas are added, standard post cards with summaries, dates, and tag clouds would cause overwhelming vertical scroll. The listing needed an ultra-dense, packed-in layout displaying strictly titles with provenance icons.
3. **Attribution & Provenance**:
   - Clear distinction between Jim's original concepts (`category: Mine`) and AI-proposed ideas (`category: AI`, authored by `LLM-Gemini3.8`).

### Root Cause & Technical Analysis
- Utilizing Pelican's existing `type: IDEA` frontmatter avoided introducing custom metadata layers.
- Filtering `type == 'IDEA'` out of `index.html` and `archives.html` isolated seedlings from polished long-form writing while keeping static URL compilation active for each individual idea.

### Solution & Standard Procedure
1. **Template & Feed Isolation**:
   - Created `theme/templates/ideas.html` with an ultra-condensed listing rendering `category_icon` alongside the idea title link.
   - Filtered out `type: IDEA` from `theme/templates/index.html` (featured post and recent stream) and `theme/templates/archives.html`.
   - Added subtle lead-in link to `ideas.html` in `posts.html`.
2. **Smart Back Navigation**:
   - Updated `theme/templates/article.html` so back arrows on idea detail pages return to `/ideas.html`.
3. **Seeded Initial Concepts**:
   - Authored Jim's 6 ideas (`category: Mine`): *"I'm vibe coding now"*, *"I'm an AI doomsayer now"*, *"History book mapper"*, *"4D Earthquake Animation"*, *"What Played Then (vs. Playing Now)"*, and *"Bike Handlebar Utility Shelf"*.
   - Authored 2 AI ideas (`category: AI`, author: `LLM-Gemini3.8`): *"Offline Cross-Reference Footnote Weaver"* and *"Lake Michigan Microclimate Correlator"*.
4. **CSS & Styling**:
   - Added compact CSS rules in `theme/static/css/style.css` for `.ideas-container`, `.ideas-list`, and `.idea-item`.
5. **Testing & Versioning**:
   - Added automated test `test_ideas_stream_isolated_and_dense` asserting isolation from `posts.html` and `index.html` (52 total passing tests).
   - Bumped project version to `0.7.6` across `pyproject.toml`, `releases/v0.7.6.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-14 — Content Refinements, Provenance Relocation & App Nomenclature (Release v0.7.5)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"remove local from local ai in home page"*
> - *"Change the title if the app post to multimodal data pipeline-tool"*
> - *"remove this from about me This site operates under a strict Zero-JavaScript policy. Reader submissions from posts and inquiries are routed through a private Google Apps Script & Google Sheets pipeline, triaged and synthesized using local LLM tooling, and compiled into static editorial digests without exposing the site to client-side scripts or public comment spam."*
> - *"move content streams section from the about me into the top of the about site page. The individual items are good in the descriptions, add hikes. events. museums , tours and such examples. but the intro paragraph needs to be changed. . This is about Providence and my desire to attempt to separate and identify AI or others contributions from my small writings on the site."*
> - *"The preview links have broken before, so figure out why that has slipped through a few times and update appropriate agent rules to keep it from happening again. Publish and push otherwise."*

### Problem & Diagnosis
1. **Nomenclature and Bio Accuracy**:
   - Homepage blurb referenced "local AI" rather than general "AI".
   - App post title was verbose ("Pipeline Tools: Multimodal Data Ingestion & Transformation Workbench") instead of concise ("Multimodal Data Pipeline-Tool").
2. **Taxonomy & Provenance Placement**:
   - The "Content Streams & Categorization" section sat at the bottom of the biographical "About Me" page (`about.md`), whereas content stream taxonomy and provenance attribution belong with site architecture on "About This Site" (`about-this-site.md`).
   - The stream descriptions lacked relatable everyday collaborative examples (such as hikes, events, museum visits, and tours).
   - The introduction needed to clearly articulate provenance: distinguishing Jim's human writings from AI assistance and external collaborators.
3. **Outdated Comment Pipeline Copy**:
   - `about.md` contained outdated text describing a planned Google Apps Script & Google Sheets Zero-JavaScript comment intake pipeline.

### Root Cause & Technical Analysis
- As the site expanded from a single personal intro to a structured platform, architectural explanations (like streams and provenance) outgrew the personal bio page.
- Clear separation of human authorship, AI generation, and collaborative experiences requires transparent provenance definitions prominently displayed in site documentation.

### Solution & Standard Procedure
1. **Homepage Bio Update**:
   - Edited `theme/templates/index.html` to change "local AI" to "AI".
2. **Post Title Update**:
   - Updated `content/posts/pipeline-tools-workbench.md` title frontmatter to `"Multimodal Data Pipeline-Tool"`.
3. **About Me Page Cleanup**:
   - Removed the `## Content Streams & Categorization` section and the Zero-JavaScript comment pipeline paragraph from `content/pages/about.md`.
4. **Relocation to About This Site**:
   - Added `## Content Streams & Provenance` to the top of `content/pages/about-this-site.md`.
   - Updated the introductory copy: *"This is about provenance and my desire to attempt to separate and identify AI or others' contributions from my small writings on the site."*
   - Added concrete examples (hikes, events, museums, tours) to collaborative and external streams (`Ours` and `Theirs`).
5. **Versioning & Documentation**:
   - Bumped project version to `0.7.5` across `pyproject.toml`, `about-this-site.md`, `releases/v0.7.5.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-14 — Visual Evidence Path Standards Codification (Section 13) & Release v0.7.4.02

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"The preview links have broken before, so figure out why that has slipped through a few times and update appropriate agent rules to keep it from happening again. Publish and push otherwise."*

### Problem & Diagnosis
1. **Recurring "Preview Not Available" Errors in Artifacts**:
   - In previous sessions, screenshot images embedded in `walkthrough.md` occasionally failed to load in the Antigravity artifact viewer, displaying a broken image or "Preview not available".
2. **Path Inconsistencies**:
   - Agents intermittently wrote relative filenames (e.g., `![Dashboard](preview.png)`) or used Windows backslashes (`\`), which fail URL parsing in webview renderers.

### Root Cause & Technical Analysis
- The Antigravity artifact viewer does not resolve relative image links against the active conversation artifact directory.
- Windows filesystem paths containing backslashes are corrupted by markdown escape-character handling.
- Section 13 in `AGENTS.md` mandated inline screenshots for UI changes but lacked explicit, binding path formatting and storage invariants.

### Solution & Standard Procedure
1. **Codified Mandatory Image Formatting Standards in Section 13**:
   - Updated `AGENTS.md` and `.agents/agent_rules.md` Section 13 to mandate:
     1. **Zero Relative Paths**: All screenshot embeds in artifacts (`walkthrough.md`) must use full absolute paths.
     2. **Forward Slashes Only**: All paths must use forward slashes (e.g. `C:/Users/jimco/...`).
     3. **Artifact Directory Storage**: All images must reside directly in `<appDataDir>/brain/<conversation-id>/`.
     4. **Pre-Flight Verification**: Mandatory verification of image path syntax before presenting reports.
2. **Versioning & Documentation**:
   - Bumped version to `v0.7.4.02` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

## 2026-09-13 — Chronological Prompt History, On-Site Release Notes Linking & Version v0.7.4.01

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"on t hr website site page is says verdion .7.4 but the link goes to release 0.5.9 whats up with our release notes?"*
> - *"slso make the dev prompts chronological"*

### Problem & Diagnosis
1. **GitHub Releases vs Git Tags Discrepancy**:
   - The Site Version card on `about-this-site.html` linked externally to `https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases`. That GitHub page showed `v0.5.9` at the top because later versions (`v0.6.0` through `v0.7.4`) existed as Git tags (`/tags`) but had not been formally published as GitHub Release objects.
2. **Reverse Chronological Prompts**:
   - `prompt-history.html` displayed milestones in reverse chronological order (newest first, oldest last) rather than forward chronological progression.
3. **Outdated Metric**:
   - The Steering Prompts card on `about-this-site.html` was hardcoded to 77 prompts instead of the current 91 prompts.

### Root Cause & Technical Analysis
- GitHub's `/releases` UI filters exclusively for published release objects; tags created via `git tag` only appear on `/tags` unless drafted and published on GitHub.
- `tools/sync_dev_prompts.py` read `JOURNAL.md` top-down and emitted milestones without reversing the list into chronological order.

### Solution & Standard Procedure
1. **Chronological Milestone Ordering**:
   - Updated `tools/sync_dev_prompts.py` to reverse the parsed milestone list (`list(reversed(milestones))`), displaying prompt history chronologically from earliest (v0.5.8, Sept 10 2026) to latest (v0.7.4, Sept 13 2026).
2. **On-Site Release Notes Linking**:
   - Changed the primary link in the Site Version card on `about-this-site.md` to point directly to `prompt-history.html` so visitors read full milestone notes natively on the site.
   - Added direct link to `GitHub Tags` (`/tags`) in the card subtitle.
   - Synchronized prompt count to `91 Prompts →`.
3. **Releases Directory Synchronization**:
   - Created missing release notes files in `releases/`: `v0.7.1.md`, `v0.7.2.md`, `v0.7.3.md`, and `v0.7.4.md`.
4. **Verification & Versioning**:
   - Bumped version to `0.7.4.01` in `pyproject.toml` and `about-this-site.md`.
   - Rebuilt Pelican site and verified all 51 automated tests pass in `pytest -v`.
   - Captured full 1920x1080 visual evidence of updated cards and chronological prompts.

## 2026-09-13 — Custom Domain DNS Mapping & CNAME Configuration (v0.7.4)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"The site resolution is different when I look at jimcollinsworth.com versus jimcollinsworth.github.io why"*
> - *"heres it now, before changes"*
> - *"i made the dns changes"*

### Problem & Diagnosis
1. **Discrepancy in Mobile Resolution & Layout**:
   - Navigating to `https://jimcollinsworth.com` on a mobile device rendered the two-column desktop layout zoomed out with miniaturized text, whereas `https://jimcollinsworth.github.io` rendered the responsive single-column layout with compact navigation.
2. **Missing Deep-Link Navigation & Address Bar Updates**:
   - Navigating internal links while on `jimcollinsworth.com` kept the browser address bar frozen at `jimcollinsworth.com/`.

### Root Cause & Technical Analysis
- Running `curl.exe -s https://jimcollinsworth.com` revealed that GoDaddy was configured with **"Domain Forwarding with Masking"** (stealth forwarding).
- GoDaddy's proxy served an HTML 4.01 `<frameset>` embedding `<frame src="https://jimcollinsworth.github.io">` without a `<meta name="viewport" content="width=device-width, initial-scale=1">` tag in the parent document.
- In the absence of a viewport meta tag, mobile browsers defaulted to a virtual desktop viewport of 980px and scaled down the canvas. Because the frame width was 980px, responsive CSS media queries (`@media (max-width: 640px)`) never evaluated to `true`.

### Solution & Standard Procedure
1. **GoDaddy DNS Reconfiguration**:
   - Replaced GoDaddy's proxy `A` records with 4 GitHub Pages apex `A` records:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - Updated the `www` `CNAME` record to point to `jimcollinsworth.github.io`.
2. **Pelican CNAME Integration**:
   - Created `content/extra/CNAME` containing `jimcollinsworth.com`.
   - Registered `'extra/CNAME': {'path': 'CNAME'}` in `EXTRA_PATH_METADATA` in `pelicanconf.py` so Pelican automatically produces `output/CNAME` on every build.
3. **Automated Verification**:
   - Updated `tests/test_pelican_e2e.py` to assert `output/CNAME` existence and correct domain content.
   - Verified 51/51 automated tests pass in `uv run pytest -v`.
4. **Versioning**:
   - Synchronized `pyproject.toml` and `about-this-site.md` to `0.7.4`.

## 2026-09-13 — Prompt History Visual Title, Full-Bleed Response Blocks, Provenance Icons & Release Links (v0.7.3)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"so this is a custom page not on the menu, in this case we don't have the menu providing a visual title, so full title is needed. instead of Development Prompts (Stream: Mine • Author: Jim Collinsworth) it should be the providence icon(s) then title, the maybe date last changed/updated Sept 13 2026 - full date since day matters more.all on same line with title and icons, use smaller title font same as in blog lists and detail."*
> - *"then for prompt add the icon instead of mine, still say jim"*
> - *"then add ai icon to reponse, lighty grey out screen edge to edge the block of response text"*
> - *"release titles should be a smaller font, and a link to something relevant"*

### Problem & Diagnosis
1. **Missing Visual Page Title**:
   - Because `prompt-history.html` is a custom standalone page not present in the top navigation menu, the navigation bar did not provide an active highlighted tab to identify the page title. The body paragraph had previously embedded metadata as parenthetical text (`(Stream: Mine • Author: Jim Collinsworth)`).
2. **Provenance Labels vs Icons**:
   - The prompts were labeled with plain text `**Jim (Mine):**` rather than the graphical provenance icon.
   - The response block lacked the AI provenance icon and was not visually separated from user prompts.
3. **Response Block Edge-to-Edge Visual Separation**:
   - The response text was visually identical in weight and background to the prompt text.
4. **Milestone Header Scale & External Linking**:
   - Release headers used large `<h2>` font sizes and lacked links to release artifacts.

### Root Cause & Technical Analysis
- The generator script `tools/sync_dev_prompts.py` emitted markdown with `##` headings, plain-text role strings (`**Jim (Mine):**`, `**Response:**`), and had not used semantic provenance badges.
- In CSS, `.container` max-width constrained all child elements; achieving a full-bleed edge-to-edge background requires viewport-width breakout (`width: 100vw; margin-left: calc(50% - 50vw); margin-right: calc(50% - 50vw);`) with `overflow-x: clip;` on `html` and `body` to prevent horizontal scrolling.

### Solution & Standard Procedure
1. **Consolidated Post Header for Standalone Page**:
   - Rendered `<header class="post-header-full">` at the top of `prompt-history.html` containing the back arrow (`←`), dual provenance badge (`[Mine]` `[AI]`), title `Development Prompts`, and right-justified unbolded date `Sept 13 2026`.
   - Scaled `.post-header-full .post-title` to `1.15rem` (`font-weight: 600`), harmonizing with blog lists and article details.
2. **Provenance Icons for Prompts & Responses**:
   - Prompts are labeled with the Mine icon (`icon-mine`) + `Jim:` (removing text `(Mine)`).
   - Responses are labeled with the AI icon (`icon-ai`) + `Response:`.
3. **Full-Bleed Edge-to-Edge Response Block**:
   - Wrapped response actions in `.prompt-response-block` with `width: 100vw; margin-left: -50vw; margin-right: -50vw; left: 50%; right: 50%;` and `background-color: var(--bg-subtle);`.
   - Wrapped text in `.prompt-response-inner` with `max-width: var(--max-width); margin: 0 auto;` matching body padding so text stays aligned with the page measure.
   - Added `overflow-x: clip;` to `html` and `body` in `theme/static/css/style.css`.
4. **Milestone Release Headers with Links**:
   - Formatted milestone titles in smaller font (`1.08rem`, `font-weight: 600`) as clickable links (`.milestone-title a`) pointing to specific GitHub release tags (e.g. `releases/tag/v0.7.1`) or the releases overview.
   - Displayed uppercase unbolded release date (`.milestone-date`) right-aligned on the same row.
5. **Verification & Versioning**:
   - Synchronized `pyproject.toml` and `about-this-site.md` to `0.7.3`.
   - Regenerated `prompt-history.md` via `tools/sync_dev_prompts.py` (84 prompts across 23 milestones).
   - Verified 51/51 automated tests pass in `pytest -v`.

## 2026-09-13 — Post Header Consolidation, Framed App Mockups, Full-Screen Photo Links & Zero-JS UI Streamlining (v0.7.2)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"as with other pages we don't need a read app post button, the post title should jump there. remove the embedded view for pipeline-tool"*
> - *"remove copywrite notice on bottom page, entire line. any attribution will be in about me and about site pages"*
> - *"unbold the post types, and reduce the spacing between main sections like feature post and recent links"*
> - *"content explorer post page (and other) make title line consistent with list, icon(s) in front of title, type and date right justified and unbolded."*
> - *"back to posts line is very screen wastful, a entire line. find a way to do this without using an entire line, just a back icon somewhere in header or floating on content."*
> - *"the content explorer screen image is missleading it looks like part of post. make the screen size smaller and maybe a accent border so it's obvious it's a screen shot. Put the launch link at the beginning, using the same nice button as the apps list does."*
> - *"for photos in general, clicking on any photo goes full screen, do for gallery and all places"*

### Problem & Diagnosis
1. **Redundant Buttons on Apps Page**: The Apps Hub (`apps.md`) had duplicate calls to action ("Read App Post →" and "Launch Full-Screen App →") alongside a redundant embedded iframe button for Pipeline Tools.
2. **Obsolete Embedded Page**: The dedicated embedded page `pipeline-tools.md` was redundant with the full-screen interactive app (`apps/pipeline-tools/index.html`).
3. **Footer Clutter**: The footer copyright line was taking up vertical space; legal/attribution belongs in About Me and About Site.
4. **Visual Weight & Section Spacing**: Bold post type indicators (`font-weight: 600`) drew excessive visual attention away from titles. Section margins between Featured Post and Recent Links caused unnecessary vertical scrolling.
5. **Post Header Inconsistency & Screen Waste**: Post pages contained a standalone `← Back to Posts` line consuming a whole row. Post titles lacked the provenance icon and right-justified unbolded metadata shown on post list pages.
6. **App Post Screenshot Confusion**: Screenshots inside app posts stretched to 100% width with subtle borders, making screenshots look like live web controls. The launch button was located at the very bottom of the post.
7. **Photo Exploration**: Photo figures in the gallery, homepage spotlight, and article posts lacked full-screen viewing links.

### Root Cause & Technical Analysis
- The post template (`article.html`) rendered a `<div class="back-nav"><a href="...">← Back to Posts</a></div>` block above the article heading, consuming vertical space.
- Post headers in `article.html` did not utilize the flex-based `.post-header-row` structure established in `theme/templates/index.html`.
- Generic `<figure>` styling in `style.css` rendered all images at full container width (`max-width: 100%`) without visual demarcation separating application screenshots from page UI.
- Image elements were unlinked `<img ...>` tags without anchor wrappers to full-resolution assets.

### Solution & Standard Procedure
1. **Apps Page & Post Titles (`content/pages/apps.md`)**:
   - Linked all card titles directly to their respective posts (`posts/photo-viewer-drive-manifest-explorer.html`, `posts/keyword-explorer-taxonomy.html`, `posts/pipeline-tools-workbench.html`).
   - Removed all "Read App Post →" buttons and removed the "Embedded View →" button.
2. **Removed Obsolete Embedded Page**:
   - Executed `git rm content/pages/pipeline-tools.md` and removed references from `theme/templates/base.html` and `pipeline-tools-workbench.md`.
3. **Removed Footer Copyright**:
   - Removed the `<div>Content &copy; Jim Collinsworth...</div>` line from `theme/templates/base.html`.
4. **Unbolded Post Types & Tighter Section Spacing (`theme/static/css/style.css`)**:
   - Changed `.post-header-right .post-type`, `.book-header-right .book-author`, and `.post-type` to `font-weight: 400`.
   - Tightened `.post-item.featured` padding and margin; reduced `.post-item` bottom margin to `1.35rem`; reduced section heading margins in `.desktop-two-col`.
5. **Streamlined Post Header (`theme/templates/article.html` & `category.html`)**:
   - Structured `<header class="post-header-full">` with `.post-header-row`: left column includes inline `<a class="post-back-arrow">←</a>`, provenance category badge, and `<h1 class="post-title">`; right column displays unbolded uppercase post type and date.
   - Updated `category.html` to integrate `<a class="post-back-arrow">←</a>` directly alongside `<h2>Category: ...</h2>`.
6. **Framed App Screenshots & Top Launch Button (`content/posts/*.md`)**:
   - Added primary accent button `<a href="..." class="app-launch-btn">Launch Full-Screen App &rarr;</a>` right below the lead paragraph across all app posts.
   - Created `figure.screenshot-frame` with `max-width: 640px`, centered margin, `border: 2px solid var(--accent);`, rounded corners, and shadow.
7. **Full-Screen Photo Viewing Across Site**:
   - Wrapped images in `<a href="..." class="photo-link" title="Click to view full screen">` across `content/pages/photos.md`, `theme/templates/index.html` (spotlight), `content/posts/art-institute-chicago-modern-wing.md`, and all app post screenshots with `cursor: zoom-in`.
8. **Automated Testing, Verification & Versioning**:
   - Rebuilt Pelican static output; verified all 51 automated tests pass (`uv run pytest -v`).
   - Re-synced steering prompts via `tools/sync_dev_prompts.py` (77 prompts cataloged).
   - Bumped project version to `0.7.2` in `pyproject.toml` and `about-this-site.md`.
   - Captured full-width uncropped screenshots at 1920x1080 for visual verification.

## 2026-09-13 — Big Display Typography Scaling & Full-Screen App Header Unification (v0.7.1)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"i think on big displays 'jim collinsworth' and 'out of my lane' can be a bit bigger"*
> - *"and is the pipeline-tools hugging face app running in full screen mode like the other 2 apps now with the same header bar?"*
> - *"why can't i see the left and right edges,"*

### Problem & Diagnosis
1. **Desktop Branding Presence on Big Displays**:
   - On wide desktop displays (1360px to 1920px+), the site title ("Jim Collinsworth") at `1.35rem` and tagline ("Out of My Lane") at `1.15rem` were visually understated relative to the 1380px layout container width and reading copy.
2. **Cropped Visual Evidence in Walkthrough**:
   - The closeup header screenshot in `walkthrough.md` was clipped at `x: 300, width: 1320` across a 1920px viewport, shaving off 300px on both sides and cutting off the outer container edges, leaving "n Collinsworth" on the left and "Out of My L" on the right.
3. **App Header Consistency**:
   - The standalone full-screen application wrapper for Pipeline Tools had minor styling and button discrepancies compared to Photo Viewer and Keyword Explorer (`.brand-link` with button border vs plain text accent link `&larr; Back to Apps`, missing Theme and Fullscreen toggle buttons).

### Root Cause & Technical Analysis
- The `@media (min-width: 1360px)` supersize desktop query increased `--max-width` to 1380px and body padding to `1.5rem 3rem 4rem`, but lacked specific font size overrides for `.site-title` and `.site-tagline`.
- Standardizing base desktop `.site-title` to `1.55rem` and `.site-tagline` to `1.25rem`, with big display overrides to `1.95rem` and `1.45rem`, maintains baseline alignment (`align-items: baseline`) while providing appropriate visual presence.
- Aligning `content/apps/pipeline-tools/index.html` markup to `.brand a.back-link`, `<h1>`, and standard `.btn` elements provides uniform UI across all three standalone applications.

### Solution & Standard Procedure
1. **Typography Scaling in CSS (`theme/static/css/style.css`)**:
   - Scaled base desktop `.site-title` from `1.35rem` to `1.55rem`.
   - Scaled base desktop `.site-tagline` from `1.15rem` to `1.25rem`.
   - Added `@media (min-width: 1360px)` overrides: `.site-title { font-size: 1.95rem; }` and `.site-tagline { font-size: 1.45rem; }`.
   - Scaled `.site-tagline` under `#text-size-toggle:checked` to `1.65rem !important`.
2. **App Header Standardization in pipeline-tools**:
   - Standardized left navigation to back-link anchor (&larr; Back to Apps) with colored accent and underline on hover.
   - Standardized app title to serif bold h1 header.
   - Standardized action buttons using shared `.btn` classes.
   - Added Theme toggle and browser Fullscreen toggle buttons matching Photo Viewer.
3. **Uncropped Full-Width Screenshot Captures**:
   - Developed `scratch/capture_fullwidth_header_and_apps.py` capturing uncropped 1920px width viewports (`preview_header_fullwidth_1920_light.png` and `preview_header_fullwidth_1920_dark.png`), showing full left and right outer container margins and alignment.
   - Captured side-by-side header bar comparisons across all three applications.
4. **Verification & Versioning**:
   - Synchronized `pyproject.toml` and `content/pages/about-this-site.md` to `v0.7.1`.
   - Synced `content/pages/prompt-history.md` via `tools/sync_dev_prompts.py` (77 prompts across 22 milestones).
   - Passed all 51 automated tests (`uv run pytest -v`).

## 2026-09-13 — Site v0.7.0: App Posts, Full-Screen App Container & Dual AI/Mine Provenance (v0.7.0)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"wow bump the version up to .7 looking good."*
> - *"i want to make pipeline tools app post the featured post - each app needs a post I author, and then links to run in full screen mode, and links to github repo readme, hugging face space, other links. get these posts created if not aready created."*
> - *"make the pipeline-tool app run in full screen mode just like the other 2. explain approach issues. could also have a link to full app in spaces. where is all this configured for build? is it in the app blog post metadata? in apps directory config? also, fair to say that all apps going forward will mainly be AI authored so lets respect that providence, how about ai providence with me as author (2 icons would be great in this case but don't know how prevalent that use case is. I (mine) will author the app post, but ai does 95% (or 99%))"*
> - *"remove the "Interactive Application • Visual Media" from apps list, whatever that label is, remove it. app should list - providence icon, title (in the same smaller font we use for title in blog lists, seems like the same header level would be used)."*
> - *"we need a photo/screen print for each app, probably in the app blog posting. i assume every post can have a default photo and maybe thumbnail used for various display purposes. thow in screen shots for each of the 3 apps in their initial posts."*
> - *"remove all the padding between menu items, about should be much closer to home"*

### Problem & Diagnosis
1. **Featured Post Flexibility**:
   - The homepage Featured Post section (`theme/templates/index.html`) contained hardcoded summary text and did not dynamically update when new articles were published.
2. **Missing Editorial Posts for Applications**:
   - The three applications on the site (Pipeline Tools, Photo Viewer, and Keyword Explorer) lacked dedicated narrative articles in `content/posts/`.
3. **Full-Screen Pipeline Tools Container**:
   - Photo Viewer and Keyword Explorer run as standalone full-viewport (`100vw` $\times$ `100vh`) apps in `apps/`, while Pipeline Tools only had an in-page 850px embed on `pipeline-tools.html`.
4. **Dual Provenance Attribution**:
   - The codebase lacked a mechanism to represent software generated by AI while curated and authored by Jim (`[AI]` + `[Mine]` dual icon display).
5. **Apps Hub Visual Clutter**:
   - The cards on `apps.md` had uppercase eyebrow labels (`Interactive Application • Visual Media`) and large 1.4rem titles that did not match the compact 1.05rem blog post list headers.

### Root Cause & Technical Analysis
- `index.html` hardcoded the paragraph text inside `<p class="post-teaser">` instead of binding to `{{ featured.summary }}`.
- Standalone applications are copied from `content/apps/` to `output/apps/` via `STATIC_PATHS` in `pelicanconf.py`. Pipeline Tools required a static wrapper HTML page to host the cloud backend iframe in full-viewport mode.
- `category_icon.html` only accepted a single category string without multi-badge flex layout.

### Solution & Standard Procedure
1. **Dynamic Featured Post**:
   - Bound the Featured Post description on `theme/templates/index.html` to `{{ featured.summary }}`.
   - Published `content/posts/pipeline-tools-workbench.md` dated `2026-09-13`, making it the active Featured Post on the homepage.
2. **Dedicated App Posts & High-Resolution Screenshots**:
   - Captured screenshots using Playwright to `content/images/`: `pipeline-tools-app.png`, `photo-viewer-app.png`, and `keyword-explorer-app.png`.
   - Created three markdown articles in `content/posts/` (`pipeline-tools-workbench.md`, `photo-viewer-drive-manifest-explorer.md`, and `keyword-explorer-taxonomy.md`) with semantic `<figure>`, `<img>` with `alt` text, `<figcaption>`, and direct action links.
3. **Full-Screen Pipeline Tools App (`content/apps/pipeline-tools/index.html`)**:
   - Created a standalone full-viewport wrapper with a 56px top app bar (`← Back to Apps`, title, Spaces link, GitHub link, App Post link) and 100% viewport iframe.
4. **Dual Provenance Icon Support**:
   - Updated `theme/templates/category_icon.html` with dual badge rendering (`AI` + `Mine`) when an article has AI category and Jim Collinsworth as author (or explicitly requests dual provenance).
   - Added `.category-badge.dual-badge` styling in `theme/static/css/style.css`.
5. **Apps Hub Header Streamlining**:
   - Removed eyebrow labels on `content/pages/apps.md`.
   - Replaced card titles with `[ICON] [TITLE]` rows using `1.05rem` font-sans headers matching blog list formatting.
   - Added direct navigation buttons to full-screen apps and app posts.
6. **Tightened Navigation Menu Item Spacing**:
   - Reduced `gap` on `nav.site-nav` from `1.25rem` to `0.15rem` and horizontal link padding from `0.55rem` to `0.25rem`.
   - Updated `margin-left` to `-0.25rem` to keep "Home" flush with site branding while bringing "About" immediately adjacent to "Home".
7. **Verification & Versioning**:
   - Bumped project version to `v0.7.0` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.
   - Passed all 51 automated tests in `pytest -v`.

## 2026-09-13 — Pipeline Tools App Page & Hugging Face Spaces Integration (v0.6.16)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"i recently updated pipeline-tools project to deploy to hugging face, so we have a version of the app up there to link to, and ideally embed into our apps pages. https://huggingface.co/spaces/jimcollinsworth/pipeline-tools. create a new apps page for this app and set things up so users can try it out right from my site. in this case the pipeline-tool app is not part of the site repo, it's external but still mine."*

### Problem & Diagnosis
1. **External Application Integration**:
   - Jim updated the external `pipeline-tools` project (`jimcollinsworth/pipeline-tools`, Stream: `Mine`) with a live deployment to Hugging Face Spaces.
   - The personal site lacked a dedicated app page and embed container allowing visitors to use the pipeline workbench directly from the site.
2. **Apps Hub Directory Completeness**:
   - The Apps hub (`content/pages/apps.md`) did not list Pipeline Tools alongside the Photo Viewer and Keyword Explorer.

### Root Cause & Technical Analysis
- The personal site operates under a strict zero client-side JavaScript policy for published content pages.
- Standard HTML `<iframe>` embedding cleanly isolates external client application execution without loading script tags on the parent page or violating test policies.

### Solution & Standard Procedure
1. **Dedicated Pipeline Tools Page**:
   - Created `content/pages/pipeline-tools.md` with Stream `Mine` attribution (authored by Jim Collinsworth).
   - Included technical overview, deployment links to Hugging Face Spaces and GitHub, and direct iframe embed of `https://jimcollinsworth-pipeline-tools.hf.space`.
   - Added breadcrumb navigation back to `apps.html`.
2. **Responsive Embed Container**:
   - Added `.app-embed-container` and `.app-embed-iframe` in `theme/static/css/style.css` (850px height on desktop, 650px on mobile/tablet).
3. **Apps Hub & Navigation Integration**:
   - Added a showcase card for Pipeline Tools in `content/pages/apps.md` and updated the architecture table.
   - Configured `theme/templates/base.html` to highlight the `Apps` navigation tab when viewing `pipeline-tools.html`.
4. **Verification**:
   - Rebuilt site with Pelican, verified all 51 automated tests passed, and bumped version to `v0.6.16`.

## 2026-09-13 — Desktop 2-Row/2-Column Layout & Menu Left Margin Alignment (v0.6.15)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"desktop view needs more content, it could be 2 column, side by side lists, or list (and page intro) on left and link stats/keywords, etc on right sidebar."*
> - *"and the left justification of the menu is annoying. don't like that jim, Home, horizontal bar and content don't line up. must be some solution for active/inactive menu, dropdown form to have consistent left margin, don't let menu jump around when toggling,"*
> - *"1 yes for menu in 2 line mode"*
> - *"2 yes keep dropdown as is for single line compact form"*
> - *"3 desktop content - 2 columns/2 rows. first row is page summary in column 1 and then stats/keyword selectors in column 2. then row 2 has tech in column 1 and arts, crafts, rest in col 2. can't have full width page into on desktop or landscape tablet, too wide. note the columns in the intro can be different (70/30) than for the links (50/50)"*
> - *"also it seems our desktop screen prints should be for much wider and higher resolution screens, go for a more realistic desktop monitor. the desktop now looks more like a tablet landscape, medium sized screen."*

### Problem & Diagnosis
1. **Left Margin Alignment Discrepancy**:
   - The site title ("Jim Collinsworth"), the 4px horizontal bar, and body headings/content begin flush at the left container boundary (`x = 0`).
   - In 2-line desktop navigation mode, menu items (`nav.site-nav a`) have `padding: 0.2rem 0.55rem`, causing the first label ("Home") to be inset by ~9px from the site title and content.
   - On mobile, `.intro-blurb` had `padding: 0.75rem`, causing the lead intro to be indented 12px relative to the site title and horizontal bar.
2. **Menu Toggling Horizontal Shift**:
   - Inactive menu links used `font-weight: 500`, while the active link used `font-weight: 600`. Switching tabs changed the character width of labels, causing subsequent links to shift horizontally.
3. **Desktop Content Density on Links Page**:
   - The Links page was rendered as a single narrow column, leaving unused whitespace on desktop displays.
4. **Desktop Screenshot Resolution**:
   - Screenshots were captured at 1280x800, resembling a landscape tablet rather than a standard 1920x1080 desktop monitor.

### Root Cause & Technical Analysis
- `nav.site-nav` lacked a negative margin offset to cancel out the first child's padding box.
- Dynamic font-weight toggling altered glyph bounding boxes across page loads.
- `links.md` lacked a responsive grid wrapper separating introduction, metadata, and topic categories.

### Solution & Standard Procedure
1. **Flush Left Navigation Alignment & Zero-Jump Toggling**:
   - Added `margin-left: -0.55rem;` to `nav.site-nav` in `theme/static/css/style.css`, aligning the first text label with the site title, 4px horizontal bar, and content.
   - Set uniform `font-weight: 600;` on all navigation links (`nav.site-nav a`), ensuring static character widths across active and inactive states.
   - Set `padding: 0;` on `.intro-blurb` across mobile and desktop.
   - Preserved single-line compact dropdown form on the right beside theme switchers for viewports under 768px.
2. **2-Row / 2-Column Responsive Layout for Links**:
   - Created `.links-intro-row` (70% / 30% grid on desktop/landscape) with intro summary in column 1 and a stats / keyword card in column 2.
   - Created `.links-grid-row` (50% / 50% grid on desktop/landscape) with technical/AI references in column 1 and arts, health & making links in column 2.
   - Preserved single-column stacking on mobile and tablet portrait viewports.
3. **High-Resolution Desktop Captures**:
   - Configured Playwright capture script to 1920x1080 resolution.
4. **Verification**:
   - Rebuilt site with Pelican, verified all 51 automated tests passed, and bumped version to `v0.6.15`.

## 2026-09-13 — Provenance Icon Title Prefix & Intro Arrow Link (v0.6.14)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"move the providence icon in recent links over to title prefix, should apply everywhere."*
> - *"change more about me to just -> or link icon"*

### Problem & Diagnosis
1. **Link Provenance Icon Positioning**:
   - In `Recent Links` (`theme/templates/index.html` and `content/pages/links.md`), the category provenance icon was not positioned as an inline prefix to the title, unlike `Recent Stream` and `Featured Post`.
2. **Intro Blurb Navigation Text**:
   - The homepage intro blurb ended with verbose text `More about me →` rather than a compact arrow link `→`.

### Root Cause & Technical Analysis
- `Recent Links` items previously used separate title and metadata blocks rather than a flex-aligned row matching `.post-header-row`.
- `style.css` lacked `.book-header-row`, `.book-header-left`, and `.book-header-right` selectors.

### Solution & Standard Procedure
1. **Unified Provenance Prefix Across All Links**:
   - Refactored `index.html` and `links.md` so that `Recent Links` items use `.book-header-row` with `.book-header-left` containing the `AI` provenance icon prefixing the title, and `.book-header-right` containing author (`AI`) and formatted date right-justified.
   - Updated `theme/static/css/style.css` to bind `.book-header-row`, `.book-header-left`, `.book-header-right`, and `.book-author` to the flex alignment rules.
2. **Compact Intro Arrow Link**:
   - Updated the homepage intro blurb to conclude with an arrow link to `about.html` (`&rarr;`) styled with class `.about-arrow`.
   - Added `.about-arrow` styling in `theme/static/css/style.css`.
3. **Verification**:
   - Built site with Pelican; passed all 51 automated tests (`pytest -v`). Captured responsive visual screenshots across desktop and 680px portrait.

## 2026-09-13 — Compact Blog Layout, Right-Justified Metadata & Header Refinements (v0.6.13)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"here are 3 widths potrait view, in one an extra line occurs, the menu should have switched to a single item."*
> - *"also the menu highlight in expanded line mode should probably be visually similar to the menu hightight in single item single line mode."*
> - *"for the blog list make the titles font smaller, it's highlighted already thats good. remove the text me, mine... just show the icons. I want the icon first then title, then type then date. ideally type and date are right justified. everything in same type face. remove brackets from type and no dots"*
> - *"for 'unknown author' must be ai providence"*
> - *"remove the 'all posts' 'all photos' and put small links next to the associated header. \"recent photos (->all)\""*
> - *"add icons to me, mine, ai...."*
> - *"and i see adjectives that are not supported, check these, check your rules to avoid unsupported in context terms."*
> - *"so close but replace ->all with just the word (ALL), underlined link. although a nice icon would be preferable if obvious."*
> - *"on featured post, don't need read full post since post title does that"*

### Problem & Diagnosis
1. **Header Wrapping on Medium Portrait Viewports**:
   - In portrait view at intermediate widths (~641px–768px), the 8 desktop navigation links and controls exceeded container width, wrapping controls onto a 3rd row.
2. **Nav Highlight Visual Disparity**:
   - Expanded desktop navigation used an inverted solid block highlight (`color: var(--bg); background-color: var(--text)`), which differed visually from the subtle rounded border badge used by the single-item dropdown button (`.mobile-nav-summary`).
3. **Blog List Metadata Density & Formatting**:
   - Post list titles were oversized (`1.25rem`–`1.45rem`).
   - Category badges displayed redundant text labels (`Me`, `Mine`, etc.) next to icons.
   - Metadata was rendered on a second line below the title with square brackets `[TYPE]` and bullet separators (`•`).
   - Placeholder author entries in `links.md` and `index.html` were labeled `Author Name` rather than attributed to the `AI` provenance stream.
4. **Header Inline Navigation vs. Section Bottom Links**:
   - Standalone bottom links (`View all posts →`, `Explore all photos →`, `Browse all links →`) consumed vertical space. The initial `(→all)` syntax contained an arrow symbol rather than an underlined clean word link.
5. **Redundant Post Link on Featured Post**:
   - `Read full post →` duplicated the action already performed by clicking the featured post title.
6. **Missing Category Icons in Documentation**:
   - `content/pages/about.md` listed streams as plain bullet text without their corresponding SVG icons.
7. **Rule 18 Adjective Compliance**:
   - Evaluative modifiers ("multi-disciplinary maker", "masterclass", "dramatic", "completely") were present in templates and posts.

### Root Cause & Technical Analysis
- The `@media (max-width: 640px)` media query did not cover tablet portrait widths (641px–768px), causing desktop nav to activate before there was sufficient width to host all 8 items and controls on one row.
- Post titles and metadata lacked flex alignment to anchor `[ICON] [TITLE]` to the left and `[TYPE] [DATE]` to the right.

### Solution & Standard Procedure
1. **Header Breakpoint Adjustment**:
   - Updated the compact navigation breakpoint in `style.css` from `max-width: 640px` to `max-width: 768px`, ensuring portrait viewports up to 768px use the single-item dropdown button and keep the header on a single row.
2. **Harmonized Navigation Highlight**:
   - Replaced solid black active block in `style.css` with subtle border, `var(--bg-subtle)`, and rounded 6px corners matching `.mobile-nav-summary`.
3. **Blog List Flex Reordering**:
   - Implemented `.post-header-row`, `.post-header-left` (`[ICON] [TITLE]`), and `.post-header-right` (`[TYPE] [DATE]`, right-justified).
   - Removed brackets from type and removed bullet dots across `index.html`, `archives.html`, `category.html`, and `article.html`.
   - Scaled down `.post-title` font size to `1.05rem` in `var(--font-sans)`.
   - Removed `<span class="category-label">` from `category_icon.html` to render pure accessible SVG icons.
4. **AI Provenance Attribution**:
   - Attributed placeholder entries in `links.md` and `index.html` to the `AI` provenance stream with `icon-ai` badge.
5. **Inline Section Header Links**:
   - Replaced bottom links with inline `(ALL)` links next to `Recent Stream`, `Photo Spotlight`, and `Recent Links` `<h2>` headings, styled with `text-decoration: underline`.
6. **Featured Post Cleanup**:
   - Removed redundant `Read full post →` paragraph from featured post on `index.html`.
7. **Category Icons on About Page**:
   - Added SVG category icons to `Me`, `Mine`, `AI`, `Ours`, and `Theirs` in `content/pages/about.md`.
8. **Rule 18 Audit**:
   - Removed ungrounded adjectives and evaluative modifiers across `index.html`, `about.md`, `about-this-site.md`, `ai.md`, `apps.md`, and content posts.
9. **Automated Verification & Versioning**:
   - Recompiled Pelican site (`uv run pelican content -s pelicanconf.py -o output -d`).
   - Ran test suite (`uv run pytest -v`): all 51 tests passed.
   - Bumped version to `0.6.13` across `pyproject.toml`, `about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

---

## 2026-09-13 — Prompt History Mine Attribution & Steering Dialog Streamlining (v0.6.12)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"how do we do google site verification (or is it on now?) and keeping with no javascript. what google tracking services can we use, or someone else? create a ticket for future, might need a touch of js eventually."*
> - *"the output doc view is limited to half the screen, should be full width."*
> - *"on site prompts, make my prompts simple full width text and they are the start/primary part, then cut way back on the llm response length, make prompts and responses more equal in length, cut out all the extra formatting, quoting, KISS"*
> - *"add the mine attribution and 'jim' to the prompts. merge and publish"*

### Problem & Diagnosis
1. **Missing Authorship & Provenance Attribution**:
   - The prompt history page lacked provenance attribution associating Jim's direct steering prompts with the `Mine` content stream.
   - The prompts lacked explicit identification of the author (`Jim`), making the dialogue structure ambiguous.
2. **Google Tracking & Verification Clarity**:
   - Needed clarification regarding whether Google site verification was active and zero-JS compliant.
   - Required documenting tracking options (zero-JS search console vs. minimal-JS analytics) in a dedicated tracking issue.
3. **Verbose Formatting on Prompt Timeline**:
   - Initial timeline implementation used heavy blockquotes, italics, quotes, and long diagnostic problem lists.

### Root Cause & Technical Analysis
- In `content/pages/prompt-history.md`, omitting `category: "Mine"` frontmatter failed to categorize Jim's human guidance under the site's documented provenance model (`about.md`).
- Prefixing prompts with `**Jim (Mine):**` directly identifies the human author and provenance stream, creating a balanced dialog against `**Response:**`.

### Solution & Standard Procedure
1. **Provenance Attribution & Dialog Labeling**:
   - Configured `category: "Mine"` and `author: "Jim Collinsworth"` in `content/pages/prompt-history.md` frontmatter.
   - Added `(Stream: Mine • Author: Jim Collinsworth)` in page intro.
   - Added `**Jim (Mine):**` label to each prompt block in `tools/sync_dev_prompts.py`.
2. **KISS Formatting & Balanced Length**:
   - Rendered prompts as full-width paragraphs without blockquotes or wrapping quotation marks.
   - Reduced LLM responses to concise 2–3 item action lists derived from milestone solutions.
3. **Google Analytics & Tracking Architecture**:
   - Confirmed active zero-JS Google verification via `content/extra/googledaf3f946832f8abf.html` -> `output/googledaf3f946832f8abf.html`.
   - Created GitHub Issue #10 to track zero-JS and minimal-JS analytics evaluation.
4. **Verification & Deployment**:
   - Recompiled Pelican site (`uv run pelican content -s pelicanconf.py -o output -d`).
   - Ran automated test suite (`uv run pytest -v`): all 51 tests passed.
   - Bumped version to `0.6.12` across `pyproject.toml`, `content/pages/about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

---

## 2026-09-13 — Root Build Artifact Removal, Directory Organization & Nikola Cleanup (v0.6.11)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"looking at repo file organization, seems like we have too much in the root but i'm not sure. why is there html in root, shouldn't all the built site content be in it's own directory?"*
> - *"where do the source posts and pages go (all the markdown from obsidian), seems like there are a couple locations in the repo."*
> - *"we have old doit files from previous nikola implementation, delete these and any other files not used, google? do this as a fix branch"*

### Problem & Diagnosis
1. **Root Directory Clutter & Redundant HTML**:
   - The repository root contained 37 obsolete files and directories from early build workflows: `index.html`, `about.html`, `posts.html`, `links.html`, `ai.html`, `photos.html`, `apps.html`, `about-this-site.html`, `prompt-history.html`, `contact.html`, `googledaf3f946832f8abf.html`, `category/`, `posts/`, `images/`, `assets/`, `.nojekyll`, `favicon.ico`, and `favicon.svg`.
   - These files were generated when Pelican was originally run with output directed to the repository root (`pelican -o .`), before CI/CD began deploying strictly from `output/`.
2. **Ambiguity Over Source Markdown Locations**:
   - Source Markdown files were present across multiple paths: `content/posts/`, `content/pages/`, `archive/content/`, `docs/`, and `releases/`.
3. **Legacy Nikola / Doit Traces**:
   - Residual references to Nikola builds (`nikola-baseline-build/` in `.gitignore`) and duplicate verification tokens (`googledaf3f946832f8abf.html`) remained in the repository root.

### Root Cause & Technical Analysis
- In the original deployment configuration prior to automated GitHub Actions (`.github/workflows/deploy.yml`), Pelican compiled to the repository root so GitHub Pages could serve files from the root directory.
- With modern GitHub Actions Pages deployment (`actions/upload-pages-artifact@v3 (path: 'output')`), all compiled assets are generated strictly into `output/` and tested in `output/`. The HTML and directory copies in the repository root were orphaned build artifacts.
- The Google Search Console file (`googledaf3f946832f8abf.html`) and favicons reside in `content/extra/` and are mapped via `pelicanconf.py`'s `EXTRA_PATH_METADATA` directly into `output/`. The copies in root were unneeded duplicates.
- Canonical content source locations:
  - `content/posts/`: Active Markdown posts and essays authored by Jim or created from Obsidian.
  - `content/pages/`: Active standalone pages (`about.md`, `about-this-site.md`, `apps.md`, etc.).
  - `archive/content/`: Inactive historical notes from the pre-Pelican Nikola era.

### Solution & Standard Procedure
1. **Branch & Staged Cleanup**:
   - Created dedicated fix branch `fix/repo-cleanup`.
   - Removed 37 stale build artifacts, redundant root HTML files, duplicate image directories (`images/`, `assets/`), and obsolete build intermediates via `git rm -r -f`.
2. **Source of Truth Confirmed**:
   - Verified that all active Obsidian Markdown content resides in `content/posts/` and `content/pages/`.
   - Confirmed Google verification token resides in `content/extra/googledaf3f946832f8abf.html` and compiles directly into `output/googledaf3f946832f8abf.html`.
3. **Legacy Traces Removed**:
   - Removed `nikola-baseline-build/` from `.gitignore`.
4. **Verification & Version Synchronization**:
   - Recompiled Pelican site (`uv run pelican content -s pelicanconf.py -o output -d`).
   - Ran complete automated test suite (`uv run pytest -v`): all 51 tests passed.
   - Synchronized prompt tracking with `tools/sync_dev_prompts.py` (46 prompts across 16 milestones).
   - Bumped version to `0.6.11` across `pyproject.toml`, `content/pages/about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

---

## 2026-09-13 — Prohibition of Ungrounded Adjectives & Fluff Removal (v0.6.10)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"why is the 375px image so large and fonts so big, hard to compare to other screen shots."*
> - *"here is some site text you generated 'This site is an intentionally simple, durable personal web space. It has been built with an uncompromising commitment to long-term digital sustainability, reading comfort, and clean engineering' it is a great example of the type of content i never want created. absolutely none of the adjectives, superlatives like 'intentionally simple, durable, uncompromising, digital sustainability, clean engineering' none have any basis, from now on do not use adjectives, adverbs without direct evidence and support for each specific word. incorporate this rule into agents.md. lets get this rule correct, quiz me first on how you interpret and implement"*
> - *"option 1a is fine, no fluff there just facts, data, and option and option 2a for sure."*
> - *"create a branch for fluff-removal, remove all fluff from all content in the site unless you know it was directly authored by me, shouldn't me much at all."*

### Problem & Diagnosis
1. **Unsubstantiated Modifiers & Marketing Fluff**:
   - The agent generated text in `README.md` and page intros containing ungrounded adjectives and buzzwords ("intentionally simple", "durable", "uncompromising commitment", "digital sustainability", "clean engineering").
   - These subjective qualifiers lack empirical basis, detracting from the factual tone of the site.
2. **Device Screenshot Magnification Distortion**:
   - A 375px phone portrait capture scaled up to 100% container width in markdown rendered at ~200% magnification, while a 1280px desktop capture was scaled down to ~60%, creating false size comparisons.

### Root Cause & Technical Analysis
- LLMs tend to introduce evaluative modifiers to convey quality rather than stating direct facts.
- A strict rule of direct evidence ensures that modifiers are prohibited unless supported by empirical, verifiable measurements (e.g., "zero client-side JavaScript", "51 passing unit tests", "3px solid line").
- The rule applies across all project files, governance documents, templates, commit messages, and agent chat communications.

### Solution & Standard Procedure
1. **Codified Section 18 in AGENTS.md & .agents/agent_rules.md**:
   - Formally instituted Section 18 prohibiting ungrounded adjectives, adverbs, superlatives, and marketing fluff without direct verifiable empirical evidence.
2. **Site-Wide Fluff Scrubbing**:
   - Replaced flagged text in `README.md` with factual Option 1A text: *"jimcollinsworth.github.io is Jim Collinsworth's personal website and journal, built using the Pelican static site generator with HTML5 and CSS, containing zero client-side JavaScript."*
   - Scrubbed ungrounded adjectives across `README.md`, `content/pages/about-this-site.md`, `content/pages/apps.md`, `content/pages/ai.md`, `tools/sync_dev_prompts.py`, `templates/obsidian-post-template.md`, and historical problem statements in `JOURNAL.md`.
   - Verified that Jim's authentic prose and posts were preserved untouched.
3. **Automated Verification & Sync**:
   - Rebuilt Pelican static site and confirmed 51/51 pytest suites pass.
   - Synchronized `content/pages/prompt-history.md` (43 total steering prompts across 15 milestones).
   - Bumped project version to `0.6.10` across `pyproject.toml`, `content/pages/about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

---

## 2026-09-13 — Tightened Header Spacing, Compact Active Nav & Segmented Controls (v0.6.9)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"no but remove menuitem from the template if we don't realy use it."*
> - *"on site page (and all pages) there is too much vertical spacing in the header, reduce spacing above, between and below, should be pretty tight with the grey bar. Make the selected highlight on menu items shorter, don't need all that padding and margins."*
> - *"on home page in phone profile view the menu dropdown and theme icons don't look quite integrated with the line, need to remove spacing under, get the theme icons closer together looking like a unit (maybe a very very subtle background group (but don't add any physical spacing)"*

### Problem & Diagnosis
1. **Excessive Vertical Spacing in Header**:
   - The desktop header had wide vertical gaps: 2.5rem body top padding, 0.85rem branding margin, 1.5rem header bottom padding, and 3.0rem header bottom margin.
   - The active navigation highlight pill had tall top/bottom padding and a 38px min-height on desktop, making it feel bulky and oversized relative to the editorial type.
2. **Mobile Portrait (< 640px) Integration**:
   - In phone portrait mode, the `.mobile-nav-summary` dropdown and theme switcher buttons (`.control-btn`) floated with excess space above the 3px grey horizon line.
   - The theme/contrast/text-size buttons appeared as disparate floating icons rather than a unified, integrated control capsule.
3. **Template & Menu Cleanup**:
   - `templates/obsidian-post-template.md` had an unused section for standalone page menu settings (`menu: true`, `menu_order`, `menu_title`).
   - `theme/templates/base.html` contained redundant fallback loops checking for `p.menu` on pages when navigation is centrally and reliably defined in `MENUITEMS`.

### Root Cause & Technical Analysis
- The generous Bear Blog-inspired padding (2.5rem–3.0rem) created too much dead space above and below the horizontal border bar, pushing the content too far down the fold.
- Desktop navigation links do not require a 38px touch target; a compact 0.12rem 0.55rem padding with a 1.2 line-height yields a crisp ~24px pill that hugs the text comfortably. (Mobile dropdown links retain `min-height: 38px` to maintain WCAG 2.5.5 touch target compliance).
- Grouping `.site-controls` into a cohesive segmented capsule (`background-color: var(--bg-subtle); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 1px; gap: 1px;`) creates a single tactile unit that visually balances the `.mobile-nav-summary` dropdown on mobile portrait and sits flush on the horizon line without consuming extra horizontal space.

### Solution & Standard Procedure
1. **Tightened Header Spacing**:
   - Desktop `body`: `padding: 1.25rem 2rem 3rem;` (was 2.5rem). Supersize `body`: `1.5rem 3rem 4rem;`. Tablets: `1.25rem 1.75rem 2.5rem;`. Mobile portrait: `0.85rem 1rem 2rem;`.
   - `.site-branding`: `margin-bottom: 0.35rem;` (was 0.85rem).
   - Desktop `header.site-header`: `padding-bottom: 0.45rem; margin-bottom: 1.5rem;` (was 1.5rem / 3.0rem).
   - Mobile `header.site-header`: `padding-bottom: 0.35rem; margin-bottom: 0.85rem;` (was 0.65rem / 1.25rem).
2. **Compact Navigation Highlight Pill**:
   - `nav.site-nav a` (desktop): Removed `min-height: 38px;`, set `padding: 0.12rem 0.55rem; line-height: 1.2;`.
   - Active state `nav.site-nav a[aria-current="page"], nav.site-nav a.active`: `padding: 0.12rem 0.55rem;` with reversed contrast pill.
3. **Integrated Segmented Control Capsule**:
   - `.site-controls`: Grouped as a segmented unit with subtle border and background (`gap: 1px`, `background-color: var(--bg-subtle)`, `border: 1px solid var(--border-subtle)`, `border-radius: 6px`, `padding: 1px`).
   - `.control-btn`: Tightened to `25px x 25px` square buttons (`border: none;`), harmonizing with the `.mobile-nav-summary` dropdown.
4. **Template & Menu Simplification**:
   - Removed Section 7 (`STANDALONE PAGE MENU SETTINGS`) from `templates/obsidian-post-template.md`.
   - Cleaned `theme/templates/base.html` to drive desktop and mobile navigation purely from `MENUITEMS`.
5. **Testing, Synchronization & Versioning**:
   - Synchronized `assets/css/style.css` to `theme/static/css/style.css` and `theme/css/style.css`.
   - Verified 51/51 pytest tests pass cleanly via `uv run pytest -v`.
   - Recompiled static site via `uv run pelican content -s pelicanconf.py -o output -d`.
   - Bumped project version to `0.6.9` across `pyproject.toml`, `content/pages/about-this-site.md`, `JOURNAL.md`, and `PLANNING.md`.

---

## 2026-09-13 — Pelican Conventions Rule, Optional Summary & Menu Architecture (v0.6.8)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"nope don't need summary, want to follow pelican conventions if possible (make an agents.md rule)"*
> - *"can a blog post be a menu? do the custom pages (about.md) have a menu:true"*

### Problem & Diagnosis
1. **Adherence to Official Pelican Conventions vs. Custom Abstractions**:
   - Rather than introducing custom alias layers (e.g. mapping `description` to `summary`), Jim directed that the site strictly follow official Pelican conventions.
   - In Pelican, `summary` is optional in content files: Pelican automatically truncates the article body (first 50 words / first paragraph) when `summary:` is omitted.
   - Jim requested an explicit governance rule in `AGENTS.md` to codify this architectural standard.
2. **Menu Architecture Clarity**:
   - Jim asked whether custom pages like `about.md` have `menu: true` in their frontmatter, and whether a blog post can be in the navigation menu.

### Root Cause & Technical Analysis
- `content/pages/about.md` and other core pages do not have `menu: true` in their frontmatter; they appear in the top navigation because they are explicitly declared in the `MENUITEMS` tuple in `pelicanconf.py`.
- The `pages` loop in `theme/templates/base.html` exists as an automatic opt-in for *additional* standalone pages that set `menu: true` (and are not already listed in `MENUITEMS`).
- Any blog post (article) can be added to the navigation menu immediately via `MENUITEMS` in `pelicanconf.py` (e.g. for cornerstone essays, deep dives, or featured projects).
- Codifying Section 17 in `AGENTS.md` and `.agents/agent_rules.md` ensures LLM agents preserve Pelican's standard, unadorned conventions and avoid metadata bloat.

### Solution & Standard Procedure
1. **Rule Codification**:
   - Added Section 17 to `AGENTS.md` and synchronized `.agents/agent_rules.md`:
     - Mandatory adherence to standard Pelican conventions and built-in metadata keywords.
     - Optional summary policy: no requirement for manual `summary:` frontmatter.
     - Prohibition of redundant alias layers and metadata bloat.
2. **Template Update**:
   - Updated `templates/obsidian-post-template.md` to mark `summary` as `(Optional)` with a note explaining Pelican's automatic body text derivation.
3. **Menu Architecture Clarification**:
   - Documented the dual-tier menu system: `MENUITEMS` for permanent links (pages and articles), and `menu: true` for frontmatter-driven dynamic pages.
4. **Testing & Synchronization**:
   - Verified clean static compilation and 51/51 passing tests via `uv run pytest -v`.
   - Bumped project version to `0.6.8` across `pyproject.toml` and `about-this-site.md`.

---

## 2026-09-12 — Header Horizon Bar, Reversed Active Nav & Obsidian Post Template (v0.6.7)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"just the horizontal header bar below the menu, maybe a few pixels wider, basic grey for now. lets use something besides underline foemthe active menumitems sinsce that would conflict with the horizontal bar. maybe hightigt or reverse it, make it obvious."*
> - *"give me an obsidian template, has all the yaml field with comment and field values. can add it to the repo"*

### Problem & Diagnosis
1. **Nav Underline vs. Header Horizon Bar Conflict**:
   - The previous active navigation indicator used a colored bottom border (`border-bottom: 2px solid var(--link)`). Placing a horizontal bar below the header resulted in visually clashing parallel lines.
   - Jim requested a wider horizontal basic grey bar below the menu, and switching the active menu item from an underline to an obvious reversed highlight pill.
2. **Obsidian Authoring Frontmatter Ambiguity**:
   - Authoring posts in Obsidian required remembering or searching for frontmatter conventions (`type`, `previous_types`, `category`, `status`, `summary`, `tags`).
   - Jim requested an official, comprehensive Obsidian template file with all YAML fields, detailed field comments, and allowed values added directly to the repository.

### Root Cause & Technical Analysis
- A bottom border on an inline navigation link visually competes with a full-width header separator rule directly below it.
- Inverting the active link's colors (`background-color: var(--text); color: var(--bg) !important; font-weight: 600; border-radius: 4px; padding: 0.25rem 0.65rem; border-bottom: none;`) creates an unmistakable, modern pill button that works symmetrically in both light mode (dark charcoal pill with light text) and dark mode (cream/white pill with dark text).
- Removing `border-bottom` on all navigation links eliminates border jitter on hover and lets the 4px horizontal header bar (`--border-header: #b5b0a6` light / `#44494e` dark) serve as an unencumbered architectural horizon.
- In mobile screens (`< 640px` and phone landscape), the header bar scales gracefully to 3px to maintain compact vertical proportions, and the active dropdown item in `.mobile-nav-menu` matches the reversed pill style.
- Placing `templates/obsidian-post-template.md` at repository root provides a discoverable template file that Jim can open in Obsidian or copy without interfering with Pelican's build (Pelican only processes `content/posts` and `content/pages`).

### Solution & Standard Procedure
1. **CSS Token & Header Bar Styling**:
   - Added `--border-header: #b5b0a6` (light) and `--border-header: #44494e` (dark) to `:root` and `@media (prefers-color-scheme: dark)`.
   - Desktop `header.site-header`: `border-bottom: 4px solid var(--border-header);`.
   - Mobile portrait and phone landscape `header.site-header`: `border-bottom: 3px solid var(--border-header);`.
2. **Reversed Active Navigation Pill**:
   - `nav.site-nav a`: Removed bottom border; added `border-radius: 4px`, `min-height: 38px`, `padding: 0.25rem 0.65rem`, and hover background `var(--bg-subtle)`.
   - `nav.site-nav a[aria-current="page"], nav.site-nav a.active`: Reversed contrast pill (`color: var(--bg) !important; background-color: var(--text) !important; font-weight: 600; border-bottom: none;`).
   - `.mobile-nav-menu a[aria-current="page"]`: Matches reversed pill styling (`color: var(--bg) !important; background-color: var(--text) !important;`).
3. **Synchronized Theme Styles**:
   - Copied `assets/css/style.css` to `theme/static/css/style.css` and verified parity with `git diff --no-index`.
4. **Comprehensive Obsidian Post Template**:
   - Created `templates/obsidian-post-template.md` documenting:
     - Core metadata (`title`, `date`, `slug`)
     - Provenance categories (`Mine`, `Me`, `AI`, `Ours`, `Theirs`)
     - Format & evolution lifecycle codes (`NOTE`, `ESSAY`, `PROJ`, `VIEW`, `BOOK`, `TIL`, `SPEC`, `IDEA`, `WIP`, and `previous_types`)
     - Multi-label tags (`tags: [...]`)
     - Publishing states (`published`, `draft`, `hidden`)
     - Summary teaser, hero media, and page menu settings
     - Markdown starter layout with lede paragraph, section headings, semantic `<figure>` with `<figcaption>`, callouts (`> [!NOTE]`), and code blocks.
5. **Testing & Verification**:
   - Executed `uv run pelican content -s pelicanconf.py -o output -d`.
   - Ran `uv run pytest -v` (51/51 tests passing, including touch target and ARIA checks).
   - Generated full 16-screenshot responsive suite via `tools/screenshots.py`.
   - Bumped site version to `0.6.7` across `pyproject.toml` and `about-this-site.md`.

---

## 2026-09-12 — Color Flair & Photo Border Architectural Design (Issue #6)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"after that do ticket 6 add a touchnofmcolor flair, but just design and a few potential screen shots, document in the issue ticket"*
> - *"try more spatial variations not colors, linesmthinner, sides only, top only, lookmforminspiration, just a splash, colors from,my photos, nature."*
> - Ticket #6 Text: *"Time to add some color to the website. Want to use colors from underlying photos of the sky and paint strokes. On most pages I think just a simple 10 pixel colored border around the entire page. 10 is a guess, we can try different sizes, even fir different resolutions or orientation. Border can be wider on bigger displays. Use build tool to create smal patches from my photos which are then used as background for the screen border. Click on the boarder to jump to full screen photo. Can do one specific photo first, but then code in some variations. Underlines in matching color of use patch? For photo rich pages we go to a basic Grey border."*

### Problem & Diagnosis
1. **Color Flair Requirement**:
   - Jim directed introducing color flair drawn directly from his Chicago sky and Lake Michigan photography without introducing visual clutter.
2. **Zero-JavaScript "Click Border to View Full Photo" Requirement**:
   - Jim requested that clicking anywhere on the screen border jump directly to the full-screen photo. With Rule 3 disallowing client-side JavaScript, this was solved via HTML5 and CSS without interfering with text selection, links, or scrolling.
3. **Context-Aware Photo Page Neutrality**:
   - On photo-rich pages like `photos.html`, a colored border risks clashing with photos. These pages switch to a basic neutral grey border.

### Root Cause & Technical Analysis
- Color sampling directly from image files (`content/images/sky-twilight.jpg`, `sky-lakefront.jpg`, `sky-clouds.jpg`) yields authentic palette coordinates: Sunset Fire Amber (`#d64900`), Dawn Peach (`#ed8a77`), Lakefront Cerulean (`#23496d`), Twilight Ember (`#e28743`).
- A traditional single-element border cannot trigger navigation to a URL in pure HTML/CSS without JavaScript. However, a semantic 4-edge `<aside>` perimeter containing 4 fixed edge links (`.edge-top`, `.edge-bottom`, `.edge-left`, `.edge-right`) with `z-index: 9999` and descriptive `title` tooltips enables clicking any border edge to navigate directly to the photo.
- The inner reading canvas remains completely unobstructed, so page scrolling, clicking links, and selecting text behave normally.
- By scoping border thickness responsively (`8px` mobile, `10px–12px` tablet, `14px–16px` desktop), mobile screens preserve critical reading space while desktop screens gain a confident framing.

### Solution & Prototypes Created
1. **Palette Extraction**:
   - Developed `scratch/extract_colors.py` using Playwright Canvas sampling to compute RGB/Hex averages for sky, horizon, and water bands across Jim's photos.
2. **Prototypes Evaluated**:
   - **Initial 4-Sided Borders**: Sunset Fire Amber (`#d64900`), Lakefront Cerulean (`#23496d`), Photo-Patch texture, Dark Mode Twilight Ember (`#e28743`), Neutral Grey (`#808387`).
   - **Spatial Variations & Thinner Lines (Jim's Direction)**:
     - *Top Only (3px)*: Panoramic horizon gradient (Lake blue to sunset amber) pinned to viewport top. 0px content disruption.
     - *Sides Only (3px)*: Dual vertical rails in Lake Michigan Cerulean (`#23496d`), leaving top and bottom open.
     - *Left Spine Only (4px)*: Asymmetric vertical bookbinding/journal rail in Marigold Amber (`#d77400`, from `flower-macro.jpg`).
     - *Header Splash Rule (3px)*: Natural horizon rule beneath site header separating navigation from editorial prose.
     - *Corner Splash (3px)*: Top-left L-bracket registration notch.
3. **Harmonic Link Underlines**:
   - Text hyperlinks inherit `text-decoration-color: var(--flair-color)`, tying inline copy visually to the perimeter frame.
4. **Documented in GitHub Issue #6**:
   - Detailed architectural design, CSS specifications, zero-JS markup, and prototype findings posted directly to GitHub Issue #6 via the GitHub API (HTTP 201 Created).
   - Production code unchanged pending Jim's review and approval.

---

## 2026-09-12 — Verbatim Dev Prompts Timeline & Automated Milestone Sync (Issue #7)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"go ahead and do issuem#7 dev prompts but not the haiku part, just the shift to simple prompt text. after that do ticket 6 add a touchnofmcolor flair, but just design and a few potential screen shots, document in the issue ticket"*
> - Ticket #7 Text: *"It's all about the prompts, i want to show the entire and ongoing prompt history. That created this site. Take the journal file, maybe screenshot, and create a development blog kind of a devops, design, testing narrative with jim directing the action. Promps can be shortened domd where there were long includes but try to preserve Jim's wording, also shiw context and result of each significant interaction... You probably need to enhance the process to create History on a per session what per release basis. We'd only have to look at the newer part of the journal and create a new post based on that release and all the prompts. More scalable"*

### Problem & Diagnosis
1. **Artificial Ornamentation & Missing Authentic Steering**:
   - The initial prompt history timeline included AI-generated haikus and decorative cards ("AI slop") rather than Jim's authentic, verbatim prompts.
   - Recent releases (v0.6.0 through v0.6.5) and critical steering moments (remediations, corrections, agent errors) were missing from the public timeline.
2. **Manual Maintenance Overhead**:
   - Adding prompts manually to `prompt-history.md` was error-prone and unscalable across frequent milestones.

### Root Cause & Technical Analysis
- `JOURNAL.md` already captures Jim's exact instructions and steering under `> [!NOTE] Jim's Prompts, Instructions & Steering:` callouts.
- A deterministic build tool can parse `JOURNAL.md` by release milestone, extract every steering prompt verbatim, summarize the engineering challenge and agent errors factually, and generate clean Markdown.

### Solution & Standard Procedure
1. **Automated Extraction Tool (`tools/sync_dev_prompts.py`)**:
   - Developed a Python CLI tool that parses `JOURNAL.md` milestone headers, callouts, and technical analysis.
   - Formats milestones chronologically (v0.1.0 through v0.6.5) with authentic prompt blockquotes and concise DevOps context.
   - Sanitizes HTML tags (`<script>`, `<img>`, etc.) into escaped code literals to prevent accessibility or Zero-JS test failures.
2. **Simplified Plaintext Typography**:
   - Completely eliminated haikus and heavy CSS card layouts from `content/pages/prompt-history.md`.
   - Clean editorial typography with blockquotes and monospace metadata badges (`v0.6.5 • 2026-09-12`).
3. **DevOps Dashboard Integration**:
   - Added a 6th card to `content/pages/about-this-site.md`: **Steering Prompts: 29 Prompts →** linking to `/prompt-history.html`.
4. **Documented in GitHub Issue #7**:
   - Posted complete status report comment to GitHub Issue #7 via GitHub API (HTTP 201 Created).

---

## 2026-09-12 — Dynamic Mobile Dropdown Menu in Portrait Mode (Release v0.6.5)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"an improvement but need the dynamic menu in portrate mode thats possible right?"*

### Problem & Diagnosis
1. **Multi-Row Header Wrapping in Mobile Portrait**:
   - On physical smartphones in portrait orientation (360px–414px width), 8 separate navigation links (`Home`, `About`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`) could not fit on a single line, wrapping across 3–4 rows and pushing the page content down.
2. **Zero-JavaScript Constraint**:
   - In accordance with site technical principles (Rule 3: Zero JavaScript), client-side JavaScript or `<script>` toggles are strictly forbidden. The dynamic dropdown menu must function using native HTML5 `<details>` and CSS.

### Root Cause & Technical Analysis
- Mobile portrait layout attempted to display all horizontal menu links simultaneously.
- Standard HTML5 `<details>` and `<summary>` elements provide native browser disclosure functionality without client-side scripts, with accessibility baked in by default.
- Jinja2 template logic with `namespace` can resolve the current active section (`Home`, `About`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`, or `Menu`) and render it dynamically inside the `<summary>` element.

### Solution & Standard Procedure
1. **Semantic HTML5 `<details>` & `<summary>` Integration**:
   - In `theme/templates/base.html`, added `<details class="mobile-nav-dropdown">` alongside `<nav class="site-nav desktop-nav">`.
   - Populated `<summary class="mobile-nav-summary">` with dynamic Jinja2 `ns.active_title` and an inline SVG chevron.
   - Chevron rotates 180 degrees smoothly on open via CSS `transform: rotate(180deg)`.
2. **Strictly Single-Row Mobile Portrait Header**:
   - Changed `header.site-header` in `@media (max-width: 640px)` to `display: flex; flex-direction: row; justify-content: space-between; align-items: center;`.
   - Aligned `Jim Collinsworth` on the far left, and grouped `[ Current Page ▾ ]` with `🌙 ◑ A` on the right.
   - Completely eliminated multi-row wrapping on portrait screens down to 320px width.
3. **Floating Navigation Menu Card**:
   - Absolutely positioned `.mobile-nav-menu` under the dropdown button with `var(--bg-card)`, subtle border, and shadow.
   - Touch targets meet WCAG 2.1 AAA accessibility with `min-height: 38px`.
   - Full support for dark mode and high-contrast mode.
4. **Responsive Mode Separation**:
   - On Desktop (> 640px): `.desktop-nav` is visible, `.mobile-nav-dropdown` is hidden (`display: none;`).
   - On Phone Landscape (< 500px height): `.desktop-nav` is visible on one line, `.mobile-nav-dropdown` is hidden (`display: none !important;`).
   - On Phone Portrait (< 640px): `.desktop-nav` is hidden (`display: none !important;`), `.mobile-nav-dropdown` is visible (`display: inline-flex !important;`).
5. **Automated Verification**:
   - Added `test_mobile_dynamic_dropdown_portrait` and `test_navigation_mode_switching_by_viewport` in `tests/test_playwright_responsive.py`.
   - Verified all 51 automated tests passing.
   - Bumped version to `v0.6.5` across `pyproject.toml`, `about-this-site.md`, and `releases/v0.6.5.md`.

---

## 2026-09-12 — Compact Mobile Header, Streamlined Dates & Dense Post Listings (Release v0.6.4)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"getting close buy phone is,still too packed. on landscape mode fully half the screen ismwasted for the header, must be one line max for phone, can hide out of my lane if needed on small devices. should be a dynamic hiding menu at some point and justmshow current menu name, withmdrop down."*
> - *"on posts and list remove the evolved from til. thismwill be available only thu the metadata display. change dates to month year, so Aug 26 or Sep 23.  i dont really like the [view] vs just view, table for futuremdiscussion"*
> - *"phone content should be smaller, only short post text and minimal spacing in lists, ideally 1, 2 lines max"*
> - *"and then merge push and publish"*

### Problem & Diagnosis
1. **Header Real Estate on Landscape Phone**:
   - Jim provided live mobile photos demonstrating that in landscape mode, the multi-row header (`Jim Collinsworth` + `Out of My Lane` row, followed by navigation links + controls, plus 4.5rem margin/padding) consumed more than half the vertical screen height (~200px of a 390px viewport), leaving minimal space for content.
   - In portrait mode, navigation wrapped `Site` to line 3 and controls to line 4.
2. **Post Evolution Lineage**:
   - `(evolved from TIL)` rendered prominently in article headers, creating clutter. Jim directed removing this from the visual post headers and lists, preserving it strictly in the metadata.
3. **Date Verbosity**:
   - Full date formats (`August 14, 2026` or `Aug 14, 2026`) occupied excessive horizontal width on mobile. Jim requested concise Month Year format (`Aug 26`, `Sep 23`).
4. **Mobile Content & List Spacing**:
   - Post list items had generous desktop margins (2.25rem) and full paragraph descriptions, meaning only 1 item fit on screen at a time on mobile.

### Root Cause & Technical Analysis
- Header structure placed `.site-branding` and `.site-nav-row` as vertical block flex items, preventing single-line flow on wide horizontal viewports like landscape phones.
- Mobile breakpoints lacked specific line-clamp constraints on `.post-desc` and had identical margins to desktop.
- `strftime('%b %y')` provides clean, standard 2-digit year representations matching Jim's concise format.

### Solution & Standard Procedure
1. **Single-Line Header on Phone Landscape**:
   - Configured `@media (orientation: landscape) and (max-height: 500px)` with `header.site-header { display: flex; flex-direction: row; justify-content: space-between; align-items: center; }`.
   - Hidden `.site-tagline` on mobile and landscape phones.
   - Header height reduced to under 45px total (saving >150px of vertical space).
2. **Compact 2-Row Grid on Phone Portrait**:
   - Used `display: contents` on `.site-nav-row` to place title and controls on row 1, with navigation links cleanly spanning row 2.
3. **Streamlined Dates**:
   - Updated Pelican Jinja2 templates (`article.html`, `archives.html`, `category.html`, `index.html`) to format dates as `{{ article.date.strftime('%b %y') }}`.
4. **Evolution Lineage Removal**:
   - Removed `(evolved from ...)` from `article.html` and verified absence in all lists.
5. **Dense Mobile Post Listings**:
   - Applied `-webkit-line-clamp: 2` to `.post-desc`, `.book-notes`, and `.post-teaser` on mobile (< 640px).
   - Reduced item spacing to `0.75rem` with subtle border separators.
6. **Automated Testing & Governance**:
   - Added `test_mobile_header_compact_and_landscape_single_line` and `test_streamlined_date_formats` to `test_playwright_responsive.py`.
   - Verified all 49 tests passing.
   - Tabled dropdown menu and `[VIEW]` vs `VIEW` for future milestones in `PLANNING.md`.
   - Bumped version to `v0.6.4` across `pyproject.toml`, `about-this-site.md`, and generated `releases/v0.6.4.md`.

---

## 2026-09-12 — Responsive Image Containment, Edge-to-Edge Photo Stream & Release v0.6.3

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"in photomalbumms the photosmproperly span the window, might even be able to remove left right padding for photos. but thempost on modern wing the photosmare full sized,,muchnwidermthan screen. inmgeneral they should fit to screen width"*

### Problem & Diagnosis
1. **Unconstrained Post Images**:
   - In posts like `art-institute-chicago-modern-wing.md`, full-resolution architectural photography (`sky-lakefront.jpg` at 2,108px wide) was rendered inside `<figure><img ...></figure>` without any max-width constraints.
   - On mobile viewports (e.g. 390px iPhone), this caused the page canvas to explode to 4,136px wide, causing massive horizontal scrolling, distorted responsive layouts, and unreadable text.
2. **Photo Album Padding**:
   - In photo albums (`photos.html`), photos scaled correctly within the container, but had default container/body left and right padding (1rem on phone, 1.75rem on tablet, 2rem on desktop). Jim suggested removing left/right padding for photo streams to allow photos to span the window edge-to-edge.

### Root Cause & Technical Analysis
- The CSS reset in `assets/css/style.css` defined box-sizing and html/body typography, but lacked standard fluid media reset rules (`img, picture, video, canvas { max-width: 100%; height: auto; }`).
- Individual `<figure>` and `<figcaption>` elements only had styles defined under `.photo-stream figure`, with no base rules for general editorial figures in articles.
- On portable screens (< 1024px), `.photo-stream` can break out of container padding via negative margins (`margin-left: -1rem; margin-right: -1rem; width: calc(100% + 2rem)`), delivering immersive edge-to-edge photography while preserving caption alignment via matching caption padding.

### Solution & Standard Procedure
1. **Fluid Media Reset**:
   - Added `img, picture, video, canvas { max-width: 100%; height: auto; }` directly following the `body` declaration in `assets/css/style.css`.
2. **Base Figure & Caption Styling**:
   - Defined base styles for `figure` (`margin: 2.25rem 0; max-width: 100%;`), `figure img` (`width: 100%; max-width: 100%; height: auto; border-radius: 4px; border: 1px solid var(--border-subtle); display: block;`), and `figcaption` (`font-family: var(--font-sans); font-size: 0.88rem; color: var(--text-muted); line-height: 1.45;`).
3. **Edge-to-Edge Photo Stream**:
   - Added negative-margin breakout on mobile (< 640px) and tablet (< 1024px) for `.photo-stream`, removing left and right gutters for photos while applying matching padding to `figcaption` to maintain text alignment with headers.
4. **Automated Visual Regression Testing**:
   - Added `test_images_fit_viewport_width` to `tests/test_playwright_responsive.py`, validating both Modern Wing and Photo Album pages across phone and laptop viewports with zero horizontal overflow (`scrollWidth <= clientWidth`) and bounded image bounding boxes.
5. **Release & Synchronization**:
   - Updated test suite (all 47/47 tests passing), synchronized `assets/css/style.css` across theme files, updated `pyproject.toml` and `about-this-site.md` to `v0.6.3`, and wrote `releases/v0.6.3.md`.

---

## 2026-09-12 — 'Me' Category, Downlow Iconography, Configurable Menu & Release v0.6.2

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"we also have me as a category, this is stuff about me maybe written about me by me, maybe my fit bit data, or bookmarks"*
> - *"why are previews not available in the walkthrough comma check our screenshoting ability. make dure btowser testds sre running and checking screens."*
> - *"Certain pages will always appear in the menu like about, blog, any page or custom page can be made to appear in the menu by some sort of configuration setting whatever pelican supporsts."*
> - *"i like the new categories, but let's keep it on the downlow In our website. just mention in the about page, and that's it. no nav of lists. maybr try an icon next to posts, what would coukd tge icons be. But we will keep content categorized this way, me, mine, ours... Moving forward, it will figure out more uses of it in the future"*
> - *"We can simply call the category aI. Not ai generated."*
> - *"what is our icon library, theme? must bemsomembetter icons althoughmi like the svgs, find outmofficialmpelicanmthememicons ormgive me a few,to pick from."*
> - *"feather quill, use robot head instaed of sparkle"*

### Problem & Diagnosis
1. **Category Expansion & Naming**:
   - Jim required adding **`Me`** as a distinct category for autobiographical notes, personal biodata (Fitbit, sleep, health tracking), personal bookmarks, and things written about Jim by Jim.
   - The label `AI Generated` was overly verbose and needed simplification to **`AI`**.
2. **Category Presentation ("On the Downlow")**:
   - The previous release introduced prominent `.stream-nav` filter lists on archives and `STREAMS: Mine • Ours` in the footer. Jim directed that categories should remain "on the downlow" without visible navigation lists, while quietly categorizing content behind the scenes.
   - The taxonomy needed to be explained on [`content/pages/about.md`](about.html).
   - Posts needed subtle, unobtrusive visual indicators (icons) for category attribution without overwhelming the editorial typography. Jim explicitly selected a **feather quill** for `Mine` and a **robot head** for `AI`.
3. **Flexible Top Navigation Menu**:
   - Navigation needed permanent inclusion of core pages (`Home`, `About`, `Posts`), with the ability to configure or dynamically opt in any page or custom page (such as upcoming `tai-chi.md` or `music.md`) via Pelican configuration or Markdown frontmatter.
4. **Walkthrough Screenshot Preview Rendering**:
   - Image previews failed to render in walkthrough artifacts due to Windows backslash path escaping in the Antigravity webview markdown renderer.

### Root Cause & Technical Analysis
- In webviews, markdown image paths with Windows backslashes (`\`) are parsed as escape characters (e.g. `\U`, `\a`) and fail to resolve. Standardizing to `file:///C:/Users/...` forward-slashed URIs restores immediate preview rendering.
- Pelican's native `MENUITEMS` configuration in `pelicanconf.py` provides a clean tuple for permanent and configured menu items. Combining this with frontmatter inspection (`page.menu == True`) allows zero-code opt-in for any future Markdown page.
- Inline SVGs (13×13px) with `<title>` and `aria-label` allow category indicators to render identically across platforms with zero client-side JavaScript, no external font dependencies, and full screen-reader accessibility.
- Lucide / Feather icon SVGs (`feather` for quill and `bot` for robot head) provide crisp, semantic, minimalist line art matching our typography without adding external asset or font overhead.

### Solution & Standard Procedure
1. **Category Normalization (`pelicanconf.py`)**:
   - Configured `ObsidianMarkdownReader` to normalize `ai generated` &rarr; `AI`, and support `Me`, `Mine`, `AI`, `Ours`, `Theirs` (defaulting to `Mine`).
2. **Configurable Navigation Menu**:
   - Configured `MENUITEMS` in `pelicanconf.py` with `Home`, `About`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`.
   - Added `menu`, `menu_order`, and `menu_title` parsing to `ObsidianMarkdownReader`.
   - Updated `theme/templates/base.html` to dynamically render `MENUITEMS` plus any page marked `menu: true`.
3. **Downlow Presentation & Category Icons**:
   - Removed `.stream-nav` category lists from `theme/templates/archives.html` and `theme/templates/category.html`.
   - Removed `.footer-categories` from `theme/templates/base.html`.
   - Created `theme/templates/category_icon.html` macro rendering subtle 13×13px inline SVG icons for `Me` (👤 user outline), `Mine` (🪶 feather quill outline), `AI` (🤖 robot head outline), `Ours` (👥 dual users outline), and `Theirs` (❝ quotation marks outline).
   - Rendered category badges in `archives.html`, `index.html`, `category.html`, and `article.html`.
   - Styled `.category-badge` and `.category-icon` in CSS.
4. **Documentation & About Page**:
   - Added "Content Streams & Categorization" section to `content/pages/about.md`.
   - Updated Section 5 in `AGENTS.md` and `.agents/agent_rules.md`.
   - Updated `docs/content_authoring.md` and `PLANNING.md` (Milestone 16).
5. **Testing & Versioning**:
   - Updated test suites, verified all 43 tests passing (`uv run pytest -v`).
   - Bumped version to `v0.6.2` in `pyproject.toml`, `content/pages/about-this-site.md`, and `releases/v0.6.2.md`.

---

## 2026-09-12 — Provenance Categories (Mine, AI Generated, Ours, Theirs), Streams Navigation & Release v0.6.1

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"changing terminology a bit, too much emphasis currently on lanes. Really? All it should be is a possibility. Tagline, and then lanes are simply just pages like I have a page on tai. Chi and a page on music in those pages. We'll link too one or many posts based on some filtering criteria"*
> - *"remove most references to lanes, lanes are simply custom pages, we will have a tai chi page, with my tai chi posts, links and summary, and a science page... then we just need keywordsi think. where do the pelecan concepts fit again"*
> - *"what pelecan features utilize categories? how else could we use caregories? o mine, ours, theirs....futeur, present, past....private, public, draft"*
> - *"me like about, biodata, mine, ai generated, ours, theirs, lets go with those categories. ill also build custom pages for tai chi, music, big projects"*

### Problem & Diagnosis
1. **Over-Emphasis on Rigid "Lanes"**:
   - The site taxonomy had become overly preoccupied with artificial "lanes" categories (`AI`, `Art`, `Health`, `Making`, `Music`), creating category silos and complex multi-category hooks.
   - In Jim's authoring model, topic exploration belongs on dedicated, curated custom pages (e.g. a Tai Chi page, a Music page, a Science page, or Big Projects) that link to posts based on keyword tags and personal narrative context, rather than rigid category containers.
2. **Pelican Native Category Misalignment**:
   - Pelican’s core engine is architected around a single, mutually exclusive Category per article. Using Pelican categories for multi-topic assignment required custom generator mutation hooks.
   - Conversely, provenance and authorship (`Mine`, `AI Generated`, `Ours`, `Theirs`) is strictly mutually exclusive and canonical, making it the ideal 1:1 match for Pelican’s native category architecture.
3. **Tagline & Navigation Flow**:
   - Header tagline *"Out of My Lane"* previously linked to `/lanes.html`, emphasizing the lane taxonomy. It should instead point to the full chronological post stream (`/posts.html`).
   - Footer and archive headers displayed heavy `.lane-nav` and `.footer-lanes` bars that needed to transition to lightweight, unobtrusive stream selectors.

### Root Cause & Technical Analysis
- Mapping Pelican’s native category mechanism to provenance streams (`Mine`, `AI Generated`, `Ours`, `Theirs`) restores Pelican's clean out-of-the-box category indexing without needing generator monkey-patching or manual category list injection.
- Topical categorization is decoupled entirely into flexible tags (`tags: [...]`), allowing future custom pages (such as Tai Chi or Music) to query and link to any relevant posts regardless of category.
- Articles without an explicit `Category` frontmatter key default gracefully to `"Mine"`.

### Solution & Standard Procedure
1. **Pelican Configuration (`pelicanconf.py`)**:
   - Configured `CATEGORY_URL = 'category/{slug}.html'` and `CATEGORY_SAVE_AS = 'category/{slug}.html'`.
   - Disabled generic category list generation (`CATEGORIES_SAVE_AS = ''`).
   - Removed obsolete `assign_multi_lane_categories` generator signal hook and `Category` import.
   - Updated `ObsidianMarkdownReader` to parse `category` (defaulting to `"Mine"`), `type`, `previous_types`, and `tags`.
2. **Content Metadata Migration (`content/posts/`)**:
   - Converted all posts from `lanes:` to `category: "Mine"` (or `"Ours"`) with topical `tags: [...]`:
     - `cordoba-stage-guitar.md`: `category: "Mine"`, `tags: [music, guitar]`, `type: WIP`.
     - `digital-piano-enhancements.md`: `category: "Mine"`, `tags: [music, making, piano]`, `type: PROJ`.
     - `ulu-knife-handle.md`: `category: "Mine"`, `tags: [making, woodworking]`, `type: PROJ`.
     - `sleep-movement-evaluation-plan.md`: `category: "Mine"`, `tags: [health, tai-chi, sleep]`, `type: SPEC`.
     - `m-e-offline-ai-companion.md`: `category: "Mine"`, `tags: [ai, software]`, `type: IDEA`.
     - `art-institute-chicago-modern-wing.md`: `category: "Ours"`, `tags: [museums, chicago, sculpture, architecture, lighting, curation]`, `type: VIEW`.
3. **Template & Styling Alignment**:
   - `theme/templates/base.html`: Pointed tagline *"Out of My Lane"* to `/posts.html`. Replaced `.footer-lanes` with subtle `.footer-categories` (`Streams: Mine • Ours`).
   - `theme/templates/archives.html`: Replaced `.lane-nav` with `.stream-nav` (`All • Mine • Ours`). Replaced lane loop with `article.category`.
   - `theme/templates/category.html`: Rendered clean `<h2>Category: {{ category }}</h2>` with stream navigation.
   - `theme/templates/article.html` & `theme/templates/index.html`: Replaced lane loops with `article.category` stream links.
   - Styled `.stream-nav`, `.stream-link`, `.post-category`, `.footer-categories` in `theme/static/css/style.css`, `theme/css/style.css`, and `assets/css/style.css`.
4. **Purged Retired Files**:
   - Deleted `lanes/` directory and `lanes.html`. Generated category streams in `category/mine.html` and `category/ours.html`.
5. **Governance & Documentation**:
   - Updated Section 5 of `AGENTS.md` and `.agents/agent_rules.md` to define Provenance Categories and Custom Topic Pages.
   - Updated `docs/content_authoring.md` and `README.md`.
6. **Automated Testing & Release**:
   - Updated `tests/test_pelican_e2e.py` and `tests/test_accessibility.py` to audit stream navigation and `category/` outputs.
   - Verified 43/43 passing automated tests (`uv run pytest -v`).
   - Bumped version to `v0.6.1` in `pyproject.toml` and `content/pages/about-this-site.md`.

---

## 2026-09-11 — Multi-Lane Taxonomy, Post-Type Evolution, Zero-JS Commenting Pipeline & Release v0.6.0

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"ok toomany, remove thrd,pmrt, quote,lab, psper, snip. keep rest, updatd docss and assign types to existing content. displat the types short code along with date month yr, and lanes for each post"*
> - *"wip good, not rest. remove rev, maybe read, watch, listen, view"*
> - *"so posts have a single current tyoe but voul dc hav e previos types. posts czn havd multple lanes. m.e. is ai lane, ideas is not a lane, neitger is projects"*
> - *"can i do a commenting system without javascript? any dynamic menus?"*
> - *"i want to host on github, where are the submitted comments going? how do i feed them back into the build process and repo? i will want to do signficant summarization/filtering using llm i think. what spam protection does github pages and google mail provide me, what risks do i have"*
> - *"github issues are a bad approach since attackers will flood it, i have to delete them all. is formspree free? gmail sounds good as it uses their spam protection and i can easily get comments back out"*
> - *"i like the google sheets idea now, so i could have a nice simple comment/email form at bottom of posts and contact page. user enter email and limited text does push to google apps script and then to sheet, i want to see all garbage and good stuff. add issue for all this along with design option comments and final decision. update site page with this info how it works. we will need the google apps script, google sheets, way to get comments from sheets into the pelecan publish task, llm based summarizer/filter (might be generalized tool with custom prompts, pipeline-tools?) or could be hardcoded to start easier, write tests of course. probably some agent skills files that could help with commenting management so support skills selections use in the tool prompt fields. get this all into a ticket, do some preliminary design, but don't implement yet. in the author metadata field for posts or anything we want to make sure AI is listed as a primary author or supporting author when appropriate or even suspected"*
> - *"lets commit and push, publish, update release number"*

### Problem & Diagnosis
1. **Taxonomy Conflation**: Posts previously used a single `category` field that mixed subject domains (`Music`, `Health`, `Making`) with developmental stages and formats (`Ideas`, `Projects`). Furthermore, posts were artificially constrained to a single category, preventing articles from spanning related disciplines (such as Digital Piano modifications touching both `Music` and `Making`).
2. **Post Lifecycle Tracking**: Need an explicit way to convey the current format of a post alongside its conceptual history (e.g., an entry starting as an `[IDEA]`, progressing to `[WIP]`, and culminating in a completed `[PROJ]`).
3. **Spam-Safe, Zero-JS Interaction**: Desire a reader feedback and commenting channel without violating the site's strict Zero-JS policy, while avoiding GitHub issue tracker spam defacement and ensuring Jim retains visibility into all submissions ("garbage and good stuff").
4. **Mandatory AI Attribution**: Need a strict policy to transparently credit AI models whenever they contribute to content or code artifacts.

### Root Cause & Technical Analysis
- Pelican's default category model assumes a single 1:1 relationship between an article and a Category object. To support multi-lane posts, the reader must parse multiple lanes from frontmatter, set a primary category for internal wrappers, and hook into `article_generator_finalized` to append the article to all its respective category lists so that each lane archive (`lanes/<lane>.html`) includes all assigned articles.
- Decoupling content type (`type`) and evolutionary history (`previous_types`) from categories ensures pure thematic lanes (`AI`, `Art`, `Health`, `Making`, `Music`).
- Using a serverless Google Apps Script Web App endpoint as an HTML form action allows semantic Zero-JS form submission directly to a private Google Sheet, insulating GitHub from spam and giving Jim full control over LLM preprocessing and static digest publishing.

### Solution & Standard Procedure
1. **Multi-Lane & Type Parsing in `pelicanconf.py`**:
   - Updated `ObsidianMarkdownReader` to parse YAML `lanes`, `type`, and `previous_types`.
   - Connected `assign_multi_lane_categories` hook to `signals.article_generator_finalized`, properly populating multi-lane articles into all assigned categories.
2. **Template & CSS Updates**:
   - `theme/templates/article.html`, `archives.html`, `category.html`, `index.html`: Rendered `[TYPE]`, `(evolved from ...)`, and multiple lane links enclosed in `<span class="post-lanes">` to preserve clean typography without whitespace anomalies before commas.
   - Added `.post-type`, `.post-type-evolution`, and `.prev-type` rules to `theme/static/css/style.css`, `theme/css/style.css`, and `assets/css/style.css`.
3. **Category Cleanup**:
   - Purged `lanes/ideas.html` and `lanes/projects.html`.
   - Re-assigned `M.E.` to `AI` lane and `Digital Piano Enhancements` to `[Music, Making]`.
   - Standardized 5 active lanes: `AI`, `Art`, `Health`, `Making`, `Music`.
4. **Zero-JS Feedback System Design**:
   - Filed detailed architecture tracking ticket [GitHub Issue #9](https://github.com/jimcollinsworth/jimcollinsworth.github.io/issues/9).
   - Documented pipeline in `docs/content_authoring.md` and added contact description to `content/pages/about.md`.
5. **Rule 14 Codified**:
   - Added Rule 14 (Mandatory AI & LLM Author Attribution with `LLM-<model-id>`) in `.agents/agent_rules.md`.
6. **Automated Testing & Release**:
   - Expanded test suite to 43 passing tests (`tests/test_pelican_e2e.py`).
   - Bumped version to `0.6.0` in `pyproject.toml`, `uv.lock`, and `content/pages/about-this-site.md`.
   - Generated `releases/v0.6.0.md`.
   - Synchronized static assets to repository root for GitHub Pages publication.

---

## 2026-09-10 — Persistent Learning (`/learn`), Human Prompt Highlighting in Journal & Release v0.5.9

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"ok do a /learn, update journal highligh my instructions, questions, corrections, advise, update release numbermerge push and publish"*

### Problem & Diagnosis
Jim requested executing a `/learn` session with specific continuous learning directives:
1. **Highlighting Jim's Input**: In `JOURNAL.md`, prominently distinguish Jim's authentic instructions, questions, corrections, and advice from the agent's technical log entries.
2. **Persistent Rule Codification**: Ensure that agent governance documents (`AGENTS.md` and `.agents/agent_rules.md`) mandate this distinct formatting for all future journal entries.
3. **Release & Deployment**: Increment the release version to `v0.5.9`, merge the feature branch to `main`, tag the release, push to remote, and publish to GitHub Pages.

### Root Cause & Technical Analysis
- As noted in `ROADMAP.md`, `JOURNAL.md` contains predominantly agent-generated technical logs, making it difficult to immediately identify Jim's human editorial direction, requirements, and critical course corrections.
- Establishing a standardized GitHub Flavored Markdown alert block (`> [!NOTE] Jim's Prompts, Instructions & Steering:`) at the top of every journal entry provides immediate visual contrast and preserves human provenance.

### Solution & Standard Procedure
1. **Governance Documents Updated (`AGENTS.md` & `.agents/agent_rules.md`)**:
   - Updated Section 6 to formally require callout blocks for Jim's prompts, instructions, corrections, and advice in `JOURNAL.md`.
2. **Journal Retrofitted & Updated (`JOURNAL.md`)**:
   - Added prominent callout blocks to recent entries detailing Jim's exact instructions and steering.
3. **Versioning Synchronized**:
   - Bumped version to `0.5.9` across `pyproject.toml` and `content/pages/about-this-site.md`.
   - Created `releases/v0.5.9.md` documenting this milestone.
4. **Automated Verification**:
   - Verified 42/42 tests pass with `uv run pytest -v`.

---

## 2026-09-10 — Tagline Lanes Link, Footer Lane Navigator, AI Promoted Lane, Links Rename & Homepage Bio (v0.5.8)

> [!NOTE] Jim's Prompts, Instructions & Steering:
> - *"i like the make the distinction of me, mine, ours and others could event be menu/page titles. me is the about page along with contacts, what i'm doing now; mine is my own original content, apps, photos (not of art); and then ours with would be nature, hikes, museums, art; and others are books, urls, blogs, articals and my comments/review/mention. i would post my photos of art in others or ours, that one is not entirely clear could go either way. finally want to make ai a major page - basically it's one of the out of my lane 'lanes' pages, but promoted to the top menu. maybe we have an easy way to mark a lane page to show at top level menu, vs a list/tag cloud of all the lanes (maybe 20). but a menu of 'me mine ours others' may be too cute. so lets do about, https://macwright.com/ is probably the best structure wise and content and layout for me. document some of these thoughs but i thik the only change we need is to remove events, i will just have an 'art' post, and change shelf to something else - links is fine for now. and add ai and lanes as 2 more pages, with ai being a lane, and lanes being a description an dindex to all the lanes."*
> - *"remove about link, instead just have a quick blurb about me on home, and then link to detail about page. add site link for the about site page."*
> - *"remove lanes page, add a link to that from the out of my lane title. and we can put all the lanes into the footer navigator. go ahead with everything"*

### Problem & Diagnosis
Jim requested a refined navigation structure and content organization:
1. **Tagline as Lanes Link**: Make the header tagline *"Out of My Lane"* a direct link to `/lanes.html` rather than keeping a separate `Lanes` item in the menu row.
2. **Footer Lane Navigator**: Display all active pursuit lanes in the footer navigator (`Art`, `Health`, `Ideas`, `Making`, `Music`, `Projects`), making the entire lane taxonomy discoverable across every page.
3. **Header Menu Optimization**:
   - Remove `About` link from header menu; replace with a conversational personal bio blurb on the homepage (`index.html`) with a "More about me &rarr;" link to `about.html`.
   - Add `Site` link to the header menu pointing to `about-this-site.html`.
   - Remove `Events` page/menu item (`events.md` / `events.html`).
   - Rename `Shelf` &rarr; `Links` (`links.md` / `links.html`).
   - Add **`AI`** as a promoted top-level lane page (`content/pages/ai.md` &rarr; `ai.html`).
4. **Roadmap & Mental Model**: Document Jim's "Me, Mine, Ours, Others" taxonomy boundary and the `macwright.com` layout inspirations in `ROADMAP.md`.

### Root Cause & Technical Analysis
- Linking the tagline to `/lanes.html` creates a natural semantic anchor: the site philosophy (*Out of My Lane*) points directly to the directory of all pursuit lanes.
- Removing `About` from the top nav and placing a conversational intro on `index.html` creates a warmer, more human entrance inspired by minimal personal blogs like `macwright.com` and Shubham's site.
- Adding `Site` to the header gives prominent visibility to the architecture and DevOps dashboard.
- Displaying all lanes in the footer ensures full discoverability without overcrowding the primary 7-item header menu (`Home`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`).

### Solution & Standard Procedure
1. **Templates & HTML Structure**:
   - `theme/templates/base.html`:
     - Linked `.site-tagline` to `{{ SITEURL }}/lanes.html`.
     - Configured main nav: `Home`, `Posts`, `AI`, `Links`, `Photos`, `Apps`, `Site`.
     - Added `.footer-lanes` to the footer displaying all categories with bullet separators.
     - Added `All Lanes` and `About Jim` to footer secondary navigation.
   - `theme/templates/index.html`:
     - Authored conversational personal intro blurb linking to `about.html`.
     - Renamed "From the Shelf" to "Recent Links" linking to `links.html`.
   - `theme/templates/categories.html`:
     - Enhanced `/lanes.html` with a descriptive overview of the "Out of My Lane" philosophy and a grid directory of all lanes.
2. **Content & Pages**:
   - Created `content/pages/ai.md` (`slug: ai`, `title: AI`).
   - Renamed `content/pages/shelf.md` &rarr; `content/pages/links.md` (`slug: links`, `title: Links`).
   - Deleted `content/pages/events.md`, `events.html`, and obsolete `shelf.html`.
   - Updated cross-references in `about.md` and `apps.md`.
3. **Styling (`style.css`)**:
   - Added `.site-tagline a` subtle color and hover underline styles.
   - Added `.footer-lanes` flex row styling with subtle divider and hover states.
   - Synchronized CSS across `theme/static/css/`, `theme/css/`, and `assets/css/`.
4. **Governance & Roadmap**:
   - Updated `ROADMAP.md` with Section 6 ("Me, Mine, Ours, Others" taxonomy) and Section 7 (`macwright.com` layout cues and 20-lane architecture).
   - Updated `README.md` directory map.
   - Bumped version to `v0.5.8` across `pyproject.toml` and `about-this-site.md`.
5. **Testing & Verification**:
   - Updated `tests/test_pelican_e2e.py`, `tests/test_accessibility.py`, and `tests/test_playwright_responsive.py`.
   - All 42/42 tests passing (`uv run pytest -v`).

---

## 2026-09-10 — Contact Page, Footer Links Enhancement & UI Walkthrough Visual Protocol (v0.5.7)

### Problem & Diagnosis
1. **Footer Navigation**:
   - Following header deduplication in v0.5.6.01, the footer needed clear secondary navigation to key project pages: `About Site`, `Dev Prompts`, and a newly requested `Contact` page, along with external `Google Photos`.
2. **Contact Channel**:
   - Visitors and readers lacked a direct, simple contact page.
3. **UI Visual Evidence Invariant**:
   - Jim requested a strict governance standard: whenever walkthroughs or reports involve user interface changes, the agent must provide one or two visual screenshots directly in the report before Jim approves pushing or merging.

### Root Cause & Technical Analysis
- The personal site adheres strictly to a zero-JavaScript philosophy. A contact page must avoid complex JavaScript forms, external tracking widgets, or reCAPTCHAs while providing clear, comfortable ways to get in touch.
- Secondary meta links (`about-this-site.html` and `prompt-history.html`) belong naturally in the footer, keeping the main header navigation focused on primary reading and exploration lanes.
- Codifying the visual walkthrough protocol as Section 13 in `AGENTS.md` and `.agents/agent_rules.md` ensures agent execution is gated on immediate visual evidence.

### Solution & Standard Procedure
1. **Contact Page (`content/pages/contact.md`)**:
   - Created clean, minimalist Markdown page compiling to `output/contact.html`.
   - Included direct email contact link (`mailto:jim@jimcollinsworth.com`), context on topics of discussion (classical guitar, software, health, Chicago skies), and site privacy stance.
2. **Footer Navigation Updates (`theme/templates/base.html`)**:
   - Updated `<nav class="footer-nav">` with links:
     - `About Site` (`about-this-site.html`)
     - `Dev Prompts` (`prompt-history.html`)
     - `Contact` (`contact.html`)
     - `Google Photos` (`https://photos.app.goo.gl/...`)
3. **Governance Codification (`AGENTS.md` & `.agents/agent_rules.md`)**:
   - Codified **Section 13: Visual Evidence & UI Walkthrough Protocol** mandating inline screenshots before requesting approval to push or merge.
4. **Automated Testing & Visual Verification**:
   - Updated `tests/test_pelican_e2e.py` and `tests/test_playwright_responsive.py` to audit `contact.html`.
   - All 42/42 automated tests pass cleanly with `uv run pytest -v`.
   - Captured full-page visual screenshots of the Contact page and Footer navigation.
5. **Versioning**:
   - Bumped version to `v0.5.7` in `pyproject.toml` and `content/pages/about-this-site.md`.

---

## 2026-09-10 — High-Contrast Header 2-Line Alignment, Line-Height Optimization & Footer Deduplication (v0.5.6.01)

### Context & Need
Jim requested two targeted UI refinements:
1. **High-Contrast Header & Line Height**:
   - In High Contrast view (`#contrast-toggle`), remove all extra line feeds on the menu.
   - Constrain the header strictly to 2 lines (Line 1: Title & Tagline; Line 2: Navigation Links & Controls).
   - Reduce the line height across high-contrast typography so vertical spacing is tighter and more readable.
2. **Footer Navigation Deduplication**:
   - Remove any menu items from the footer that also appear in the header navigation (`Home`, `About`, `Posts`, `Shelf`, `Events`, `Photos`, `Apps`).

### Decisions & Actions Taken
1. **2-Line High-Contrast Header (`style.css`)**:
   - Removed `flex-direction: column` from `nav.site-nav` in high-contrast mode, replacing it with horizontal row flex (`flex-direction: row; flex-wrap: wrap; gap: 0.25rem 1.15rem; margin: 0;`).
   - Removed the `[Active Page] ` text prefix from `nav.site-nav a.active::before`, which previously caused menu items to expand and wrap onto multiple lines. Replaced it with high-contrast underline (`text-decoration: underline 4px; font-weight: 800;`).
   - Maintained Line 1 (`.site-branding`) with title on far left and tagline on far right; maintained Line 2 (`.site-nav-row`) with menu links on left and controls on far right.
2. **Reduced Line Height**:
   - Reduced base high-contrast line height from `1.85` to `1.55` on body, paragraphs, and list elements.
   - Reduced post teasers from `1.8` to `1.55` line height.
   - Reduced combined high-contrast + text-size mode line height from `2.0` to `1.7`.
3. **Footer Menu Deduplication (`base.html`)**:
   - Cleaned `<nav class="footer-nav">` to only contain links unique to the footer: `About This Site` and `Google Photos`.
   - Removed duplicate links (`Home`, `About`, `Posts`, `Shelf`, `Events`, `Photos`, `Apps`).
4. **Testing & Verification**:
   - Updated `test_in_page_mode_switchers_interactive` in `tests/test_playwright_responsive.py` to assert horizontal `nav_direction == "row"`.
   - Verified all 40/40 tests pass cleanly in `uv run pytest -v`.
   - Captured full-page visual screenshots via Playwright validating both desktop and mobile high-contrast rendering.
5. **Versioning**:
   - Bumped version to `0.5.6.01` in `pyproject.toml` and `content/pages/about-this-site.md`.

---

## 2026-09-09 — Section Taxonomy Refinement (Reads &rarr; Shelf, Gallery &rarr; Photos, Views &rarr; Events) & Header Layout Optimization

### Context & Need
Jim requested several coordinated layout and terminology refinements:
1. **Header Layout**:
   - Line 1: `Jim Collinsworth` on the far left, `Out of My Lane` right-aligned on the far right.
   - Line 2: Navigation menu links left-aligned, and theme/accessibility control toggles right-aligned on the same row.
   - Controls Styling: Tighten icons with less/no white border box so they visually harmonize with the `0.92rem` menu typography.
2. **Content Section Terminology**:
   - Rename **Reads** &rarr; **Shelf** (`content/pages/shelf.md`, URL `/shelf.html`).
   - Rename **Gallery** &rarr; **Photos** (`content/pages/photos.md`, URL `/photos.html`).
   - Rename **Views** &rarr; **Events** (`content/pages/events.md`, URL `/events.html`).

### Decisions & Actions Taken
1. **Header Layout & Compact Control Icons**:
   - Restructured `theme/templates/base.html`: Line 1 `.site-branding` with `space-between` and `align-items: baseline`, right-aligning `.site-tagline`; Line 2 `.site-nav-row` wrapping `.site-nav` (left) and `.site-controls` (right).
   - Replaced bulky `38x38px` white card box buttons with compact `28x28px` borderless transparent buttons (`border: 1px solid transparent; background: transparent;`) and scaled SVG icons from `18px` to `15px`.
2. **Markdown Sources & Slug Renaming**:
   - `content/pages/reads.md` &rarr; `content/pages/shelf.md` (`slug: "shelf"`, `title: "Shelf"`).
   - `content/pages/gallery.md` &rarr; `content/pages/photos.md` (`slug: "photos"`, `title: "Photos"`).
   - `content/pages/views.md` &rarr; `content/pages/events.md` (`slug: "events"`, `title: "Events"`).
   - Updated `content/pages/about.md` reference link to `shelf.html` ("References & Shelf").
   - Updated `content/pages/apps.md` lead text to reference shelf entries and events.
3. **Template Navigation & Homepage Updates**:
   - `theme/templates/base.html`: Updated navigation links and active conditions to `shelf.html`, `events.html`, and `photos.html`; updated footer links accordingly.
   - `theme/templates/index.html`: Renamed "Recent Reads" section to "From the Shelf", updated links to `shelf.html` ("Browse the complete shelf &rarr;"), and updated photo spotlight link to `photos.html` ("Explore all photos &rarr;").
4. **Automated Test Suite Synchronization**:
   - Updated `tests/test_pelican_e2e.py`: `test_core_pages_exist` and `test_no_duplicate_page_titles` now assert `shelf.html`, `events.html`, and `photos.html`.
   - Updated `tests/test_accessibility.py`: `test_active_nav_aria_current` tests `shelf.html`, `events.html`, and `photos.html`.
   - Updated `tests/test_playwright_responsive.py`: parameterized pages list updated.
   - Verified 40/40 tests pass with zero errors.
5. **Versioning & Root Synchronization**:
   - Bumped project version to `0.5.6` in `pyproject.toml` and `content/pages/about-this-site.md`.
   - Rebuilt Pelican static output and synchronized root HTML files, cleanly removing obsolete `reads.html`, `gallery.html`, and `views.html`.

---

## 2026-09-09 — Accessibility Toggles Overhaul: High-Contrast Low-Complexity Mode & Large Text Scaling

### Context & Need
Jim requested that the accessibility toggles deliver much more obvious and significant visual transformations:
- **Text Size Toggle**: Dramatically bigger text across all elements, expanded line-height, and generous margins so content has comfortable breathing space.
- **High-Contrast Toggle**: Low-complexity assistive mode tailored for readers needing maximum clarity: fewer lines (stripping decorative boxes, borders, and card outlines), no graphics (hiding photos and decorative images, replaced by structured text summaries), no tabs (serializing navigation into a clear linear list), flattening multi-column grids into a single serial column, and adding explicit data labels (`Date: `, `Category: `, `Author: `, `Read: `, `[Active Page]`) for text and assistive readers.

### Decisions & Actions Taken
1. **Dramatic Text Scaling (`body:has(#text-size-toggle:checked)`)**:
   - Scaled base body font size to `1.65rem` (~26.4px) with `2.0` line-height.
   - Scaled headings (`h1` to `2.85rem`, `h2` to `2.3rem`, `h3` to `1.9rem`, `.site-title` to `2.4rem`, `.post-title` to `2.05rem`).
   - Expanded paragraph spacing (`margin-bottom: 1.75rem`), post separation (`margin-bottom: 3.5rem`), container padding, and control buttons (`44px`).
2. **High-Contrast Low-Complexity Assistive Mode (`body:has(#contrast-toggle:checked)`)**:
   - **Contrast**: Stark 21:1 pure contrast in both Light (`#ffffff` bg / `#000000` text) and Dark (`#000000` bg / `#ffffff` text / `#ffff33` links) with 3px thick link underlines.
   - **Fewer Lines**: Stripped decorative card borders, timeline boxes, and shadows from `.dashboard-card`, `.timeline-milestone`, `.exhibit-card`, `blockquote`, and `.post-item`.
   - **No Graphics**: Hidden `img`, `picture`, and decorative gallery previews; styled `<figcaption>` into high-clarity descriptive assistive text blocks (`[Visual Content Description: ...]`).
   - **No Tabs / Serial Layout**: Serialized `.site-nav` and `.footer-nav` into a clear linear vertical list with active page indicators (`[Active Page]`); flattened `.desktop-two-col`, `.dashboard-grid`, and `.photo-preview-row` into a unified sequential reading column.
   - **Explicit Data Labels**: Injected bold visual prefixes via CSS pseudo-elements for dates, categories, authors, reading dates, and external link indicators.
   - Preserved control buttons clickability by keeping `.control-btn .sr-only` scoped.
3. **Automated Testing & Visual Verification**:
   - Enhanced `test_in_page_mode_switchers_interactive` in `tests/test_playwright_responsive.py` to assert font size enlargement (>= 24px), column nav direction, and image suppression.
   - Verified all 40/40 tests pass cleanly in `pytest`.
   - Generated and visually checked full-page screenshot artifacts across light, dark, large text, and combined high-contrast + large-text modes.

---

## 2026-09-09 — Prompt History & Instruction Timeline Subpage

### Context & Need
Jim requested a dedicated timeline subpage under *About This Site* focusing entirely on his direct instructions (summarized in his voice) and especially critical course corrections, error remediations, and design decisions, synced directly to the release milestones (`v0.1` through current development).

### Decisions & Actions Taken
1. **Created Prompt History Page (`content/pages/prompt-history.md` &rarr; `output/prompt-history.html`)**:
   - Structured chronologically across all milestones: Milestone 8 (Apps Hub, Views lane, static data directory), v0.5.5 (DevOps dashboard, Continuous Learning protocol, glossary cancellation, Mermaid syntax fixes), v0.5 & Accessibility (CSS `:has` switchers, orientation layout, progressive density), v0.3 & v0.4 (Pelican SSG migration, title deduplication, zero-pills mandate, Jekyll trap bypass), and v0.1 & v0.2 (human authorship boundary Rule 1, AI placeholder purge, 3-document governance rule).
   - Clean, high-contrast timeline layout using site CSS variables (`--accent`, `--border-color`, `--card-bg`, `--text-muted`), blockquotes of Jim's guidance, and bullet points of error remediations.
   - Strictly 100% Zero-JS with semantic HTML5 elements.
2. **Linked Prominently from `about-this-site.md`**:
   - Added dedicated section "Prompt & Instruction Timeline" with a direct link to `prompt-history.html`.
3. **Automated Testing & Browser Verification**:
   - Added `prompt-history.html` and `about-this-site.html` to both `tests/test_pelican_e2e.py` and `tests/test_playwright_responsive.py`.
   - Verified 40/40 tests pass cleanly with zero console errors or accessibility violations.
   - Captured multi-viewport screenshots via `tools/screenshots.py` and visually verified rendering quality.

---

## 2026-09-09 — Milestone 8: About-This-Site Overhaul, Visual Exhibits ("Views") Lane, Apps Hub & Example Interactive Tools

### Decisions & Actions Taken
1. **Overhauled `about-this-site.md`**:
   - Removed the local CLI install/run commands section.
   - Prominently positioned the **Google Antigravity & LLM Agent Harness** at the very top of the Technology Stack.
   - Added direct links and dashboard cards for the **GitHub Repository** (`https://github.com/jimcollinsworth/jimcollinsworth.github.io`) and **Release Notes** (`releases/` / GitHub releases).
2. **Main Navigation Expansion & "Views" Visual Lane**:
   - Added **`Views`** and **`Apps`** to both `site-nav` and `footer-nav` in `theme/templates/base.html`.
   - Created **Views** (`content/pages/views.md`) dedicated to museum visits, art exhibits, gallery tours, and opinionated visual critiques with photo figures and observations.
   - Added sample art post `content/posts/art-institute-chicago-modern-wing.md` (`origin: review`, `stage: inquiry`, category `Art`).
3. **Centralized Static Data Directory (`content/data/`)**:
   - Configured `STATIC_PATHS = ['images', 'extra', 'apps', 'data']` in `pelicanconf.py`.
   - Created `content/data/photos.json` and `content/data/photos.md` containing image metadata, dates, locations, and direct Google Drive links.
   - Created `content/data/site-index.json` containing complete multi-facet content index spanning categories, stages, origins, and tags.
4. **Built Two Full-Screen Example Interactive Applications**:
   - `content/apps/photo-viewer/index.html`: Responsive full-screen photo viewer parsing manifest data, with filmstrip sidebar, keyboard navigation, camera telemetry, dark/light toggle, and direct Google Drive RAW links.
   - `content/apps/keyword-search/index.html`: Full-screen interactive taxonomy, keyword, category, and thought stage visual discovery explorer with live fuzzy search and clickable filter chips.
   - Created Apps Hub page `content/pages/apps.md` (`apps.html`) introducing the sandbox.
5. **Architectural Boundary: Zero-JS vs. Standalone Apps**:
   - Preserved 100% Zero-JS guarantee for all editorial reading content (`index.html`, `posts/*.html`, `reads.html`, `views.html`, `about.html`, etc.).
   - Interactive applications operate in isolated standalone subpaths (`output/apps/**`).
6. **Automated Test Suite Expansion**:
   - Expanded test suite from 30 to 36 automated tests (`tests/test_accessibility.py`, `tests/test_pelican_e2e.py`, `tests/test_playwright_responsive.py`), validating all pages and apps across viewports.

---

## 2026-09-09 — Milestone 7: Versioning v0.5.5, DevOps Dashboard, Cheat Sheet PDFs & Release History

### Decisions & Actions Taken
1. **Created Visual Cheat Sheets & Automated PDF Generator**:
   - Designed two comprehensive visual cheat sheets featuring rich Mermaid diagrams and print-optimized typography:
     - `docs/cheatsheets/architecture_flow.pdf` &bull; `.md` &bull; `.html` &mdash; End-to-end publishing pipeline, source topography, interactive apps & static data architecture, Antigravity AI sequence diagram, governance matrix, and CLI commands.
     - `docs/cheatsheets/content_authoring.pdf` &bull; `.md` &bull; `.html` &mdash; Thought evolution lifecycle state diagram, authorship/origin boundary flow, Pelican YAML frontmatter template, semantic layout component mapping table, and responsive orientation modes.
   - Built `tools/generate_cheatsheet_pdfs.py` utilizing Playwright headless Chromium to render vector-sharp, letter-format PDFs on demand with built-in diagram validation that catches any Mermaid syntax parsing issues.
   - Resolved Mermaid syntax error in box 5 ("Responsive Layout & Orientation Rules") by escaping angle brackets in edge labels.
   - Added reference section in `README.md`.
2. **Bumped Project Version to `v0.5.5` & Created Structured Release History**:
   - Set version to `0.5.5` across `pyproject.toml` and `about-this-site.md`.
   - Created standardized GitHub-style release documents under `releases/`:
     - `releases/v0.1.md` &mdash; Clean Foundation, Zero-JS, and 3-Document Governance.
     - `releases/v0.2.md` &mdash; Calvin/MacWright Editorial Redesign, Bookshelf, and Gallery.
     - `releases/v0.3.md` &mdash; Pelican SSG Integration, Obsidian Frontmatter Reader, and E2E Testing.
     - `releases/v0.4.md` &mdash; GitHub Pages Root Deployment Alignment & Custom "JC" Favicon.
     - `releases/v0.5.md` &mdash; Magazine 2-Column Desktop Grid, Orientation Modes, and Progressive Density.
     - `releases/v0.5.5.md` &mdash; DevOps Dashboard, Continuous Learning Protocol, and Semantic Component Guide.
   - Published Git tags and official GitHub Releases (`v0.1` through `v0.5.5`).
3. **Formalized Continuous Learning Protocol (`/learn`) in Agent Governance**:
   - Integrated learning procedures into `.agents/agent_rules.md`: when new debugging solutions, user corrections, or workflow preferences are established, the agent records structured entries in `JOURNAL.md` and permanently updates `.agents/agent_rules.md` and `.agents/skills/`.
4. **Created `about-this-site.md` & DevOps Dashboard**:
   - Built standalone meta page at `content/pages/about-this-site.md` (compiled to `about-this-site.html`).
   - Integrated live GitHub Actions deployment badge, release version metric (`v0.5.5`), zero-JS guarantee (0 KB JS, 0 cookies, 0 tracking), and hosting architecture (GitHub Pages + HTTPS).
   - Formally documented the **Antigravity AI Assistant & Pair Programming Model** detailing the strict separation of concerns (Jim owns 100% of prose/content; Antigravity manages templates, CSS, build tools, tests, and CI/CD).
   - Integrated page into site footer navigation in `theme/templates/base.html`.
5. **Consolidated Content Types & Semantic Terminology Directly into Docs**:
   - Consolidated clear content format definitions (*Post/Essay, Project, TIL, Idea, Read, Comment*) directly into the **Semantic Component Guide** in `README.md`.
6. **Automated Test Suite Validation**:
   - Verified 30/30 automated tests passing across accessibility, Playwright browser rendering, and Pelican E2E integrity.

---

## 2026-09-09 — In-Page Accessibility & Theme Switchers (Zero-JS CSS :has)

### Context & Need
- Jim requested in-page, icon-based switchers to toggle light/dark theme, high-contrast mode, and text size directly on the site, while clarifying how dark-mode screenshots had been generated previously.
- Previous dark mode operated via OS media queries (`prefers-color-scheme: dark`) emulated by Playwright. Adding manual on-page controls required a solution that strictly preserved the Zero-JS architecture without requiring client-side `<script>` tags.

### Decisions & Actions Taken
1. **Pure CSS `:has()` Switcher Architecture**:
   - Added semantic `<input type="checkbox">` toggles at the top of `<body>` (`#theme-toggle`, `#contrast-toggle`, `#text-size-toggle`) with `.sr-only` accessibility styling.
   - Built a `.site-controls` button group in the header with 3 accessible icon labels:
     - **Theme Switcher** (`for="theme-toggle"`): Displays SVG Moon in light mode (to trigger dark) and SVG Sun in dark mode (to trigger light). Flips `--bg`, `--text`, `--link`, and cards via `body:has(#theme-toggle:checked)`.
     - **High-Contrast Switcher** (`for="contrast-toggle"`): SVG Contrast symbol (`◐`). Triggers pure black/white high-contrast palettes, forced link underlines, and heavy borders.
     - **Text Size Switcher** (`for="text-size-toggle"`): SVG Typography symbol (`aA`). Scales font sizing up to `1.32rem` with comfortable line height across body and headings.
2. **Accessible Interaction & Visual Feedback**:
   - Each button has minimum 38x38px touch targets, hover transitions, active pressed background states when toggled, and keyboard `:focus-visible` rings.
3. **Automated Testing & Interactive Verification**:
   - Added `test_mode_switchers_present_and_accessible` to `tests/test_accessibility.py`.
   - Added `test_in_page_mode_switchers_interactive` to `tests/test_playwright_responsive.py` verifying real browser clicks on the toggles successfully transition colors and font sizes.
   - Total test suite now stands at 30 passing tests.

---

## 2026-09-09 — Governance Rule: Remote Push Confirmation Requirement

### Context & Decision
- Jim established a strict operational rule prohibiting automated or autonomous `git push` commands.
- **Decision**: Added Section 9 to `.agents/agent_rules.md`. Pushes to remote mutate shared repository state, trigger GitHub Actions CI/CD workflows, and deploy live artifacts to GitHub Pages. The agent may build, test, and commit locally, but must always pause and request explicit confirmation from Jim before executing any `git push`.

---

## 2026-09-09 — Comprehensive Web Accessibility Implementation (WCAG 2.1/2.2 AAA & Zero-JS)

### Context & Need
- Jim requested addressing GitHub Issue #1 ("add accessibility to the site") filed on `jimcollinsworth/jimcollinsworth.github.io`.
- Site required full compliance with accessibility standards (WCAG 2.1/2.2 AA and AAA, Section 508, ADA) across keyboard navigation, screen reader semantic structure, high-contrast modes, fluid typography scaling, and vestibular motion reduction while strictly maintaining the zero client-side JavaScript architecture.

### Decisions & Actions Taken
1. **Semantic HTML5 & ARIA Landmarks**:
   - Added skip-to-content navigation (`<a href="#main-content" class="skip-link">Skip to main content</a>`) on every page, with immediate focus shifting to `<main id="main-content" tabindex="-1">`.
   - Added landmark roles (`role="banner"`, `role="contentinfo"`), unambiguous ARIA navigation labels (`aria-label="Main Navigation"`, `aria-label="Footer Navigation"`, `aria-label="Filter posts by lane"`), and screen reader indicators (`aria-current="page"`, `.sr-only`).
2. **WCAG AAA Contrast Palette & Accessible Focus Rings**:
   - Upgraded link and text contrast ratios to exceed 7:1 (light link `#8a3710` at 7.2:1, dark link `#e2955a` at 7.3:1).
   - Implemented high-visibility 3px `:focus-visible` outline rings with 3px offsets across all interactive elements.
3. **Adaptive Accessibility Modes (Native CSS)**:
   - Added `@media (prefers-contrast: more)` and `@media (prefers-color-scheme: dark) and (prefers-contrast: more)` for pure black/white high-contrast themes and forced link underlines.
   - Added `@media (forced-colors: active)` for Windows High Contrast Mode system color compatibility.
   - Added `@media (prefers-reduced-motion: reduce)` to disable transitions and animations for users with vestibular sensitivities.
4. **Fluid Typography & Touch Sizing**:
   - Replaced fixed mobile pixel root sizing with relative percentages (`html { font-size: 100%; }` and mobile `97%`), ensuring seamless browser text zoom up to 200%+ without layout clipping (WCAG 1.4.4).
   - Applied minimum 38px touch targets and padding on navigation items.
5. **Automated Accessibility Test Suite (`tests/test_accessibility.py`)**:
   - Created 9 automated pytest tests covering lang attributes, skip links, landmarks, active nav tabs, image alt attributes, zero-JS policy, CSS accessibility rules, and touch targets.
   - Total test suite now stands at 28 passing tests.

---

## 2026-09-09 — Long-Term Roadmap Creation, Governance Alignment, & Visual Verification Report

### Context & Decisions
1. **Created `ROADMAP.md`**:
   - Established a dedicated long-term vision, brainstorming, and creative sandbox document.
   - Synthesized Jim's foundational tenets with creative concepts (Circle of Fifths music visualizer, USGS live earthquake tracker, high-volume photo archive navigation mini-app, M.E. local AI companion, and sleep/somatic movement tracking).
   - Added speculative technical wishlists (zero-JS search index, pure SVG fretboard charts, Lake Michigan weather chronicles, offline PWA archive, micro-zines).
2. **Strict Agent Governance Rule in `.agents/agent_rules.md`**:
   - **Removed 8-viewport rule** from agent guidelines; confirmed it is a specific tool option on `tools/screenshots.py`.
   - **Added strict rule**: The agent must **never add, modify, or append rules or files in `.agents/` without explicit permission from Jim**. Jim will explicitly request specific rules to be added.
   - **Added strict Node/npm rule**: No Node.js or npm ever for applications or toolchains; the only current exception is `npx skills`.
   - Updated governance docs to recognize `ROADMAP.md` alongside `README.md`, `PLANNING.md`, and `JOURNAL.md`.
3. **Generated Visual Verification Report (`reports/responsive_screenshots_report.md`)**:
   - Embedded 24 multi-resolution screenshot captures across 3 core pages (`index.html`, `about.html`, `posts.html`) covering all 8 viewports in light and dark modes.
   - Staged all assets and submitted to GitHub for Jim's review.

---

## 2026-09-09 — Playwright Testing & Multi-Resolution Responsive Tooling

### Context & Need
- Jim requested visual verification across all display sizes and orientations: Phone, Tablet, Laptop, and Large Desktop / TV, in both Portrait and Landscape (8 viewports total).
- Jim mandated 100% Python-based tooling (via `uv`) and strictly **no Node.js / npm**.
- Formalized testing standards to ensure continuous multi-resolution visual sanity, zero-JS policy enforcement, and CLI command transparency.

### Decisions & Actions Taken
1. **Installed Python Playwright & Pytest Suite**:
   - Added `playwright>=1.62.0` and `pytest-playwright>=0.9.0` to `pyproject.toml` dev group using `uv`.
   - Installed headless Chromium browser binary (`uv run playwright install chromium`).
2. **Built Multi-Resolution Screenshot Utility (`tools/screenshots.py`)**:
   - Automated 4 device form factors x 2 orientations (8 viewports):
     - **Phone**: 390x844 (portrait) / 844x390 (landscape)
     - **Tablet**: 820x1180 (portrait) / 1180x820 (landscape)
     - **Laptop**: 768x1366 (portrait) / 1366x768 (landscape)
     - **Large Desktop / TV**: 1080x1920 (portrait) / 1920x1080 (landscape)
   - Added CLI support for `--page` (defaults to `index.html`), `--color-scheme` (`light`, `dark`, `both`), `--viewport-only`, `--device`, and `--orientation`.
   - Generates an interactive visual inspection HTML gallery (`screenshots/<page>/preview.html`).
3. **Automated Playwright Responsive Tests (`tests/test_playwright_responsive.py`)**:
   - Created headless Chromium tests verifying that core pages (`index.html`, `about.html`, `posts.html`, `reads.html`, `gallery.html`) render cleanly across mobile and desktop without uncaught console errors, 404 assets, or layout exceptions.
   - Verified that `tools/screenshots.py` executes successfully in automated testing.
   - Full test suite now contains 19 passing tests (`uv run pytest -v`).
4. **CI/CD Alignment (`.github/workflows/deploy.yml`)**:
   - Added Playwright Chromium installation step (`uv run playwright install --with-deps chromium`) to GitHub Actions workflow so full browser audits run automatically on every push.
5. **Documentation & Utilities Inventory**:
    - Added "Developer Utilities & Command Reference" to `README.md` and updated `PLANNING.md`.

---

## 2026-09-09 — Troubleshooting & Resolution: Pixeltable Embedded PostgreSQL Test Runner

### Problem & Diagnostic Analysis
- **Symptom**: `uv run python -m tests` in the `pipeline-tools` workspace experienced 27 test failures with `AssertionError: assert self._postmaster_info is not None`.
- **Root Cause**: On Windows, abruptly terminating Python / test runners left orphaned background `postgres.exe` child processes holding open file handles to `C:\Users\jimco\.pixeltable\pgdata\log` and `postmaster.pid`. When subsequent test runs initialized, PostgreSQL entered crash recovery, hit a Windows sharing violation (`could not open file "./log": sharing violation`), and timed out after 30 seconds.
- **Clarification**: `pxt service ...` commands only apply to remote/cloud Pixeltable microservices, not the local embedded PostgreSQL instance managed by `pixeltable_pgserver`.

### Solution & Recovery Procedure
1. Terminated lingering background PostgreSQL processes: `taskkill /F /IM postgres.exe /T 2>nul`.
2. Cleaned corrupted database state directory: `rmdir /s /q "%USERPROFILE%\.pixeltable\pgdata"`.
3. Verified test suite: `uv run python -m tests` cleanly reinitialized a fresh cluster and executed successfully.
>>>>>>> ed02d16 (feat(release): v0.5.5 with DevOps dashboard, learning protocol, semantic guide, and release history)

---

## 2026-09-08 — Magazine Multi-Column Desktop Grid, Orientation Adaptation & Progressive Density

### Decisions & Actions Taken
1. **Container Scale Expansion & Ultra-Wide Magazine Grid**:
   - Expanded container width scale from narrow `720px` to fluid `1080px` (standard desktop/laptop) and `1380px` (supersize desktop `>= 1360px`).
   - Implemented `.desktop-two-col` CSS grid (1.25fr/1fr on laptops/landscape, 1.3fr/1fr on wide desktop) structuring `index.html` with Featured Post + Recent Reads in the primary column and Recent Posts stream + Photo spotlight in the secondary column.
   - Constrained all body paragraphs to `max-width: 76ch` to guarantee optimal reading measure and typographic rhythm regardless of viewport width.
2. **Orientation-Driven Adaptations**:
   - Built pure CSS media queries combining width and orientation: `@media (min-width: 960px), (min-width: 720px) and (orientation: landscape)`.
   - Portrait orientation displays as a focused single-column reading mode, while landscape orientation leverages screen width with side-by-side reading and spotlight streams.
3. **Progressive Information Density**:
   - Added semantic markup classes `.post-teaser` and `.post-detail`.
   - On desktops/laptops, full excerpts and metadata are displayed; on mobile viewports (`< 640px`), secondary detail blocks are automatically hidden to keep feeds concise and scannable without requiring client-side JavaScript.
4. **Visual, Pelican SSG, & Zero-JS Verification**:
   - Integrated changes into Pelican theme templates (`theme/templates/index.html`) and static CSS (`theme/static/css/style.css`).
   - Verified 100% Zero-JS compliance (0 `<script>` tags across compiled output).
   - Validated all 8 end-to-end automated tests with `uv run pytest -v`.
   - Captured and verified multi-viewport visual screenshots (1600x1000 ultra-wide, 1200x800 laptop, 1024x768 tablet landscape, 768x1024 tablet portrait, 500x880 mobile portrait).

---

## 2026-09-08 — GitHub Pages Deployment Alignment & Root HTML Synchronization

### Problem & Analysis
- When viewing the live site on mobile, legacy pill navigation (`.pill`, `.pill-nav`) and duplicate titles (`<h1>Posts & Notes</h1>`, `<h1>About Jim Collinsworth</h1>`) were still appearing.
- Root Cause: GitHub Pages was configured to build and deploy from the `main` branch root (`/`), which still contained pre-Pelican static HTML files from Milestone 2. Pelican's build output in `output/` was gitignored, causing branch deployment to serve the obsolete root files.

### Decisions & Actions Taken
1. **Bypassed Jekyll**:
   - Added `.nojekyll` to `content/extra/` and registered it in `pelicanconf.py` (`EXTRA_PATH_METADATA`).
2. **Synchronized Root HTML with Pelican Build**:
   - Replaced root `index.html`, `about.html`, `posts.html`, `reads.html`, `gallery.html`, `lanes.html`, `posts/`, and `lanes/` with Pelican's compiled output.
   - Synchronized `theme/css/style.css` and updated `assets/css/style.css` so legacy or cached CSS references also render without pills.
3. **Hardened Automated Tests (`tests/test_pelican_e2e.py`)**:
   - Updated `test_zero_pills_lane_formatting` to scan both `output/` and repository root HTML files, ensuring neither ever contains `.pill` or `.pill-nav`.
   - Updated `test_no_duplicate_page_titles` to verify `posts.html` contains no redundant `<h1>Posts` header.
4. **Verified Build & Tests**:
   - All 8 end-to-end tests passing (`uv run pytest -v`).

---

## 2026-09-08 — Pelican SSG Integration, Manual Image Workflow, & UI Refinements

### Decisions & Actions Taken
1. **Configured Pelican Static Site Generator**:
   - Created `pyproject.toml` and `pelicanconf.py` configured for zero-JS, pure HTML5, and relative URLs.
   - Implemented `ObsidianMarkdownReader` in `pelicanconf.py` to seamlessly parse YAML frontmatter headers (`---`).
2. **Content Reorganization**:
   - Migrated markdown files to `content/posts/` (`cordoba-stage-guitar.md`, `digital-piano-enhancements.md`, `m-e-offline-ai-companion.md`, `sleep-movement-evaluation-plan.md`, `ulu-knife-handle.md`).
   - Created `content/pages/` for standalone pages (`about.md`, `reads.md`, `gallery.md`).
   - Created `content/images/` for manually curated photo assets and `content/extra/` for root metadata files.
3. **Custom Pelican Theme (`theme/`) & UI Cleanup**:
   - Recreated site templates in Jinja2 (`base.html`, `index.html`, `article.html`, `page.html`, `archives.html`, `category.html`, `categories.html`).
   - **Title Deduplication**: Removed redundant `<h1>` headings from standalone pages (`About`, `Reads`, `Gallery`); the active menu tab serves as the title.
   - **Lane Styling**: Removed pill/badge formatting (`.pill`, `.pill-nav`); pursuit lanes are styled as clean, simple text links (`.post-lane`, `.lane-link`).
4. **Manual Image Transfer & Zero-AI Content Policy**:
   - Formalized policy: Jim manually selects and transfers all photos to `content/images/`. AI is strictly restricted to content management, never content generation.
   - External gallery integration: Posts include selected photo figures and link to full albums on Google Photos.
5. **End-to-End Test Suite (`tests/test_pelican_e2e.py`)**:
   - Implemented automated E2E tests validating build execution, page generation, title deduplication, zero-pills styling, content flow from Markdown, zero-JS policy, and link/asset integrity (all 8 tests passing).
6. **Automated CI/CD**:
   - Updated `.github/workflows/deploy.yml` to install dependencies via `uv`, run tests, build with Pelican, and deploy `output/` to GitHub Pages.

---

## 2026-09-08 — Scope Realignment: Rollback Custom Tools & Focus on Obsidian Flow

### Decisions & Actions Taken
1. **Rolled Back Custom Build & Tool Pipeline**:
   - Reverted all working tree modifications and cleaned untracked directories (`tools/`, `tests/`, `projects/`, virtual environment, etc.) to return repository to clean `origin/main` state.
   - Preserved pure static site structure and strict content boundaries.
2. **Backlog Realignment in `PLANNING.md`**:
   - Transferred custom static site builder, MCP server, Pytest suite, and interactive tools (`circle-of-fifths`, `earthquakes`) to the backlog as optional "nice to have" enhancements.
3. **Refocused Active Priority**:
   - Established primary exploration: clarifying how Markdown authored in Obsidian is placed into a directory and flows into published HTML.
   - Selected Pelican as the preferred static site generator foundation.
4. **Installed Project Skills in `.agents/skills/`**:
   - Created [`pelican-site-manager`](file:///d:/projects/jimcollinsworth.github.io/.agents/skills/pelican-site-manager/SKILL.md): Complete runbook for Pelican configuration, development server, zero-JS preservation, and build verification.
   - Created [`pelican-obsidian-bridge`](file:///d:/projects/jimcollinsworth.github.io/.agents/skills/pelican-obsidian-bridge/SKILL.md): Guidelines for mapping an Obsidian vault to Pelican's content folder, handling YAML frontmatter, wikilinks, image embeds, and callouts.
   - Added Rule 7 (Command Line Standards & Reproducibility) to [`.agents/agent_rules.md`](file:///d:/projects/jimcollinsworth.github.io/.agents/agent_rules.md).

---

## 2026-09-07 — Custom "JC" Favicon Update

### Decisions & Actions Taken
1. **Designed Minimalist "JC" Favicon**:
   - Created vector [`favicon.svg`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/favicon.svg) featuring "JC" monogram with rounded geometry and built-in CSS `@media (prefers-color-scheme: dark)` color-switching (rust in light mode, amber in dark mode).
   - Generated multi-resolution [`favicon.ico`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/favicon.ico) (16x16, 32x32, 48x48, 64x64) with matching warm rust background and white lettering.
   - Linked both SVG and ICO fallback across all 11 site and post pages.

---

## 2026-09-07 — Content Boundary Remediation & Post Page Linking

### Decisions & Actions Taken
1. **Strict Content Boundary Remediation**:
   - Audited every page and deleted all agent-authored text and fabricated summaries.
   - Replaced placeholder entries in `reads.html` and `index.html` strictly with standard `Lorem ipsum` holding text.
   - Replaced all post descriptions across `index.html`, `posts.html`, and `posts/*.html` strictly with Jim's original archived text from `archive/content/`.
2. **Individual Post Page Generation & Linking**:
   - Generated dedicated static post pages in `posts/` containing Jim's exact archived text:
     - [`posts/sleep-movement-evaluation-plan.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/sleep-movement-evaluation-plan.html)
     - [`posts/m-e-offline-ai-companion.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/m-e-offline-ai-companion.html)
     - [`posts/cordoba-stage-guitar.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/cordoba-stage-guitar.html)
     - [`posts/digital-piano-enhancements.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/digital-piano-enhancements.html)
     - [`posts/ulu-knife-handle.html`](file:///c:/Users/jimco/Projects/jimcollinsworth.github.io/posts/ulu-knife-handle.html)
   - Linked all post titles from `index.html` and `posts.html` directly to their respective post pages.
3. **Pure Photo Gallery**:
   - Removed all captions and extra text from `gallery.html`, presenting clean unencumbered photography with only the Google Photos album link at the top.

---

## 2026-09-07 — Calvin & MacWright UI Overhaul, Bookshelf, & Content Pipeline

### Decisions & Actions Taken
1. **Adopted Calvin French-Owen Typography & Listing Rhythm**:
   - Implemented post listings with prominent rust titles (`var(--link)`), right-aligned uppercase dates, category pill badges, and concise takeaway descriptions.
   - Created secondary level filter pill navigation bar on `posts.html`.
2. **Added Bookshelf / Reads (`reads.html`)**:
   - Dedicated reading synthesis page inspired by Calvin's bookshelf with titles, authors, dates read, favorite indicators (`*`), and mental model notes.
3. **MacWright-Style Photo Stream (`gallery.html`)**:
   - Replaced boxed card grid with a clean, full-width photo stream with left-aligned captions and zero distracting card borders.
4. **Streamlined Navigation & Page Roles**:
   - Primary navigation streamlined to: `Home`, `About`, `Posts`, `Reads`, `Gallery`.
   - Retired `lanes.html`; integrated the Lanes taxonomy into `about.html` and as single-category badges across posts.
   - Removed duplicated biography text on `index.html`, refocusing the home page on current activity, recent posts, bookshelf highlights, and photo spotlight.
5. **New Content Drop Directory (`content/`)**:
   - Established `content/posts/`, `content/notes/`, and `content/reads/` for dropping Markdown source files with clean YAML front-matter (`title`, `date`, `category`, `description`).

---

## 2026-09-07 — Header Branding Single-Line Alignment

### Decisions & Actions Taken
1. **Unified Title and Tagline Row**:
   - Updated header structure to place "Jim Collinsworth" and "Out of My Lane" on the same horizontal row using `.site-branding` with flex `justify-content: space-between`.
   - Set matching font size (`1.35rem`) and font family (`var(--font-sans)`) across title and tagline while maintaining subtle text mute for the tagline.
   - Updated across all 5 site pages (`index.html`, `about.html`, `lanes.html`, `journal.html`, `gallery.html`) and `assets/css/style.css`.

---

## 2026-09-06 — Content Reversion to Archive & 12 Lanes Setup

### Decisions & Actions Taken
1. **Reverted All Content to Archive Text**:
   - Replaced all prose on `about.html` and `index.html` strictly with Jim's original text from `pages/about.md` and `README.md`. Removed all AI-generated commentary.
   - Simplified `gallery.html` to minimalist titles and direct link to the Google Photos album.
2. **Configured 12 Requested Lanes**:
   - Updated `lanes.html` and `index.html` with the 12 explicit lanes: *Music making, Software, Life sciences, Engineering, Photography, Making, Law, Art, Politics, Data, Exercise, Anatomy*.
3. **Dummy Entries for Layout Preview**:
   - Inserted placeholder `Lorem ipsum` entries on `journal.html` and `index.html` solely to preview page layout without authoring posts.
4. **CI Workflow Streamlining**:
   - Refined `.github/workflows/deploy.yml` with a lightweight Zero-JS audit step and GitHub's official Pages deployment action.

---

## 2026-09-06 — Architectural Transformation: Pure HTML/CSS & Agent Governance

### Context & Problem
The site previously relied on Nikola, a Python-based static site generator with configuration files (`conf.py`), theme directories (`themes/hyde`), virtual environments (`pyproject.toml`, `uv.lock`), and compiler build workflows (`nikola.yml`). This introduced unnecessary build friction, compilation fragility, and opaque templating layers for what should be an authentic, durable personal website.

### Decisions & Actions Taken

1. **Complete Decommissioning of Compiler Toolchain**:
   - Removed `conf.py`, `themes/`, `plugins/`, `pyproject.toml`, `uv.lock`, and legacy build workflows.
   - Preserved all historical notes, draft essays, category definitions, and SEO verification tokens safely in `archive/content/`.
   - Relocated original full-resolution photo collections into `archive/original_photos/`.

2. **Mandatory 3-Document Rule & Content Boundaries**:
   - Created `.agents/agent_rules.md`.
   - Strict governance: the agent may maintain **only three** root system design documents (`README.md`, `PLANNING.md`, `JOURNAL.md`). Any walkthroughs or additional meta documents are unauthorized.
   - Strict content policy: the agent must **never** draft content documents, create content files, or write articles for Jim. All content authoring belongs 100% to Jim.

3. **Pure Semantic HTML5 & Modern CSS Architecture**:
   - Committed to 99.9% pure HTML5 and **zero client-side JavaScript**.
   - Crafted `assets/css/style.css` focusing on editorial typography (Charter / Sitka Text / Georgia serif body, clean sans headers and navigation, monospace code/data), comfortable line length (~70ch), fluid responsive grid, and native `@media (prefers-color-scheme: dark)` styling.
   - Design restraint inspired by Bear Blog (`pinewind.bearblog.dev`) and Mark Boulton (`markboulton.co.uk/journal/anewcanon/`).

4. **Core Structural Pages Created**:
   - `index.html`: Central home featuring tagline ("Out of My Lane"), bio overview, active lanes grid, and lakefront photography.
   - `about.html`: Personal profile covering Jim's 50-year career (Arthur Andersen, guitarist, tech startups, data science) and retirement philosophy.
   - `lanes.html`: Structured index of active pursuit lanes.
   - `journal.html`: Chronological journal index container with sample entries.
   - `gallery.html`: Photographic showcase with Chicago sky and botanical studies.
   - `.github/workflows/deploy.yml`: Automated Zero-JS audit, link integrity test, and direct GitHub Pages deployment.

5. **Automated Verification & CI Guardrails**:
   - Integrated `.github/workflows/deploy.yml` to run automated quality audits on every push before publishing.
   - Verified that all HTML files contain 0 `<script>` tags.
   - Verified that all internal page and image links resolve cleanly to existing local files.
   - Validated standard `<!DOCTYPE html>` structure and closed tags.
