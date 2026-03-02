from __future__ import annotations

import argparse

from github_interest_studio.exporters import write_json_report
from github_interest_studio.planner import top_recommendations
from github_interest_studio.profiles import PROFILE_PRESETS
from github_interest_studio.roadmaps import write_markdown_roadmap


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="github-interest-studio",
        description="Rank GitHub project ideas based on interest, skill, and time.",
    )
    parser.add_argument(
        "--interests",
        default="",
        help="Comma-separated interests/tags (example: python,ai,automation).",
    )
    parser.add_argument(
        "--level",
        choices=("junior", "mid", "senior"),
        default=None,
        help="Current level used to balance challenge.",
    )
    parser.add_argument(
        "--hours",
        type=int,
        default=0,
        help="Approximate hours available for one project cycle.",
    )
    parser.add_argument(
        "--profile",
        choices=tuple(sorted(PROFILE_PRESETS.keys())),
        default="",
        help="Load a preset profile and use flags to override specific values.",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=3,
        help="How many recommendations to return.",
    )
    parser.add_argument(
        "--require-tags",
        default="",
        help="Optional comma-separated tags that every recommendation must include.",
    )
    parser.add_argument(
        "--max-hours",
        type=int,
        default=0,
        help="Optional upper bound for project estimated hours.",
    )
    parser.add_argument(
        "--json-out",
        default="",
        help="Optional path to save recommendations as JSON.",
    )
    parser.add_argument(
        "--roadmap-out",
        default="",
        help="Optional path to save a markdown roadmap.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    interests_raw = args.interests
    level = args.level
    hours = args.hours
    if args.profile:
        profile = PROFILE_PRESETS[args.profile]
        if not interests_raw:
            interests_raw = profile.interests
        if level is None:
            level = profile.level
        if hours <= 0:
            hours = profile.hours
    if not interests_raw:
        interests_raw = "python,data"
    if level is None:
        level = "mid"
    if hours <= 0:
        hours = 24
    interests = {item.strip().lower() for item in interests_raw.split(",") if item.strip()}
    required_tags = {item.strip().lower() for item in args.require_tags.split(",") if item.strip()}
    ranked = top_recommendations(
        interests=interests,
        user_level=level,
        available_hours=max(hours, 1),
        top_n=max(args.top, 1),
        required_tags=required_tags,
        max_hours=args.max_hours if args.max_hours > 0 else None,
    )
    print("Recommended projects:")
    for index, rec in enumerate(ranked, start=1):
        tags = ", ".join(rec.project.tags)
        print(f"{index}. {rec.project.title} [{rec.score}]")
        print(f"   - difficulty: {rec.project.difficulty}")
        print(f"   - est. hours: {rec.project.estimated_hours}")
        print(f"   - tags: {tags}")
        print(f"   - summary: {rec.project.summary}")
    if args.json_out:
        output_path = write_json_report(args.json_out, ranked)
        print(f"\nJSON report written to: {output_path}")
    if args.roadmap_out:
        roadmap_path = write_markdown_roadmap(args.roadmap_out, ranked)
        print(f"Roadmap written to: {roadmap_path}")


if __name__ == "__main__":
    main()
