"""
pelicanconf.py — Pelican Static Site Generator Configuration
for jimcollinsworth.github.io
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml
from markdown import Markdown
from pelican import signals
from pelican.readers import MarkdownReader, pelican_open

AUTHOR = 'Jim Collinsworth'
SITENAME = 'Jim Collinsworth'
SITESUBTITLE = 'Out of My Lane'
SITEURL = ''

# Navigation Menu Configuration
# Permanent core items (Home, About, Posts) + configurable custom pages.
# Any custom page can also set `menu: true` in frontmatter to appear automatically.
MENUITEMS = (
    ('Home', '/index.html', 'index.html'),
    ('About', '/about.html', 'about'),
    ('Posts', '/posts.html', 'posts.html'),
    ('AI', '/ai.html', 'ai'),
    ('Links', '/links.html', 'links'),
    ('Photos', '/photos.html', 'photos'),
    ('Apps', '/apps.html', 'apps'),
    ('Site', '/about-this-site.html', 'about-this-site'),
)

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Source directory layout
ARTICLE_PATHS = ['posts', 'ideas']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra', 'apps', 'data']

# Copy root-level metadata files
EXTRA_PATH_METADATA = {
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googledaf3f946832f8abf.html': {'path': 'googledaf3f946832f8abf.html'},
    'extra/.nojekyll': {'path': '.nojekyll'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Clean URL structure
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
ARCHIVES_SAVE_AS = 'posts.html'
INDEX_SAVE_AS = 'index.html'
CATEGORIES_SAVE_AS = ''

# Disable author and tag pages
TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Disable feeds (pure static site)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Custom theme
THEME = 'theme'

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Relative URLs for reliable resolution locally and on GitHub Pages
RELATIVE_URLS = True

# Disable caching for clean, deterministic builds
LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIR = True

# Site summary data (AI haiku summary)
_SUMMARY_FILE = Path(__file__).parent / 'content' / 'data' / 'site-summary.json'
if _SUMMARY_FILE.exists():
    try:
        SITE_SUMMARY = json.loads(_SUMMARY_FILE.read_text(encoding='utf-8'))
    except Exception:
        SITE_SUMMARY = None
else:
    SITE_SUMMARY = None

# Recent releases data with exact timestamps
RECENT_RELEASES = [
    {
        "version": "v0.7.12",
        "timestamp": "Sept 15 2026, 11:45 AM CDT",
        "summary": "Intra-page provenance attribution, pure markdown shortcuts for Mine/AI, & rule codification",
    },
    {
        "version": "v0.7.11",
        "timestamp": "Sept 15 2026, 11:08 AM CDT",
        "summary": "Margin alignment across viewports, edge-to-edge photo bleed, static data table removal from apps & table scrollbars",
    },
    {
        "version": "v0.7.10",
        "timestamp": "Sept 15 2026, 9:38 AM CDT",
        "summary": "Chat bubbles for prompts, AI haiku summary generator, mobile header simplification & compact buttons",
    },
    {
        "version": "v0.7.9.01",
        "timestamp": "Sept 15 2026, 8:58 AM CDT",
        "summary": "Date architecture simplification (date as occurrence) & pure markdown validation",
    },
    {
        "version": "v0.7.9",
        "timestamp": "Sept 14 2026, 4:50 PM CDT",
        "summary": "Google Photos header badge, dedicated ideas directory, 2 new ideas",
    },
    {
        "version": "v0.7.8",
        "timestamp": "Sept 14 2026, 4:30 PM CDT",
        "summary": "Pure Markdown migration, automatic intra-site link resolution & blueprints",
    },
    {
        "version": "v0.7.7",
        "timestamp": "Sept 14 2026, 3:33 PM CDT",
        "summary": "Homepage photo spotlight & photo asset size management standards",
    },
    {
        "version": "v0.7.6",
        "timestamp": "Sept 14 2026, 2:59 PM CDT",
        "summary": "Condensed ideas stream & feed isolation",
    },
    {
        "version": "v0.7.5",
        "timestamp": "Sept 14 2026, 12:10 PM CDT",
        "summary": "Provenance stream relocation to About Site & bio update",
    },
]


class ObsidianMarkdownReader(MarkdownReader):
    """
    Reader for Obsidian Markdown files with YAML front-matter delimiters (---).
    Automatically parses YAML metadata, resolves Obsidian wikilinks and Markdown .md
    links to Pelican intra-site references, wraps standalone images into figures,
    and formats metadata for Pelican.
    """
    enabled = True
    file_extensions = ['md', 'markdown']
    _file_map: dict[str, str] | None = None

    @classmethod
    def _build_file_map(cls, content_root: Path) -> dict[str, str]:
        file_map: dict[str, str] = {}
        for p in content_root.rglob('*.md'):
            rel = p.relative_to(content_root).as_posix()
            file_map[p.name] = rel
            file_map[p.stem] = rel
            file_map[rel] = rel
        return file_map

    def _resolve_links(self, text: str) -> str:
        content_root = Path(self.settings.get('PATH', 'content')).resolve()
        if ObsidianMarkdownReader._file_map is None:
            ObsidianMarkdownReader._file_map = self._build_file_map(content_root)
        file_map = ObsidianMarkdownReader._file_map
        is_post = 'posts' in Path(self._source_path).parts or 'ideas' in Path(self._source_path).parts
        link_prefix = '../' if is_post else ''

        # 1. Resolve Obsidian Wikilinks: [[target|label]] or [[target]]
        def wikilink_sub(m: re.Match) -> str:
            target = m.group(1).strip()
            label = m.group(2).strip() if m.group(2) else target
            clean_target = target.removesuffix('.md').removesuffix('.markdown')
            if clean_target == 'posts':
                return f'[{label}]({link_prefix}posts.html)'
            resolved = file_map.get(target) or file_map.get(clean_target) or file_map.get(f'{clean_target}.md')
            if resolved:
                return f'[{label}]({{filename}}/{resolved})'
            return f'[{label}]({target})'

        text = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', wikilink_sub, text)

        # 2. Resolve standard Markdown links: [label](target.md) or [label](path/to/target.md)
        def mdlink_sub(m: re.Match) -> str:
            label = m.group(1)
            target = m.group(2).strip()
            if target.startswith(('http://', 'https://', 'mailto:', '#', '{filename}')):
                return m.group(0)
            clean = target.split('#')[0].split('?')[0]
            if clean in ('posts.md', 'posts.markdown', 'posts'):
                frag = target[len(clean):]
                return f'[{label}]({link_prefix}posts.html{frag})'
            if clean.endswith(('.md', '.markdown')):
                clean_name = Path(clean).name
                clean_stem = Path(clean).stem
                resolved = file_map.get(clean) or file_map.get(clean_name) or file_map.get(clean_stem)
                if resolved:
                    frag = target[len(clean):]
                    return f'[{label}]({{filename}}/{resolved}{frag})'
            return m.group(0)

        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', mdlink_sub, text)
        return text

    def _wrap_figures(self, html: str) -> str:
        is_post = 'posts' in Path(self._source_path).parts or 'ideas' in Path(self._source_path).parts
        def fig_repl(m: re.Match) -> str:
            full_tag = m.group(0)
            img_match = re.search(r'<img\s+([^>]*alt="([^"]+)"[^>]*)>', full_tag)
            if not img_match:
                return full_tag
            alt = img_match.group(2).strip()
            src_match = re.search(r'src="([^"]+)"', full_tag)
            if not src_match:
                return full_tag
            src = src_match.group(1).strip()
            if is_post and src.startswith('images/'):
                src = '../' + src
            elif not is_post and src.startswith('../images/'):
                src = src[3:]

            return (
                f'<figure>\n'
                f'  <a href="{src}" class="photo-link" title="Click to view full screen">\n'
                f'    <img src="{src}" alt="{alt}" loading="lazy">\n'
                f'  </a>\n'
                f'  <figcaption>{alt}</figcaption>\n'
                f'</figure>'
            )

        return re.sub(r'<p>\s*<img\s+[^>]*alt="[^"]+"[^>]*\s*/?>\s*</p>', fig_repl, html)

    def _wrap_tables(self, html: str) -> str:
        def table_repl(m: re.Match) -> str:
            table_html = m.group(0)
            return f'<div class="table-container">\n{table_html}\n</div>'

        return re.sub(r'<table\b[^>]*>.*?</table>', table_repl, html, flags=re.DOTALL)

    def _decorate_provenance_badges(self, html: str) -> str:
        category_svgs = {
            'Me': '<span class="category-badge" title="Provenance: Me" aria-label="Provenance: Me"><svg class="category-icon icon-me" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg></span>',
            'Mine': '<span class="category-badge" title="Provenance: Mine" aria-label="Provenance: Mine"><svg class="category-icon icon-mine" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span>',
            'AI': '<span class="category-badge" title="Provenance: AI" aria-label="Provenance: AI"><svg class="category-icon icon-ai" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg></span>',
            'Ours': '<span class="category-badge" title="Provenance: Ours" aria-label="Provenance: Ours"><svg class="category-icon icon-ours" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-3-3.87"></path><path d="M7 21v-2a4 4 0 0 1 3-3.87"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></span>',
            'Theirs': '<span class="category-badge" title="Provenance: Theirs" aria-label="Provenance: Theirs"><svg class="category-icon icon-theirs" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.75-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 2-2 3-3 4"></path><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.75-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 2-2 3-3 4"></path></svg></span>',
        }
        dual_ai_mine = '<span class="category-badge dual-badge" title="Provenance: AI & Mine" aria-label="Provenance: AI and Mine"><svg class="category-icon icon-ai" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg><svg class="category-icon icon-mine" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="margin-left: 2px;"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg></span>'

        # Dual provenance shortcuts
        html = html.replace('[AI+Mine]', dual_ai_mine).replace('[Mine+AI]', dual_ai_mine)

        # Single provenance shortcuts: [Mine], [AI], [Me], [Ours], [Theirs]
        for cat_name, badge_html in category_svgs.items():
            html = html.replace(f'[{cat_name}]', badge_html)
            html = html.replace(f'<li><strong>{cat_name}</strong>:', f'<li>{badge_html} <strong>{cat_name}</strong>:')

        return html

    def read(self, source_path: str) -> tuple[str, dict[str, Any]]:
        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])
        extra_meta: dict[str, Any] = {}

        with pelican_open(source_path) as text:
            m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
            if m:
                raw_meta, body = m.groups()
                parsed = yaml.safe_load(raw_meta) or {}

                # Category: Provenance (Me, Mine, AI, Ours, Theirs)
                cat = parsed.get('category') or parsed.get('lanes')
                if isinstance(cat, list) and cat:
                    raw_cat = str(cat[0]).strip()
                elif isinstance(cat, str) and cat:
                    raw_cat = str(cat.split(',')[0]).strip()
                else:
                    raw_cat = 'Mine'

                # Normalize 'AI Generated' -> 'AI', support Me, Mine, Ours, Theirs
                raw_lower = raw_cat.lower()
                if raw_lower in ['ai generated', 'ai-generated', 'ai']:
                    parsed['category'] = 'AI'
                elif raw_lower == 'me':
                    parsed['category'] = 'Me'
                elif raw_lower == 'ours':
                    parsed['category'] = 'Ours'
                elif raw_lower == 'theirs':
                    parsed['category'] = 'Theirs'
                else:
                    parsed['category'] = 'Mine'

                # Menu configuration support for pages
                if 'menu' in parsed:
                    extra_meta['menu'] = bool(parsed['menu'])
                if 'menu_order' in parsed:
                    try:
                        extra_meta['menu_order'] = int(parsed['menu_order'])
                    except (ValueError, TypeError):
                        extra_meta['menu_order'] = 99
                if 'menu_title' in parsed:
                    extra_meta['menu_title'] = str(parsed['menu_title']).strip()

                # Post type: single active short code (uppercase)
                if 'type' in parsed and parsed['type']:
                    parsed['type'] = str(parsed['type']).strip().upper()
                    extra_meta['type'] = parsed['type']

                # Type evolution: optional list of previous types
                if 'previous_types' in parsed and parsed['previous_types']:
                    raw_prev = parsed['previous_types']
                    if isinstance(raw_prev, list):
                        extra_meta['previous_types'] = [str(x).strip().upper() for x in raw_prev if str(x).strip()]
                    elif isinstance(raw_prev, str):
                        extra_meta['previous_types'] = [x.strip().upper() for x in raw_prev.split(',') if x.strip()]

                # Automatic link resolution for Obsidian Markdown links
                resolved_body = self._resolve_links(body)

                headers: list[str] = []
                for k, v in parsed.items():
                    if isinstance(v, list):
                        headers.append(f'{k}: ' + ', '.join(str(i) for i in v))
                    else:
                        headers.append(f'{k}: {v}')
                text = '\n'.join(headers) + '\n\n' + resolved_body
            else:
                text = self._resolve_links(text)

            content = self._md.convert(text)
            content = self._wrap_figures(content)
            content = self._wrap_tables(content)
            content = self._decorate_provenance_badges(content)

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        # Assign post type, type evolution lineage, and menu settings
        if 'type' in extra_meta:
            metadata['type'] = extra_meta['type']
        if 'previous_types' in extra_meta:
            metadata['previous_types'] = extra_meta['previous_types']
        if 'menu' in extra_meta:
            metadata['menu'] = extra_meta['menu']
        if 'menu_order' in extra_meta:
            metadata['menu_order'] = extra_meta['menu_order']
        if 'menu_title' in extra_meta:
            metadata['menu_title'] = extra_meta['menu_title']

        # Route ideas to output/ideas/{slug}.html
        if 'ideas' in Path(source_path).parts:
            slug = metadata.get('slug', '')
            if not slug and 'title' in metadata:
                slug = re.sub(r'[^a-z0-9]+', '-', str(metadata['title']).lower()).strip('-')
            if slug:
                metadata['url'] = f'ideas/{slug}.html'
                metadata['save_as'] = f'ideas/{slug}.html'

        return content, metadata


def add_obsidian_reader(readers_instance: Any) -> None:
    readers_instance.reader_classes['md'] = ObsidianMarkdownReader
    readers_instance.reader_classes['markdown'] = ObsidianMarkdownReader


signals.readers_init.connect(add_obsidian_reader)
