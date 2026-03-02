from __future__ import annotations

import json
from pathlib import Path

from github_interest_studio.planner import Recommendation


def recommendation_to_dict(item: Recommendation) -> dict[str, object]:
    return {
        "slug": item.project.slug,
        "title": item.project.title,
        "score": item.score,
        "difficulty": item.project.difficulty,
        "estimated_hours": item.project.estimated_hours,
        "tags": list(item.project.tags),
        "summary": item.project.summary,
    }


def write_json_report(path: str | Path, recommendations: list[Recommendation]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = [recommendation_to_dict(item) for item in recommendations]
    target.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return target
