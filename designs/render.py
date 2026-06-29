"""Render slide HTMLs to 1920×1080 PNGs via playwright."""
import os, glob
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SLIDES_DIR = ROOT / "slides"
BUILD_DIR = ROOT / "build"
BUILD_DIR.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1920, "height": 1080},
                              device_scale_factor=1)
    page = ctx.new_page()
    for html in sorted(SLIDES_DIR.glob("*.html")):
        out = BUILD_DIR / (html.stem + ".png")
        page.goto(f"file://{html.resolve()}")
        page.wait_for_timeout(800)  # give fonts a moment
        page.screenshot(path=str(out), full_page=False)
        print(f"  rendered  {out.name}")
    browser.close()

print(f"Done. Output in {BUILD_DIR}/")
