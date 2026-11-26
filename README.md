# Fortune in a Pot

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/gibalers-rgb/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/gibalers-rgb/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)


A tiny program for the make.fun bounty **Fortune in a Pot**: it writes one
kind, funny fortune for a houseplant — a single line of at most 120
characters — to `/output/entry.txt`.

## Run

```sh
python3 main.py
```

The program is deterministic, uses only the Python standard library, and
makes no network access. It reads the `OUTPUT_PATH` environment variable
when set (default `/output/entry.txt`) and validates the fortune before
writing it: non-empty, a single line, no control characters, no stray
whitespace, and at most 120 characters.

## The fortune

> Soon a sunbeam will stop at your pot first, and your keeper will introduce you to a guest by name, not 'the plant'.

## License

MIT — see [LICENSE](LICENSE).
