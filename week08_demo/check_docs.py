"""Week 8: is your project ready for demo day?

Fill in docs/PROJECT.md (replace every TODO), then run:  pytest week08_demo
"""
import re
from pathlib import Path

PROJECT_MD = Path(__file__).parents[1] / "docs" / "PROJECT.md"

REQUIRED_SECTIONS = ["Problem", "Architecture", "Setup", "Evaluation", "Security", "Demo", "What I would do next"]


def missing_sections(text: str) -> list[str]:
    """Sections (## headings) from REQUIRED_SECTIONS that are not in the text."""
    found = {h.strip().lower() for h in re.findall(r"^##\s+(.+)$", text, re.M)}
    return [s for s in REQUIRED_SECTIONS if s.lower() not in found]


def problems(text: str) -> list[str]:
    issues = [f"missing section: {s}" for s in missing_sections(text)]
    if "TODO" in text:
        issues.append(f"{text.count('TODO')} TODO placeholder(s) left")
    if not re.search(r"https://\S+", text.split("## Demo", 1)[-1]):
        issues.append("no live app / demo video link in the Demo section")
    if len(text.split()) < 400:
        issues.append(f"only {len(text.split())} words; aim for 400+")
    return issues


if __name__ == "__main__":
    found = problems(PROJECT_MD.read_text(encoding="utf-8"))
    print("\n".join(found) or "Ready for demo day!")
