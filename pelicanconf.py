"""
pelicanconf.py — Pelican Static Site Generator Configuration
for jimcollinsworth.github.io (Lakeview Theme & Lanes Pipeline)
"""

from __future__ import annotations

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

# Navigation Menu Configuration — strictly Home and About
MENUITEMS = (
    ('Home', '/index.html', 'index.html'),
    ('About', '/about.html', 'about'),
)

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Source directory layout
ARTICLE_PATHS = ['posts', 'ideas']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['media', 'extra', 'apps', 'data']

# Default all articles and pages to draft status
DEFAULT_METADATA = {
    'status': 'draft',
}

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

# Categories mapped to Lanes
CATEGORY_URL = 'lanes/{slug}.html'
CATEGORY_SAVE_AS = 'lanes/{slug}.html'
CATEGORIES_URL = 'lanes.html'
CATEGORIES_SAVE_AS = 'lanes.html'

# Tags
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'

ARCHIVES_SAVE_AS = 'posts.html'
INDEX_SAVE_AS = 'index.html'

# Disable authors
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Feeds disabled for development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Custom Lakeview Theme
THEME = 'themes/lakeview'

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
            if clean_target in ('lanes', 'categories'):
                return f'[{label}]({link_prefix}lanes.html)'
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
            if clean in ('lanes.md', 'lanes', 'categories.md', 'categories'):
                frag = target[len(clean):]
                return f'[{label}]({link_prefix}lanes.html{frag})'
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
            src = src_match.group(1).strip()
            if is_post and (src.startswith('media/') or src.startswith('images/') or src.startswith('attachments/')):
                src = '../' + src
            elif not is_post and src.startswith('../'):
                src = src.lstrip('../')

            return (
                f'<figure>\n'
                f'  <a href="{src}" class="photo-link" title="Click to view full screen">\n'
                f'    <img src="{src}" alt="{alt}" loading="lazy">\n'
                f'  </a>\n'
                f'  <figcaption>{alt}</figcaption>\n'
                f'</figure>'
            )

        return re.sub(r'<p>\s*<img\s+[^>]*alt="[^"]+"[^>]*\s*/?>\s*(?:</p>|\n)', fig_repl, html, flags=re.DOTALL)

    def _wrap_tables(self, html: str) -> str:
        def table_repl(m: re.Match) -> str:
            table_html = m.group(0)
            return f'<div class="table-container">\n{table_html}\n</div>'

        return re.sub(r'<table\b[^>]*>.*?</table>', table_repl, html, flags=re.DOTALL)

    def read(self, source_path: str) -> tuple[str, dict[str, Any]]:
        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])
        extra_meta: dict[str, Any] = {}

        with pelican_open(source_path) as text:
            # Strip UTF-8 BOM if present
            if text.startswith('\ufeff'):
                text = text[1:]

            m = re.match(r'^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$', text, re.DOTALL)
            if m:
                raw_meta, body = m.groups()
                parsed = yaml.safe_load(raw_meta) or {}

                # Normalize category/lanes in parsed dict for Pelican metadata parser
                if 'category' in parsed and parsed['category']:
                    parsed['category'] = str(parsed['category']).strip()
                elif 'lanes' in parsed and parsed['lanes']:
                    raw_lane = parsed['lanes']
                    if isinstance(raw_lane, list):
                        parsed['category'] = str(raw_lane[0]).strip()
                    else:
                        parsed['category'] = str(raw_lane).split(',')[0].strip()

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

                # Featured status
                if 'featured' in parsed:
                    extra_meta['featured'] = bool(parsed['featured'])

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

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        # Transfer extra parsed metadata
        for k, v in extra_meta.items():
            metadata[k] = v

        # Route ideas to output/ideas/{slug}.html
        if 'ideas' in Path(source_path).parts:
            slug = metadata.get('slug', '')
            if not slug and 'title' in metadata:
                slug = re.sub(r'[^a-z0-9]+', '-', str(metadata['title']).lower()).strip('-')
            if slug:
                metadata['url'] = f'ideas/{slug}.html'
                metadata['save_as'] = f'ideas/{slug}.html'

        return content, metadata


def merge_lane_and_tag_metadata(generator: Any) -> None:
    """
    Pelican signal handler to enrich Category (Lane) and Tag objects with
    authored Markdown prose, titles, summaries, and icons from content/lanes/
    or content/categories/ and content/tags/.
    Also prunes ghost categories so only authored lanes are emitted.
    """
    content_dir = Path(generator.settings.get('PATH', 'content')).resolve()
    lanes_dirs = [content_dir / 'lanes', content_dir / 'categories']
    tags_dir = content_dir / 'tags'
    md_parser = Markdown(**generator.settings.get('MARKDOWN', {}))

    # 1. Enrich Categories / Lanes
    authored_lanes: dict[str, dict[str, Any]] = {}
    for l_dir in lanes_dirs:
        if l_dir.exists():
            for p in l_dir.glob('*.md'):
                slug = p.stem.lower()
                text = p.read_text(encoding='utf-8-sig')
                m = re.match(r'^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$', text, re.DOTALL)
                if m:
                    meta = yaml.safe_load(m.group(1)) or {}
                    body = m.group(2).strip()
                    intro_html = md_parser.convert(body) if body else ''
                    authored_lanes[slug] = {
                        'title': meta.get('title', slug.capitalize()),
                        'icon': meta.get('icon', ''),
                        'summary': meta.get('summary', ''),
                        'image': meta.get('image', ''),
                        'intro_html': intro_html,
                    }

    # Filter categories in generator: keep only those with authored markdown files
    retained_categories: list[Any] = []
    for cat, articles in generator.categories:
        slug = cat.slug.lower()
        if slug in authored_lanes:
            lane_data = authored_lanes[slug]
            cat.name = lane_data['title']
            cat.slug = slug  # Re-assert slug after name assignment
            cat.title = lane_data['title']
            cat.icon = lane_data['icon']
            cat.summary = lane_data['summary']
            cat.image = lane_data['image']
            cat.intro_html = lane_data['intro_html']
            for art in articles:
                art.category = cat
            retained_categories.append((cat, articles))
        else:
            # Orphaned category lacking a definition file: clear category pointer on articles
            for art in articles:
                art.category = None

    generator.categories = retained_categories

    # 2. Enrich Tags
    if tags_dir.exists():
        for p in tags_dir.glob('*.md'):
            slug = p.stem.lower()
            text = p.read_text(encoding='utf-8-sig')
            m = re.match(r'^---\s*\r?\n(.*?)\r?\n---\s*\r?\n(.*)$', text, re.DOTALL)
            if m:
                meta = yaml.safe_load(m.group(1)) or {}
                body = m.group(2).strip()
                intro_html = md_parser.convert(body) if body else ''
            if hasattr(generator, 'tags'):
                tags_iter = generator.tags.items() if isinstance(generator.tags, dict) else generator.tags
                for item in tags_iter:
                    tag = item[0] if isinstance(item, tuple) else item
                    if tag.slug.lower() == slug:
                        tag.title = meta.get('title', slug.capitalize())
                        tag.summary = meta.get('summary', '')
                        tag.intro_html = intro_html


def add_obsidian_reader(readers_instance: Any) -> None:
    readers_instance.reader_classes['md'] = ObsidianMarkdownReader
    readers_instance.reader_classes['markdown'] = ObsidianMarkdownReader


signals.readers_init.connect(add_obsidian_reader)
signals.article_generator_finalized.connect(merge_lane_and_tag_metadata)
