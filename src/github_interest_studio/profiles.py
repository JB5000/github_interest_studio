from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserProfile:
    interests: str
    level: str
    hours: int


PROFILE_PRESETS: dict[str, UserProfile] = {
    "bioinformatics": UserProfile(
        interests="python,bioinformatics,cli,data",
        level="senior",
        hours=40,
    ),
    "trading": UserProfile(
        interests="python,crypto,automation,data",
        level="mid",
        hours=26,
    ),
    "ai": UserProfile(
        interests="python,ai,evaluation,automation",
        level="mid",
        hours=36,
    ),
    "frontend": UserProfile(
        interests="javascript,frontend,productivity,design",
        level="mid",
        hours=24,
    ),
}
