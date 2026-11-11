"""Rend des slides HTML (1080x1350) en JPEG.

Usage : python3 tools/render.py posts/AAAA-MM-JJ
Le dossier doit contenir 1.html, 2.html, ... (images référencées en chemin relatif).
Produit 1.jpg, 2.jpg, ... à côté.

Dépendances : pip install --break-system-packages playwright
Navigateur : /usr/bin/google-chrome s'il existe, sinon `python3 -m playwright install chromium`.
"""
import asyncio, os, pathlib, sys
from playwright.async_api import async_playwright

folder = pathlib.Path(sys.argv[1]).resolve()
pages = sorted(folder.glob("[0-9]*.html"), key=lambda p: int(p.stem))


async def main():
    async with async_playwright() as p:
        kw = {"args": ["--allow-file-access-from-files"]}
        if os.path.exists("/usr/bin/google-chrome"):
            kw["executable_path"] = "/usr/bin/google-chrome"
        browser = await p.chromium.launch(**kw)
        page = await browser.new_page(viewport={"width": 1080, "height": 1350})
        for f in pages:
            await page.goto(f.as_uri())
            await page.evaluate("document.fonts.ready")
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(400)
            out = f.with_suffix(".jpg")
            await page.screenshot(path=str(out), type="jpeg", quality=92,
                                  clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            print("ok", out.name)
        await browser.close()

asyncio.run(main())
