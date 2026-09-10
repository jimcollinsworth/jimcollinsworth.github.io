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
        "reads.html",
        "views.html",
        "gallery.html",
        "apps.html",
        "about-this-site.html",
        "lanes.html",
        "favicon.svg",
        "favicon.ico",
    ]
    for page in expected_pages:
        target = OUTPUT_DIR / page
        assert target.exists(), f"Expected {page} to exist in output/"


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


def test_lane_archive_pages_exist():
    """Verify that pursuit lane category pages exist in output/lanes/."""
    expected_lanes = [
        "art.html",
        "health.html",
        "ideas.html",
        "making.html",
        "music.html",
        "projects.html",
    ]
    for lane in expected_lanes:
        target = OUTPUT_DIR / "lanes" / lane
        assert target.exists(), f"Expected lane archive {lane} in output/lanes/"


def test_no_duplicate_page_titles():
    """
    Verify that standalone pages (About, Reads, Gallery) omit duplicate <h1> headers
    because the active menu tab already serves as the title.
    """
    about_html = (OUTPUT_DIR / "about.html").read_text(encoding="utf-8")
    assert '<h1 class="page-title"' not in about_html
    assert '<h1>About' not in about_html
    # Verify the active nav tab is set
    assert 'class="active"' in about_html and 'About</a>' in about_html

    reads_html = (OUTPUT_DIR / "reads.html").read_text(encoding="utf-8")
    assert '<h1>Reads' not in reads_html
    assert 'class="active"' in reads_html and 'Reads</a>' in reads_html

    gallery_html = (OUTPUT_DIR / "gallery.html").read_text(encoding="utf-8")
    assert '<h1>Gallery' not in gallery_html
    assert 'class="active"' in gallery_html and 'Gallery</a>' in gallery_html

    posts_html = (OUTPUT_DIR / "posts.html").read_text(encoding="utf-8")
    assert '<h1>Posts' not in posts_html
    assert 'class="active"' in posts_html and 'Posts</a>' in posts_html

    views_html = (OUTPUT_DIR / "views.html").read_text(encoding="utf-8")
    assert '<h1>Views' not in views_html
    assert 'class="active"' in views_html and 'Views</a>' in views_html

    apps_html = (OUTPUT_DIR / "apps.html").read_text(encoding="utf-8")
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

    # Verify that posts.html uses lane-nav and lane-link
    posts_html = (OUTPUT_DIR / "posts.html").read_text(encoding="utf-8")
    assert 'class="lane-nav"' in posts_html
    assert 'class="lane-link' in posts_html


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
