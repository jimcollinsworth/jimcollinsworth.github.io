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
from pelican.urlwrappers import Category

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
STATIC_PATHS = ['images', 'extra']

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
CATEGORY_URL = 'lanes/{slug}.html'
CATEGORY_SAVE_AS = 'lanes/{slug}.html'
ARCHIVES_SAVE_AS = 'posts.html'
INDEX_SAVE_AS = 'index.html'
CATEGORIES_SAVE_AS = 'lanes.html'

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
    Automatically parses YAML metadata (including multi-lane assignments and post-type
    evolution lineage) and formats it for Pelican's internal processor.
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

                # Multi-lane parsing: accept list or comma-separated string
                raw_lanes = parsed.get('lanes') or parsed.get('category')
                lanes_list: list[str] = []
                if isinstance(raw_lanes, list):
                    lanes_list = [str(l).strip() for l in raw_lanes if str(l).strip()]
                elif isinstance(raw_lanes, str):
                    lanes_list = [l.strip() for l in raw_lanes.split(',') if l.strip()]

                if lanes_list:
                    # Primary category for Pelican's native internals
                    parsed['category'] = lanes_list[0]
                    extra_meta['lanes_raw'] = lanes_list

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

        # Wrap all assigned lanes in Category objects
        if 'lanes_raw' in extra_meta:
            metadata['lanes'] = [Category(name, self.settings) for name in extra_meta['lanes_raw']]
        elif 'category' in metadata and isinstance(metadata['category'], Category):
            metadata['lanes'] = [metadata['category']]

        # Assign post type and type evolution lineage
        if 'type' in extra_meta:
            metadata['type'] = extra_meta['type']
        if 'previous_types' in extra_meta:
            metadata['previous_types'] = extra_meta['previous_types']

        return content, metadata


def assign_multi_lane_categories(generator: Any) -> None:
    """
    Populate multi-lane articles into all respective lane categories in Pelican's generator,
    ensuring that an article belonging to multiple lanes (e.g. [Music, Making])
    is generated on both lanes/music.html and lanes/making.html.
    """
    categories_map: dict[str, tuple[Category, list[Any]]] = {}

    # Map existing categories from generator
    for cat, arts in generator.categories:
        categories_map[cat.name] = (cat, list(arts))

    # Ensure every lane specified on every article is represented
    for article in generator.articles:
        lanes = getattr(article, 'lanes', [])
        if not lanes and hasattr(article, 'category'):
            lanes = [article.category]

        for lane in lanes:
            lane_name = lane.name if hasattr(lane, 'name') else str(lane)
            if lane_name not in categories_map:
                cat_obj = lane if isinstance(lane, Category) else Category(lane_name, generator.settings)
                categories_map[lane_name] = (cat_obj, [])

            cat_obj, arts = categories_map[lane_name]
            if article not in arts:
                arts.append(article)

    # Re-sort articles in each lane chronologically (newest first)
    reverse_archives = generator.context.get('NEWEST_FIRST_ARCHIVES', True)
    updated_categories: list[tuple[Category, list[Any]]] = []
    for cat_name, (cat_obj, arts) in sorted(
        categories_map.items(),
        reverse=generator.settings.get('REVERSE_CATEGORY_ORDER', False),
    ):
        arts_sorted = list(arts)
        arts_sorted.sort(key=lambda a: getattr(a, 'date', None), reverse=reverse_archives)
        updated_categories.append((cat_obj, arts_sorted))

    generator.categories = updated_categories
    generator.context['categories'] = updated_categories


def add_obsidian_reader(readers_instance: Any) -> None:
    readers_instance.reader_classes['md'] = ObsidianMarkdownReader
    readers_instance.reader_classes['markdown'] = ObsidianMarkdownReader


signals.readers_init.connect(add_obsidian_reader)
signals.article_generator_finalized.connect(assign_multi_lane_categories)
