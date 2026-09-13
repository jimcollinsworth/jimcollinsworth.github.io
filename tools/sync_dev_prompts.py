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

        total_prompt_count += len(prompts)

        # Extract Problem & Diagnosis
        problem_match = re.search(r"### Problem & Diagnosis\s*\n(.*?)(?=\n###|\n---|\Z)", sec, re.DOTALL)
        problem_text = problem_match.group(1).strip() if problem_match else ""

        # Extract Solution & Standard Procedure
        solution_match = re.search(r"### Solution & Standard Procedure\s*\n(.*?)(?=\n###|\n---|\Z)", sec, re.DOTALL)
        solution_text = solution_match.group(1).strip() if solution_match else ""

        # Extract Root Cause & Technical Analysis
        root_cause_match = re.search(r"### Root Cause & Technical Analysis\s*\n(.*?)(?=\n###|\n---|\Z)", sec, re.DOTALL)
        root_cause_text = root_cause_match.group(1).strip() if root_cause_match else ""

        if prompts or problem_text:
            milestones.append({
                "date": date_str,
                "title": title_str,
                "prompts": prompts,
                "problem": problem_text,
                "root_cause": root_cause_text,
                "solution": solution_text,
            })

    return milestones, total_prompt_count


import html

def sanitize_html_content(text: str) -> str:
    """Format markdown bold and code for safe rendering inside raw HTML tags."""
    # Convert bold **text** to <strong>text</strong>
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # Convert backtick code `code` to <code>escaped</code>
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{html.escape(m.group(1))}</code>", text)
    # Escape any stray angle brackets that look like HTML tags
    text = re.sub(r"<(?!/?(?:strong|em|code|span|a\b))([^>]+)>", r"&lt;\1&gt;", text)
    return text


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
    md.append(f"    <strong>Development Prompts</strong> is an unadorned, chronological chronicle of human-directed pair programming for <code>jimcollinsworth.github.io</code>. Extracted directly from <code>JOURNAL.md</code> via <code>tools/sync_dev_prompts.py</code>, it captures <strong>{total_prompts} direct steering prompts</strong> across {len(milestones)} releases and milestones. Prompts are presented in Jim's simple, verbatim words, paired with concise release summaries and notes on what the agent did wrong and how it was corrected.")
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

        # Jim's Prompts
        if m["prompts"]:
            md.append("**Jim's Direct Prompts:**")
            md.append("")
            for p in m["prompts"]:
                escaped_p = html.escape(p)
                md.append(f'> *"{escaped_p}"*')
                md.append("")

        # Factual Summary & Remediation
        if m["problem"] or m["solution"]:
            md.append("**Course Corrections & Technical Remediation:**")
            md.append("")
            prob_lines = [l.strip() for l in m["problem"].split("\n") if l.strip()]
            for line in prob_lines:
                cleaned_line = re.sub(r"^\d+\.\s*", "", line)
                if cleaned_line.startswith("- "):
                    cleaned_line = cleaned_line[2:]
                sanitized_line = sanitize_html_content(cleaned_line)
                md.append(f"- {sanitized_line}")
            md.append("")

        md.append("---")
        md.append("")

    md.append('<div style="margin-top: 1.5rem;">')
    md.append('  <a href="about-this-site.html">&larr; Return to About This Site</a> &bull;')
    md.append('  <a href="https://github.com/jimcollinsworth/jimcollinsworth.github.io/releases" target="_blank" rel="noopener">View GitHub Releases History &rarr;</a>')
    md.append("</div>")
    md.append("")

    return "\n".join(md)

    md.append("</div>")
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
