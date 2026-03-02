# GitHub Interest Studio

`github_interest_studio` is a small CLI that helps you choose portfolio project ideas based on your interests, available time, and current skill level.

## Why it helps

- Turns vague interests into ranked, practical project ideas.
- Balances ambition vs feasibility using skill + time-fit scoring.
- Exports results to JSON and a markdown roadmap ready to commit.

## Quickstart

```bash
cd github_interest_studio
python3 -m pip install -e ".[dev]"
github-interest-studio --interests python,ai,automation --level mid --hours 30 --top 3
```

## Preset profiles

Use a preset and override just what you need:

```bash
github-interest-studio --profile bioinformatics --top 4 --max-hours 40
github-interest-studio --profile ai --require-tags python,ai
```

## Output files

```bash
github-interest-studio \
  --profile trading \
  --json-out outputs/recommendations.json \
  --roadmap-out outputs/roadmap.md
```

## Test suite

```bash
cd github_interest_studio
pytest -q
```
