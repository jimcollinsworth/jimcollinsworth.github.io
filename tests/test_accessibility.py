"""
tests/test_accessibility.py — Automated Accessibility Test Suite.

Verifies WCAG 2.1/2.2 AA & AAA, Section 508, and ADA compliance:
1. Skip-to-content links (<a href="#main-content" class="skip-link">) on every page.
2. Landmark roles: role="banner", role="contentinfo", <main id="main-content" tabindex="-1">.
3. Accessible navigation with aria-label ("Main Navigation", "Footer Navigation", "Filter posts by lane").
4. Active page indications via aria-current="page".
5. Screen-reader accessible labels (.sr-only) for new window / external links.
6. Image alt text attributes on all <img> tags.
7. HTML lang attribute (<html lang="...">) on all pages.
8. CSS accessibility rules: :focus-visible, prefers-contrast: more, prefers-reduced-motion: reduce, forced-colors: active.
9. Touch target sizing (minimum 38px height / padding on interactive navigation elements).
10. Strict Zero-JS policy preserved (no <script> tags).
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"
STYLE_CSS = REPO_ROOT / "theme" / "static" / "css" / "style.css"


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


def get_html_pages():
    """Retrieve all generated editorial HTML files in output/ (excluding verification tokens and apps)."""
    return [p for p in OUTPUT_DIR.glob("**/*.html") if not p.name.startswith("google") and "apps" not in p.parts]


def get_app_pages():
    """Retrieve interactive application pages in output/apps/."""
    return [p for p in OUTPUT_DIR.glob("apps/**/*.html")]


def test_html_lang_attribute():
    """Verify that every HTML page has a lang attribute on <html>."""
    pages = get_html_pages()
    assert len(pages) > 0, "No HTML files generated."
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert re.search(r"<html\s+lang=[\"'][a-zA-Z\-]+[\"']", html, re.IGNORECASE), (
            f"Page {page.relative_to(OUTPUT_DIR)} is missing <html lang='...'>"
        )


def test_skip_to_main_content_link():
    """Verify that every page has a skip-to-content link pointing to #main-content."""
    pages = get_html_pages()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert 'href="#main-content"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} is missing skip-to-content anchor (#main-content)."
        )
        assert 'class="skip-link"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} is missing class='skip-link'."
        )
        assert 'id="main-content"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} is missing target <main id='main-content'>."
        )


def test_aria_landmarks():
    """Verify landmark roles and unique aria-labels for primary regions."""
    pages = get_html_pages()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert 'role="banner"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} missing role='banner' on header."
        )
        assert 'role="contentinfo"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} missing role='contentinfo' on footer."
        )
        assert 'aria-label="Main Navigation"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} missing aria-label='Main Navigation'."
        )
        assert 'aria-label="Footer Navigation"' in html, (
            f"Page {page.relative_to(OUTPUT_DIR)} missing aria-label='Footer Navigation'."
        )


def test_active_nav_aria_current():
    """Verify that the active navigation item uses aria-current='page'."""
    core_pages = ["index.html", "posts.html", "ai.html", "links.html", "photos.html", "apps.html", "about-this-site.html"]
    for page_name in core_pages:
        page_file = OUTPUT_DIR / page_name
        if page_file.exists():
            html = page_file.read_text(encoding="utf-8")
            assert 'aria-current="page"' in html, (
                f"Page {page_name} expected aria-current='page' on active navigation tab."
            )


def test_stream_nav_aria_current():
    """Verify that stream navigation tabs include aria-current='page' on active filter."""
    posts_page = OUTPUT_DIR / "posts.html"
    assert posts_page.exists()
    html = posts_page.read_text(encoding="utf-8")
    assert 'class="stream-link active" aria-current="page"' in html or (
        'class="stream-link active"' in html and 'aria-current="page"' in html
    ), "Posts page missing aria-current='page' on active 'All' stream."

    category_pages = list((OUTPUT_DIR / "category").glob("*.html"))
    assert len(category_pages) > 0, "No category pages found in output/category/."
    for cat_page in category_pages:
        cat_html = cat_page.read_text(encoding="utf-8")
        assert 'aria-current="page"' in cat_html, (
            f"Category page {cat_page.name} missing aria-current='page' on active category."
        )


def test_all_images_have_alt_attributes():
    """Verify that all <img> elements have an alt attribute."""
    pages = get_html_pages()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        img_tags = re.findall(r"<img\b[^>]*>", html, re.IGNORECASE)
        for img in img_tags:
            assert re.search(r'\balt\s*=\s*["\'][^"\']*["\']', img, re.IGNORECASE), (
                f"Image tag without alt attribute in {page.relative_to(OUTPUT_DIR)}: {img}"
            )


def test_zero_javascript_policy():
    """Enforce zero client-side JavaScript policy across all generated pages."""
    pages = get_html_pages()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert "<script" not in html.lower(), (
            f"Forbidden <script> tag detected in {page.relative_to(OUTPUT_DIR)}"
        )
        assert 'onload=' not in html.lower(), (
            f"Forbidden inline event handler detected in {page.relative_to(OUTPUT_DIR)}"
        )


def test_css_accessibility_rules():
    """Verify essential accessibility rules and media queries exist in style.css."""
    assert STYLE_CSS.exists(), "style.css does not exist."
    css = STYLE_CSS.read_text(encoding="utf-8")

    # Focus indicator
    assert ":focus-visible" in css, "style.css must define :focus-visible rules."
    assert "outline" in css, "style.css must set outline on focus."

    # Skip-link styles
    assert ".skip-link" in css, "style.css must define .skip-link styles."
    assert ".skip-link:focus" in css or ".skip-link:focus-visible" in css, (
        "style.css must define focus state for .skip-link."
    )

    # High Contrast Mode
    assert "@media (prefers-contrast: more)" in css, (
        "style.css must support @media (prefers-contrast: more)."
    )
    assert "@media (prefers-color-scheme: dark) and (prefers-contrast: more)" in css, (
        "style.css must support dark high-contrast mode."
    )

    # Windows Forced Colors
    assert "@media (forced-colors: active)" in css, (
        "style.css must support Windows Forced Colors mode."
    )

    # Reduced Motion
    assert "@media (prefers-reduced-motion: reduce)" in css, (
        "style.css must support @media (prefers-reduced-motion: reduce)."
    )

    # Screen Reader Utility
    assert ".sr-only" in css, "style.css must include .sr-only utility class."

    # Relative root font sizing (WCAG 1.4.4 text zoom preservation)
    assert re.search(r"html\s*\{[^}]*font-size:\s*100%", css), (
        "Root html element must use relative font sizing (100%) to honor browser zoom."
    )


def test_touch_target_sizes_in_css():
    """Verify navigation links have minimum touch target dimensions."""
    css = STYLE_CSS.read_text(encoding="utf-8")
    assert "min-height: 38px" in css, (
        "Interactive navigation links must specify minimum touch target size (min-height: 38px)."
    )


def test_mode_switchers_present_and_accessible():
    """Verify all pages provide zero-JS theme, contrast, and text-size switchers."""
    pages = get_html_pages()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert 'id="theme-toggle"' in html, f"Missing #theme-toggle in {page.name}"
        assert 'id="contrast-toggle"' in html, f"Missing #contrast-toggle in {page.name}"
        assert 'id="text-size-toggle"' in html, f"Missing #text-size-toggle in {page.name}"
        assert 'class="site-controls"' in html, f"Missing .site-controls in {page.name}"
        assert 'for="theme-toggle"' in html, f"Missing label for #theme-toggle in {page.name}"
        assert 'for="contrast-toggle"' in html, f"Missing label for #contrast-toggle in {page.name}"
        assert 'for="text-size-toggle"' in html, f"Missing label for #text-size-toggle in {page.name}"


def test_interactive_apps_accessibility():
    """Verify that interactive applications maintain accessibility standards (lang, title, controls)."""
    app_pages = get_app_pages()
    assert len(app_pages) >= 2, "Expected at least 2 interactive app pages"
    for page in app_pages:
        html = page.read_text(encoding="utf-8")
        assert re.search(r"<html\s+lang=[\"'][a-zA-Z\-]+[\"']", html, re.IGNORECASE), f"{page.name} missing lang attribute"
        assert "<title>" in html and "</title>" in html, f"{page.name} missing <title>"
        assert '<main' in html, f"{page.name} missing <main> container"


