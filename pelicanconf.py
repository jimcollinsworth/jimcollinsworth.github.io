"""
pelicanconf.py — Pelican Static Site Generator Configuration
for jimcollinsworth.github.io
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

PATH = 'content'
OUTPUT_PATH = 'output'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Source directory layout
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra', 'apps', 'data']

# Copy root-level metadata files
EXTRA_PATH_METADATA = {
    'extra/favicon.svg': {'path': 'favicon.svg'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/googledaf3f946832f8abf.html': {'path': 'googledaf3f946832f8abf.html'},
    'extra/.nojekyll': {'path': '.nojekyll'},
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


class ObsidianMarkdownReader(MarkdownReader):
    """
    Reader for Obsidian Markdown files with YAML front-matter delimiters (---).
    Automatically parses YAML metadata (provenance category, format short code,
    lifecycle evolution lineage, and keyword tags) and formats it for Pelican.
    """
    enabled = True
    file_extensions = ['md', 'markdown']

    def read(self, source_path: str) -> tuple[str, dict[str, Any]]:
        self._source_path = source_path
        self._md = Markdown(**self.settings['MARKDOWN'])
        extra_meta: dict[str, Any] = {}

        with pelican_open(source_path) as text:
            m = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', text, re.DOTALL)
            if m:
                raw_meta, body = m.groups()
                parsed = yaml.safe_load(raw_meta) or {}

                # Category: Provenance (Mine, AI Generated, Ours, Theirs)
                cat = parsed.get('category') or parsed.get('lanes')
                if isinstance(cat, list) and cat:
                    parsed['category'] = str(cat[0]).strip()
                elif isinstance(cat, str) and cat:
                    parsed['category'] = str(cat.split(',')[0]).strip()
                else:
                    parsed['category'] = 'Mine'

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

                headers: list[str] = []
                for k, v in parsed.items():
                    if isinstance(v, list):
                        headers.append(f'{k}: ' + ', '.join(str(i) for i in v))
                    else:
                        headers.append(f'{k}: {v}')
                text = '\n'.join(headers) + '\n\n' + body
            content = self._md.convert(text)

        if hasattr(self._md, 'Meta'):
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        # Assign post type and type evolution lineage
        if 'type' in extra_meta:
            metadata['type'] = extra_meta['type']
        if 'previous_types' in extra_meta:
            metadata['previous_types'] = extra_meta['previous_types']

        return content, metadata


def add_obsidian_reader(readers_instance: Any) -> None:
    readers_instance.reader_classes['md'] = ObsidianMarkdownReader
    readers_instance.reader_classes['markdown'] = ObsidianMarkdownReader


signals.readers_init.connect(add_obsidian_reader)
