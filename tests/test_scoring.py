from github_interest_studio.catalog import PROJECT_TEMPLATES
from github_interest_studio.scoring import score_project


def _find(slug: str):
    return next(item for item in PROJECT_TEMPLATES if item.slug == slug)


def test_interest_overlap_improves_score():
    target = _find("agent-evaluator")
    low = score_project(target, interests={"frontend"}, user_level="mid", available_hours=60)
    high = score_project(target, interests={"ai", "evaluation", "python"}, user_level="mid", available_hours=60)
    assert high > low


def test_large_time_mismatch_reduces_score():
    target = _find("bio-sequence-toolkit")
    low_time = score_project(target, interests={"bioinformatics"}, user_level="senior", available_hours=8)
    full_time = score_project(target, interests={"bioinformatics"}, user_level="senior", available_hours=50)
    assert full_time > low_time
