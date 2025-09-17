#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 Alvaro Orozco

import os
import re
import sys
import yaml
import unicodedata
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BASE_DIR = SCRIPT_DIR.parent
SECTIONS_DIR = BASE_DIR / "sections"

SCHEMA_FILE = BASE_DIR / "schema.yaml"
OUTPUT_FILE = BASE_DIR / "README.md"
OUTPUT_IMG_DIR = OUTPUT_FILE.parent / "img"

def sanitize_string(path: str) -> str:
    """Python equivalent of the Go sanitizeString: produce safe snake_case filenames."""
    t = unicodedata.normalize("NFD", path)
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    t = t.replace(" ", "_").replace("-", "_")
    t = re.sub(r"[^a-zA-Z0-9_./]", "", t)
    t = t.lower()
    t = re.sub(r"_+", "_", t)
    t = t.replace("_.md", ".md")
    return os.path.normpath(t)

def load_schema():
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if isinstance(data, dict) and "sections" in data:
        return data["sections"]
    if isinstance(data, list):
        return data
    raise ValueError("schema.yaml must be either a list or a dict with key 'sections'")

def section_filename(section: dict, parent_path: Path) -> Path | None:
    key = section.get("alias") or section.get("Alias") or section.get("title") or section.get("Title")
    if not key:
        return None
    rel = sanitize_string(f"{key}.md")
    return parent_path / rel

def read_markdown(md_path: Path) -> str:
    if md_path and md_path.exists():
        try:
            content = md_path.read_text(encoding="utf-8").strip()
            content = rewrite_image_paths(content)
            return content + "\n"
        except Exception as e:
            print(f"[ERROR] Reading {md_path}: {e}", file=sys.stderr)
    else:
        print(f"[WARNING] File not found: {md_path}", file=sys.stderr)
    return ""

def rewrite_image_paths(content: str) -> str:
    """Rewrite relative image paths to point to the local img/ directory."""
    # Rewrite Markdown images: ![alt](path) or [text](path) if path points to img/
    content = re.sub(
        r'(!?\[.*?\]\()([^\)]+img[^\)]+)(\))',
        lambda m: f"{m.group(1)}img/{Path(m.group(2)).name}{m.group(3)}",
        content
    )
    # Rewrite HTML <img src="path">
    content = re.sub(
        r'(<img\s+[^>]*src=["\'])([^"\']+img/[^"\']+)(["\'])',
        lambda m: f'{m.group(1)}img/{Path(m.group(2)).name}{m.group(3)}',
        content
    )
    return content

def build_document(sections, parent_dir: Path, level=1) -> str:
    parts = []
    for section in sections or []:
        title = (section.get("title") or section.get("Title") or
                 section.get("alias") or section.get("Alias") or "Section").strip()

        children = section.get("children") or section.get("Children") or []

        if children:
            # Parent sections need headers
            parts.append(f"{'#' * level} {title}\n\n")

            child_dir_name = sanitize_string(section.get("alias") or section.get("title") or "")
            next_dir = parent_dir / child_dir_name
            parts.append(build_document(children, next_dir, level + 1))
        else:
            # Leaf sections already contain headers
            md_path = section_filename(section, parent_dir)
            if md_path is not None:
                content = read_markdown(md_path)
                if content:
                    parts.append(content)
                    if not content.endswith("\n"):
                        parts.append("\n")

        if parts and not parts[-1].endswith("\n\n"):
            parts.append("\n")
    return "".join(parts)

def main():
    if not SCHEMA_FILE.exists():
        print(f"Error: {SCHEMA_FILE} not found.", file=sys.stderr)
        sys.exit(1)
    if not SECTIONS_DIR.exists():
        print(f"Error: {SECTIONS_DIR} not found.", file=sys.stderr)
        sys.exit(1)

    sections = load_schema()
    document_content = build_document(sections, SECTIONS_DIR)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(document_content)

    print(f"README generated successfully: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
