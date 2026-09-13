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


def generate_prompt_history_markdown(milestones: list[dict], total_prompts: int) -> str:
    """Generate clean, plaintext prompt timeline without over-produced styling."""
    md = []
    md.append("---")
    md.append('title: "Development Prompts & Instruction Timeline"')
    md.append('slug: "prompt-history"')
    md.append("---")
    md.append("")
    md.append('<div class="page-intro">')
    md.append("  <p>")
    md.append(f"    <strong>Development Prompts</strong> lists steering prompts and technical corrections for <code>jimcollinsworth.github.io</code>, extracted from <code>JOURNAL.md</code> via <code>tools/sync_dev_prompts.py</code>. It contains <strong>{total_prompts} prompts</strong> from Jim across {len(milestones)} milestones, alongside concise summaries of actions taken.")
    md.append("  </p>")
    md.append("</div>")
    md.append("")

    for m in milestones:
        title = m['title']
        date_str = m['date']
        md.append(f"## {title}")
        if date_str:
            md.append(f"*{date_str}*")
        md.append("")

        # Jim's Prompts: simple full-width text, start/primary part, no blockquotes, no italics, no quotes
        for p in m["prompts"]:
            md.append(p.strip())
            md.append("")

        # LLM Response: concise, balanced length, no nested tags
        if m["actions"]:
            md.append("**Response:**")
            md.append("")
            for a in m["actions"]:
                md.append(f"- {a}")
            md.append("")

        md.append("---")
        md.append("")

    md.append('<div style="margin-top: 1.5rem;">')
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

