from github_interest_studio.planner import top_recommendations


def test_top_recommendations_count():
    ranked = top_recommendations(
        interests={"python", "automation"},
        user_level="mid",
        available_hours=24,
        top_n=2,
    )
    assert len(ranked) == 2


def test_rank_order_descending():
    ranked = top_recommendations(
        interests={"python", "data", "api"},
        user_level="mid",
        available_hours=30,
        top_n=4,
    )
    scores = [item.score for item in ranked]
    assert scores == sorted(scores, reverse=True)
