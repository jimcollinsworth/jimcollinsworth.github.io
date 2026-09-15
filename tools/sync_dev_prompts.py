"""
tools/sync_dev_prompts.py
=========================
Parses JOURNAL.md to extract Jim's direct steering prompts, agent errors/corrections,
and architectural milestones, generating a comprehensive, scalable
'Development Prompts & Instruction Timeline' for content/pages/prompt-history.md.

Honors Jim's instructions:
- Simple prompt text (preserve Jim's verbatim wording, no haikus).
- Highlights critical agent errors and course corrections.
- Scalable on a per-session / per-release basis.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JOURNAL_PATH = REPO_ROOT / "JOURNAL.md"
PROMPT_HISTORY_PAGE = REPO_ROOT / "content" / "pages" / "prompt-history.md"


def parse_journal() -> tuple[list[dict], int]:
    """Parse JOURNAL.md and return structured milestone entries and total prompt count."""
    text = JOURNAL_PATH.read_text(encoding="utf-8")
    
    # Split by section headers (## YYYY-MM-DD ...)
    raw_sections = re.split(r"\n(?=## \d{4}-\d{2}-\d{2})", text)
    milestones = []
    total_prompt_count = 0

    for sec in raw_sections:
        if not sec.strip().startswith("## "):
            continue

        lines = [l for l in sec.strip().split("\n") if l.strip()]
        header_line = lines[0].replace("## ", "").strip()

        # Extract title and date
        header_match = re.match(r"^(\d{4}-\d{2}-\d{2})\s*[—–-]\s*(.*)$", header_line)
        if header_match:
            date_str, title_str = header_match.groups()
        else:
            date_str, title_str = "", header_line

        # Extract Jim's prompts
        prompts = []
        prompt_block_match = re.search(
            r">\s*\[!NOTE\]\s*Jim'?s?\s*(?:Prompts|Instructions|Guidance|Steering)[^\n]*\n((?:>[^\n]*\n?)+)",
            sec,
            re.IGNORECASE
        )
        if prompt_block_match:
            block = prompt_block_match.group(1)
            bullet_prompts = re.findall(r'>\s*-\s*\*(?:""|")?(.*?)(?:""|")?\*(?:\s*|$)', block, re.DOTALL)
            if bullet_prompts:
                for bp in bullet_prompts:
                    cleaned = bp.strip().strip('"').strip()
                    if cleaned:
                        prompts.append(cleaned)
            else:
                quotes = re.findall(r'"([^"\n]{10,})"', block)
                for q in quotes:
                    prompts.append(q.strip())

        if not prompts:
            continue

        total_prompt_count += len(prompts)

        # Extract concise actions from Solution & Standard Procedure or Decisions & Actions Taken
        sol_match = re.search(r"### (?:Solution[^\n]*|Decisions & Actions Taken)\s*\n(.*?)(?=\n###|\n---|\Z)", sec, re.DOTALL)
        sol_text = sol_match.group(1).strip() if sol_match else ""

        actions = []
        items = re.findall(r"^\d+\.\s*\*\*(.*?)\*\*:\s*(.*)", sol_text, re.MULTILINE)
        if items:
            for name, desc in items[:3]:
                first_line = desc.strip().split("\n")[0].strip()
                first_line = re.sub(r"^[-*]\s*", "", first_line)
                first_sent = first_line.split(". ")[0].strip().rstrip(".")
                actions.append(f"{name}: {first_sent}.")
        else:
            bullets = re.findall(r"^[-*]\s*(.*)", sol_text, re.MULTILINE)
            if bullets:
                for b in bullets[:2]:
                    first_line = b.strip().split("\n")[0].strip()
                    actions.append(first_line)
            elif sol_text:
                first_line = sol_text.split("\n")[0].strip()
                if first_line:
                    actions.append(first_line)

        milestones.append({
            "date": date_str,
            "title": title_str,
            "prompts": prompts,
            "actions": actions,
        })

    return milestones, total_prompt_count


def format_date(d_str: str) -> str:
    """Format YYYY-MM-DD into 'Sept 13 2026'."""
    if not d_str:
        return ""
    try:
        parts = d_str.split("-")
        year = parts[0]
        month = int(parts[1])
        day = int(parts[2])
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        return f"{months[month - 1]} {day} {year}"
    except Exception:
        return d_str


def get_release_timestamps() -> dict[str, str]:
    """Extract release timestamps from git log."""
    try:
        import subprocess
        out = subprocess.check_output(
            ["git", "log", "--format=%ai|%s"],
            cwd=REPO_ROOT,
            text=True,
            encoding="utf-8"
        )
        release_times = {}
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
        for line in out.splitlines():
            m = re.search(r"v\d+\.\d+(?:\.\d+)?", line)
            if m:
                tag = m.group(0)
                if tag not in release_times:
                    parts = line.split("|")
                    if len(parts) >= 1:
                        raw = parts[0].strip()
                        try:
                            dt_part, tz = raw.rsplit(" ", 1)
                            date_part, time_part = dt_part.split(" ")
                            y, mo, d = date_part.split("-")
                            hh, mm, ss = time_part.split(":")
                            hour = int(hh)
                            minute = int(mm)
                            ampm = "AM" if hour < 12 else "PM"
                            display_hour = hour % 12
                            if display_hour == 0:
                                display_hour = 12
                            formatted = f"{months[int(mo)-1]} {int(d)} {y}, {display_hour}:{minute:02d} {ampm} CDT"
                            release_times[tag] = formatted
                        except Exception:
                            release_times[tag] = raw
        return release_times
    except Exception:
        return {}


def generate_prompt_history_markdown(milestones: list[dict], total_prompts: int) -> str:
    """Generate clean prompt timeline honoring Jim's layout rules."""
    ICON_MINE = '<svg class="category-icon icon-mine" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"></path><line x1="16" y1="8" x2="2" y2="22"></line><line x1="17.5" y1="15" x2="9" y2="15"></line></svg>'
    ICON_AI = '<svg class="category-icon icon-ai" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 8V4H8"></path><rect width="16" height="12" x="4" y="8" rx="2"></rect><path d="M2 14h2"></path><path d="M20 14h2"></path><path d="M15 13v2"></path><path d="M9 13v2"></path></svg>'
    
    latest_date_str = milestones[0]["date"] if milestones and milestones[0].get("date") else "2026-09-13"
    latest_formatted = format_date(latest_date_str)

    # Order milestones chronologically (oldest to newest)
    chronological_milestones = list(reversed(milestones))

    md = []
    md.append("---")
    md.append('title: "Development Prompts"')
    md.append('slug: "prompt-history"')
    md.append('category: "Mine"')
    md.append('author: "Jim Collinsworth"')
    md.append("---")
    md.append("")
    md.append('<header class="post-header-full">')
    md.append('  <div class="post-header-row">')
    md.append('    <div class="post-header-left">')
    md.append('      <a href="about-this-site.html" class="post-back-arrow" title="Back to About This Site" aria-label="Back to About This Site">&larr;</a>')
    md.append(f'      <span class="category-badge dual-badge" title="Provenance: Jim Collinsworth &bull; AI Pair" aria-label="Category: Mine and AI">{ICON_MINE}{ICON_AI}</span>')
    md.append('      <h1 class="post-title">Development Prompts</h1>')
    md.append('    </div>')
    md.append('    <div class="post-header-right">')
    md.append(f'      <time datetime="{latest_date_str}">{latest_formatted}</time>')
    md.append('    </div>')
    md.append('  </div>')
    md.append('</header>')
    md.append("")
    md.append(f"Steering prompts and technical corrections for `jimcollinsworth.github.io`, chronologically extracted from `JOURNAL.md` via `tools/sync_dev_prompts.py`. It contains **{total_prompts} prompts** from Jim across {len(milestones)} milestones, alongside concise summaries of actions taken.")
    md.append("")

    release_timestamps = get_release_timestamps()

    for m in chronological_milestones:
        title = m['title']
        date_str = m['date']
        
        # Link to relevant GitHub release tag or releases overview
        ver_match = re.search(r"v\d+\.\d+(?:\.\d+)?", title)
        tag = ver_match.group(0) if ver_match else ""
        if tag:
            rel_link = f"https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases/tag/{tag}"
            formatted_dt = release_timestamps.get(tag, format_date(date_str))
        else:
            rel_link = "https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases"
            formatted_dt = format_date(date_str)

        date_html = f'<time datetime="{date_str}" class="milestone-date">{formatted_dt}</time>' if formatted_dt else ''

        md.append('<div class="milestone-header">')
        md.append(f'  <h2 class="milestone-title"><a href="{rel_link}" target="_blank" rel="noopener">{title}</a></h2>')
        if date_html:
            md.append(f'  {date_html}')
        md.append('</div>')
        md.append("")

        # Conversational Chat Thread: Jim (Mine) & AI Pair
        md.append('<div class="chat-thread">')
        
        # Jim's Chat Bubble
        md.append('  <div class="chat-bubble chat-user">')
        md.append(f'    <div class="chat-meta"><span class="category-badge" title="Provenance: Mine">{ICON_MINE}</span> <strong class="chat-name">Jim</strong></div>')
        md.append('    <div class="chat-body">')
        for p in m["prompts"]:
            sanitized_p = re.sub(r"<(/?[a-zA-Z0-9]+[^>]*)>", r"&lt;\1&gt;", p.strip())
            sanitized_p = re.sub(r"`([^`]+)`", r"<code>\1</code>", sanitized_p)
            md.append(f'      <p>{sanitized_p}</p>')
        md.append('    </div>')
        md.append('  </div>')

        # AI Assistant Chat Bubble
        if m["actions"]:
            md.append('  <div class="chat-bubble chat-ai">')
            md.append(f'    <div class="chat-meta"><span class="category-badge" title="Provenance: AI">{ICON_AI}</span> <strong class="chat-name">AI Assistant (LLM-Gemini3.8)</strong></div>')
            md.append('    <div class="chat-body">')
            md.append('      <ul class="response-actions">')
            for a in m["actions"]:
                sanitized_a = re.sub(r"<(/?[a-zA-Z0-9]+[^>]*)>", r"&lt;\1&gt;", a)
                sanitized_a = re.sub(r"`([^`]+)`", r"<code>\1</code>", sanitized_a)
                md.append(f'        <li>{sanitized_a}</li>')
            md.append('      </ul>')
            md.append('    </div>')
            md.append('  </div>')

        md.append('</div>')
        md.append("")

    md.append('<div style="margin-top: 2rem; padding-top: 1.25rem; border-top: 1px solid var(--border-subtle);">')
    md.append('  <a href="about-this-site.html">&larr; Return to About This Site</a> &bull;')
    md.append('  <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases" target="_blank" rel="noopener">View GitHub Releases History &rarr;</a>')
    md.append("</div>")
    md.append("")

    return "\n".join(md)


def main():
    milestones, total_prompts = parse_journal()
    print(f"Parsed {len(milestones)} milestones and {total_prompts} total steering prompts from JOURNAL.md")
    
    content = generate_prompt_history_markdown(milestones, total_prompts)
    PROMPT_HISTORY_PAGE.write_text(content, encoding="utf-8")
    print(f"Successfully generated {PROMPT_HISTORY_PAGE} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    main()

