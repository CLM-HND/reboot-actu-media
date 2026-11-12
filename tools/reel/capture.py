"""Capture une animation HTML image par image (window.render(t), window.DURATION) en PNG 1080x1920.
Usage : python3 capture.py reel.html frames/ 30
"""
import asyncio, os, pathlib, sys
from playwright.async_api import async_playwright

html, out, fps = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]), int(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)


async def main():
    async with async_playwright() as p:
        kw = {"args": ["--allow-file-access-from-files"]}
        if os.path.exists("/usr/bin/google-chrome"):
            kw["executable_path"] = "/usr/bin/google-chrome"
        b = await p.chromium.launch(**kw)
        page = await b.new_page(viewport={"width": 1080, "height": 1920})
        await page.goto(html.as_uri())
        await page.evaluate("document.fonts.ready")
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(500)
        dur = await page.evaluate("window.DURATION")
        n = int(dur * fps)
        stage = page.locator("#stage")
        for i in range(n):
            await page.evaluate(f"render({i / fps})")
            await stage.screenshot(path=str(out / f"f{i:05d}.png"))
        await b.close()
        print("frames", n, "duree", dur)

asyncio.run(main())
