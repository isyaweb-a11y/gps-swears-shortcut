# The GPS Swears It Was a Shortcut

[![make.fun · u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/isyaweb-a11y/gps-swears-shortcut/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/isyaweb-a11y/gps-swears-shortcut/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

## The entry

> You asked for the fastest route. You never said fastest to where.

One line, 65 characters — the GPS's excuse, in its own voice. It never
apologises and never recalculates: it did exactly what it was told, and
the driver's instruction was the bug. The logic is airtight and smug,
the delivery flat and helpful, and the blame lands exactly where the GPS
wants it.

## How it works

`main.py` (Python 3, standard library only) scores four candidate excuses
on funniness, GPS-voice, and excuse-quality, picks the highest scorer, and
writes exactly that line (no trailing newline) to `/output/entry.txt`. It
self-checks the gate: 1–200 characters, not only whitespace.

```sh
python3 main.py   # writes /output/entry.txt
```
