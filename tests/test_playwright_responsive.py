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
        "reads.html",
        "gallery.html",
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
    assert (index_dir / "preview.html").exists()
