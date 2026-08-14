#!/usr/bin/env python3
"""Create a small source snapshot from public documentation pages."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
TARGETS_PATH = Path(__file__).with_name("targets.json")


@dataclass
class PageInfo:
    title: str
    url: str
    page_title: str = ""
    headings: list[str] = field(default_factory=list)
    links: list[dict[str, str]] = field(default_factory=list)


class OutlineParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.page_title = ""
        self.headings: list[str] = []
        self.links: list[dict[str, str]] = []
        self._tag: str | None = None
        self._href: str | None = None
        self._buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = dict(attrs)
        if tag in {"title", "h1", "h2", "h3", "a"}:
            self._tag = tag
            self._href = attrs_dict.get("href") if tag == "a" else None
            self._buffer = []

    def handle_data(self, data: str) -> None:
        if self._tag:
            self._buffer.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag != self._tag:
            return
        text = clean_text("".join(self._buffer))
        if not text:
            self._reset()
            return
        if tag == "title":
            self.page_title = text
        elif tag in {"h1", "h2", "h3"} and text not in self.headings:
            self.headings.append(text)
        elif tag == "a" and self._href:
            href = urljoin(self.base_url, self._href)
            if href.startswith("https://docs.spring.io/") or href.startswith("https://spring.io/"):
                self.links.append({"text": text, "url": href})
        self._reset()

    def _reset(self) -> None:
        self._tag = None
        self._href = None
        self._buffer = []


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def fetch(url: str) -> str:
    request = Request(url, headers={"User-Agent": "cocerebro-docs-to-skill/0.1"})
    with urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def parse_page(source: dict[str, str]) -> PageInfo:
    html = fetch(source["url"])
    parser = OutlineParser(source["url"])
    parser.feed(html)
    seen: set[str] = set()
    links: list[dict[str, str]] = []
    for link in parser.links:
        key = f"{link['text']}|{link['url']}"
        if key not in seen:
            seen.add(key)
            links.append(link)
    return PageInfo(
        title=source["title"],
        url=source["url"],
        page_title=parser.page_title,
        headings=parser.headings[:80],
        links=links[:160],
    )


def write_markdown(slug: str, target: dict[str, object], pages: list[PageInfo]) -> Path:
    out = ROOT / "sources" / f"{slug}-sources.md"
    lines = [
        f"# {target['name']} Sources",
        "",
        f"- Captured: {datetime.now(timezone.utc).isoformat()}",
        f"- Version hint: {target.get('version_hint', 'unknown')}",
        "- Policy: source links and outline only; no full documentation copy.",
        "",
    ]
    for page in pages:
        lines.extend(
            [
                f"## {page.title}",
                "",
                f"- URL: {page.url}",
                f"- Page title: {page.page_title or 'unknown'}",
                "",
                "### Headings",
                "",
            ]
        )
        for heading in page.headings[:30]:
            lines.append(f"- {heading}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("slug")
    args = parser.parse_args()

    targets = json.loads(TARGETS_PATH.read_text(encoding="utf-8"))
    if args.slug not in targets:
        print(f"Unknown target: {args.slug}", file=sys.stderr)
        print("Known targets: " + ", ".join(sorted(targets)), file=sys.stderr)
        return 2

    target = targets[args.slug]
    pages: list[PageInfo] = []
    errors: list[str] = []
    for source in target["sources"]:
        try:
            pages.append(parse_page(source))
        except (OSError, URLError) as exc:
            errors.append(f"{source['url']}: {exc}")

    snapshot = {
        "slug": args.slug,
        "name": target["name"],
        "version_hint": target.get("version_hint"),
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "pages": [page.__dict__ for page in pages],
        "errors": errors,
    }
    snapshot_path = ROOT / "sources" / f"{args.slug}-docs-snapshot.json"
    snapshot_path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
    markdown_path = write_markdown(args.slug, target, pages)
    print(f"Wrote {snapshot_path}")
    print(f"Wrote {markdown_path}")
    if errors:
        print("Completed with fetch errors:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
    return 0 if pages else 1


if __name__ == "__main__":
    raise SystemExit(main())
