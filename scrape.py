"""
AMC公式ドキュメントを取得し、1ページ1ファイルで docs/ に保存する。
あわせて、ドライブ用に全ページをURL順にまとめた amc_all_documentation.md を作る。

取得できたページ数が少なすぎる回は、何も書き換えずにエラーで終了する
（一時的に弾かれたときに「大量削除」のPRができるのを防ぐため）。
"""
import asyncio
import os
import re
import shutil
import sys
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright

START_URL = "https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud/overview"
TARGET_PREFIX = "https://advertising.amazon.com/API/docs/en-us/guides/amazon-marketing-cloud"
DOCS_DIR = Path("docs")
COMBINED_FILE = Path("amc_all_documentation.md")
COMBINED_HEADER = "# Amazon Marketing Cloud (AMC) Guides Consolidated Documentation\n"

# 取得ページ数の下限（絶対数）と、前回比でどこまでの減少を許すか
MIN_PAGES = int(os.environ.get("MIN_PAGES", "60"))
MAX_DROP_RATIO = float(os.environ.get("MAX_DROP_RATIO", "0.2"))

# 毎回変わりうる、中身と関係のない行（保存前に取り除く）
NOISE_LINES = {"Was this page helpful?", "Loading...", "Loading"}


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}".rstrip("/")


def url_to_filename(url: str) -> str:
    """URLのパスからファイル名を作る（例: .../admin/instance-management → admin__instance-management.md）"""
    rest = url[len(TARGET_PREFIX):].strip("/") or "index"
    rest = re.sub(r"[^A-Za-z0-9_\-/]", "_", rest)
    return rest.replace("/", "__") + ".md"


def clean_markdown(text: str) -> str:
    lines = [ln.rstrip() for ln in text.splitlines()]
    lines = [ln for ln in lines if ln.strip() not in NOISE_LINES]
    text = "\n".join(lines)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


async def expand_all_sidebar_menus(page):
    """左側の折りたたまれているツリーメニューをすべてクリックして展開する"""
    for _ in range(5):
        toggles = await page.locator(
            "nav button[aria-expanded='false'], aside button[aria-expanded='false'], .menu-item button"
        ).all()
        if not toggles:
            break
        for btn in toggles:
            try:
                if await btn.is_visible():
                    await btn.click(timeout=1000)
                    await page.wait_for_timeout(200)
            except Exception:
                pass


def extract_main(soup: BeautifulSoup):
    main_elem = (
        soup.find("main")
        or soup.find(attrs={"role": "main"})
        or soup.find("article")
        or soup.find(
            "div",
            class_=lambda c: c and any(k in c for k in ["doc-content", "main-content", "page-content"]),
        )
        or soup.body
    )
    if not main_elem:
        return None
    for noise in main_elem.find_all(["nav", "header", "footer", "aside", "script", "style", "iframe"]):
        noise.decompose()
    for noise in main_elem.find_all(
        "div",
        class_=lambda c: c and any(k in c.lower() for k in ["sidebar", "nav", "menu", "breadcrumb", "toc"]),
    ):
        noise.decompose()
    return main_elem


async def crawl() -> dict:
    """{url: (title, markdown)} を返す"""
    pages = {}
    visited = set()
    queue = deque([normalize_url(START_URL)])

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        print("初期ページを読み込み、メニューツリーを展開中...")
        await page.goto(START_URL, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)
        await expand_all_sidebar_menus(page)
        for a in BeautifulSoup(await page.content(), "html.parser").find_all("a", href=True):
            link = normalize_url(urljoin(START_URL, a["href"]))
            if link.startswith(TARGET_PREFIX) and link not in queue:
                queue.append(link)
        print(f"検出された対象URL数: {len(queue)} 件")

        while queue:
            current_url = queue.popleft()
            if current_url in visited:
                continue
            visited.add(current_url)
            print(f"[{len(visited)}] 取得中: {current_url}")
            try:
                await page.goto(current_url, wait_until="networkidle", timeout=30000)
                try:
                    await page.wait_for_selector("h1, [role='main']", timeout=8000)
                    await page.wait_for_function(
                        '() => !document.body.innerText.trim().startsWith("Loading")', timeout=5000
                    )
                except Exception:
                    await page.wait_for_timeout(1500)

                soup = BeautifulSoup(await page.content(), "html.parser")
                for a_tag in soup.find_all("a", href=True):
                    link = normalize_url(urljoin(current_url, a_tag["href"]))
                    if link.startswith(TARGET_PREFIX) and link not in visited and link not in queue:
                        queue.append(link)

                main_elem = extract_main(soup)
                if main_elem is None:
                    continue
                body = clean_markdown(md(str(main_elem), heading_style="ATX", strip=["img"]))
                if not body or body.lower().startswith("loading"):
                    print("  -> 本文が空のためスキップ")
                    continue
                title = soup.title.get_text(strip=True) if soup.title else current_url
                pages[current_url] = (title, body)
            except Exception as e:
                print(f"  -> エラー ({current_url}): {e}")
            await asyncio.sleep(0.8)

        await browser.close()
    return pages


def check_page_count(new_count: int) -> None:
    prev_count = len(list(DOCS_DIR.glob("*.md"))) if DOCS_DIR.exists() else 0
    print(f"今回 {new_count} ページ / 前回 {prev_count} ページ")
    if new_count < MIN_PAGES:
        sys.exit(f"取得ページ数が下限（{MIN_PAGES}）を下回ったため、更新せずに終了します。")
    if prev_count and new_count < prev_count * (1 - MAX_DROP_RATIO):
        sys.exit(f"前回より{MAX_DROP_RATIO:.0%}以上減ったため、取得失敗とみなして更新せずに終了します。")


def write_outputs(pages: dict) -> None:
    # docs/ を作り直す（消えたページはPRで「削除」として見える）
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir()
    for url, (title, body) in pages.items():
        (DOCS_DIR / url_to_filename(url)).write_text(
            f"# {title}\n**URL:** {url}\n\n{body}\n", encoding="utf-8"
        )

    # ドライブ用のまとめファイル（URL順）
    parts = [COMBINED_HEADER]
    for url in sorted(pages):
        title, body = pages[url]
        parts.append(f"\n---\n# {title}\n**URL:** {url}\n\n{body}\n")
    COMBINED_FILE.write_text("".join(parts), encoding="utf-8")
    print(f"保存完了: docs/ に {len(pages)} ファイル、{COMBINED_FILE}")


if __name__ == "__main__":
    result = asyncio.run(crawl())
    check_page_count(len(result))
    write_outputs(result)
