## Hi there 👋

<!--
**wang2000star/wang2000star** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->


### 编程语言 <picture style="margin-right: 10px;"><img src="./Statistics.gif" width="30" alt="Statistics"></picture>
<img align="center" src="./profile/top-langs.svg" alt="wang2000star" width="350" height="250">


### Github 贡献图 <picture style="margin-right: 10px;"><img src="./Statistics.gif" width="30" alt="Statistics"></picture>
[![wang2000star's github activity graph](./profile/activity-graph.svg)](https://github.com/wang2000star/wang2000star)

<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#05070d">
<meta name="description" content="实时显示 UTC、洛杉矶、AOE、北京等世界主要城市时间的在线世界时钟，自动处理夏令时，支持添加任意 IANA 时区。">
<title>World Clock · 世界时钟</title>
<style>
  :root {
    color-scheme: dark;
    --bg: #05070d;
    --text: #f4f7fc;
    --muted: #8c98ad;
    --dim: #5e6a7e;
    --line: rgba(255, 255, 255, 0.075);
    --line-strong: rgba(255, 255, 255, 0.12);
    --card: rgba(13, 19, 32, 0.72);
    --font: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    --mono: "SF Mono", ui-monospace, "Cascadia Code", "Roboto Mono", Menlo, monospace;
  }

  * { box-sizing: border-box; }
  [hidden] { display: none !important; }

  html { background: var(--bg); }

  body {
    margin: 0;
    min-height: 100vh;
    color: var(--text);
    font-family: var(--font);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    background:
      radial-gradient(1000px 700px at 8% -12%, rgba(59, 130, 246, 0.14), transparent 58%),
      radial-gradient(900px 620px at 98% 2%, rgba(167, 139, 250, 0.10), transparent 55%),
      radial-gradient(800px 600px at 55% 105%, rgba(20, 184, 166, 0.055), transparent 60%),
      var(--bg);
    overflow-x: hidden;
  }

  body::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    opacity: 0.55;
    background-image:
      linear-gradient(rgba(148, 177, 220, 0.045) 1px, transparent 1px),
      linear-gradient(90deg, rgba(148, 177, 220, 0.045) 1px, transparent 1px);
    background-size: 86px 86px;
    -webkit-mask-image: radial-gradient(ellipse 90% 60% at 50% 0%, black 10%, transparent 78%);
    mask-image: radial-gradient(ellipse 90% 60% at 50% 0%, black 10%, transparent 78%);
  }

  body::after {
    content: "";
    position: fixed;
    left: 50%;
    top: -340px;
    width: 900px;
    height: 700px;
    z-index: 0;
    transform: translateX(-50%);
    pointer-events: none;
    background: radial-gradient(ellipse at center, rgba(110, 160, 255, 0.09), transparent 66%);
    filter: blur(20px);
  }

  button, input { font: inherit; }
  button { -webkit-tap-highlight-color: transparent; }

  .page {
    position: relative;
    z-index: 1;
    width: min(1376px, calc(100% - 88px));
    margin: 0 auto;
    padding: 24px 0 26px;
  }

  /* ---------- top bar ---------- */
  .topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    min-height: 42px;
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    color: inherit;
    text-decoration: none;
  }

  .brand-mark {
    width: 40px;
    height: 40px;
    display: grid;
    place-items: center;
    border-radius: 13px;
    color: #dbeafe;
    background: linear-gradient(145deg, rgba(125, 211, 252, 0.16), rgba(167, 139, 250, 0.10));
    border: 1px solid rgba(191, 219, 254, 0.17);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 0 34px rgba(96, 165, 250, 0.10);
  }
  .brand-mark svg { width: 22px; height: 22px; }

  .brand-copy strong {
    display: block;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.02em;
    white-space: nowrap;
  }
  .brand-copy small {
    display: block;
    margin-top: 3px;
    color: var(--muted);
    font-size: 9px;
    font-weight: 500;
    letter-spacing: 0.24em;
    text-transform: uppercase;
  }

  .top-actions { display: flex; align-items: center; gap: 10px; }

  .segmented {
    display: flex;
    align-items: center;
    gap: 2px;
    padding: 3px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid var(--line);
  }
  .segmented button {
    appearance: none;
    border: 0;
    background: transparent;
    color: var(--muted);
    padding: 7px 11px;
    border-radius: 999px;
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.08em;
    cursor: pointer;
    transition: color 160ms ease, background 160ms ease, box-shadow 160ms ease;
  }
  .segmented button:hover { color: #dbe7fb; }
  .segmented button.active {
    color: #f8fbff;
    background: rgba(255, 255, 255, 0.105);
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 2px 8px rgba(0, 0, 0, 0.24);
  }

  .btn-add {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    white-space: nowrap;
    padding: 9px 15px 9px 12px;
    border: 1px solid rgba(219, 234, 254, 0.5);
    border-radius: 999px;
    background: linear-gradient(180deg, #f5f9ff, #d7e7fb);
    color: #0b1424;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.01em;
    cursor: pointer;
    box-shadow: 0 0 32px rgba(147, 197, 253, 0.14), inset 0 1px 0 #fff;
    transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
  }
  .btn-add svg { width: 14px; height: 14px; }
  .btn-add:hover {
    transform: translateY(-1px);
    filter: brightness(1.025);
    box-shadow: 0 0 38px rgba(147, 197, 253, 0.24), inset 0 1px 0 #fff;
  }
  .btn-add:active { transform: translateY(0); }

  /* ---------- hero ---------- */
  .hero {
    display: grid;
    grid-template-columns: minmax(0, 1.12fr) minmax(340px, 0.88fr);
    align-items: center;
    gap: 18px;
    min-height: 276px;
    padding: 22px 0 28px;
  }

  .hero-copy { min-width: 0; }

  .eyebrow {
    display: flex;
    align-items: center;
    gap: 9px;
    color: var(--muted);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.22em;
    text-transform: uppercase;
  }
  .eyebrow b {
    color: #c9d6ea;
    font-weight: 600;
    letter-spacing: 0.12em;
  }
  .eyebrow .slash { color: #374156; letter-spacing: 0; }

  .live-dot {
    position: relative;
    width: 6px;
    height: 6px;
    flex: 0 0 auto;
    border-radius: 50%;
    background: #5eead4;
    box-shadow: 0 0 0 4px rgba(94, 234, 212, 0.10), 0 0 14px rgba(94, 234, 212, 0.55);
  }
  .live-dot::after {
    content: "";
    position: absolute;
    inset: -4px;
    border-radius: inherit;
    border: 1px solid rgba(94, 234, 212, 0.35);
    animation: ping 2.4s ease-out infinite;
  }
  @keyframes ping {
    0% { transform: scale(0.6); opacity: 0.8; }
    70%, 100% { transform: scale(1.8); opacity: 0; }
  }

  .hero-clock {
    display: flex;
    align-items: baseline;
    margin-top: 13px;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
  .hero-hm {
    font-size: clamp(70px, 8.15vw, 114px);
    font-weight: 200;
    line-height: 0.94;
    letter-spacing: -0.065em;
    background: linear-gradient(180deg, #ffffff 18%, #b7c7df 82%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    filter: drop-shadow(0 10px 34px rgba(173, 204, 255, 0.12));
  }
  .hero-sec {
    margin-left: 12px;
    color: #71809a;
    font-size: clamp(26px, 2.8vw, 38px);
    font-weight: 300;
    letter-spacing: -0.04em;
  }
  .hero-period {
    margin-left: 12px;
    color: #8b9ab1;
    font-family: var(--mono);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.16em;
  }
  .hero-period.is-hidden { display: none; }

  .hero-date {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-top: 19px;
    color: #bac6d9;
    font-size: 13px;
    letter-spacing: 0.01em;
  }
  .hero-date .sep {
    width: 3px;
    height: 3px;
    border-radius: 50%;
    background: #4a5568;
  }
  .hero-date .weekday { color: #8c99ad; }

  .hero-sub {
    margin: 10px 0 0;
    color: var(--dim);
    font-size: 11px;
    letter-spacing: 0.01em;
  }
  .hero-sub b { color: #a8b5ca; font-weight: 600; }

  .hero-visual {
    position: relative;
    justify-self: end;
    width: min(100%, 344px);
    aspect-ratio: 1;
    isolation: isolate;
  }
  .hero-visual::before {
    content: "";
    position: absolute;
    inset: 8%;
    z-index: -1;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, rgba(90, 160, 255, 0.20), rgba(88, 80, 255, 0.055) 48%, transparent 70%);
    filter: blur(28px);
  }
  .globe-svg { display: block; width: 100%; height: 100%; overflow: visible; }

  .globe-sphere { animation: breathe 9s ease-in-out infinite; transform-origin: 240px 240px; }
  @keyframes breathe {
    0%, 100% { opacity: 0.98; }
    50% { opacity: 0.84; }
  }

  .globe-arc {
    stroke-dasharray: 2.5 7;
    animation: dash 26s linear infinite;
  }
  .globe-arc.reverse { animation-direction: reverse; animation-duration: 34s; }
  @keyframes dash { to { stroke-dashoffset: -190; } }

  .city-pulse { animation: cityPulse 3.2s ease-out infinite; transform-box: fill-box; transform-origin: center; }
  .city-pulse.p2 { animation-delay: 1.1s; }
  .city-pulse.p3 { animation-delay: 2.1s; }
  @keyframes cityPulse {
    0% { transform: scale(0.5); opacity: 0.55; }
    70%, 100% { transform: scale(2.1); opacity: 0; }
  }

  .utc-chip {
    position: absolute;
    left: 2%;
    bottom: 7%;
    display: flex;
    align-items: center;
    gap: 9px;
    padding: 9px 13px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.10);
    background: rgba(9, 14, 25, 0.74);
    -webkit-backdrop-filter: blur(16px);
    backdrop-filter: blur(16px);
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.28), inset 0 1px 0 rgba(255, 255, 255, 0.05);
  }
  .utc-chip-label {
    color: #7f8da5;
    font-family: var(--mono);
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 0.16em;
  }
  .utc-chip strong {
    color: #d7e7fb;
    font-family: var(--mono);
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.02em;
    font-variant-numeric: tabular-nums;
  }
  .utc-chip .tiny-dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #5eead4;
    box-shadow: 0 0 8px rgba(94, 234, 212, 0.7);
  }

  /* ---------- section heading ---------- */
  .section-head {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 24px;
    padding: 14px 0 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.055);
  }
  .section-title {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 0;
    font-size: 17px;
    font-weight: 550;
    letter-spacing: 0.01em;
  }
  .count-chip {
    display: inline-grid;
    place-items: center;
    min-width: 22px;
    height: 20px;
    padding: 0 6px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.055);
    border: 1px solid rgba(255, 255, 255, 0.07);
    color: #96a4ba;
    font-family: var(--mono);
    font-size: 9px;
    font-weight: 500;
  }
  .section-sub {
    margin: 5px 0 0;
    color: #5e6b80;
    font-size: 10.5px;
    letter-spacing: 0.015em;
  }

  .legend {
    display: flex;
    align-items: center;
    gap: 16px;
    padding-bottom: 2px;
    color: #6b788e;
    font-size: 9.5px;
    white-space: nowrap;
  }
  .legend span { display: inline-flex; align-items: center; gap: 6px; }
  .legend i {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    display: inline-block;
  }
  .legend .work-dot { background: #5eead4; box-shadow: 0 0 8px rgba(94, 234, 212, 0.45); }
  .legend .night-dot { background: #818cf8; box-shadow: 0 0 8px rgba(129, 140, 248, 0.4); }

  /* ---------- cards ---------- */
  .clock-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 13px;
  }

  .clock-card {
    position: relative;
    min-width: 0;
    padding: 15px 18px 13px;
    overflow: hidden;
    border-radius: 19px;
    border: 1px solid var(--line);
    background:
      radial-gradient(130% 110% at 0% 0%, var(--accent-soft, rgba(255, 255, 255, 0.045)), transparent 48%),
      linear-gradient(155deg, rgba(17, 24, 40, 0.82), rgba(9, 14, 25, 0.78));
    box-shadow:
      inset 0 1px 0 rgba(255, 255, 255, 0.045),
      0 18px 42px -28px rgba(0, 0, 0, 0.9);
    -webkit-backdrop-filter: blur(18px);
    backdrop-filter: blur(18px);
    transition: border-color 220ms ease, transform 220ms ease, box-shadow 220ms ease;
    animation: cardIn 600ms cubic-bezier(0.22, 0.75, 0.24, 1) both;
    animation-delay: calc(var(--i, 0) * 42ms);
  }
  .clock-card::after {
    content: "";
    position: absolute;
    top: 0;
    left: 24px;
    right: 24px;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--accent), transparent);
    opacity: 0.28;
    pointer-events: none;
  }
  .clock-card:hover {
    transform: translateY(-3px);
    border-color: rgba(255, 255, 255, 0.14);
    box-shadow:
      inset 0 1px 0 rgba(255, 255, 255, 0.055),
      0 22px 52px -26px rgba(0, 0, 0, 0.95),
      0 0 42px -18px var(--accent);
  }
  .clock-card.is-removing {
    animation: cardOut 200ms ease forwards;
    pointer-events: none;
  }
  @keyframes cardIn {
    from { opacity: 0; translate: 0 12px; }
    to { opacity: 1; translate: 0 0; }
  }
  @keyframes cardOut {
    to { opacity: 0; transform: scale(0.965) translateY(5px); }
  }

  .card-head {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding-right: 18px;
    min-height: 30px;
  }
  .city {
    display: flex;
    align-items: center;
    gap: 9px;
    min-width: 0;
  }
  .region {
    display: inline-grid;
    place-items: center;
    flex: 0 0 auto;
    min-width: 27px;
    height: 19px;
    padding: 0 5px;
    border-radius: 6px;
    border: 1px solid rgba(255, 255, 255, 0.07);
    background: rgba(255, 255, 255, 0.035);
    color: var(--accent);
    font-family: var(--mono);
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 0.07em;
  }
  .city-text { min-width: 0; }
  .city-text h3 {
    display: flex;
    align-items: center;
    gap: 6px;
    margin: 0;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.01em;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .local-chip {
    display: inline-flex;
    align-items: center;
    height: 14px;
    padding: 0 4px;
    border-radius: 4px;
    color: var(--accent);
    background: var(--accent-soft);
    font-size: 7px;
    font-weight: 700;
    letter-spacing: 0.06em;
    flex: 0 0 auto;
  }
  .city-en {
    display: block;
    margin-top: 2px;
    color: #6f7c91;
    font-size: 9.5px;
    font-weight: 500;
    letter-spacing: 0.025em;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .remove {
    position: absolute;
    top: 11px;
    right: 11px;
    width: 23px;
    height: 23px;
    display: grid;
    place-items: center;
    padding: 0;
    border: 1px solid transparent;
    border-radius: 7px;
    background: transparent;
    color: #67748a;
    cursor: pointer;
    opacity: 0;
    transform: scale(0.9);
    transition: opacity 160ms ease, transform 160ms ease, color 160ms ease, background 160ms ease, border-color 160ms ease;
  }
  .remove svg { width: 11px; height: 11px; }
  .clock-card:hover .remove,
  .remove:focus-visible { opacity: 1; transform: scale(1); }
  .remove:hover {
    color: #fca5a5;
    background: rgba(248, 113, 113, 0.08);
    border-color: rgba(248, 113, 113, 0.16);
  }

  .time-line {
    display: flex;
    align-items: baseline;
    margin-top: 10px;
    font-variant-numeric: tabular-nums;
    white-space: nowrap;
  }
  .time-main {
    color: #f5f8fe;
    font-size: 38px;
    font-weight: 300;
    line-height: 1;
    letter-spacing: -0.045em;
  }
  .time-sec {
    margin-left: 5px;
    color: #6f7e95;
    font-size: 14px;
    font-weight: 400;
    letter-spacing: -0.015em;
  }
  .time-period {
    margin-left: 7px;
    color: #8290a6;
    font-family: var(--mono);
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 0.12em;
  }
  .time-period.is-hidden { display: none; }

  .date-line {
    display: flex;
    align-items: center;
    gap: 7px;
    min-height: 16px;
    margin-top: 7px;
    color: #8997ac;
    font-size: 10.5px;
    letter-spacing: 0.01em;
  }
  .date-diff {
    display: inline-flex;
    align-items: center;
    height: 15px;
    padding: 0 5px;
    border-radius: 4px;
    color: var(--accent);
    background: var(--accent-soft);
    font-size: 8.5px;
    font-weight: 600;
    letter-spacing: 0.02em;
  }
  .date-diff.behind { color: #94a3b8; background: rgba(148, 163, 184, 0.09); }

  .dayline {
    position: relative;
    height: 4px;
    margin: 11px 0 10px;
    border-radius: 99px;
    background: linear-gradient(90deg,
      #111a2c 0%, #111a2c 21%,
      #3d3651 26%, #6b4f54 31%,
      #1c3149 38%, #1b3d51 50%, #1c3149 62%,
      #6b4f54 69%, #3d3651 74%,
      #111a2c 79%, #111a2c 100%);
    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.025);
  }
  .dayline-marker {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #f8fbff;
    box-shadow: 0 0 0 2px #0c1321, 0 0 12px var(--accent);
    transform: translate(-50%, -50%);
    transition: left 900ms linear;
  }

  .card-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
  }
  .foot-left { display: flex; align-items: center; gap: 10px; min-width: 0; }
  .offset {
    display: inline-flex;
    align-items: center;
    height: 19px;
    padding: 0 6px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.045);
    border: 1px solid rgba(255, 255, 255, 0.055);
    color: #a5b2c6;
    font-family: var(--mono);
    font-size: 9px;
    font-weight: 500;
    letter-spacing: 0.02em;
    white-space: nowrap;
  }
  .day-status {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    color: #8b98ab;
    font-size: 9.5px;
    white-space: nowrap;
  }
  .status-icon {
    display: inline-flex;
    width: 11px;
    height: 11px;
    color: #fbbf24;
  }
  .status-icon svg { width: 100%; height: 100%; }
  .day-status.is-night .status-icon { color: #818cf8; }
  .day-status.is-night .status-label { color: #7683a1; }
  .day-status.is-work .status-icon { color: #5eead4; }
  .day-status.is-work .status-label { color: #7fd6c9; }

  .dial {
    position: relative;
    width: 30px;
    height: 30px;
    flex: 0 0 auto;
    border-radius: 50%;
    background: radial-gradient(circle at 38% 32%, rgba(255, 255, 255, 0.07), rgba(255, 255, 255, 0.018) 60%);
    border: 1px solid rgba(255, 255, 255, 0.075);
    box-shadow: inset 0 0 0 3px rgba(6, 10, 18, 0.5);
  }
  .dial::before {
    content: "";
    position: absolute;
    inset: 3px;
    border-radius: 50%;
    background: repeating-conic-gradient(from -0.5deg, rgba(255, 255, 255, 0.2) 0deg 1deg, transparent 1deg 30deg);
    -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 2px), #000 calc(100% - 1.5px));
    mask-image: radial-gradient(farthest-side, transparent calc(100% - 2px), #000 calc(100% - 1.5px));
    opacity: 0.6;
  }
  .dial-hand {
    position: absolute;
    left: 50%;
    bottom: 50%;
    border-radius: 2px;
    transform-origin: 50% 100%;
    transition: transform 300ms cubic-bezier(0.2, 0.8, 0.2, 1);
  }
  .dial-hour {
    width: 2px;
    height: 7px;
    margin-left: -1px;
    background: var(--accent);
    opacity: 0.9;
  }
  .dial-minute {
    width: 1px;
    height: 10px;
    margin-left: -0.5px;
    background: #e2ecfa;
    opacity: 0.85;
  }
  .dial-pin {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 2px;
    height: 2px;
    margin: -1px 0 0 -1px;
    border-radius: 50%;
    background: #fff;
  }

  /* ---------- empty ---------- */
  .empty-state {
    display: grid;
    place-items: center;
    min-height: 300px;
    margin-top: 4px;
    border: 1px dashed rgba(255, 255, 255, 0.10);
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.012);
    text-align: center;
  }
  .empty-inner { max-width: 340px; padding: 32px; }
  .empty-icon {
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    margin: 0 auto 16px;
    border-radius: 15px;
    color: #9ec5ff;
    background: rgba(125, 211, 252, 0.08);
    border: 1px solid rgba(125, 211, 252, 0.14);
  }
  .empty-icon svg { width: 22px; height: 22px; }
  .empty-title { margin: 0; font-size: 15px; font-weight: 600; }
  .empty-copy { margin: 7px 0 18px; color: var(--muted); font-size: 11px; line-height: 1.7; }
  .btn-ghost {
    appearance: none;
    border: 1px solid rgba(255, 255, 255, 0.13);
    background: rgba(255, 255, 255, 0.045);
    color: #dbe7fb;
    border-radius: 999px;
    padding: 8px 15px;
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    transition: background 160ms ease, border-color 160ms ease;
  }
  .btn-ghost:hover { background: rgba(255, 255, 255, 0.08); border-color: rgba(255, 255, 255, 0.2); }

  /* ---------- footer ---------- */
  .site-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    margin-top: 16px;
    padding-top: 12px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    color: #4f5b6e;
    font-size: 9.5px;
    letter-spacing: 0.015em;
  }
  .site-foot span { display: inline-flex; align-items: center; gap: 7px; }
  .site-foot .foot-dot {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #3d4b62;
  }
  .site-foot .aoe-note { color: #566277; font-family: var(--mono); font-size: 8.5px; letter-spacing: 0.03em; }

  /* ---------- modal ---------- */
  .modal {
    position: fixed;
    inset: 0;
    z-index: 80;
    display: grid;
    place-items: center;
    padding: 24px;
    visibility: hidden;
    opacity: 0;
    transition: opacity 180ms ease, visibility 180ms ease;
  }
  .modal.open { visibility: visible; opacity: 1; }
  .modal-backdrop {
    position: absolute;
    inset: 0;
    background: rgba(2, 5, 12, 0.74);
    -webkit-backdrop-filter: blur(12px) saturate(0.8);
    backdrop-filter: blur(12px) saturate(0.8);
  }
  .modal-panel {
    position: relative;
    width: min(540px, 100%);
    max-height: min(710px, calc(100vh - 48px));
    min-height: min(472px, calc(100vh - 48px));
    display: flex;
    flex-direction: column;
    overflow: hidden;
    border-radius: 22px;
    border: 1px solid rgba(255, 255, 255, 0.10);
    background:
      radial-gradient(90% 100% at 0% 0%, rgba(125, 211, 252, 0.075), transparent 46%),
      linear-gradient(180deg, rgba(17, 25, 43, 0.99), rgba(8, 12, 22, 0.99));
    box-shadow: 0 40px 100px rgba(0, 0, 0, 0.62), inset 0 1px 0 rgba(255, 255, 255, 0.06);
    transform: translateY(10px) scale(0.985);
    transition: transform 220ms cubic-bezier(0.22, 0.75, 0.24, 1);
  }
  .modal.open .modal-panel { transform: none; }

  .modal-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    padding: 21px 23px 0;
  }
  .modal-kicker {
    margin: 0 0 5px;
    color: #6d7c93;
    font-family: var(--mono);
    font-size: 8px;
    font-weight: 600;
    letter-spacing: 0.19em;
  }
  .modal-title {
    margin: 0;
    font-size: 20px;
    font-weight: 550;
    letter-spacing: -0.01em;
  }
  .icon-btn {
    display: grid;
    place-items: center;
    width: 31px;
    height: 31px;
    padding: 0;
    border: 1px solid rgba(255, 255, 255, 0.09);
    border-radius: 9px;
    background: rgba(255, 255, 255, 0.035);
    color: #8190a7;
    cursor: pointer;
    transition: color 150ms ease, background 150ms ease, border-color 150ms ease;
  }
  .icon-btn svg { width: 12px; height: 12px; }
  .icon-btn:hover { color: #e5eefb; background: rgba(255, 255, 255, 0.07); border-color: rgba(255, 255, 255, 0.15); }

  .search-box {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 17px 23px 0;
    padding: 11px 13px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.095);
    background: rgba(255, 255, 255, 0.035);
    transition: border-color 160ms ease, box-shadow 160ms ease;
  }
  .search-box:focus-within {
    border-color: rgba(125, 211, 252, 0.42);
    box-shadow: 0 0 0 3px rgba(125, 211, 252, 0.08);
  }
  .search-box svg { width: 15px; height: 15px; flex: 0 0 auto; color: #64748b; }
  .search-box input {
    width: 100%;
    min-width: 0;
    padding: 0;
    border: 0;
    outline: 0;
    background: transparent;
    color: #eaf2ff;
    font-size: 12px;
    letter-spacing: 0.01em;
  }
  .search-box input::placeholder { color: #566277; }
  .modal-hint {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 17px 25px 8px;
    color: #6e7c92;
    font-size: 9.5px;
    letter-spacing: 0.04em;
  }
  .modal-hint .hint-count { color: #505c6f; font-family: var(--mono); font-size: 8px; letter-spacing: 0.01em; }

  .zone-list {
    overflow-y: auto;
    overscroll-behavior: contain;
    padding: 2px 12px 15px;
    scrollbar-width: thin;
    scrollbar-color: rgba(255, 255, 255, 0.16) transparent;
  }
  .zone-list::-webkit-scrollbar { width: 8px; }
  .zone-list::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.14); border: 2px solid transparent; background-clip: padding-box; border-radius: 99px; }
  .zone-list::-webkit-scrollbar-track { background: transparent; }

  .zone-option {
    display: flex;
    align-items: center;
    gap: 11px;
    width: 100%;
    padding: 9px 11px;
    border: 0;
    border-radius: 11px;
    background: transparent;
    color: inherit;
    text-align: left;
    cursor: pointer;
    transition: background 140ms ease;
  }
  .zone-option:hover { background: rgba(255, 255, 255, 0.05); }
  .zone-option:disabled { cursor: default; opacity: 0.42; }
  .zone-option:disabled:hover { background: transparent; }
  .zone-option .region { min-width: 26px; height: 18px; }
  .zone-option-info { min-width: 0; flex: 1; }
  .zone-option-name {
    display: flex;
    align-items: baseline;
    gap: 6px;
    min-width: 0;
    color: #dbe6f6;
    font-size: 13px;
    font-weight: 550;
    white-space: nowrap;
  }
  .zone-option-name em {
    overflow: hidden;
    color: #66748a;
    font-size: 9.5px;
    font-style: normal;
    font-weight: 500;
    text-overflow: ellipsis;
  }
  .zone-option-id {
    display: block;
    margin-top: 2px;
    overflow: hidden;
    color: #4c586b;
    font-family: var(--mono);
    font-size: 9px;
    letter-spacing: 0.01em;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .zone-option-time {
    flex: 0 0 auto;
    text-align: right;
  }
  .zone-option-time strong {
    display: block;
    color: #b4c3d9;
    font-family: var(--mono);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.01em;
    font-variant-numeric: tabular-nums;
  }
  .zone-option-time small {
    display: block;
    margin-top: 2px;
    color: #4f5c6f;
    font-family: var(--mono);
    font-size: 8.5px;
    letter-spacing: 0.01em;
  }
  .zone-option-add {
    display: grid;
    place-items: center;
    width: 22px;
    height: 22px;
    flex: 0 0 auto;
    margin-left: 3px;
    border-radius: 7px;
    color: #8ea3bf;
    background: rgba(255, 255, 255, 0.035);
  }
  .zone-option-add svg { width: 10px; height: 10px; }
  .zone-option:not(:disabled):hover .zone-option-add { color: #dbeafe; background: rgba(125, 211, 252, 0.10); }
  .zone-option.is-added .zone-option-add { color: #5eead4; background: rgba(94, 234, 212, 0.08); }
  .zone-empty {
    padding: 34px 20px 38px;
    text-align: center;
    color: #6f7d92;
    font-size: 11px;
    line-height: 1.8;
  }

  /* ---------- toast ---------- */
  .toast {
    position: fixed;
    left: 50%;
    bottom: 28px;
    z-index: 100;
    max-width: calc(100vw - 32px);
    padding: 10px 15px;
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    background: rgba(12, 19, 33, 0.92);
    color: #dbe7f8;
    font-size: 11px;
    box-shadow: 0 18px 48px rgba(0, 0, 0, 0.46), inset 0 1px 0 rgba(255, 255, 255, 0.06);
    -webkit-backdrop-filter: blur(16px);
    backdrop-filter: blur(16px);
    opacity: 0;
    transform: translate(-50%, 10px);
    pointer-events: none;
    transition: opacity 180ms ease, transform 180ms ease;
  }
  .toast.show { opacity: 1; transform: translate(-50%, 0); }

  body.modal-open { overflow: hidden; }

  :focus-visible {
    outline: 2px solid rgba(125, 211, 252, 0.7);
    outline-offset: 2px;
  }

  @media (hover: none) {
    .remove { opacity: 0.55; transform: none; }
  }

  /* ---------- responsive ---------- */
  @media (max-width: 1180px) {
    .page { width: min(1100px, calc(100% - 64px)); }
    .clock-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
    .hero { grid-template-columns: minmax(0, 1.2fr) minmax(300px, 0.8fr); }
    .hero-visual { width: min(100%, 320px); }
  }

  @media (max-width: 900px) {
    .page { width: calc(100% - 48px); }
    .hero { grid-template-columns: minmax(0, 1fr) 286px; gap: 8px; padding: 24px 0 30px; }
    .hero-visual { width: 286px; }
    .utc-chip { left: 0; bottom: 2%; }
    .clock-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .hero-hm { font-size: clamp(68px, 10vw, 98px); }
  }

  @media (max-width: 680px) {
    .page { width: calc(100% - 32px); padding-top: 18px; }
    .brand-copy small { display: none; }
    .brand-mark { width: 36px; height: 36px; border-radius: 11px; }
    .top-actions { gap: 7px; }
    .segmented button { padding: 7px 9px; }
    .btn-add { padding: 8px 12px 8px 10px; font-size: 10px; }
    .btn-add svg { width: 12px; height: 12px; }
    .hero { grid-template-columns: 1fr; min-height: 0; padding: 32px 0 30px; }
    .hero-visual { display: none; }
    .hero-hm { font-size: clamp(64px, 21vw, 92px); }
    .hero-sec { font-size: 25px; margin-left: 8px; }
    .hero-period { margin-left: 8px; }
    .hero-date { font-size: 12px; margin-top: 17px; }
    .section-head { align-items: flex-start; }
    .legend { display: none; }
    .section-sub { font-size: 9px; }
    .clock-grid { grid-template-columns: 1fr; gap: 10px; }
    .clock-card { padding: 16px 17px 14px; }
    .time-main { font-size: 40px; }
    .remove { opacity: 0.55; transform: none; }
    .site-foot { flex-direction: column; align-items: flex-start; gap: 7px; }
    .modal { padding: 12px; }
    .modal-panel { max-height: calc(100vh - 24px); border-radius: 18px; }
    .modal-head { padding: 18px 18px 0; }
    .search-box { margin-left: 18px; margin-right: 18px; }
    .modal-hint { padding-left: 20px; padding-right: 20px; }
    .zone-list { padding-left: 8px; padding-right: 8px; }
    .zone-option { padding-left: 9px; padding-right: 9px; gap: 9px; }
    .zone-option-name em { display: none; }
  }

  @media (max-width: 360px) {
    .topbar { gap: 10px; }
    .btn-add {
      width: 36px;
      height: 36px;
      padding: 0;
      justify-content: center;
    }
    .btn-add .btn-label { display: none; }
  }

  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
      scroll-behavior: auto !important;
    }
  }
</style>
</head>
<body>
  <div class="page">
    <header class="topbar">
      <div class="brand">
        <span class="brand-mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="8.7"></circle>
            <path d="M3.4 12h17.2M12 3.3c2.4 2.35 3.65 5.25 3.65 8.7S14.4 18.35 12 20.7c-2.4-2.35-3.65-5.25-3.65-8.7S9.6 5.65 12 3.3Z"></path>
            <path d="M5.2 6.8c1.8 1.05 4.1 1.65 6.8 1.65s5-.6 6.8-1.65M5.2 17.2c1.8-1.05 4.1-1.65 6.8-1.65s5 .6 6.8 1.65"></path>
          </svg>
        </span>
        <span class="brand-copy">
          <strong>World Clock</strong>
          <small>世界时钟 · Live</small>
        </span>
      </div>

      <div class="top-actions">
        <div class="segmented" role="group" aria-label="时间格式">
          <button type="button" data-format="24" class="active" aria-pressed="true">24H</button>
          <button type="button" data-format="12" aria-pressed="false">12H</button>
        </div>
        <button type="button" class="btn-add" id="open-add" aria-label="添加城市">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
            <path d="M12 5v14M5 12h14"></path>
          </svg>
          <span class="btn-label">添加城市</span>
        </button>
      </div>
    </header>

    <main>
      <section class="hero" aria-label="本地时间">
        <div class="hero-copy">
          <div class="eyebrow">
            <span class="live-dot" aria-hidden="true"></span>
            <span>本地时间</span>
            <span class="slash">/</span>
            <b id="local-zone-name">Local</b>
          </div>
          <div class="hero-clock" aria-live="off">
            <span class="hero-hm" id="hero-hm">00:00</span>
            <span class="hero-sec" id="hero-sec">:00</span>
            <span class="hero-period" id="hero-period">AM</span>
          </div>
          <div class="hero-date">
            <span id="hero-date">—</span>
            <span class="sep" aria-hidden="true"></span>
            <span class="weekday" id="hero-weekday">—</span>
          </div>
          <p class="hero-sub">全球 <b id="zone-count">8</b> 个时区，实时同步 · 自动处理夏令时</p>
        </div>

        <div class="hero-visual" aria-hidden="true">
          <svg class="globe-svg" viewBox="0 0 480 480" fill="none">
            <defs>
              <radialGradient id="sphereGrad" cx="33%" cy="27%" r="78%">
                <stop offset="0%" stop-color="#20385e" stop-opacity="0.92"></stop>
                <stop offset="46%" stop-color="#0f1c33" stop-opacity="0.96"></stop>
                <stop offset="100%" stop-color="#060a13"></stop>
              </radialGradient>
              <radialGradient id="sphereGloss" cx="30%" cy="22%" r="58%">
                <stop offset="0%" stop-color="#b7dcff" stop-opacity="0.16"></stop>
                <stop offset="58%" stop-color="#8fb7ff" stop-opacity="0.035"></stop>
                <stop offset="100%" stop-color="#8fb7ff" stop-opacity="0"></stop>
              </radialGradient>
              <linearGradient id="rimGrad" x1="90" y1="80" x2="390" y2="410" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stop-color="#b7e2ff" stop-opacity="0.56"></stop>
                <stop offset="48%" stop-color="#7789ff" stop-opacity="0.10"></stop>
                <stop offset="100%" stop-color="#c4b5fd" stop-opacity="0.38"></stop>
              </linearGradient>
              <linearGradient id="arcGrad" x1="140" y1="150" x2="380" y2="330" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stop-color="#7dd3fc" stop-opacity="0.08"></stop>
                <stop offset="50%" stop-color="#7dd3fc" stop-opacity="0.46"></stop>
                <stop offset="100%" stop-color="#c4b5fd" stop-opacity="0.12"></stop>
              </linearGradient>
              <clipPath id="globeClip">
                <circle cx="240" cy="240" r="168"></circle>
              </clipPath>
            </defs>

            <circle cx="240" cy="240" r="216" stroke="#7c8cff" stroke-opacity="0.10" stroke-dasharray="1 9"></circle>
            <circle cx="240" cy="240" r="195" stroke="#a5b4fc" stroke-opacity="0.055"></circle>

            <g class="globe-sphere">
              <circle cx="240" cy="240" r="168" fill="url(#sphereGrad)" stroke="url(#rimGrad)" stroke-width="1.2"></circle>
              <g clip-path="url(#globeClip)">
                <circle cx="240" cy="240" r="168" fill="url(#sphereGloss)"></circle>
                <g stroke="#a5cbff" stroke-opacity="0.12" stroke-width="0.85">
                  <ellipse cx="240" cy="240" rx="56" ry="168"></ellipse>
                  <ellipse cx="240" cy="240" rx="112" ry="168"></ellipse>
                  <ellipse cx="240" cy="240" rx="152" ry="168"></ellipse>
                  <path d="M240 72v336"></path>
                  <ellipse cx="240" cy="145" rx="159" ry="17"></ellipse>
                  <ellipse cx="240" cy="187" rx="167" ry="18"></ellipse>
                  <ellipse cx="240" cy="240" rx="168" ry="18"></ellipse>
                  <ellipse cx="240" cy="293" rx="167" ry="18"></ellipse>
                  <ellipse cx="240" cy="335" rx="159" ry="17"></ellipse>
                </g>
                <g stroke="url(#arcGrad)" stroke-width="1.05" stroke-linecap="round">
                  <path class="globe-arc" d="M150 235 Q230 124 250 185"></path>
                  <path class="globe-arc reverse" d="M250 185 Q305 128 350 215"></path>
                  <path class="globe-arc" d="M350 215 Q407 258 380 320"></path>
                  <path class="globe-arc reverse" d="M150 235 Q252 48 365 230"></path>
                  <path class="globe-arc" d="M205 215 Q178 270 215 315"></path>
                </g>
                <g fill="#8ccfff">
                  <circle cx="150" cy="235" r="2.1" fill-opacity="0.9"></circle>
                  <circle cx="205" cy="215" r="1.8" fill-opacity="0.75"></circle>
                  <circle cx="250" cy="185" r="1.8" fill-opacity="0.75"></circle>
                  <circle cx="305" cy="245" r="1.7" fill-opacity="0.65"></circle>
                  <circle cx="350" cy="215" r="2.1" fill-opacity="0.9"></circle>
                  <circle cx="365" cy="230" r="1.5" fill-opacity="0.55"></circle>
                  <circle cx="380" cy="320" r="2" fill-opacity="0.8"></circle>
                  <circle cx="215" cy="315" r="1.7" fill-opacity="0.65"></circle>
                </g>
                <g fill="#9ddcff">
                  <circle class="city-pulse" cx="150" cy="235" r="5" fill-opacity="0.15"></circle>
                  <circle class="city-pulse p2" cx="350" cy="215" r="5" fill-opacity="0.15"></circle>
                  <circle class="city-pulse p3" cx="380" cy="320" r="5" fill-opacity="0.15"></circle>
                </g>
                <g fill="#8ea4c4" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="7.5" font-weight="600" letter-spacing="1.4">
                  <text x="142" y="228" text-anchor="end" fill-opacity="0.65">LAX</text>
                  <text x="242" y="177" text-anchor="end" fill-opacity="0.6">LON</text>
                  <text x="359" y="207" fill-opacity="0.7">BEI</text>
                  <text x="391" y="330" fill-opacity="0.65">SYD</text>
                </g>
              </g>
              <circle cx="240" cy="240" r="168" stroke="#dbeafe" stroke-opacity="0.045" stroke-width="7"></circle>
            </g>

            <g transform="rotate(-18 240 245)" opacity="0.75">
              <ellipse cx="240" cy="245" rx="226" ry="82" stroke="#8099c9" stroke-opacity="0.13" stroke-width="0.8" stroke-dasharray="2 9"></ellipse>
              <circle r="2.7" fill="#9ddcff" fill-opacity="0.9">
                <animateMotion dur="30s" repeatCount="indefinite" path="M 14 245 a 226 82 0 1 0 452 0 a 226 82 0 1 0 -452 0"></animateMotion>
              </circle>
              <circle r="1.5" fill="#c4b5fd" fill-opacity="0.8">
                <animateMotion dur="30s" begin="-15s" repeatCount="indefinite" path="M 14 245 a 226 82 0 1 0 452 0 a 226 82 0 1 0 -452 0"></animateMotion>
              </circle>
            </g>

            <g fill="#dbeafe">
              <circle cx="58" cy="118" r="1.1" opacity="0.35"></circle>
              <circle cx="422" cy="92" r="1.3" opacity="0.38"></circle>
              <circle cx="446" cy="204" r="0.9" opacity="0.28"></circle>
              <circle cx="43" cy="304" r="1.1" opacity="0.28"></circle>
              <circle cx="390" cy="438" r="0.9" opacity="0.26"></circle>
              <circle cx="102" cy="418" r="1.2" opacity="0.24"></circle>
              <circle cx="328" cy="40" r="0.8" opacity="0.32"></circle>
              <circle cx="462" cy="340" r="0.8" opacity="0.24"></circle>
            </g>
          </svg>

          <div class="utc-chip">
            <span class="tiny-dot"></span>
            <span class="utc-chip-label">UTC</span>
            <strong id="hero-utc">00:00</strong>
          </div>
        </div>
      </section>

      <section class="section-head" aria-labelledby="world-clock-title">
        <div>
          <h2 class="section-title" id="world-clock-title">世界时钟 <span class="count-chip" id="count-chip">8</span></h2>
          <p class="section-sub">卡片右上角 × 可移除城市 · 时间每秒刷新</p>
        </div>
        <div class="legend" aria-label="状态图例">
          <span><i class="work-dot"></i>工作时段 · 当地工作日 9–18</span>
          <span><i class="night-dot"></i>夜间</span>
        </div>
      </section>

      <div class="clock-grid" id="clock-grid" aria-live="off"></div>

      <div class="empty-state" id="empty-state" hidden>
        <div class="empty-inner">
          <div class="empty-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round">
              <circle cx="12" cy="12" r="8.5"></circle>
              <path d="M12 7.5V12l3 1.8"></path>
            </svg>
          </div>
          <h2 class="empty-title">还没有添加城市</h2>
          <p class="empty-copy">从全球 400 多个 IANA 时区中挑选城市，建立你的世界时钟。</p>
          <button type="button" class="btn-ghost" id="reset-empty">恢复默认城市</button>
        </div>
      </div>
    </main>

    <footer class="site-foot">
      <span><i class="foot-dot"></i> 时间由设备时钟实时计算 · 基于 Intl API</span>
      <span class="aoe-note">AOE = ANYWHERE ON EARTH · UTC−12</span>
    </footer>
  </div>

  <div class="modal" id="modal" aria-hidden="true">
    <div class="modal-backdrop" data-close-modal></div>
    <div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="modal-title">
      <div class="modal-head">
        <div>
          <p class="modal-kicker">ADD A TIME ZONE</p>
          <h2 class="modal-title" id="modal-title">添加城市</h2>
        </div>
        <button type="button" class="icon-btn" id="close-modal" aria-label="关闭">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">
            <path d="M6 6l12 12M18 6L6 18"></path>
          </svg>
        </button>
      </div>
      <div class="search-box">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true">
          <circle cx="11" cy="11" r="6.7"></circle>
          <path d="M16 16l4.2 4.2"></path>
        </svg>
        <input type="search" id="zone-search" placeholder="搜索城市或时区，例如：东京、Europe/London" autocomplete="off" spellcheck="false" aria-label="搜索城市或时区">
      </div>
      <div class="modal-hint">
        <span id="modal-hint-label">热门城市</span>
        <span class="hint-count" id="modal-hint-count"></span>
      </div>
      <div class="zone-list" id="zone-list"></div>
    </div>
  </div>

  <div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
(function () {
  'use strict';

  var STORAGE_KEY = 'world-clock.zones.v1';
  var FORMAT_KEY = 'world-clock.format.v1';
  var DEFAULT_ZONES = [
    'Asia/Shanghai',
    'America/Los_Angeles',
    'Etc/UTC',
    'Etc/GMT+12',
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney'
  ];

  var ZONE_META = {
    'Asia/Shanghai': { zh: '北京', en: 'Beijing', region: 'CN' },
    'Asia/Hong_Kong': { zh: '香港', en: 'Hong Kong', region: 'HK' },
    'Asia/Taipei': { zh: '台北', en: 'Taipei', region: 'TW' },
    'Asia/Tokyo': { zh: '东京', en: 'Tokyo', region: 'JP' },
    'Asia/Seoul': { zh: '首尔', en: 'Seoul', region: 'KR' },
    'Asia/Singapore': { zh: '新加坡', en: 'Singapore', region: 'SG' },
    'Asia/Bangkok': { zh: '曼谷', en: 'Bangkok', region: 'TH' },
    'Asia/Dubai': { zh: '迪拜', en: 'Dubai', region: 'AE' },
    'Asia/Kolkata': { zh: '加尔各答', en: 'Kolkata', region: 'IN' },
    'Asia/Colombo': { zh: '科伦坡', en: 'Colombo', region: 'LK' },
    'Asia/Kathmandu': { zh: '加德满都', en: 'Kathmandu', region: 'NP' },
    'Asia/Dhaka': { zh: '达卡', en: 'Dhaka', region: 'BD' },
    'Asia/Karachi': { zh: '卡拉奇', en: 'Karachi', region: 'PK' },
    'Asia/Riyadh': { zh: '利雅得', en: 'Riyadh', region: 'SA' },
    'Asia/Jerusalem': { zh: '耶路撒冷', en: 'Jerusalem', region: 'IL' },
    'Asia/Istanbul': { zh: '伊斯坦布尔', en: 'Istanbul', region: 'TR' },
    'Asia/Jakarta': { zh: '雅加达', en: 'Jakarta', region: 'ID' },
    'Asia/Kuala_Lumpur': { zh: '吉隆坡', en: 'Kuala Lumpur', region: 'MY' },
    'Asia/Manila': { zh: '马尼拉', en: 'Manila', region: 'PH' },
    'Asia/Ho_Chi_Minh': { zh: '胡志明市', en: 'Ho Chi Minh City', region: 'VN' },
    'Asia/Hanoi': { zh: '河内', en: 'Hanoi', region: 'VN' },
    'Europe/London': { zh: '伦敦', en: 'London', region: 'GB' },
    'Europe/Paris': { zh: '巴黎', en: 'Paris', region: 'FR' },
    'Europe/Berlin': { zh: '柏林', en: 'Berlin', region: 'DE' },
    'Europe/Madrid': { zh: '马德里', en: 'Madrid', region: 'ES' },
    'Europe/Rome': { zh: '罗马', en: 'Rome', region: 'IT' },
    'Europe/Amsterdam': { zh: '阿姆斯特丹', en: 'Amsterdam', region: 'NL' },
    'Europe/Zurich': { zh: '苏黎世', en: 'Zurich', region: 'CH' },
    'Europe/Stockholm': { zh: '斯德哥尔摩', en: 'Stockholm', region: 'SE' },
    'Europe/Moscow': { zh: '莫斯科', en: 'Moscow', region: 'RU' },
    'Europe/Lisbon': { zh: '里斯本', en: 'Lisbon', region: 'PT' },
    'Europe/Dublin': { zh: '都柏林', en: 'Dublin', region: 'IE' },
    'Europe/Athens': { zh: '雅典', en: 'Athens', region: 'GR' },
    'Europe/Warsaw': { zh: '华沙', en: 'Warsaw', region: 'PL' },
    'Europe/Kyiv': { zh: '基辅', en: 'Kyiv', region: 'UA' },
    'America/Los_Angeles': { zh: '洛杉矶', en: 'Los Angeles', region: 'US' },
    'America/New_York': { zh: '纽约', en: 'New York', region: 'US' },
    'America/Chicago': { zh: '芝加哥', en: 'Chicago', region: 'US' },
    'America/Denver': { zh: '丹佛', en: 'Denver', region: 'US' },
    'America/Phoenix': { zh: '凤凰城', en: 'Phoenix', region: 'US' },
    'America/Toronto': { zh: '多伦多', en: 'Toronto', region: 'CA' },
    'America/Vancouver': { zh: '温哥华', en: 'Vancouver', region: 'CA' },
    'America/Mexico_City': { zh: '墨西哥城', en: 'Mexico City', region: 'MX' },
    'America/Sao_Paulo': { zh: '圣保罗', en: 'São Paulo', region: 'BR' },
    'America/Argentina/Buenos_Aires': { zh: '布宜诺斯艾利斯', en: 'Buenos Aires', region: 'AR' },
    'America/Bogota': { zh: '波哥大', en: 'Bogotá', region: 'CO' },
    'America/Lima': { zh: '利马', en: 'Lima', region: 'PE' },
    'America/Santiago': { zh: '圣地亚哥', en: 'Santiago', region: 'CL' },
    'Pacific/Honolulu': { zh: '檀香山', en: 'Honolulu', region: 'US' },
    'America/Anchorage': { zh: '安克雷奇', en: 'Anchorage', region: 'US' },
    'Australia/Sydney': { zh: '悉尼', en: 'Sydney', region: 'AU' },
    'Australia/Melbourne': { zh: '墨尔本', en: 'Melbourne', region: 'AU' },
    'Australia/Brisbane': { zh: '布里斯班', en: 'Brisbane', region: 'AU' },
    'Australia/Perth': { zh: '珀斯', en: 'Perth', region: 'AU' },
    'Pacific/Auckland': { zh: '奥克兰', en: 'Auckland', region: 'NZ' },
    'Pacific/Fiji': { zh: '苏瓦', en: 'Suva', region: 'FJ' },
    'Africa/Cairo': { zh: '开罗', en: 'Cairo', region: 'EG' },
    'Africa/Johannesburg': { zh: '约翰内斯堡', en: 'Johannesburg', region: 'ZA' },
    'Africa/Nairobi': { zh: '内罗毕', en: 'Nairobi', region: 'KE' },
    'Africa/Lagos': { zh: '拉各斯', en: 'Lagos', region: 'NG' },
    'Africa/Casablanca': { zh: '卡萨布兰卡', en: 'Casablanca', region: 'MA' },
    'Etc/UTC': { zh: 'UTC', en: 'Coordinated Universal Time', region: 'UTC' },
    'Etc/GMT+12': { zh: 'AOE', en: 'Anywhere on Earth', region: 'AOE' }
  };

  var ACCENTS = ['#f6c453', '#fb8b6d', '#67e8f9', '#c4b5fd', '#7dd3fc', '#86efac', '#f9a8d4', '#5eead4', '#fca5a5', '#bef264', '#f0abfc', '#93c5fd'];
  var WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
  var WEEKDAYS_FULL = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];

  var ICONS = {
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"></circle><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4L6 18M18 6l1.4-1.4"></path></svg>',
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.6 8.6 0 1 0 10.5 10.5Z"></path></svg>',
    work: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2.5"></rect><path d="M8 7V5.5A1.5 1.5 0 0 1 9.5 4h5A1.5 1.5 0 0 1 16 5.5V7M3 12h18M10 12v2h4v-2"></path></svg>'
  };

  var grid = document.getElementById('clock-grid');
  var emptyState = document.getElementById('empty-state');
  var countChip = document.getElementById('count-chip');
  var zoneCount = document.getElementById('zone-count');
  var heroHm = document.getElementById('hero-hm');
  var heroSec = document.getElementById('hero-sec');
  var heroPeriod = document.getElementById('hero-period');
  var heroDate = document.getElementById('hero-date');
  var heroWeekday = document.getElementById('hero-weekday');
  var heroUtc = document.getElementById('hero-utc');
  var localZoneName = document.getElementById('local-zone-name');
  var modal = document.getElementById('modal');
  var modalSearch = document.getElementById('zone-search');
  var zoneList = document.getElementById('zone-list');
  var modalHintLabel = document.getElementById('modal-hint-label');
  var modalHintCount = document.getElementById('modal-hint-count');
  var openAddButton = document.getElementById('open-add');
  var closeModalButton = document.getElementById('close-modal');
  var resetEmptyButton = document.getElementById('reset-empty');
  var toastEl = document.getElementById('toast');
  var formatButtons = Array.prototype.slice.call(document.querySelectorAll('[data-format]'));

  var formatterCache = new Map();
  var zoneValidity = new Map();
  var searchIndex = new Map();
  var supportedZones = null;
  var cardMap = new Map();
  var toastTimer = null;
  var lastFocusedElement = null;

  var state = {
    zones: [],
    format: '24',
    localZone: 'Etc/UTC'
  };

  function pad(value) {
    return String(value).padStart(2, '0');
  }

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (character) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character];
    });
  }

  function isValidZone(zone) {
    if (typeof zone !== 'string' || zone.length === 0) return false;
    if (zoneValidity.has(zone)) return zoneValidity.get(zone);
    var valid = true;
    try {
      new Intl.DateTimeFormat('en-US', { timeZone: zone }).format(0);
    } catch (error) {
      valid = false;
    }
    zoneValidity.set(zone, valid);
    return valid;
  }

  function hashCode(value) {
    var hash = 0;
    for (var i = 0; i < value.length; i += 1) {
      hash = (hash * 31 + value.charCodeAt(i)) | 0;
    }
    return Math.abs(hash);
  }

  function accentFor(zone) {
    return ACCENTS[hashCode(zone) % ACCENTS.length];
  }

  function hexToRgba(hex, alpha) {
    var clean = hex.replace('#', '');
    var value = parseInt(clean, 16);
    var red = (value >> 16) & 255;
    var green = (value >> 8) & 255;
    var blue = value & 255;
    return 'rgba(' + red + ', ' + green + ', ' + blue + ', ' + alpha + ')';
  }

  function getMeta(zone) {
    if (ZONE_META[zone]) {
      return {
        zh: ZONE_META[zone].zh,
        en: ZONE_META[zone].en,
        region: ZONE_META[zone].region,
        accent: accentFor(zone)
      };
    }
    var segment = zone.split('/').pop().replace(/_/g, ' ');
    var prefix = zone.split('/')[0];
    var regionMap = { Asia: 'AS', Europe: 'EU', America: 'AM', Africa: 'AF', Australia: 'OC', Pacific: 'PA', Atlantic: 'AT', Indian: 'IN', Etc: 'UTC' };
    return {
      zh: segment,
      en: segment,
      region: regionMap[prefix] || 'TZ',
      accent: accentFor(zone)
    };
  }

  function loadZones() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (raw === null) return DEFAULT_ZONES.slice();
      var parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return DEFAULT_ZONES.slice();
      var seen = {};
      return parsed.filter(function (zone) {
        if (typeof zone !== 'string' || seen[zone] || !isValidZone(zone)) return false;
        seen[zone] = true;
        return true;
      });
    } catch (error) {
      return DEFAULT_ZONES.slice();
    }
  }

  function loadFormat() {
    try {
      return localStorage.getItem(FORMAT_KEY) === '12' ? '12' : '24';
    } catch (error) {
      return '24';
    }
  }

  function persistZones() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.zones));
    } catch (error) {}
  }

  function persistFormat() {
    try {
      localStorage.setItem(FORMAT_KEY, state.format);
    } catch (error) {}
  }

  function getParts(zone, date) {
    var formatter = formatterCache.get(zone);
    if (!formatter) {
      formatter = new Intl.DateTimeFormat('en-US', {
        timeZone: zone,
        hourCycle: 'h23',
        year: 'numeric',
        month: 'numeric',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
      formatterCache.set(zone, formatter);
    }
    var parts = formatter.formatToParts(date);
    var result = {};
    for (var i = 0; i < parts.length; i += 1) {
      if (parts[i].type !== 'literal') result[parts[i].type] = parts[i].value;
    }
    return {
      year: Number(result.year),
      month: Number(result.month),
      day: Number(result.day),
      hour: Number(result.hour),
      minute: Number(result.minute),
      second: Number(result.second)
    };
  }

  function offsetMinutes(parts, date) {
    var localAsUtc = Date.UTC(parts.year, parts.month - 1, parts.day, parts.hour, parts.minute, parts.second);
    var epochSecond = Math.floor(date.getTime() / 1000) * 1000;
    return Math.round((localAsUtc - epochSecond) / 60000);
  }

  function offsetLabel(minutes) {
    if (minutes === 0) return 'UTC';
    var sign = minutes > 0 ? '+' : '−';
    var absolute = Math.abs(minutes);
    var hours = Math.floor(absolute / 60);
    var mins = absolute % 60;
    return 'UTC' + sign + hours + (mins ? ':' + pad(mins) : '');
  }

  function weekdayIndex(year, month, day) {
    return new Date(Date.UTC(year, month - 1, day)).getUTCDay();
  }

  function dayStatus(hour, weekday) {
    var isWorkday = weekday >= 1 && weekday <= 5;
    if (isWorkday && hour >= 9 && hour < 18) {
      return { label: '工作时段', className: 'is-work', icon: 'work' };
    }
    if (hour >= 6 && hour < 18) {
      return { label: '白天', className: 'is-day', icon: 'sun' };
    }
    return { label: '夜间', className: 'is-night', icon: 'moon' };
  }

  function timeText(parts) {
    var hour = parts.hour;
    var period = hour < 12 ? 'AM' : 'PM';
    if (state.format === '12') {
      hour = hour % 12 || 12;
    }
    return {
      main: (state.format === '12' ? String(hour) : pad(hour)) + ':' + pad(parts.minute),
      seconds: ':' + pad(parts.second),
      period: period
    };
  }

  function dateText(parts, currentYear) {
    var yearPrefix = parts.year !== currentYear ? parts.year + '年' : '';
    return yearPrefix + parts.month + '月' + parts.day + '日 ' + WEEKDAYS[weekdayIndex(parts.year, parts.month, parts.day)];
  }

  function dayDifference(parts, localAnchor) {
    var anchor = Date.UTC(parts.year, parts.month - 1, parts.day);
    return Math.round((anchor - localAnchor) / 86400000);
  }

  function setPeriodVisibility(element, visible) {
    if (element) element.classList.toggle('is-hidden', !visible);
  }

  function buildCard(zone, index) {
    var meta = getMeta(zone);
    var card = document.createElement('article');
    card.className = 'clock-card' + (zone === state.localZone ? ' is-local' : '');
    card.setAttribute('role', 'group');
    card.dataset.zone = zone;
    card.style.setProperty('--accent', meta.accent);
    card.style.setProperty('--accent-soft', hexToRgba(meta.accent, 0.10));
    card.style.setProperty('--i', String(index));

    card.innerHTML = [
      '<button type="button" class="remove" aria-label="移除 ' + escapeHtml(meta.zh) + '" title="移除 ' + escapeHtml(meta.zh) + '">',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"></path></svg>',
      '</button>',
      '<div class="card-head">',
        '<div class="city">',
          '<span class="region">' + escapeHtml(meta.region) + '</span>',
          '<div class="city-text">',
            '<h3>' + escapeHtml(meta.zh) + (zone === state.localZone ? '<span class="local-chip">本地</span>' : '') + '</h3>',
            '<span class="city-en">' + escapeHtml(meta.en) + '</span>',
          '</div>',
        '</div>',
      '</div>',
      '<div class="time-line">',
        '<span class="time-main">--:--</span>',
        '<span class="time-sec">:--</span>',
        '<span class="time-period">AM</span>',
      '</div>',
      '<div class="date-line">',
        '<span class="date-text">—</span>',
        '<span class="date-diff" hidden></span>',
      '</div>',
      '<div class="dayline" aria-hidden="true"><span class="dayline-marker"></span></div>',
      '<div class="card-foot">',
        '<div class="foot-left">',
          '<span class="offset">UTC</span>',
          '<span class="day-status"><span class="status-icon">' + ICONS.moon + '</span><span class="status-label">夜间</span></span>',
        '</div>',
        '<div class="dial" aria-hidden="true">',
          '<span class="dial-hand dial-hour"></span>',
          '<span class="dial-hand dial-minute"></span>',
          '<span class="dial-pin"></span>',
        '</div>',
      '</div>'
    ].join('');

    var refs = {
      root: card,
      zone: zone,
      meta: meta,
      time: card.querySelector('.time-main'),
      seconds: card.querySelector('.time-sec'),
      period: card.querySelector('.time-period'),
      date: card.querySelector('.date-text'),
      diff: card.querySelector('.date-diff'),
      offset: card.querySelector('.offset'),
      status: card.querySelector('.day-status'),
      statusIcon: card.querySelector('.status-icon'),
      statusLabel: card.querySelector('.status-label'),
      marker: card.querySelector('.dayline-marker'),
      dialHour: card.querySelector('.dial-hour'),
      dialMinute: card.querySelector('.dial-minute')
    };

    refs.lastStatus = '';
    card.querySelector('.remove').addEventListener('click', function () {
      removeZone(zone);
    });

    cardMap.set(zone, refs);
    return card;
  }

  function renderGrid() {
    grid.innerHTML = '';
    cardMap.clear();
    state.zones.forEach(function (zone, index) {
      grid.appendChild(buildCard(zone, index));
    });
    updateCounts();
    tick();
  }

  function updateCounts() {
    var total = state.zones.length;
    countChip.textContent = String(total);
    zoneCount.textContent = String(total);
    emptyState.hidden = total !== 0;
    grid.hidden = total === 0;
  }

  function appendCard(zone) {
    var card = buildCard(zone, 0);
    grid.appendChild(card);
    emptyState.hidden = true;
    grid.hidden = false;
    updateCounts();
    tick();
    card.style.animationDelay = '0ms';
  }

  function addZone(zone) {
    if (!isValidZone(zone) || state.zones.indexOf(zone) !== -1) return false;
    state.zones.push(zone);
    persistZones();
    appendCard(zone);
    showToast('已添加 ' + getMeta(zone).zh);
    return true;
  }

  function removeZone(zone) {
    var refs = cardMap.get(zone);
    if (!refs) return;
    refs.root.classList.add('is-removing');
    showToast('已移除 ' + refs.meta.zh);
    window.setTimeout(function () {
      if (refs.root.parentNode) refs.root.parentNode.removeChild(refs.root);
      cardMap.delete(zone);
      state.zones = state.zones.filter(function (item) { return item !== zone; });
      persistZones();
      updateCounts();
    }, 205);
  }

  function resetDefaults() {
    state.zones = DEFAULT_ZONES.slice();
    persistZones();
    renderGrid();
    showToast('已恢复默认城市');
  }

  function updateCard(refs, now, localAnchor, currentYear) {
    var parts = getParts(refs.zone, now);
    var formatted = timeText(parts);
    var offset = offsetMinutes(parts, now);
    var weekday = weekdayIndex(parts.year, parts.month, parts.day);
    var status = dayStatus(parts.hour, weekday);
    var diff = dayDifference(parts, localAnchor);

    refs.time.textContent = formatted.main;
    refs.seconds.textContent = formatted.seconds;
    refs.period.textContent = formatted.period;
    setPeriodVisibility(refs.period, state.format === '12');
    refs.date.textContent = dateText(parts, currentYear);
    refs.offset.textContent = offsetLabel(offset);

    if (diff === 0) {
      refs.diff.hidden = true;
      refs.diff.textContent = '';
    } else {
      refs.diff.hidden = false;
      refs.diff.textContent = diff === 1 ? '明天' : diff === -1 ? '昨天' : (diff > 0 ? '+' + diff + '天' : diff + '天');
      refs.diff.classList.toggle('behind', diff < 0);
    }

    refs.marker.style.left = (((parts.hour * 3600 + parts.minute * 60 + parts.second) / 86400) * 100).toFixed(3) + '%';

    if (refs.lastStatus !== status.className) {
      refs.status.classList.remove('is-work', 'is-day', 'is-night');
      refs.status.classList.add(status.className);
      refs.statusIcon.innerHTML = ICONS[status.icon];
      refs.statusLabel.textContent = status.label;
      refs.lastStatus = status.className;
    }

    refs.dialHour.style.transform = 'rotate(' + ((parts.hour % 12) * 30 + parts.minute * 0.5) + 'deg)';
    refs.dialMinute.style.transform = 'rotate(' + (parts.minute * 6 + parts.second * 0.1) + 'deg)';

    var aria = (refs.zone === state.localZone ? '本地时区，' : '') + refs.meta.zh + '，当地时间 ' + formatted.main + '，' + offsetLabel(offset) + '，' + status.label;
    if (refs.root.getAttribute('aria-label') !== aria) refs.root.setAttribute('aria-label', aria);
  }

  function tick() {
    var now = new Date();
    var localYear = now.getFullYear();
    var localAnchor = Date.UTC(localYear, now.getMonth(), now.getDate());
    var local = {
      year: localYear,
      month: now.getMonth() + 1,
      day: now.getDate(),
      hour: now.getHours(),
      minute: now.getMinutes(),
      second: now.getSeconds()
    };
    var formatted = timeText(local);

    heroHm.textContent = formatted.main;
    heroSec.textContent = formatted.seconds;
    heroPeriod.textContent = formatted.period;
    setPeriodVisibility(heroPeriod, state.format === '12');
    heroDate.textContent = localYear + '年' + local.month + '月' + local.day + '日';
    heroWeekday.textContent = WEEKDAYS_FULL[now.getDay()];
    heroUtc.textContent = pad(now.getUTCHours()) + ':' + pad(now.getUTCMinutes());

    cardMap.forEach(function (refs) {
      updateCard(refs, now, localAnchor, localYear);
    });
  }

  function setFormat(format, persist) {
    state.format = format === '12' ? '12' : '24';
    formatButtons.forEach(function (button) {
      var active = button.dataset.format === state.format;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
    if (persist !== false) persistFormat();
    tick();
  }

  function showToast(message) {
    toastEl.textContent = message;
    toastEl.classList.add('show');
    if (toastTimer) window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(function () {
      toastEl.classList.remove('show');
    }, 2000);
  }

  function supportedZoneList() {
    if (supportedZones) return supportedZones;
    var list = [];
    try {
      if (typeof Intl.supportedValuesOf === 'function') {
        list = Intl.supportedValuesOf('timeZone');
      }
    } catch (error) {}
    var merged = [];
    var seen = {};
    var add = function (zone) {
      if (!zone || seen[zone] || !isValidZone(zone)) return;
      seen[zone] = true;
      merged.push(zone);
    };
    Object.keys(ZONE_META).forEach(add);
    DEFAULT_ZONES.forEach(add);
    list.forEach(add);
    merged.sort(function (a, b) {
      var metaA = getMeta(a);
      var metaB = getMeta(b);
      return metaA.zh.localeCompare(metaB.zh, 'zh-CN') || a.localeCompare(b);
    });
    merged.forEach(function (zone) {
      var meta = getMeta(zone);
      searchIndex.set(zone, (meta.zh + ' ' + meta.en + ' ' + meta.region + ' ' + zone).toLowerCase());
    });
    supportedZones = merged;
    return merged;
  }

  function popularZones() {
    return [
      'Asia/Shanghai', 'Asia/Tokyo', 'Asia/Singapore', 'Asia/Dubai',
      'Europe/London', 'Europe/Paris', 'Europe/Berlin',
      'America/New_York', 'America/Los_Angeles', 'America/Chicago',
      'Australia/Sydney', 'Pacific/Auckland', 'Etc/UTC', 'Etc/GMT+12'
    ];
  }

  function renderZoneList(query) {
    supportedZoneList();
    var normalized = query.trim().toLowerCase();
    var matches;
    if (normalized) {
      matches = supportedZones.filter(function (zone) {
        return searchIndex.get(zone).indexOf(normalized) !== -1;
      }).slice(0, 60);
      modalHintLabel.textContent = '搜索结果';
    } else {
      matches = popularZones();
      modalHintLabel.textContent = '热门城市';
    }

    modalHintCount.textContent = normalized ? '找到 ' + matches.length + ' 个结果' : '全球 ' + supportedZones.length + ' 个可用时区';

    if (matches.length === 0) {
      zoneList.innerHTML = '<div class="zone-empty">没有找到匹配的时区<br>试试搜索「东京」或「Europe/London」</div>';
      return;
    }

    var now = new Date();
    var html = matches.map(function (zone) {
      var meta = getMeta(zone);
      var added = state.zones.indexOf(zone) !== -1;
      var parts = getParts(zone, now);
      var formatted = timeText(parts);
      var modalTime = formatted.main + (state.format === '12' ? ' ' + formatted.period : '');
      var offset = offsetLabel(offsetMinutes(parts, now));
      return [
        '<button type="button" class="zone-option' + (added ? ' is-added' : '') + '" data-zone="' + escapeHtml(zone) + '"' + (added ? ' disabled' : '') + '>',
          '<span class="region">' + escapeHtml(meta.region) + '</span>',
          '<span class="zone-option-info">',
            '<span class="zone-option-name">' + escapeHtml(meta.zh) + '<em>' + escapeHtml(meta.en) + '</em></span>',
            '<span class="zone-option-id">' + escapeHtml(zone) + '</span>',
          '</span>',
          '<span class="zone-option-time"><strong>' + modalTime + '</strong><small>' + offset + '</small></span>',
          '<span class="zone-option-add" aria-hidden="true">' + (added ? '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"></path></svg>' : '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M12 5v14M5 12h14"></path></svg>') + '</span>',
        '</button>'
      ].join('');
    }).join('');

    zoneList.innerHTML = html;
  }

  function openModal() {
    lastFocusedElement = document.activeElement;
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');
    modalSearch.value = '';
    renderZoneList('');
    window.setTimeout(function () {
      modalSearch.focus();
    }, 80);
  }

  function closeModal() {
    if (!modal.classList.contains('open')) return;
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');
    if (lastFocusedElement && typeof lastFocusedElement.focus === 'function') {
      lastFocusedElement.focus();
    }
  }

  function handleTabTrap(event) {
    if (event.key !== 'Tab' || !modal.classList.contains('open')) return;
    var focusable = modal.querySelectorAll('button:not([disabled]), input:not([disabled]), [href], [tabindex]:not([tabindex="-1"])');
    if (!focusable.length) return;
    var first = focusable[0];
    var last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && document.activeElement === last) {
      event.preventDefault();
      first.focus();
    }
  }

  function init() {
    state.zones = loadZones();
    state.format = loadFormat();
    state.localZone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'Etc/UTC';

    var localParts = state.localZone.split('/');
    var localMeta = ZONE_META[state.localZone];
    var localCity = localMeta ? localMeta.zh : localParts[localParts.length - 1].replace(/_/g, ' ');
    localZoneName.textContent = localCity;
    localZoneName.title = state.localZone;

    setFormat(state.format, false);
    renderGrid();
    supportedZoneList();

    openAddButton.addEventListener('click', openModal);
    closeModalButton.addEventListener('click', closeModal);
    resetEmptyButton.addEventListener('click', resetDefaults);

    modal.addEventListener('click', function (event) {
      if (event.target.closest('[data-close-modal]')) closeModal();
    });

    modalSearch.addEventListener('input', function () {
      renderZoneList(modalSearch.value);
    });

    zoneList.addEventListener('click', function (event) {
      var option = event.target.closest('.zone-option');
      if (!option || option.disabled) return;
      var zone = option.dataset.zone;
      if (addZone(zone)) closeModal();
    });

    formatButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        setFormat(button.dataset.format, true);
      });
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') closeModal();
      handleTabTrap(event);
    });

    document.addEventListener('visibilitychange', function () {
      if (!document.hidden) tick();
    });

    window.setInterval(tick, 1000);
  }

  init();
})();
</script>
</body>
</html>
