#!/usr/bin/env python3
"""Generate a GitHub-compatible animated contribution calendar SVG."""

from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path


LEVELS = {
    "NONE": 0,
    "FIRST_QUARTILE": 1,
    "SECOND_QUARTILE": 2,
    "THIRD_QUARTILE": 3,
    "FOURTH_QUARTILE": 4,
}

COLORS = ("var(--level-0)", "var(--level-1)", "var(--level-2)", "var(--level-3)", "var(--level-4)")


def load_calendar(source: Path) -> tuple[list[list[dict]], int]:
    payload = json.loads(source.read_text(encoding="utf-8"))
    calendar = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    if not weeks:
        raise ValueError("GitHub returned an empty contribution calendar")
    return weeks, int(calendar["totalContributions"])


def render(weeks: list[list[dict]], total: int) -> str:
    cell = 11
    gap = 3
    left = 8
    top = 28
    columns = len(weeks)
    width = left * 2 + columns * cell + (columns - 1) * gap
    height = 145

    first_day = weeks[0]["contributionDays"][0]["date"]
    last_day = weeks[-1]["contributionDays"][-1]["date"]
    accessible_title = html.escape(
        f"{total:,} GitHub contributions from {first_day} to {last_day}"
    )

    base_cells: list[str] = []
    sweep_cells: list[str] = []
    month_labels: list[str] = []
    last_month = ""

    for week_index, week in enumerate(weeks):
        x = left + week_index * (cell + gap)
        days = week["contributionDays"]
        if days:
            parsed = date.fromisoformat(days[0]["date"])
            month = parsed.strftime("%b")
            if parsed.day <= 7 and month != last_month:
                month_labels.append(
                    f'<text x="{x}" y="14" class="month">{month}</text>'
                )
                last_month = month

        for day in days:
            y = top + int(day["weekday"]) * (cell + gap)
            count = int(day["contributionCount"])
            level = LEVELS.get(day["contributionLevel"], 0)
            day_label = html.escape(
                f'{count} contribution{"s" if count != 1 else ""} on {day["date"]}'
            )
            base_cells.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2.5" '
                f'fill="{COLORS[level]}"><title>{day_label}</title></rect>'
            )
            sweep_cells.append(
                f'<rect class="sweep c{week_index}" x="{x}" y="{y}" '
                f'width="{cell}" height="{cell}" rx="2.5"/>'
            )

    delay_rules = "\n".join(
        f".c{index} {{ animation-delay: {index * 65}ms; }}"
        for index in range(columns)
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{accessible_title}</title>
  <desc id="desc">A real GitHub contribution calendar with a soft green highlight moving from left to right. The underlying activity remains visible when animation is disabled.</desc>
  <style>
    :root {{
      --ink: #8b949e;
      --level-0: #161b22;
      --level-1: #0e4429;
      --level-2: #006d32;
      --level-3: #26a641;
      --level-4: #39d353;
      --sweep: #b7f7c5;
    }}
    .month, .caption {{
      fill: var(--ink);
      font: 10px -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    .caption {{ font-size: 11px; }}
    .sweep {{
      fill: var(--sweep);
      opacity: 0;
      transform-box: fill-box;
      transform-origin: center;
      animation: scan 6900ms cubic-bezier(.22,.8,.26,1) infinite;
    }}
    {delay_rules}
    @keyframes scan {{
      0%, 8%, 100% {{ opacity: 0; transform: scale(.72); }}
      2.5% {{ opacity: .92; transform: scale(1); }}
      5% {{ opacity: .18; transform: scale(1); }}
    }}
    @media (prefers-color-scheme: light) {{
      :root {{
        --ink: #57606a;
        --level-0: #ebedf0;
        --level-1: #9be9a8;
        --level-2: #40c463;
        --level-3: #30a14e;
        --level-4: #216e39;
        --sweep: #0b5d2a;
      }}
    }}
    @media (prefers-reduced-motion: reduce) {{
      .sweep {{ animation: none; opacity: 0; }}
    }}
  </style>
  <g aria-hidden="true">
    {"".join(month_labels)}
    {"".join(base_cells)}
    {"".join(sweep_cells)}
  </g>
  <text x="{left}" y="140" class="caption">{total:,} contributions in the last year</text>
</svg>
"""


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: generate_contribution_wave.py INPUT_JSON OUTPUT_SVG"
        )
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    weeks, total = load_calendar(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render(weeks, total), encoding="utf-8")


if __name__ == "__main__":
    main()
