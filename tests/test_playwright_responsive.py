"""
tests/test_playwright_responsive.py — Playwright Browser & Responsive Test Suite.

Verifies:
1. Headless Chromium loads core pages (index, about, posts, reads, gallery).
2. Zero console errors or unhandled page exceptions occur across responsive viewports.
3. Multi-resolution screenshot generator (tools/screenshots.py) functions correctly.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = REPO_ROOT / "output"


@pytest.fixture(scope="module")
def browser_context():
    """Launch headless Chromium browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.mark.parametrize(
    "page_name",
    [
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
    ],
)
@pytest.mark.parametrize(
    "viewport",
    [
        {"width": 390, "height": 844, "name": "phone_portrait"},
        {"width": 1920, "height": 1080, "name": "desktop_landscape"},
    ],
)
def test_pages_render_without_console_errors(browser_context, page_name, viewport):
    """Verify that pages load cleanly in Chromium with zero console errors or failed requests."""
    target_file = OUTPUT_DIR / page_name
    assert target_file.exists(), f"Target HTML file {target_file} does not exist"

    errors = []
    context = browser_context.new_context(
        viewport={"width": viewport["width"], "height": viewport["height"]}
    )
    page = context.new_page()
    page.on("pageerror", lambda err: errors.append(str(err)))
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

    try:
        response = page.goto(target_file.as_uri())
        assert response is not None
        assert response.status in [200, 0]  # 0 is standard for file:// schemes

        # Verify main content is rendered
        main_el = page.query_selector("main")
        assert main_el is not None, f"Missing <main> tag on {page_name}"

        # Ensure no uncaught errors
        assert len(errors) == 0, f"Page errors found on {page_name} ({viewport['name']}): {errors}"
    finally:
        context.close()


def test_screenshot_script_execution(tmp_path):
    """Verify that tools/screenshots.py executes cleanly via CLI and outputs images."""
    cmd = [
        sys.executable,
        str(REPO_ROOT / "tools" / "screenshots.py"),
        "--page",
        "index.html",
        "--outdir",
        str(tmp_path),
        "--device",
        "phone",
        "--orientation",
        "portrait",
    ]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
    assert proc.returncode == 0, f"Screenshot script failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}"

    index_dir = tmp_path / "index"
    assert index_dir.exists()
    screenshots = list(index_dir.glob("*.png"))
    assert len(screenshots) == 1
    screenshot = screenshots[0]
    # Verify non-empty screenshot with valid PNG header
    assert screenshot.stat().st_size > 5000, f"Screenshot file too small: {screenshot.stat().st_size} bytes"
    with open(screenshot, "rb") as sf:
        header = sf.read(8)
        assert header == b"\x89PNG\r\n\x1a\n", "Invalid PNG file header"
    assert (index_dir / "preview.html").exists()


def test_in_page_mode_switchers_interactive(browser_context):
    """Verify clicking theme, contrast, and text size switchers changes visual state in browser."""
    index_file = OUTPUT_DIR / "index.html"
    assert index_file.exists()

    page = browser_context.new_page()
    try:
        page.goto(f"file:///{index_file.as_posix()}")

        # Initial Light Theme
        initial_bg = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
        assert "250, 248, 245" in initial_bg  # #faf8f5

        # Click Theme Toggle -> switches to Dark
        page.click('label[for="theme-toggle"]')
        is_checked = page.evaluate("() => document.getElementById('theme-toggle').checked")
        assert is_checked is True, f"theme-toggle was not checked: {is_checked}"
        page.wait_for_function("() => window.getComputedStyle(document.body).backgroundColor.includes('20, 22, 23')")
        dark_bg = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
        assert "20, 22, 23" in dark_bg, f"dark_bg was {dark_bg}"

        # Click Contrast Toggle -> switches to High Contrast Dark & Low Complexity
        page.click('label[for="contrast-toggle"]')
        page.wait_for_function("() => window.getComputedStyle(document.body).backgroundColor.includes('0, 0, 0')")
        contrast_bg = page.evaluate("() => window.getComputedStyle(document.body).backgroundColor")
        assert "0, 0, 0" in contrast_bg  # #000000

        # Verify Low-Complexity mode: graphics hidden, nav remains clean 2-line row, desktop grid flattened
        nav_direction = page.evaluate("() => window.getComputedStyle(document.querySelector('nav.site-nav')).flexDirection")
        assert nav_direction == "row", f"Expected row nav direction, got {nav_direction}"
        img_display = page.evaluate("() => window.getComputedStyle(document.querySelector('.photo-stream img')).display")
        assert img_display == "none", f"Expected img display none in low complexity mode, got {img_display}"

        # Click Text Size Toggle -> dramatically increases body font size
        page.click('label[for="text-size-toggle"]')
        page.wait_for_function("() => parseFloat(window.getComputedStyle(document.body).fontSize) >= 24")
        enlarged_font_size = page.evaluate("() => parseFloat(window.getComputedStyle(document.body).fontSize)")
        assert enlarged_font_size >= 24, f"Expected enlarged font size >= 24px, got {enlarged_font_size}"
    finally:
        page.close()


@pytest.mark.parametrize(
    "page_rel_path",
    [
        "posts/art-institute-chicago-modern-wing.html",
        "photos.html",
    ],
)
@pytest.mark.parametrize(
    "viewport",
    [
        {"width": 390, "height": 844, "name": "phone_portrait"},
        {"width": 1366, "height": 768, "name": "laptop_landscape"},
    ],
)
def test_images_fit_viewport_width(browser_context, page_rel_path, viewport):
    """Verify that images and figures stay contained within viewport without horizontal overflow."""
    target_file = OUTPUT_DIR / page_rel_path
    assert target_file.exists(), f"Target file {target_file} does not exist"

    context = browser_context.new_context(
        viewport={"width": viewport["width"], "height": viewport["height"]}
    )
    page = context.new_page()
    try:
        page.goto(f"file:///{target_file.as_posix()}")
        page.wait_for_load_state("networkidle")

        # Check that page does not have horizontal scrollbar overflow
        scroll_width = page.evaluate("() => document.documentElement.scrollWidth")
        client_width = page.evaluate("() => document.documentElement.clientWidth")
        assert scroll_width <= client_width + 2, (
            f"Page {page_rel_path} has horizontal scroll overflow: scrollWidth={scroll_width}, clientWidth={client_width}"
        )

        # Check each image bounding box
        img_boxes = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('img:not(.mode-toggle-input)')).map(img => {
                const rect = img.getBoundingClientRect();
                return { src: img.src, width: rect.width, right: rect.right };
            });
        }""")
        for box in img_boxes:
            assert box["width"] <= viewport["width"] + 2, (
                f"Image {box['src']} width {box['width']} exceeds viewport {viewport['width']}"
            )
    finally:
        context.close()


def test_mobile_header_compact_and_landscape_single_line(browser_context):
    """Verify header is strictly 1-line in phone landscape and tagline is hidden on mobile."""
    target_file = OUTPUT_DIR / "about-this-site.html"
    assert target_file.exists()

    # Test Phone Landscape (844x390)
    context = browser_context.new_context(viewport={"width": 844, "height": 390})
    page = context.new_page()
    try:
        page.goto(f"file:///{target_file.as_posix()}")
        header_height = page.evaluate("() => document.querySelector('header.site-header').getBoundingClientRect().height")
        assert header_height <= 50, f"Header height in landscape phone was {header_height}px, expected <= 50px (single line)"

        tagline_display = page.evaluate("() => window.getComputedStyle(document.querySelector('.site-tagline')).display")
        assert tagline_display == "none", f"Tagline should be hidden in landscape phone, got {tagline_display}"
    finally:
        context.close()

    # Test Phone Portrait (390x844)
    context = browser_context.new_context(viewport={"width": 390, "height": 844})
    page = context.new_page()
    try:
        page.goto(f"file:///{target_file.as_posix()}")
        tagline_display = page.evaluate("() => window.getComputedStyle(document.querySelector('.site-tagline')).display")
        assert tagline_display == "none", f"Tagline should be hidden in portrait phone, got {tagline_display}"
    finally:
        context.close()


def test_streamlined_date_formats():
    """Verify dates across posts and archive match '%b %y' format (e.g. Aug 26)."""
    import re
    posts_file = OUTPUT_DIR / "posts.html"
    assert posts_file.exists()
    html = posts_file.read_text(encoding="utf-8")
    assert re.search(r"<time datetime=\"\d{4}-\d{2}-\d{2}\">[A-Z][a-z]{2} \d{2}</time>", html), (
        "Expected date format '%b %y' (e.g. Aug 26) in posts.html"
    )


def test_mobile_dynamic_dropdown_portrait(browser_context):
    """Verify dynamic hiding dropdown menu in mobile portrait mode with zero-JS disclosure."""
    test_cases = [
        ("index.html", "Home"),
        ("posts.html", "Posts"),
        ("about-this-site.html", "Site"),
        ("posts/art-institute-chicago-modern-wing.html", "Posts"),
    ]

    context = browser_context.new_context(viewport={"width": 390, "height": 844})
    page = context.new_page()
    try:
        for relative_url, expected_title in test_cases:
            target = OUTPUT_DIR / relative_url
            assert target.exists(), f"Target file does not exist: {target}"
            page.goto(f"file:///{target.resolve().as_posix()}")

            # 1. Verify desktop nav is hidden and dropdown is visible
            desktop_nav = page.locator(".desktop-nav")
            dropdown = page.locator(".mobile-nav-dropdown")
            summary = page.locator(".mobile-nav-summary")
            current_label = page.locator(".mobile-nav-current")

            assert not desktop_nav.is_visible(), f"Desktop nav should be hidden on mobile portrait ({relative_url})"
            assert dropdown.is_visible(), f"Mobile dropdown should be visible on mobile portrait ({relative_url})"
            assert current_label.inner_text().strip() == expected_title, (
                f"Expected mobile dropdown label '{expected_title}', got '{current_label.inner_text().strip()}' on {relative_url}"
            )

            # 2. Verify details disclosure is initially closed
            is_open = page.evaluate("() => document.querySelector('.mobile-nav-dropdown').hasAttribute('open')")
            assert not is_open, f"Dropdown should be initially closed on {relative_url}"

            # 3. Click summary to open details menu
            summary.click()
            is_open_after = page.evaluate("() => document.querySelector('.mobile-nav-dropdown').hasAttribute('open')")
            assert is_open_after, f"Dropdown should be open after clicking summary on {relative_url}"

            # 4. Verify menu contains links and active link has aria-current
            active_link = page.locator(".mobile-nav-menu a.active")
            assert active_link.is_visible(), f"Active link in mobile menu should be visible when open on {relative_url}"
            assert active_link.get_attribute("aria-current") == "page"

            # 5. Click summary again to close
            summary.click()
            is_closed_after = not page.evaluate("() => document.querySelector('.mobile-nav-dropdown').hasAttribute('open')")
            assert is_closed_after, f"Dropdown should close after second click on {relative_url}"
    finally:
        context.close()


def test_navigation_mode_switching_by_viewport(browser_context):
    """Verify responsive visibility: desktop nav on laptop & landscape, dropdown on portrait."""
    target = OUTPUT_DIR / "posts.html"
    assert target.exists()

    # A. Desktop Laptop (1366x768)
    ctx_desktop = browser_context.new_context(viewport={"width": 1366, "height": 768})
    page_d = ctx_desktop.new_page()
    page_d.goto(f"file:///{target.resolve().as_posix()}")
    assert page_d.locator(".desktop-nav").is_visible()
    assert not page_d.locator(".mobile-nav-dropdown").is_visible()
    ctx_desktop.close()

    # B. Phone Landscape (844x390)
    ctx_land = browser_context.new_context(viewport={"width": 844, "height": 390})
    page_l = ctx_land.new_page()
    page_l.goto(f"file:///{target.resolve().as_posix()}")
    assert page_l.locator(".desktop-nav").is_visible()
    assert not page_l.locator(".mobile-nav-dropdown").is_visible()
    land_height = page_l.evaluate("() => document.querySelector('header.site-header').getBoundingClientRect().height")
    assert land_height <= 50, f"Landscape header height was {land_height}px, expected <= 50px"
    ctx_land.close()

    # C. Phone Portrait (390x844)
    ctx_port = browser_context.new_context(viewport={"width": 390, "height": 844})
    page_p = ctx_port.new_page()
    page_p.goto(f"file:///{target.resolve().as_posix()}")
    assert not page_p.locator(".desktop-nav").is_visible()
    assert page_p.locator(".mobile-nav-dropdown").is_visible()
    ctx_port.close()




