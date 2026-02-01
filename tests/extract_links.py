#!/usr/bin/env python3
"""
Extract all outbound links from HTML and JS files and generate a text file
listing each link with the page/source file it appears on.
Covers index.html and header.js (injected nav links).
"""

import re
from pathlib import Path
from urllib.parse import urlparse
from html.parser import HTMLParser
from collections import defaultdict
from datetime import datetime

# Base URL and domain for this site
BASE_URL = "https://aiboyscout.com"
BASE_DOMAIN = "aiboyscout.com"


class LinkExtractor(HTMLParser):
    """HTML parser to extract links from HTML files."""

    def __init__(self, source_file):
        super().__init__()
        self.source_file = source_file
        self.links = []
        self.current_tag = None
        self.current_attrs = {}

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_attrs = dict(attrs)

        if tag == "a" and "href" in self.current_attrs:
            href = self.current_attrs["href"]
            if href and not href.startswith("#") and not href.startswith("javascript:"):
                self.links.append(href)


def extract_urls_from_js(file_path):
    """Extract http(s) URLs from JavaScript (e.g. href="..." in template strings)."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Match href="https://..." or href='https://...'
        pattern = re.compile(r'href\s*=\s*["\'](https?://[^"\']+)["\']')
        return list(pattern.findall(content))
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []


def is_external_link(url):
    """Check if a URL is external (not pointing to the same site)."""
    if not url:
        return False

    if url.startswith("#") or url.startswith("javascript:") or url.startswith("mailto:") or url.startswith("tel:"):
        return False

    if not url.startswith("http://") and not url.startswith("https://"):
        return False

    try:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        if BASE_DOMAIN in domain or "jordanbaucke.github.io" in domain:
            return False
        return True
    except Exception:
        return False


def extract_links_from_html(file_path):
    """Extract all external links from an HTML file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        parser = LinkExtractor(file_path)
        parser.feed(content)

        return [link for link in parser.links if is_external_link(link)]
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return []


def main():
    """Extract links from index.html and header.js."""
    project_root = Path(__file__).parent.parent
    tests_dir = project_root / "tests"

    # Files to scan: HTML and JS that contain links on the page
    sources = [
        (project_root / "index.html", extract_links_from_html),
        (project_root / "header.js", extract_urls_from_js),
    ]

    link_map = defaultdict(list)

    for file_path, extract_fn in sources:
        if not file_path.exists():
            print(f"Warning: {file_path} not found")
            continue

        print(f"Processing {file_path.name}...")
        links = extract_fn(file_path)

        for link in links:
            if is_external_link(link):
                link_map[link].append(file_path.name)

    # Output: outbound_links.txt
    output_file = tests_dir / "outbound_links.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Outbound Links Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Generated: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"Total unique external links: {len(link_map)}\n\n")
        f.write("-" * 80 + "\n\n")

        for link in sorted(link_map.keys()):
            pages = sorted(set(link_map[link]))
            f.write(f"URL: {link}\n")
            f.write(f"Found on: {', '.join(pages)}\n")
            f.write("\n")

    print(f"\n✓ Extracted {len(link_map)} unique external links")
    print(f"✓ Report saved to: {output_file}")

    # Lychee input: one URL per line (for optional use)
    lychee_input = tests_dir / "lychee_input.txt"
    with open(lychee_input, "w", encoding="utf-8") as f:
        for link in sorted(link_map.keys()):
            f.write(f"{link}\n")

    print(f"✓ Lychee input file saved to: {lychee_input}")


if __name__ == "__main__":
    main()
