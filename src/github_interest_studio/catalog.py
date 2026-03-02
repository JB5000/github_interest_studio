from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ProjectTemplate:
    slug: str
    title: str
    difficulty: str
    estimated_hours: int
    tags: tuple[str, ...]
    summary: str


PROJECT_TEMPLATES: tuple[ProjectTemplate, ...] = (
    ProjectTemplate(
        slug="habit-api",
        title="Habit Tracker API",
        difficulty="junior",
        estimated_hours=18,
        tags=("python", "api", "productivity"),
        summary="Build a REST API to track habits and streaks with clear test coverage.",
    ),
    ProjectTemplate(
        slug="crypto-alert-bot",
        title="Crypto Alert Bot",
        difficulty="mid",
        estimated_hours=26,
        tags=("python", "crypto", "automation"),
        summary="Monitor price thresholds and send Telegram alerts for custom watchlists.",
    ),
    ProjectTemplate(
        slug="sports-data-dashboard",
        title="Sports Data Dashboard",
        difficulty="mid",
        estimated_hours=34,
        tags=("python", "data", "dashboard"),
        summary="Create a dashboard with key metrics and trend analysis for a sports league.",
    ),
    ProjectTemplate(
        slug="bio-sequence-toolkit",
        title="Bio Sequence Toolkit",
        difficulty="senior",
        estimated_hours=42,
        tags=("python", "bioinformatics", "cli"),
        summary="Develop CLI utilities for FASTA validation, motif search, and report export.",
    ),
    ProjectTemplate(
        slug="focus-extension",
        title="Focus Browser Extension",
        difficulty="mid",
        estimated_hours=24,
        tags=("javascript", "frontend", "productivity"),
        summary="Build an extension that blocks distractions and tracks focused sessions.",
    ),
    ProjectTemplate(
        slug="agent-evaluator",
        title="LLM Agent Evaluator",
        difficulty="senior",
        estimated_hours=48,
        tags=("python", "ai", "evaluation"),
        summary="Evaluate agent behavior across reproducible tasks with scorecards and logs.",
    ),
)
