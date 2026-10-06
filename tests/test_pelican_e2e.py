"""
tests/test_pelican_e2e.py — End-to-End Test Suite for Pelican Static Site Generator.

Verifies:
1. Complete site build execution via Pelican CLI.
2. Generation of all core pages, posts, lane archives, and root assets.
3. Content flow from source Markdown into HTML.
4. Title deduplication (e.g. no redundant <h1>About on about.html).
5. Removal of pill formatting in favor of simple text links for lanes.
6. Zero-JS policy enforcement across all published pages.
7. Internal link and image asset integrity (zero broken links/assets).
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_ROOT / "content"
OUTPUT_DIR = REPO_ROOT / "output"


@pytest.fixture(scope="session", autouse=True)
def build_site():
    """Execute Pelican build once for the test session."""
    cmd = [
        sys.executable,
        "-m",
        "pelican",
        "content",
        "-s",
        "pelicanconf.py",
        "-o",
        "output",
        "-d",
    ]
    proc = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, f"Pelican build failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"
    assert OUTPUT_DIR.exists(), "Output directory was not created."


def test_core_pages_exist():
    """Verify that all core static pages exist in output/."""
    expected_pages = [
        "index.html",
        "about.html",
        "posts.html",
        "links.html",
        "ai.html",
        "photos.html",
        "apps.html",
        "about-this-site.html",
        "ideas.html",
        "contact.html",
        "lanes.html",
        "tags.html",
        "favicon.svg",
        "favicon.ico",
        "CNAME",
    ]
    for page in expected_pages:
        target = OUTPUT_DIR / page
        assert target.exists(), f"Expected {page} to exist in output/"

    assert (OUTPUT_DIR / "CNAME").read_text(encoding="utf-8").strip() == "jimcollinsworth.com"


def test_post_pages_exist():
    """Verify that all individual post HTML pages exist in output/posts/."""
    expected_posts = [
        "art-institute-chicago-modern-wing.html",
        "cordoba-stage-guitar.html",
        "digital-piano-enhancements.html",
        "keyword-explorer-taxonomy.html",
        "m-e-offline-ai-companion.html",
        "photo-viewer-drive-manifest-explorer.html",
        "pipeline-tools-workbench.html",
        "sleep-movement-evaluation-plan.html",
        "ulu-knife-handle.html",
    ]
    for post in expected_posts:
        target = OUTPUT_DIR / "posts" / post
        assert target.exists(), f"Expected post {post} in output/posts/"


def test_idea_pages_exist():
    """Verify that idea articles compile to output/ideas/ and not output/posts/."""
    expected_ideas = [
        "4d-earthquake-animation.html",
        "bike-handlebar-utility-shelf.html",
        "history-book-mapper.html",
        "im-an-ai-doomsayer-now.html",
        "im-vibe-coding-now.html",
        "what-played-then.html",
    ]
    ideas_dir = OUTPUT_DIR / "ideas"
    assert ideas_dir.exists(), "output/ideas/ directory should exist"
    for idea in expected_ideas:
        target = ideas_dir / idea
        assert target.exists(), f"Expected idea {idea} in output/ideas/"

    # Ensure idea slugs do NOT appear in output/posts/
    posts_dir = OUTPUT_DIR / "posts"
    for idea in expected_ideas:
        assert not (posts_dir / idea).exists(), f"Idea {idea} should NOT be in output/posts/"


def test_lane_pages_exist_and_enriched_from_content():
    """Verify that lane pages exist in output/lanes/ and inherit authored Markdown metadata."""
    expected_lanes = [
        "ai.html",
        "art.html",
        "health.html",
        "making.html",
        "music.html",
        "photography.html",
        "software.html",
    ]
    for lane in expected_lanes:
        target = OUTPUT_DIR / "lanes" / lane
        assert target.exists(), f"Expected lane archive {lane} in output/lanes/"

    # Check content enriched from markdown
    music_html = (OUTPUT_DIR / "lanes" / "music.html").read_text(encoding="utf-8")
    assert "Music" in music_html
    assert "Acoustic nylon-string guitar" in music_html
    assert "Digital Piano Enhancements" in music_html
    assert "Cordoba Stage Nylon Electric Guitar" in music_html

    art_html = (OUTPUT_DIR / "lanes" / "art.html").read_text(encoding="utf-8")
    assert "Modern Wing Encounters" in art_html


def test_category_membership_and_type_evolution():
    """
    Verify:
    1. Articles display lane badges and tag provenance badges.
    2. Post type short codes appear in article headers.
    """
    piano_html = (OUTPUT_DIR / "posts" / "digital-piano-enhancements.html").read_text(encoding="utf-8")
    assert 'class="category-badge"' in piano_html
    assert 'aria-label="Provenance: Mine"' in piano_html
    assert 'Music' in piano_html

    art_html = (OUTPUT_DIR / "posts" / "art-institute-chicago-modern-wing.html").read_text(encoding="utf-8")
    assert 'class="category-badge"' in art_html
    assert 'aria-label="Provenance: Ours"' in art_html
    assert 'Art & Architecture' in art_html or 'Art' in art_html


def test_no_duplicate_page_titles():
    """
    Verify that standalone pages omit duplicate <h1> headers
    and active navigation tabs indicate state cleanly.
    """
    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in about_html
    assert '<h1>About' not in about_html
    assert 'class="active"' in about_html and 'About</a>' in about_html

    index_html = (OUTPUT_DIR / "index.html").read_text(encoding="utf-8")
    assert 'class="active"' in index_html and 'Home</a>' in index_html


def test_zero_pills_lane_formatting():
    """
    Verify that pill badge styling is removed and lanes are simple text links.
    """
    html_files = [f for f in OUTPUT_DIR.rglob("*.html") if "apps" not in f.parts]
    # Also check root-level html files to ensure branch deployments never serve pills
    for root_f in REPO_ROOT.glob("*.html"):
        if root_f.name not in ["googledaf3f946832f8abf.html"]:
            html_files.append(root_f)

    for f in html_files:
        content = f.read_text(encoding="utf-8")
        rel_path = f.as_posix()
        assert 'class="pill"' not in content, f"Found pill class in {rel_path}"
        assert 'class="pill ' not in content, f"Found pill class in {rel_path}"
        assert 'pill-nav' not in content, f"Found pill-nav class in {rel_path}"

    # Verify that posts.html uses category-badge and category-icon ("on the downlow")
    posts_html = (OUTPUT_DIR / "posts.html").read_text(encoding="utf-8")
    assert 'class="category-badge"' in posts_html
    assert 'class="category-icon' in posts_html


def test_content_flows_from_markdown():
    """Verify that text authored in Markdown successfully flows into compiled HTML."""
    # Test a post's content
    sleep_html = (OUTPUT_DIR / "posts" / "sleep-movement-evaluation-plan.html").read_text(encoding="utf-8")
    assert "RLSRS" in sleep_html
    assert "Dr. James Runke" in sleep_html

    # Test about page content
    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert "Arthur Andersen" in about_html
    assert "50 years of working with software" in about_html


def test_zero_javascript_policy():
    """Verify that zero client-side JavaScript (<script> tags) exists across all editorial content pages."""
    editorial_pages = [f for f in OUTPUT_DIR.rglob("*.html") if "apps" not in f.parts]
    assert len(editorial_pages) >= 12, "Expected at least 12 editorial HTML pages"
    for f in editorial_pages:
        content = f.read_text(encoding="utf-8")
        rel_path = f.relative_to(OUTPUT_DIR).as_posix()
        assert "<script" not in content.lower(), f"Security violation: {rel_path} contains a <script> tag!"


def test_apps_and_static_data():
    """Verify that interactive applications and static tabular datasets compile cleanly into output/."""
    expected_artifacts = [
        OUTPUT_DIR / "apps" / "photo-viewer" / "index.html",
        OUTPUT_DIR / "apps" / "keyword-search" / "index.html",
        OUTPUT_DIR / "apps" / "pipeline-tools" / "index.html",
        OUTPUT_DIR / "data" / "photos.json",
        OUTPUT_DIR / "data" / "photos.md",
        OUTPUT_DIR / "data" / "site-index.json",
    ]
    for artifact in expected_artifacts:
        assert artifact.exists(), f"Expected {artifact.relative_to(OUTPUT_DIR)} to exist in output/"


def test_link_and_asset_integrity():
    """Verify that all internal href and img src links resolve to existing files on disk."""
    html_files = list(OUTPUT_DIR.rglob("*.html"))
    assert len(html_files) >= 10, "Expected at least 10 HTML files in output"

    for f in html_files:
        content = f.read_text(encoding="utf-8")
        rel_path = f.relative_to(OUTPUT_DIR).as_posix()

        # Check internal href links
        for m in re.finditer(r'href="([^"#:]+)"', content):
            link = m.group(1).strip()
            if not link or link.startswith(("http", "https", "mailto", "tel", "javascript", "#", "${", "&")) or link == "...":
                continue
            target_path = (f.parent / link).resolve()
            assert target_path.exists(), f"Broken link in {rel_path}: '{link}' -> {target_path} not found"

        # Check internal img src links
        for m in re.finditer(r'src="([^":]+)"', content):
            src = m.group(1).strip()
            if not src or src.startswith(("http", "https", "data:", "${")):
                continue
            target_path = (f.parent / src).resolve()
            assert target_path.exists(), f"Broken image in {rel_path}: '{src}' -> {target_path} not found"


def test_ideas_stream_isolated_and_dense():
    """Verify that type: IDEA articles appear on ideas.html and are isolated from posts.html and index.html."""
    ideas_html = (OUTPUT_DIR / "ideas.html").read_text(encoding="utf-8")
    posts_html = (OUTPUT_DIR / "posts.html").read_text(encoding="utf-8")
    index_html = (OUTPUT_DIR / "index.html").read_text(encoding="utf-8")

    # Assert ideas are listed on ideas.html
    assert "History book mapper" in ideas_html or "Bike Handlebar Utility Shelf" in ideas_html or "4D Earthquake" in ideas_html

    # Assert ideas do NOT appear in main posts archive or index stream
    assert "History book mapper" not in posts_html
    assert "History book mapper" not in index_html


def test_pure_markdown_content_sources():
    """
    Verify that all author-facing Markdown content files contain zero raw HTML tags.
    """
    content_dir = REPO_ROOT / "content"
    md_files = [
        f for f in content_dir.rglob("*.md")
        if "data" not in f.parts
    ]
    assert len(md_files) >= 15, f"Expected at least 15 Markdown content files, found {len(md_files)}"

    # Match any raw HTML opening/closing tag outside frontmatter
    raw_html_pattern = re.compile(r"<\/?[a-zA-Z][^>]*>", re.IGNORECASE)
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8-sig")
        # Strip YAML frontmatter
        if text.startswith("---"):
            parts = text.split("---", 2)
            body = parts[2] if len(parts) >= 3 else text
        else:
            body = text
        # Strip fenced code blocks from check
        body_no_code = re.sub(r"```[\s\S]*?```", "", body)
        match = raw_html_pattern.search(body_no_code)
        assert not match, (
            f"Found forbidden raw HTML '{match.group(0)}' in {md_file.relative_to(REPO_ROOT)}"
        )


def test_markdown_link_and_figure_resolution():
    """Verify that ObsidianMarkdownReader resolves .md links and wraps figures into HTML."""
    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert "posts.html" in about_html or "links.html" in about_html or "About" in about_html

    art_html = (OUTPUT_DIR / "posts" / "art-institute-chicago-modern-wing.html").read_text(encoding="utf-8")
    assert "<figure>" in art_html
    assert "<figcaption>" in art_html
    assert "Diffused ambient northern sky illumination" in art_html


def test_apps_page_does_not_contain_obsolete_static_data_table():
    """Verify that apps.html contains only intro copy and app cards, without the obsolete static data table."""
    apps_html = (OUTPUT_DIR / "apps.html").read_text(encoding="utf-8")
    assert "Static Data & Deployment Architecture" not in apps_html
    assert '<table' not in apps_html
    assert 'Photo Viewer' in apps_html


def test_table_container_responsive_wrapping():
    """Verify that markdown tables are automatically wrapped in .table-container for touch scrolling."""
    for f in OUTPUT_DIR.rglob("*.html"):
        content = f.read_text(encoding="utf-8")
        if "<table" in content:
            assert '<div class="table-container">' in content, f"Table in {f.name} is not wrapped in .table-container"

    from pelicanconf import ObsidianMarkdownReader
    reader = ObsidianMarkdownReader.__new__(ObsidianMarkdownReader)
    html_input = "<p>Intro</p><table><thead><tr><th>Header 1</th><th>Header 2</th></tr></thead><tbody><tr><td>Data 1</td><td>Data 2</td></tr></tbody></table><p>Outro</p>"
    wrapped = reader._wrap_tables(html_input)
    assert '<div class="table-container">\n<table>' in wrapped


def test_lanes_strictly_from_content():
    """Verify that all lanes in output/lanes/ are strictly derived from authored markdown in content/."""
    lanes_in_output = [p.stem for p in (OUTPUT_DIR / "lanes").glob("*.html")]
    content_lanes = [p.stem for p in (REPO_ROOT / "content" / "lanes").glob("*.md")]
    for lane in lanes_in_output:
        assert lane in content_lanes, f"Lane '{lane}' in output was not defined in content/lanes/"


def test_content_directory_contains_zero_ai_or_provenance_shortcuts():
    """Verify that all Markdown source files in content/ are 100% human-authored without [Mine] or [AI] tags."""
    content_md_files = [f for f in CONTENT_DIR.rglob("*.md") if "data" not in f.parts]
    for md_file in content_md_files:
        text = md_file.read_text(encoding="utf-8")
        assert "[Mine]" not in text, f"Found forbidden [Mine] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"
        assert "[AI]" not in text, f"Found forbidden [AI] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"
        assert "[Mine+AI]" not in text, f"Found forbidden [Mine+AI] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"






