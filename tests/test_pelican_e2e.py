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
        "prompt-history.html",
        "contact.html",
        "favicon.svg",
        "favicon.ico",
    ]
    for page in expected_pages:
        target = OUTPUT_DIR / page
        assert target.exists(), f"Expected {page} to exist in output/"

    # lanes.html must not exist
    assert not (OUTPUT_DIR / "lanes.html").exists(), "lanes.html should be retired"


def test_post_pages_exist():
    """Verify that all individual post HTML pages exist in output/posts/."""
    expected_posts = [
        "art-institute-chicago-modern-wing.html",
        "cordoba-stage-guitar.html",
        "digital-piano-enhancements.html",
        "m-e-offline-ai-companion.html",
        "sleep-movement-evaluation-plan.html",
        "ulu-knife-handle.html",
    ]
    for post in expected_posts:
        target = OUTPUT_DIR / "posts" / post
        assert target.exists(), f"Expected post {post} in output/posts/"


def test_category_archive_pages_exist():
    """Verify that provenance category pages exist in output/category/ and lanes/ is absent."""
    expected_categories = [
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

    # Post-type short codes and evolution lineage verification
    piano_html = (OUTPUT_DIR / "posts" / "digital-piano-enhancements.html").read_text(encoding="utf-8")
    assert '<span class="post-type">[PROJ]</span>' in piano_html
    assert "(evolved from" in piano_html
    assert '<span class="prev-type">IDEA</span>' in piano_html
    assert '<span class="prev-type">WIP</span>' in piano_html
    assert 'class="category-badge"' in piano_html
    assert 'Mine</span>' in piano_html

    me_html = (OUTPUT_DIR / "posts" / "m-e-offline-ai-companion.html").read_text(encoding="utf-8")
    assert '<span class="post-type">[IDEA]</span>' in me_html
    assert 'class="category-badge"' in me_html
    assert 'Mine</span>' in me_html

    sleep_html = (OUTPUT_DIR / "posts" / "sleep-movement-evaluation-plan.html").read_text(encoding="utf-8")
    assert '<span class="post-type">[SPEC]</span>' in sleep_html
    assert '<span class="prev-type">IDEA</span>' in sleep_html
    assert '<span class="prev-type">LOG</span>' in sleep_html
    assert 'class="category-badge"' in sleep_html
    assert 'Mine</span>' in sleep_html

    art_html = (OUTPUT_DIR / "posts" / "art-institute-chicago-modern-wing.html").read_text(encoding="utf-8")
    assert '<span class="post-type">[VIEW]</span>' in art_html
    assert '<span class="prev-type">TIL</span>' in art_html
    assert 'class="category-badge"' in art_html
    assert 'Ours</span>' in art_html


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
