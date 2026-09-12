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


