import argparse
import os
from pathlib import Path

from dotenv import dotenv_values

from .parser import load_folder, timestamp
from .pipeline import run_pipeline
from .provider import OpenAIProvider
from .reporting import export_report
from .storage import write_json

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = ROOT / "I Married a Broken Soldier. He was a Duke"


def load_environment() -> None:
    # A blank template value must not prevent discovering a key added while the app is open.
    values = dotenv_values(ROOT / ".env")
    for name in ("OPENAI_API_KEY", "SELECTOR_MODEL", "JUDGE_MODEL"):
        if not os.getenv(name) and values.get(name):
            os.environ[name] = values[name]


def main() -> int:
    load_environment()
    parser = argparse.ArgumentParser(description="Find and review promos using ONE episode per candidate")
    sub = parser.add_subparsers(dest="command", required=True)
    parse = sub.add_parser("parse", help="Validate and inventory scripts without an API key")
    parse.add_argument("input", type=Path, nargs="?", default=DEFAULT_INPUT)
    parse.add_argument("--output", type=Path, default=Path("runs/inventory"))
    run = sub.add_parser("run", help="Run Luna selection and independent Sol judging")
    run.add_argument("input", type=Path, nargs="?", default=DEFAULT_INPUT)
    run.add_argument("--output", type=Path, default=Path("runs/pilot"))
    run.add_argument("--episodes", help="Comma-separated episode numbers; omit to process all episodes")
    run.add_argument("--selector-model", default=os.getenv("SELECTOR_MODEL", "gpt-6-luna"))
    run.add_argument("--judge-model", default=os.getenv("JUDGE_MODEL", "gpt-6.1-sol"))
    run.add_argument("--candidates", type=int, default=3)
    run.add_argument("--workers", type=int, default=2)
    run.add_argument("--rubric", type=Path, default=ROOT / "criteria.md")
    report = sub.add_parser("report", help="Rebuild exports from saved results without model calls")
    report.add_argument("run", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "parse":
            episodes, errors = load_folder(args.input)
            write_json(args.output / "inventory.json", {"episodes": [e.model_dump() for e in episodes], "errors": errors})
            for episode in episodes:
                print(f"{episode.id}: {timestamp(episode.duration_cs)}, {len(episode.events)} events, {len(episode.warnings)} warnings")
            print(f"Parsed {len(episodes)} episodes; {len(errors)} failures. Output: {args.output}")
            for error in errors:
                print(f"PARSE ERROR: {error['file']}: {error['error']}")
            return 1 if errors else 0
        if args.command == "run":
            provider = OpenAIProvider(args.output / "raw", os.getenv("OPENAI_API_KEY", ""))
            numbers = {int(n.strip()) for n in args.episodes.split(",")} if args.episodes else None
            summary = run_pipeline(folder=args.input, output=args.output, provider=provider,
                                   rubric=args.rubric.read_text(encoding="utf-8"),
                                   selector_model=args.selector_model, judge_model=args.judge_model,
                                   episode_numbers=numbers, max_candidates=args.candidates, workers=args.workers)
            print(f"Usage: {summary['usage']}")
            exported = export_report(args.output)
            failed = any(r["status"] in ("api_failed", "partial_failure", "processing_failed") for r in exported["coverage"])
            print(f"Exports saved in {args.output / 'exports'}")
            return 1 if summary["parse_errors"] or failed else 0
        export_report(args.run)
        print(f"Exports saved in {args.run / 'exports'}")
        return 0
    except (ValueError, OSError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
