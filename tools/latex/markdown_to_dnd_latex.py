#!/usr/bin/env python3
"""Convert a small, practical Markdown subset to the dndbook LaTeX format.

The converter deliberately does not translate or rewrite prose. It only maps
Markdown structure to LaTeX structure and can follow local Markdown links.
It uses Python's standard library only.
"""

from __future__ import annotations

import argparse
import html
import os
import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TEMPLATE = ROOT / "tools" / "latex" / "dnd"


def latex_escape(value: str) -> str:
    """Escape text that is not already being handled as Markdown markup."""
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def slugify(value: str) -> str:
    value = re.sub(r"[^\w -]", "", value.lower(), flags=re.UNICODE)
    return re.sub(r"[- ]+", "_", value).strip("_") or "section"


def label_name(value: str) -> str:
    """Keep only characters that are safe in a LaTeX label name."""
    return re.sub(r"[^A-Za-z0-9:.-]+", "_", value).strip("_") or "section"


def split_table_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


class Converter:
    def __init__(self, *, follow_links: bool, language: str) -> None:
        self.follow_links = follow_links
        self.language = language
        self.seen: set[Path] = set()
        self.labels: set[str] = set()
        self.base_heading: int | None = None

    def inline(self, value: str) -> str:
        """Render inline Markdown without changing its visible wording."""
        value = html.unescape(value)
        value = re.sub(r"<!--.*?-->", "", value)
        value = re.sub(r"</?span(?:\s[^>]*)?>", "", value)
        output: list[str] = []
        index = 0

        while index < len(value):
            if value[index] == "`":
                end = value.find("`", index + 1)
                if end != -1:
                    output.append(r"\texttt{" + latex_escape(value[index + 1 : end]) + "}")
                    index = end + 1
                    continue

            image = re.match(r"!\[([^]]*)\]\(([^)]+)\)", value[index:])
            if image:
                alt, path = image.groups()
                output.append(
                    r"\includegraphics[width=\linewidth]{"
                    + latex_escape(path)
                    + "}"
                )
                index += image.end()
                continue

            styled_link = re.match(r"(\*\*|__|\*|_)(\[[^]]+\]\(([^)]+)\))\1", value[index:])
            if styled_link:
                marker, link_text, _ = styled_link.groups()
                command = r"\textbf{" if len(marker) == 2 else r"\emph{"
                output.append(command + self.inline(link_text) + "}")
                index += styled_link.end()
                continue

            link = re.match(r"\[([^]]+)\]\(([^)]+)\)", value[index:])
            if link:
                label, target = link.groups()
                label_tex = self.inline(label)
                if target.startswith("#"):
                    output.append(r"\hyperref[" + label_name(target[1:]) + "]{" + label_tex + "}")
                elif re.match(r"https?://", target):
                    output.append(r"\href{" + latex_escape(target) + "}{" + label_tex + "}")
                else:
                    output.append(label_tex)
                index += link.end()
                continue

            for marker, command in (
                ("**", r"\textbf{"),
                ("__", r"\textbf{"),
                ("*", r"\emph{"),
                ("_", r"\emph{"),
            ):
                if value.startswith(marker, index):
                    end = value.find(marker, index + len(marker))
                    if end != -1:
                        output.append(command + self.inline(value[index + len(marker) : end]) + "}")
                        index = end + len(marker)
                        break
            else:
                if value[index] == "°":
                    output.append(r"\degree{}")
                else:
                    output.append(latex_escape(value[index]))
                index += 1
                continue
            continue

        return "".join(output)

    def heading(self, level: int, title: str) -> str:
        explicit = re.search(r"\s*\{#([^}]+)\}\s*$", title)
        if explicit:
            anchor = explicit.group(1)
            title = title[: explicit.start()].rstrip()
        else:
            anchor = slugify(re.sub(r"[*_]", "", title))

        if self.base_heading is None:
            self.base_heading = level
        mapped = max(1, level - self.base_heading + 1)
        command = {1: "chapter", 2: "section", 3: "subsection"}.get(mapped, "subsubsection")
        label = label_name(anchor)
        if not explicit and label in self.labels:
            suffix = 2
            while f"{label}_{suffix}" in self.labels:
                suffix += 1
            label = f"{label}_{suffix}"
        self.labels.add(label)
        return f"\\{command}{{{self.inline(title)}}}\\label{{{label}}}\n"

    def local_target(self, source: Path, target: str) -> Path | None:
        target = unquote(target.split("#", 1)[0])
        if not target or target.startswith(("http://", "https://")):
            return None
        candidate = (source.parent / target).resolve()
        return candidate if candidate.suffix.lower() == ".md" and candidate.is_file() else None

    def paragraph(self, lines: list[str], source: Path) -> str:
        if len(lines) == 1:
            link = re.fullmatch(r"\s*\[(?:\*\*)?([^]]+?)(?:\*\*)?\]\(([^)]+)\)\s*", lines[0])
            if link and self.follow_links:
                target = self.local_target(source, link.group(2))
                if target is not None:
                    return self.file_fragment(target)

        rendered: list[str] = []
        for line in lines:
            if line.strip() == "\\":
                rendered.append(r"\\")
            else:
                rendered.append(self.inline(line.strip()))
        return " ".join(rendered) + "\n\n"

    def quote(self, lines: list[str], source: Path) -> str:
        body = [re.sub(r"^\s*> ?", "", line) for line in lines]
        title = "Nota"
        if body:
            match = re.fullmatch(r"\*\*([^*]+)\*\*", body[0].strip())
            if match:
                title = match.group(1)
                body = body[1:]
        content = self.blocks(body, source)
        if title == "Nota" and not content.strip():
            return ""
        if title == "Nota":
            return "\\begin{DndReadAloud}[color=PhbLightCyan]\n" + content + "\\end{DndReadAloud}\n\n"
        return (
            "\\begin{DndComment}[color=PhbLightCyan]{"
            + self.inline(title)
            + "}\n"
            + content
            + "\\end{DndComment}\n\n"
        )

    def table(self, lines: list[str]) -> str:
        rows = [split_table_row(line) for line in lines]
        if len(rows) < 2:
            return ""
        header = rows[0]
        data = rows[2:]
        columns = len(header)
        preamble = " ".join("X" for _ in range(columns))
        output = [f"\\begin{{DndTable}}[color=PhbLightCyan]{{{preamble}}}\n"]
        output.append(" & ".join(self.inline(cell) for cell in header) + r" \\" + "\n")
        for row in data:
            row += [""] * (columns - len(row))
            output.append(" & ".join(self.inline(cell) for cell in row[:columns]) + r" \\" + "\n")
        output.append("\\end{DndTable}\n\n")
        return "".join(output)

    def list_block(self, lines: list[str], ordered: bool) -> str:
        environment = "enumerate" if ordered else "itemize"
        output = [f"\\begin{{{environment}}}\n"]
        for line in lines:
            match = re.match(r"^\s*(?:\d+[.)]|[-*+])\s+(.*)$", line)
            if match:
                output.append("  \\item " + self.inline(match.group(1)) + "\n")
        output.append(f"\\end{{{environment}}}\n\n")
        return "".join(output)

    def blocks(self, lines: list[str], source: Path) -> str:
        output: list[str] = []
        index = 0
        while index < len(lines):
            line = lines[index]
            if not line.strip() or line.lstrip().startswith("<!--"):
                index += 1
                continue

            fence = re.match(r"^\s*```", line)
            if fence:
                index += 1
                code: list[str] = []
                while index < len(lines) and not re.match(r"^\s*```", lines[index]):
                    code.append(lines[index])
                    index += 1
                index += 1
                output.append("\\begin{lstlisting}\n" + "\n".join(code) + "\n\\end{lstlisting}\n\n")
                continue

            heading = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
            if heading:
                output.append(self.heading(len(heading.group(1)), heading.group(2)))
                index += 1
                continue

            if re.match(r"^\s*>", line):
                quote_lines: list[str] = []
                while index < len(lines) and (re.match(r"^\s*>", lines[index]) or not lines[index].strip()):
                    quote_lines.append(lines[index])
                    index += 1
                output.append(self.quote(quote_lines, source))
                continue

            if index + 1 < len(lines) and "|" in line and is_table_separator(lines[index + 1]):
                table_lines = [line, lines[index + 1]]
                index += 2
                while index < len(lines) and "|" in lines[index] and lines[index].strip():
                    table_lines.append(lines[index])
                    index += 1
                output.append(self.table(table_lines))
                continue

            if re.match(r"^\s*(?:[-*_])(?:\s*[-*_]){2,}\s*$", line):
                output.append("\\par\\medskip\\noindent\\rule{\\linewidth}{0.4pt}\\medskip\n\n")
                index += 1
                continue

            list_match = re.match(r"^\s*(\d+[.)]|[-*+])\s+", line)
            if list_match:
                ordered = list_match.group(1)[0].isdigit()
                list_lines: list[str] = []
                while index < len(lines):
                    if re.match(r"^\s*(?:\d+[.)]|[-*+])\s+", lines[index]):
                        list_lines.append(lines[index])
                        index += 1
                    elif lines[index].startswith(("  ", "\t")) and lines[index].strip():
                        list_lines.append(lines[index])
                        index += 1
                    else:
                        break
                output.append(self.list_block(list_lines, ordered))
                continue

            paragraph_lines = [line]
            index += 1
            while index < len(lines) and lines[index].strip():
                next_line = lines[index]
                if (
                    re.match(r"^\s*(?:#{1,6})\s+", next_line)
                    or re.match(r"^\s*>", next_line)
                    or re.match(r"^\s*```", next_line)
                    or re.match(r"^\s*(?:\d+[.)]|[-*+])\s+", next_line)
                ):
                    break
                paragraph_lines.append(next_line)
                index += 1
            output.append(self.paragraph(paragraph_lines, source))

        return "".join(output)

    def file_fragment(self, path: Path) -> str:
        path = path.resolve()
        if path in self.seen:
            return ""
        self.seen.add(path)
        lines = path.read_text(encoding="utf-8").splitlines()
        if lines and lines[0].strip() == "---":
            end = next((i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None)
            if end is not None:
                lines = lines[end + 1 :]
        return self.blocks(lines, path)


def metadata(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    values: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([\w-]+):\s*(.*?)\s*$", line)
        if match:
            values[match.group(1)] = match.group(2).strip("'\"")
    return values


def build_document(args: argparse.Namespace) -> str:
    first = Path(args.input[0]).resolve()
    converter = Converter(follow_links=args.follow_links, language=args.language)
    source_metadata = metadata(first)
    title = args.title or source_metadata.get("title") or first.stem.replace("_", " ")
    author = args.author or source_metadata.get("author", "")
    body = "".join(converter.file_fragment(Path(path).resolve()) for path in args.input)
    for path in args.include:
        body += converter.file_fragment(Path(path).resolve())

    output = Path(args.output).resolve()
    template_img = Path(args.template_dir).resolve() / "img"
    graphic_path = Path(os.path.relpath(template_img, output.parent)).as_posix()
    language = args.language
    return f"""\\documentclass[a4paper,10pt,twoside,twocolumn,openany,bg=full,nodeprecatedcode]{{dndbook}}
\\usepackage[{language}]{{babel}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{caption}}
\\usepackage{{graphicx}}
\\usepackage{{listings}}
\\usepackage[hidelinks]{{hyperref}}
\\graphicspath{{{{{graphic_path}/}}}}
\\captionsetup[table]{{labelformat=empty,font={{sf,sc,bf,}},skip=0pt}}
\\renewcommand{{\\tocchapterabbreviationname}}{{Cap.}}

\\title{{{converter.inline(title)}}}
\\author{{{converter.inline(author)}}}
\\date{{}}

\\begin{{document}}
\\frontmatter
\\maketitle
\\tableofcontents
\\mainmatter

{body}
\\end{{document}}
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="+", help="Markdown file(s) to convert")
    parser.add_argument("-o", "--output", required=True, help="Output .tex file")
    parser.add_argument("--include", action="append", default=[], help="Additional Markdown file")
    parser.add_argument("--follow-links", action="store_true", help="Include local Markdown links")
    parser.add_argument("--title", help="Override the document title")
    parser.add_argument("--author", help="Override the document author")
    parser.add_argument("--language", default="italian", help="babel language (default: italian)")
    parser.add_argument("--template-dir", default=str(DEFAULT_TEMPLATE), help="Vendored dnd template directory")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_document(args), encoding="utf-8")
    print(f"LaTeX creato: {output}")


if __name__ == "__main__":
    main()
