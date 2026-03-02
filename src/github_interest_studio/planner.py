from __future__ import annotations

from dataclasses import dataclass

from github_interest_studio.catalog import PROJECT_TEMPLATES, ProjectTemplate
from github_interest_studio.scoring import score_project


@dataclass(frozen=True, slots=True)
class Recommendation:
    project: ProjectTemplate
    score: float


def rank_projects(
    interests: set[str],
    user_level: str,
    available_hours: int,
    required_tags: set[str] | None = None,
    max_hours: int | None = None,
) -> list[Recommendation]:
    required_tags = required_tags or set()
    scored = [
        Recommendation(
            project=project,
            score=score_project(
                project=project,
                interests=interests,
                user_level=user_level,
                available_hours=available_hours,
            ),
        )
        for project in PROJECT_TEMPLATES
        if required_tags.issubset(set(project.tags))
        if max_hours is None or project.estimated_hours <= max_hours
    ]
    return sorted(scored, key=lambda item: item.score, reverse=True)


def top_recommendations(
    interests: set[str],
    user_level: str,
    available_hours: int,
    top_n: int = 3,
    required_tags: set[str] | None = None,
    max_hours: int | None = None,
) -> list[Recommendation]:
    return rank_projects(
        interests=interests,
        user_level=user_level,
        available_hours=available_hours,
        required_tags=required_tags,
        max_hours=max_hours,
    )[: max(top_n, 1)]
