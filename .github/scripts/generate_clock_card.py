#!/usr/bin/env python3
"""Generate a world clock SVG card for the GitHub profile README.

The card is time-stamped at generation time and refreshed by GitHub Actions.
Times are computed with zoneinfo so DST is handled correctly.
"""

from datetime import datetime, timezone
from html import escape
from pathlib import Path
from zoneinfo import ZoneInfo

OUTPUT = Path(__file__).resolve().parents[2] / "profile" / "world-clock.svg"

CITIES = [
    ("UTC", "Etc/UTC", "协调世界时", "#7aa2f7"),
    ("北京", "Asia/Shanghai", "中国标准时间", "#f7768e"),
    ("东京", "Asia/Tokyo", "日本标准时间", "#ff9e64"),
    ("伦敦", "Europe/London", "英国时间", "#9ece6a"),
    ("纽约", "America/New_York", "美国东部时间", "#bb9af7"),
    ("洛杉矶", "America/Los_Angeles", "美国太平洋时间", "#2ac3de"),
]

WEEKDAYS = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]


def fmt_time(dt: datetime) -> str:
    return dt.strftime("%H:%M:%S")


def fmt_date(dt: datetime) -> str:
    return f"{dt.year}年{dt.month}月{dt.day}日 {WEEKDAYS[dt.weekday()]}"


def fmt_offset(dt: datetime) -> str:
    off = dt.utcoffset()
    if off is None:
        return ""
    total = int(off.total_seconds() // 60)
    sign = "+" if total >= 0 else "-"
    total = abs(total)
    return f"UTC{sign}{total // 60:02d}:{total % 60:02d}"


def build() -> str:
    now = datetime.now(timezone.utc)

    cards = []
    cols = 3
    card_w, card_h = 360, 118
    gap_x, gap_y = 24, 20
    start_x, start_y = 30, 108

    for i, (name, zone, desc, accent) in enumerate(CITIES):
        dt = now.astimezone(ZoneInfo(zone))
        x = start_x + (i % cols) * (card_w + gap_x)
        y = start_y + (i // cols) * (card_h + gap_y)
        cards.append(f"""
      <g transform="translate({x},{y})">
        <rect width="{card_w}" height="{card_h}" rx="12" fill="#111827" stroke="#1f2937"/>
        <rect width="4" height="{card_h}" rx="2" fill="{accent}"/>
        <text x="20" y="30" fill="{accent}" font-size="14" font-weight="600">{escape(name)}</text>
        <text x="{card_w - 20}" y="30" fill="#6b7280" font-size="12" text-anchor="end">{escape(fmt_offset(dt))}</text>
        <text x="20" y="76" fill="#f4f7fc" font-size="38" font-weight="700" font-family="ui-monospace,SFMono-Regular,Menlo,monospace" letter-spacing="1">{fmt_time(dt)}</text>
        <text x="20" y="102" fill="#8b98ad" font-size="12">{escape(fmt_date(dt))}</text>
      </g>""")

    gen_time = now.astimezone(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
    grid_h = 2 * card_h + gap_y

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1152" height="{start_y + grid_h + 62}" viewBox="0 0 1152 {start_y + grid_h + 62}" role="img" aria-labelledby="title desc">
  <title id="title">World Clock · 世界时钟</title>
  <desc id="desc">UTC、北京、东京、伦敦、纽约、洛杉矶的实时时间卡片，点击可打开显示访客本地时间的实时网页。</desc>
  <defs>
    <linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#60a5fa"/>
      <stop offset="0.5" stop-color="#a78bfa"/>
      <stop offset="1" stop-color="#2dd4bf"/>
    </linearGradient>
  </defs>
  <rect width="1152" height="{start_y + grid_h + 62}" rx="14" fill="#05070d"/>
  <rect x="0.5" y="0.5" width="1151" height="{start_y + grid_h + 61}" rx="14" fill="none" stroke="#1f2937"/>
  <text x="30" y="46" fill="url(#hdr)" font-size="26" font-weight="700">WORLD CLOCK</text>
  <text x="196" y="46" fill="#8b98ad" font-size="14">世界时钟 · 点击打开实时版（显示你的本地时间）→</text>
  <line x1="30" y1="66" x2="1122" y2="66" stroke="#1f2937"/>
  {''.join(cards)}
  <text x="30" y="{start_y + grid_h + 34}" fill="#4b5563" font-size="12">卡片每 10 分钟自动更新 · 生成于北京时间 {gen_time}</text>
</svg>
"""


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUTPUT}")
