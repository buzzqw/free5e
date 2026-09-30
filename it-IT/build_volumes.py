#!/usr/bin/env python3
"""Assemble the three Italian Free5e books into standalone Markdown files.

The repository stores each book as a tree of Markdown files.  This script keeps
that layout as the source of truth and creates one self-contained Markdown file
per core volume.  The source directory can be changed with ``--source`` so the
same command also works with a separate copy of the translation material.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit


@dataclass(frozen=True)
class Book:
    directory: str
    main_file: str
    output_file: str


BOOKS = (
    Book("Characters_Codex", "Characters_Codex.md", "Characters_Codex.md"),
    Book(
        "Conductors_Companion",
        "Conductors_Companion.md",
        "Conductors_Companion.md",
    ),
    Book(
        "Monstrous_Manuscript",
        "Monstrous_Manuscript.md",
        "Monstrous_Manuscript.md",
    ),
)

# Markdown links with a target containing spaces should use angle brackets;
# all links in the repository use the simpler, unquoted form.  The optional
# tail preserves a Markdown link title, if one is present.
MARKDOWN_LINK = re.compile(
    r"(?P<image>!?)\[(?P<label>[^\]]*)\]"
    r"\((?P<target><[^>]*>|[^\s)]+)(?P<tail>[^)]*)\)"
)
FRONT_MATTER = re.compile(r"\A---\s*\n.*?\n---\s*(?:\n|\Z)", re.DOTALL)


class BuildError(RuntimeError):
    """An error that should be shown without a Python traceback."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Crea i tre volumi italiani completi in Markdown."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="cartella che contiene i tre alberi dei libri (predefinita: it-IT)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="cartella di destinazione (predefinita: <source>/volumes)",
    )
    parser.add_argument(
        "--book",
        dest="books",
        action="append",
        choices=[book.directory for book in BOOKS],
        help="genera solo questo libro; può essere specificato più volte",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="interrompe la generazione se trova un link Markdown locale mancante",
    )
    parser.add_argument(
        "--keep-links",
        action="store_true",
        help="non converte i link ai file sorgente in ancore interne",
    )
    return parser.parse_args()


def local_target(source_file: Path, target: str, book_root: Path) -> Path | None:
    """Resolve a local Markdown link, or return ``None`` for other URLs."""

    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or not parsed.path.lower().endswith(".md"):
        return None

    candidate = (source_file.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(book_root.resolve())
    except ValueError:
        return None
    return candidate


def linked_files(source_file: Path, text: str, book_root: Path) -> list[Path]:
    """Return local Markdown targets in the order in which they occur."""

    targets: list[Path] = []
    for match in MARKDOWN_LINK.finditer(text):
        if match.group("image"):
            continue
        target = local_target(source_file, match.group("target"), book_root)
        if target is not None:
            targets.append(target)
    return targets


def collect_order(book_root: Path, main_file: Path) -> tuple[list[Path], list[str]]:
    """Follow the book indexes, then append any unlinked Markdown files.

    A depth-first walk preserves the order of each book's existing indexes and
    puts an index before the files it references.  The fallback is important
    for source material that has not yet been added to an index.
    """

    all_files = sorted(book_root.rglob("*.md"))
    all_files_set = set(all_files)
    ordered: list[Path] = []
    visited: set[Path] = set()
    warnings: list[str] = []

    def visit(path: Path) -> None:
        path = path.resolve()
        if path in visited:
            return
        if path not in all_files_set:
            warnings.append(f"link locale mancante: {path.relative_to(book_root)}")
            return

        visited.add(path)
        ordered.append(path)
        text = path.read_text(encoding="utf-8")
        for target in linked_files(path, text, book_root):
            visit(target)

    visit(main_file)
    for path in all_files:
        visit(path)

    return ordered, sorted(set(warnings))


def anchor_for(book: Book, relative_file: Path) -> str:
    """Create a stable, HTML-safe anchor for a source file."""

    value = "-".join(relative_file.with_suffix("").parts)
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", value).strip("-").lower()
    return f"volume-{book.directory.lower()}-{value}"


def explicit_anchors(text: str) -> set[str]:
    """Collect anchors that are explicitly present in a source file."""

    anchors: set[str] = set()
    for match in re.finditer(
        r'<a\s+[^>]*id=["\']([^"\']+)["\']|\{#([^}]+)\}', text
    ):
        anchors.add(match.group(1) or match.group(2))
    return anchors


def fragment_aliases(files: list[Path], texts: dict[Path, str]) -> dict[Path, set[str]]:
    """Restore renderer-generated cross-file fragment IDs.

    The original build gives every file an ID such as
    ``Acid_Splash_acid_splash``.  Once files are concatenated, that ID is no
    longer generated automatically by Markdown, so add it as a small alias at
    the beginning of the corresponding section.
    """

    explicit = set().union(*(explicit_anchors(texts[path]) for path in files))
    fragments: set[str] = set()
    for text in texts.values():
        fragments.update(re.findall(r"\]\(#([^\s)]+)", text))

    aliases: dict[Path, set[str]] = {path: set() for path in files}
    for fragment in fragments - explicit:
        candidates = [
            path
            for path in files
            if fragment == path.stem or fragment.startswith(f"{path.stem}_")
        ]
        if candidates:
            target = max(candidates, key=lambda path: len(path.stem))
            aliases[target].add(fragment)
    return aliases


def rewrite_links(
    text: str,
    source_file: Path,
    book_root: Path,
    book: Book,
    anchors: dict[Path, str],
    source_anchors: dict[Path, set[str]],
    asset_root: Path,
    destination: Path,
) -> str:
    """Turn links to source files into links to sections in the volume."""

    def replace(match: re.Match[str]) -> str:
        if match.group("image"):
            target_text = match.group("target")
            plain_target = (
                target_text[1:-1]
                if target_text.startswith("<") and target_text.endswith(">")
                else target_text
            )
            parsed = urlsplit(plain_target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                return match.group(0)
            asset = (source_file.parent / unquote(parsed.path)).resolve()
            try:
                asset.relative_to(asset_root.resolve())
            except ValueError:
                return match.group(0)
            if not asset.is_file():
                return match.group(0)
            relative_asset = Path(
                os.path.relpath(asset, destination.parent)
            ).as_posix()
            return (
                f"![{match.group('label')}]({relative_asset}"
                f"{match.group('tail')})"
            )

        target_text = match.group("target")
        target = local_target(source_file, target_text, book_root)
        if target is None or target not in anchors:
            return match.group(0)

        parsed = urlsplit(
            target_text[1:-1]
            if target_text.startswith("<") and target_text.endswith(">")
            else target_text
        )
        # A fragment generated by the original multi-file renderer may no
        # longer exist after concatenation.  Keep explicit anchors, otherwise
        # land on the beginning of the referenced source file.
        fragment = (
            parsed.fragment
            if parsed.fragment and parsed.fragment in source_anchors[target]
            else ""
        )
        destination_link = f"#{fragment}" if fragment else f"#{anchors[target]}"
        return f"[{match.group('label')}]({destination_link}{match.group('tail')})"

    return MARKDOWN_LINK.sub(replace, text)


def without_front_matter(text: str) -> str:
    """Remove document metadata from included files."""

    return FRONT_MATTER.sub("", text, count=1)


def italian_front_matter(text: str) -> str:
    """Ensure the generated Italian book advertises the correct language."""

    if not FRONT_MATTER.match(text):
        return text
    return re.sub(r"(?m)^lang:\s*[^\n]+$", "lang: it", text, count=1)


def build_book(
    source: Path,
    output: Path,
    book: Book,
    *,
    strict: bool,
    keep_links: bool,
) -> tuple[Path, int, list[str]]:
    book_root = (source / book.directory).resolve()
    main_file = book_root / book.main_file
    if not book_root.is_dir():
        raise BuildError(f"cartella del libro non trovata: {book_root}")
    if not main_file.is_file():
        raise BuildError(f"indice principale non trovato: {main_file}")

    files, warnings = collect_order(book_root, main_file)
    if strict and warnings:
        raise BuildError(f"{book.directory}: " + "; ".join(warnings))

    source_texts = {
        path: path.read_text(encoding="utf-8").replace("\r\n", "\n")
        for path in files
    }
    aliases = fragment_aliases(files, source_texts)
    anchors = {
        path: anchor_for(book, path.relative_to(book_root)) for path in files
    }
    source_anchors = {
        path: explicit_anchors(source_texts[path]) | aliases[path] for path in files
    }
    destination = output / book.output_file
    sections: list[str] = []
    for index, path in enumerate(files):
        relative = path.relative_to(book_root)
        text = source_texts[path]
        if index == 0:
            text = italian_front_matter(text)
        else:
            text = without_front_matter(text)

        if not keep_links:
            text = rewrite_links(
                text,
                path,
                book_root,
                book,
                anchors,
                source_anchors,
                source.parent,
                destination,
            )

        text = text.strip()
        if aliases[path]:
            alias_markup = "\n".join(
                f'<a id="{alias}"></a>' for alias in sorted(aliases[path])
            )
            text = f"{alias_markup}\n\n{text}"
        if index == 0:
            sections.append(text)
        else:
            sections.append(f'<a id="{anchors[path]}"></a>\n\n{text}')

    generated = "\n\n".join(sections).rstrip() + "\n"
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_suffix(destination.suffix + ".tmp")
    temporary.write_text(generated, encoding="utf-8", newline="\n")
    temporary.replace(destination)
    return destination, len(files), warnings


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    output = (
        args.output.expanduser().resolve()
        if args.output is not None
        else source / "volumes"
    )
    selected = set(args.books) if args.books else {book.directory for book in BOOKS}

    try:
        for book in BOOKS:
            if book.directory not in selected:
                continue
            destination, count, warnings = build_book(
                source,
                output,
                book,
                strict=args.strict,
                keep_links=args.keep_links,
            )
            print(f"Creato {destination} ({count} file sorgente)")
            for warning in warnings:
                print(f"Avviso: {book.directory}: {warning}", file=sys.stderr)
    except (BuildError, OSError) as error:
        print(f"Errore: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
