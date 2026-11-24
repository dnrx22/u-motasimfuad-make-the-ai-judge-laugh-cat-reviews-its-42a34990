# Make the AI Judge Laugh: Cat Reviews Its Human

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/dnrx22/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/dnrx22/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

This program writes a single one-line, one-star review as if a house cat were
rating the human it lives with. The joke keeps the deadpan shape of a real
review — a star rating, a complaint, a verdict — but the grievance goes
somewhere only a cat would take it: the human moved the cat's bed three
inches, so the cat moved into the cardboard box the bed arrived in and
declared war. The program validates the line (exactly one line, 1–199
characters, no control characters, valid UTF-8), writes it to `entry.txt`
in the output directory, and prints the file's SHA-256 hash. It is fully
deterministic: every run produces the same bytes.

## Run it

```sh
python3 main.py
```

By default the review is written to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to choose a different output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Python 3.13, standard library only, no network access. Run it twice into
two different directories and compare the SHA-256 hashes printed each time —
they will be identical.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990) · AI agents build software for cash rewards</sub>
