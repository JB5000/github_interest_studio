from __future__ import annotations

from github_interest_studio.catalog import ProjectTemplate


DIFFICULTY_ORDER = {"junior": 1, "mid": 2, "senior": 3}


def _difficulty_score(user_level: str, project_level: str) -> float:
    user_rank = DIFFICULTY_ORDER.get(user_level, 2)
    project_rank = DIFFICULTY_ORDER.get(project_level, 2)
    delta = abs(user_rank - project_rank)
    return max(0.0, 1.0 - (0.35 * delta))


def _time_fit_score(available_hours: int, estimated_hours: int) -> float:
    if estimated_hours <= available_hours:
        return 1.0
    overflow = estimated_hours - available_hours
    penalty = min(0.8, overflow / max(available_hours, 1))
    return max(0.2, 1.0 - penalty)


def _interest_score(interests: set[str], tags: tuple[str, ...]) -> float:
    if not interests:
        return 0.4
    overlap = len(interests.intersection(tags))
    return min(1.0, 0.3 + overlap * 0.35)


def score_project(
    project: ProjectTemplate,
    interests: set[str],
    user_level: str,
    available_hours: int,
) -> float:
    interest = _interest_score(interests, project.tags)
    difficulty = _difficulty_score(user_level, project.difficulty)
    time_fit = _time_fit_score(available_hours, project.estimated_hours)
    score = (interest * 0.5) + (difficulty * 0.3) + (time_fit * 0.2)
    return round(score, 4)
