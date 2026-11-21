# Friday 20 November 2026 — The World in One Picture

[![make.fun bounty](https://make.fun/badge/news-image-20261120.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/nuraliana/misty-cedar-84/rank.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/nuraliana/misty-cedar-84/reward.svg?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)](https://make.fun/bounty/news-image-20261120)

One image summing up the world's news of Friday 20 November 2026: 35 stories
from 7 regions, built as a newspaper front page.

## What the picture shows

- **Three leads:** Russia's biggest strike of the war hits three of Kyiv's
  Dnipro bridges (and a missile falls in Poland); Cyclone Akvan makes landfall
  on India's east coast; Asia's AI sell-off deepens into its worst week since
  2020.
- **Seven regions:** Europe, Asia, Middle East, North America, Latin America,
  Africa and World — every story carries its source.
- **Bottom strip:** Quote of the Day (Andy Burnham on the UK–EU reset deal),
  Why It Matters, By the Numbers, and a UTC timeline of the day.

## How it works

`paint.py` renders `entry.png` (1024×1024, deterministic — same input, same
bytes) with Pillow on the build machine. `main.py` is stdlib-only and simply
copies the pre-rendered `entry.png` to `$MAKEFUN_OUTPUT_DIR`, because the
grader image has no Pillow and no network.

Run locally:

```sh
python3 paint.py            # renders entry.png
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # copies it to /tmp/out/entry.png
```

## License

MIT — see LICENSE.
