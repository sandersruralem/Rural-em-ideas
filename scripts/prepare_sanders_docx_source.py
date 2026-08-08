#!/usr/bin/env python3
"""Create a Word-oriented Markdown edition of the Sanders County fact pack."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "context" / "sanders-county-fact-pack.md"
OUTPUT = ROOT / "context" / "sanders-county-fact-pack.docx-source.md"

DEFINITION_SECTIONS = {1, 2, 4, 5, 7, 8, 9, 10}


def wrapped_items(lines: list[str], marker: str = "- ") -> list[str]:
    items: list[str] = []
    current: list[str] = []
    for line in lines:
        if line.startswith(marker):
            if current:
                items.append(" ".join(current))
            current = [line[len(marker) :].strip()]
        elif current and (line.startswith("  ") or not line.strip()):
            if line.strip():
                current.append(line.strip())
        elif current:
            items.append(" ".join(current))
            current = []
    if current:
        items.append(" ".join(current))
    return items


def paragraphs_before_bullets(lines: list[str]) -> list[str]:
    result: list[str] = []
    paragraph: list[str] = []
    for line in lines:
        if line.startswith("- "):
            break
        if line.strip():
            paragraph.append(line.strip())
        elif paragraph:
            result.extend([" ".join(paragraph), ""])
            paragraph = []
    if paragraph:
        result.extend([" ".join(paragraph), ""])
    return result


def escape_cell(text: str) -> str:
    return text.replace("|", r"\|").strip()


def definition_table(lines: list[str]) -> list[str]:
    result = paragraphs_before_bullets(lines)
    result.extend(["| Item | Detail |", "| --- | --- |"])
    for item in wrapped_items(lines):
        if ":" in item:
            label, detail = item.split(":", 1)
        else:
            label, detail = item, ""
        result.append(f"| {escape_cell(label)} | {escape_cell(detail)} |")
    return result


def join_fenced_text(lines: list[str]) -> str:
    inside = False
    words: list[str] = []
    for line in lines:
        if line.startswith("```"):
            inside = not inside
        elif inside and line.strip():
            words.append(line.strip())
    return " ".join(words)


def split_sections(lines: list[str]) -> dict[int, tuple[str, list[str]]]:
    sections: dict[int, tuple[str, list[str]]] = {}
    starts: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"## (\d+)\. (.+)", line)
        if match:
            starts.append((index, int(match.group(1)), match.group(2)))
    for position, (start, number, title) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else len(lines)
        for index in range(start + 1, end):
            if lines[index] in {"## Maintenance log", "## Sources used"}:
                end = index
                break
        sections[number] = (title, lines[start + 1 : end])
    return sections


def source_rows(lines: list[str]) -> tuple[list[tuple[str, str, str, str]], list[str]]:
    rows: list[tuple[str, str, str, str]] = []
    limitation_index = (
        lines.index("### Research notes / limitations")
        if "### Research notes / limitations" in lines
        else len(lines)
    )
    limitations = wrapped_items(lines[limitation_index + 1 :])
    source_lines = lines[:limitation_index]
    category = ""
    current: list[str] = []

    def flush() -> None:
        if not current:
            return
        text = " ".join(part.strip() for part in current)
        match = re.match(r"(\d+)\.\s+(.*)", text)
        if not match:
            current.clear()
            return
        number, citation = match.groups()
        urls = re.findall(r"https?://\S+", citation)
        clean_urls = [url.rstrip(".,;)") for url in urls]
        for url in urls:
            citation = citation.replace(url, "")
        citation = re.sub(r"[\s—;-]+$", "", citation).strip()
        rows.append((number, category, citation, "<br>".join(clean_urls)))
        current.clear()

    for line in source_lines:
        if line.startswith("### "):
            flush()
            category = line[4:].strip()
        elif re.match(r"\d+\.\s+", line):
            flush()
            current.append(line.strip())
        elif current and (line.startswith("   ") or line.startswith("    ")):
            current.append(line.strip())
    flush()
    return rows, limitations


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    sections = split_sections(lines)

    rules_start = lines.index("## Rules for this file") + 1
    rules_end = next(i for i in range(rules_start, len(lines)) if lines[i].startswith("## 1."))
    rules = wrapped_items(lines[rules_start:rules_end])

    maintenance_start = lines.index("## Maintenance log")
    sources_start = lines.index("## Sources used")
    maintenance = [
        line
        for line in lines[maintenance_start + 1 : sources_start]
        if line.strip() and line != "---"
    ]
    rows, limitations = source_rows(lines[sources_start + 1 :])

    output: list[str] = [
        "# County Fact Pack",
        "",
        "## Sanders County, Montana",
        "",
        "*Office-ready research draft for Emergency Manager review*",
        "",
        "| Document control | Value |",
        "| --- | --- |",
        "| Version | 0.1 research draft |",
        "| Owner | Emergency Manager |",
        "| Data classification | Green — public information only |",
        "| Review cycle | Quarterly and after any plan change, election, or reorganization |",
        "| Status | DRAFT — verify before operational use |",
        "| Prepared | August 8, 2026 |",
        "",
        "### Purpose",
        "",
        "This fact pack provides concise, verified local context for emergency-management planning and AI-assisted drafting. It is not an emergency operations plan and does not authorize operational decisions.",
        "",
        "> **Draft-control notice:** Facts marked **UNKNOWN** require local verification. Do not use this document to announce a road closure, shelter opening, evacuation, activation, or other operational decision.",
        "",
    ]

    for number in range(1, 13):
        title, body = sections[number]
        output.extend([f"## {number}. {title}", ""])
        if number in DEFINITION_SECTIONS:
            output.extend(definition_table(body))
        elif number == 3:
            note_index = body.index("Notes on past significant events, publicly reported:")
            output.extend(body[:note_index])
            output.extend(["", "### Publicly reported significant events", ""])
            output.extend(body[note_index + 1 :])
        elif number == 12:
            instruction = join_fenced_text(body)
            output.extend(["> **Standing instruction to the model**", ">", f"> {instruction}"])
        else:
            output.extend(body)
        output.append("")

    output.extend(
        [
            "## Open items requiring local verification",
            "",
            "| Topic | Verification needed |",
            "| --- | --- |",
            "| Emergency Management staffing | Confirm deputy, part-time, and administrative support. |",
            "| River monitoring | Confirm office-preferred gauges beyond PLNM8 and PERM8. |",
            "| EOC | Confirm primary and alternate locations, layout, and activation procedure. |",
            "| Activation levels | Insert the county's actual level names and triggers. |",
            "| Volunteer programs | Confirm current CERT, ARES, auxiliary, and SAR arrangements. |",
            "| Public works | Confirm staffing and equipment classes suitable for public release. |",
            "| Emergency facilities | Verify current MOUs, ADA access, generators, and capacity ranges. |",
            "| Public warning | Confirm Hyper-Reach signup instructions, message limits, and siren coverage. |",
            "| At-risk populations | Confirm whether aggregate medical-equipment dependency data exists. |",
            "| Mutual aid | Verify the current agreement inventory and state coordination path. |",
            "",
            "## Maintenance log",
            "",
            *maintenance,
            "",
            "## Appendix A — Data-handling rules",
            "",
        ]
    )
    output.extend(f"- {rule}" for rule in rules)
    output.extend(
        [
            "",
            "## Appendix B — Sources",
            "",
            "All content was drawn from publicly available Green sources. No non-public plans, CAD data, or personally identifying details were used.",
            "",
            "| # | Category | Source | URL |",
            "| --- | --- | --- | --- |",
        ]
    )
    for number, category, citation, urls in rows:
        output.append(
            f"| {number} | {escape_cell(category)} | {escape_cell(citation)} | {escape_cell(urls)} |"
        )
    output.extend(["", "### Research limitations", ""])
    output.extend(f"- {item}" for item in limitations)
    output.append("")

    OUTPUT.write_text("\n".join(output), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
