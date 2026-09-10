#!/usr/bin/env python3
"""
engineering_update.py — Generates engineering_update.md from existing report files.

Produces the Engineering Update format (distinct from the PDM weekly_report.md).
Run after the other modules have generated their report files.

Usage:
    python3 modules/engineering_update.py --from 2026-08-21 --to 2026-08-27
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

_pkg_root = str(Path(__file__).parent.parent)
if _pkg_root not in sys.path:
    sys.path.insert(0, _pkg_root)

from lib.utils import ROOT, get_week_range


def _ordinal_suffix(n: int) -> str:
    if 11 <= (n % 100) <= 13:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def fmt_date_range(start: str, end: str) -> str:
    s = date.fromisoformat(start)
    e = date.fromisoformat(end)
    s_str = s.strftime("%B %-d") + _ordinal_suffix(s.day) + " " + str(s.year)
    e_str = e.strftime("%B %-d") + _ordinal_suffix(e.day) + " " + str(e.year)
    return f"{s_str} - {e_str}"


def parse_radar(md: str) -> tuple[int, list[str]]:
    """Returns (count, list of formatted ticket strings)."""
    count = 0
    m = re.search(r"\*\*Total:\*\* (\d+)", md)
    if m:
        count = int(m.group(1))

    tickets = []
    for match in re.finditer(r"### #(\d+) — (.+)", md):
        ticket_id = match.group(1)
        subject = match.group(2).strip()
        tickets.append(f"{subject} - {ticket_id}")

    return count, tickets


def parse_errors(md: str) -> dict:
    """Returns {us_panel, us_portal, eu_panel, eu_portal}."""
    result = {"us_panel": "?", "us_portal": "?", "eu_panel": "?", "eu_portal": "?"}
    for line in md.splitlines():
        line_l = line.lower()
        m = re.search(r"(\d+)\s+panel.*?(\d+)\s+portal", line_l)
        if not m:
            continue
        if "us dc" in line_l or ("us " in line_l and "eu" not in line_l and "qa" not in line_l):
            result["us_panel"] = m.group(1)
            result["us_portal"] = m.group(2)
        elif "eu dc" in line_l or ("eu " in line_l and "qa" not in line_l):
            result["eu_panel"] = m.group(1)
            result["eu_portal"] = m.group(2)
    return result


def _extract_copy_paste(md: str) -> str:
    section = md.split("## Copy-paste block", 1)
    if len(section) < 2:
        return ""
    m = re.search(r"```\n(.*?)```", section[1], re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_perf_body(md: str) -> str:
    """Perf block stripped of the 'Slow Query Report [date]' header line."""
    block = _extract_copy_paste(md)
    if not block:
        return ""
    lines = block.splitlines()
    if lines and lines[0].startswith("Slow Query Report"):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines = lines[1:]
    return "\n".join(lines)


def parse_slow_endpoint_body(md: str) -> str:
    """Slow endpoint block stripped of the 'Top 3 Slowest Queries' header line."""
    block = _extract_copy_paste(md)
    if not block:
        return ""
    lines = block.splitlines()
    if lines and re.match(r"top \d+", lines[0].lower()):
        lines = lines[1:]
    while lines and not lines[0].strip():
        lines = lines[1:]
    return "\n".join(lines)


def assemble(start: str, end: str, folder: Path) -> str:
    radar_file         = folder / "radar_report.md"
    error_file         = folder / "error_report.md"
    perf_file          = folder / "perf_report.md"
    slow_endpoint_file = folder / "slow_endpoint_report.md"

    radar_count, radar_tickets = 0, []
    if radar_file.exists():
        radar_count, radar_tickets = parse_radar(radar_file.read_text())
    else:
        print("  [eng-update] radar_report.md missing")

    errors = {"us_panel": "NA", "us_portal": "NA", "eu_panel": "NA", "eu_portal": "NA"}
    if error_file.exists():
        errors = parse_errors(error_file.read_text())
    else:
        print("  [eng-update] error_report.md missing")

    perf_body = ""
    if perf_file.exists():
        perf_body = parse_perf_body(perf_file.read_text())
    else:
        print("  [eng-update] perf_report.md missing")

    slow_body = ""
    if slow_endpoint_file.exists():
        slow_body = parse_slow_endpoint_body(slow_endpoint_file.read_text())
    else:
        print("  [eng-update] slow_endpoint_report.md missing")

    date_range = fmt_date_range(start, end)

    lines = [
        f"Engineering weekly updates: {date_range}",
        "",
        f"Radar Bug Count : {radar_count}",
        "Radar Bug tickets :",
    ]

    if radar_tickets:
        lines.extend(radar_tickets)
    else:
        lines.append("None")

    lines += [
        "",
        f"500 Errors: Panel-{errors['us_panel']}, Portal-{errors['us_portal']} (US) | Panel-{errors['eu_panel']}, Portal-{errors['eu_portal']} (EU)",
        "",
        "4.   Query Performance Breakdown",
    ]

    if perf_body:
        lines.append(perf_body)
    else:
        lines.append("         • [performance report pending]")

    lines += [
        "",
        "5. Top 20 Slowest Queries",
    ]

    if slow_body:
        lines.append(slow_body)
    else:
        lines.append("         • [slow-endpoint report pending]")

    lines += [
        "",
        "6. EQC Scores - NA",
        "7. Engineering Items",
        "",
        "[PASTE ENGINEERING ITEMS HERE]",
    ]

    return "\n".join(lines)


def main(start: str = None, end: str = None) -> Path:
    if not start or not end:
        start, end = get_week_range()

    folder = ROOT / "reports" / f"{start}_to_{end}"
    if not folder.exists():
        print(f"ERROR: {folder} does not exist — run run_all.py first")
        return None

    print(f"[eng-update] {start} → {end}")
    content = assemble(start, end, folder)

    out = folder / "engineering_update.md"
    out.write_text(content)
    print(f"[eng-update] saved → {out}")
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate engineering_update.md")
    parser.add_argument("--from", dest="date_from", help="Start date YYYY-MM-DD")
    parser.add_argument("--to",   dest="date_to",   help="End date YYYY-MM-DD")
    args = parser.parse_args()
    main(start=args.date_from, end=args.date_to)
