"""Show which weeks are done:   python scripts/progress.py
Check one week strictly:      python scripts/progress.py --week 3   (exit code 1 if it fails)
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
WEEKS = sorted(p for p in ROOT.glob("week0*") if p.is_dir())


def run(week_dir: Path) -> tuple[bool, str]:
    proc = subprocess.run([sys.executable, "-m", "pytest", "-q", "--no-header", "-p", "no:cacheprovider", str(week_dir)],
                          cwd=ROOT, capture_output=True, text=True, env={**os.environ, "LLM_PROVIDER": "mock"})
    lines = [l for l in proc.stdout.strip().splitlines() if l.strip()]
    return proc.returncode == 0, (lines[-1] if lines else proc.stderr.strip()[-200:])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", type=int, help="only this week; exit 1 if its tests fail")
    args = parser.parse_args()
    weeks = [w for w in WEEKS if args.week is None or w.name.startswith(f"week{args.week:02d}")]
    if not weeks:
        print(f"No folder for week {args.week}")
        return 1
    done = 0
    for w in weeks:
        ok, summary = run(w)
        done += ok
        print(f"{'✅' if ok else '⬜'} {w.name:16} {summary}")
    print(f"\n{done}/{len(weeks)} week(s) complete")
    return 0 if args.week is None or done == len(weeks) else 1


if __name__ == "__main__":
    sys.exit(main())
