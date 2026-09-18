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
        "prompt-history.html",
        "contact.html",
        "favicon.svg",
        "favicon.ico",
        "CNAME",
    ]
    for page in expected_pages:
        target = OUTPUT_DIR / page
        assert target.exists(), f"Expected {page} to exist in output/"

    assert (OUTPUT_DIR / "CNAME").read_text(encoding="utf-8").strip() == "jimcollinsworth.com"

    # lanes.html must not exist
    assert not (OUTPUT_DIR / "lanes.html").exists(), "lanes.html should be retired"


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
        "lake-michigan-microclimate-correlator.html",
        "offline-footnote-weaver.html",
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


def test_category_archive_pages_exist():
    """Verify that provenance category pages exist in output/category/ and lanes/ is absent."""
    expected_categories = [
        "ai.html",
        "mine.html",
        "ours.html",
    ]
    for cat in expected_categories:
        target = OUTPUT_DIR / "category" / cat
        assert target.exists(), f"Expected category archive {cat} in output/category/"

    # Entire legacy lanes directory should be absent
    assert not (OUTPUT_DIR / "lanes").exists(), "output/lanes/ should NOT exist"


def test_category_membership_and_type_evolution():
    """
    Verify:
    1. Articles appear in their assigned provenance category page (e.g. Digital Piano in Mine, Modern Wing in Ours).
    2. Post type short codes [TYPE] and evolution lineage appear in article headers.
    """
    mine_category = (OUTPUT_DIR / "category" / "mine.html").read_text(encoding="utf-8")
    ours_category = (OUTPUT_DIR / "category" / "ours.html").read_text(encoding="utf-8")

    assert "Digital Piano Enhancements" in mine_category, "Digital Piano should appear in Mine category"
    assert "M.E. (Mental Entity / My Essence)" in mine_category, "M.E. should appear in Mine category"
    assert "Modern Wing Encounters" in ours_category, "Modern Wing should appear in Ours category"

    # Post-type short codes verification (no brackets, icon-only category per Jim's instruction)
    piano_html = (OUTPUT_DIR / "posts" / "digital-piano-enhancements.html").read_text(encoding="utf-8")
    assert '<span class="post-type">PROJ</span>' in piano_html
    assert "(evolved from" not in piano_html
    assert 'class="category-badge"' in piano_html
    assert 'aria-label="Category: Mine"' in piano_html

    me_html = (OUTPUT_DIR / "posts" / "m-e-offline-ai-companion.html").read_text(encoding="utf-8")
    assert '<span class="post-type">IDEA</span>' in me_html
    assert 'class="category-badge"' in me_html
    assert 'aria-label="Category: Mine"' in me_html

    sleep_html = (OUTPUT_DIR / "posts" / "sleep-movement-evaluation-plan.html").read_text(encoding="utf-8")
    assert '<span class="post-type">SPEC</span>' in sleep_html
    assert "(evolved from" not in sleep_html
    assert 'class="category-badge"' in sleep_html
    assert 'aria-label="Category: Mine"' in sleep_html

    art_html = (OUTPUT_DIR / "posts" / "art-institute-chicago-modern-wing.html").read_text(encoding="utf-8")
    assert '<span class="post-type">VIEW</span>' in art_html
    assert "(evolved from" not in art_html
    assert 'class="category-badge"' in art_html
    assert 'aria-label="Category: Ours"' in art_html


def test_no_duplicate_page_titles():
    """
    Verify that standalone pages omit duplicate <h1> headers
    because the active menu tab already serves as the title.
    """
    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in about_html
    assert '<h1>About' not in about_html

    links_html = (OUTPUT_DIR / "links.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in links_html
    assert '<h1>Links' not in links_html
    assert 'class="active"' in links_html and 'Links</a>' in links_html

    ai_html = (OUTPUT_DIR / "ai.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in ai_html
    assert '<h1>AI' not in ai_html
    assert 'class="active"' in ai_html and 'AI</a>' in ai_html

    photos_html = (OUTPUT_DIR / "photos.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in photos_html
    assert '<h1>Photos' not in photos_html
    assert 'class="active"' in photos_html and 'Photos</a>' in photos_html

    posts_html = (OUTPUT_DIR / "posts.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in posts_html
    assert '<h1>Posts' not in posts_html
    assert 'class="active"' in posts_html and 'Posts</a>' in posts_html

    apps_html = (OUTPUT_DIR / "apps.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in apps_html
    assert '<h1>Apps' not in apps_html
    assert 'class="active"' in apps_html and 'Apps</a>' in apps_html


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
            if not link or link.startswith(("http", "https", "mailto", "tel", "javascript", "#", "${")):
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
    assert "History book mapper" in ideas_html
    assert "Offline Cross-Reference Footnote Weaver" in ideas_html

    # Assert ideas do NOT appear in main posts archive or index stream
    assert "History book mapper" not in posts_html
    assert "History book mapper" not in index_html
    assert "Offline Cross-Reference Footnote Weaver" not in posts_html
    assert "Offline Cross-Reference Footnote Weaver" not in index_html


def test_pure_markdown_content_sources():
    """
    Verify that all author-facing Markdown content files contain zero raw HTML tags.
    Note: Can be disabled or modified if optional inline HTML in Markdown sources is desired later.
    """
    content_dir = REPO_ROOT / "content"
    md_files = [
        f for f in content_dir.rglob("*.md")
        if f.name != "prompt-history.md" and "data" not in f.parts
    ]
    assert len(md_files) >= 20, f"Expected at least 20 Markdown content files, found {len(md_files)}"

    # Match any raw HTML opening/closing tag outside frontmatter
    raw_html_pattern = re.compile(r"<\/?[a-zA-Z][^>]*>", re.IGNORECASE)
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8")
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
    about_site_html = (OUTPUT_DIR / "about-this-site.html").read_text(encoding="utf-8")
    assert 'href="./prompt-history.html"' in about_site_html or 'href="prompt-history.html"' in about_site_html
    assert "Development Prompts" in about_site_html

    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert 'href="./posts.html#music"' in about_html or 'href="posts.html#music"' in about_html
    assert 'href="./links.html"' in about_html or 'href="links.html"' in about_html

    art_html = (OUTPUT_DIR / "posts" / "art-institute-chicago-modern-wing.html").read_text(encoding="utf-8")
    assert "<figure>" in art_html
    assert "<figcaption>" in art_html
    assert "Diffused ambient northern sky illumination" in art_html


def test_apps_page_does_not_contain_obsolete_static_data_table():
    """Verify that apps.html contains only intro copy and app cards, without the obsolete static data table."""
    apps_html = (OUTPUT_DIR / "apps.html").read_text(encoding="utf-8")
    assert "Static Data & Deployment Architecture" not in apps_html
    assert '<table' not in apps_html
    assert 'class="apps-grid"' in apps_html
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


def test_intra_page_provenance_and_markdown_shortcuts():
    """Verify that pure Markdown provenance shortcuts ([Mine], [AI], [Me]) compile to SVG badges."""
    about_site_html = (OUTPUT_DIR / "about-this-site.html").read_text(encoding="utf-8")
    assert 'icon-mine' in about_site_html
    assert 'icon-ai' in about_site_html
    assert 'Site History Haiku' in about_site_html
    assert '[Mine]' not in about_site_html, "[Mine] shortcut should be converted to SVG badge"
    assert '[AI]' not in about_site_html, "[AI] shortcut should be converted to SVG badge"

    apps_html = (OUTPUT_DIR / "apps.html").read_text(encoding="utf-8")
    assert 'icon-mine' in apps_html
    assert '[Mine]' not in apps_html

    photos_html = (OUTPUT_DIR / "photos.html").read_text(encoding="utf-8")
    assert 'icon-mine' in photos_html

    from pelicanconf import ObsidianMarkdownReader
    reader = ObsidianMarkdownReader.__new__(ObsidianMarkdownReader)
    test_html = "<h2>[Mine] My Heading</h2><p>[AI] AI Content</p><p>[AI+Mine] Dual Stewardship</p>"
    decorated = reader._decorate_provenance_badges(test_html)
    assert 'icon-mine' in decorated
    assert 'icon-ai' in decorated
    assert 'dual-badge' in decorated
    assert '[Mine]' not in decorated
    assert '[AI]' not in decorated
    assert '[Mine+AI]' not in decorated


def test_content_directory_contains_zero_ai_or_provenance_shortcuts():
    """Verify that all Markdown source files in content/ are 100% human-authored without [Mine] or [AI] tags."""
    content_md_files = [f for f in CONTENT_DIR.rglob("*.md") if "data" not in f.parts]
    for md_file in content_md_files:
        text = md_file.read_text(encoding="utf-8")
        assert "[Mine]" not in text, f"Found forbidden [Mine] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"
        assert "[AI]" not in text, f"Found forbidden [AI] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"
        assert "[Mine+AI]" not in text, f"Found forbidden [Mine+AI] tag in source Markdown {md_file.relative_to(REPO_ROOT)}"






