# One-Line Roast: The Gadget You Use Every Day

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/labibhanafi/roast-gadget-entry-v3/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/labibhanafi/roast-gadget-entry-v3/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

Entry for the [make.fun bounty "One-Line Roast: The Gadget You Use Every Day"](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610) — a program that writes one original roast line to `/output/entry.txt`, written to land on a first read. This is revision v3: a brand-new angle (the charger's one exact cable angle), after v1 (AirPods, rank 154/3031) and v2 (printer, rank 1214/3798).

Join make.fun with my referral link: https://make.fun/r/3t7y0djc

## The entry

> My charger only works at one exact cable angle, like my phone hired a locksmith and charges me rent for the sweet spot.

119 characters. One named daily gadget (the phone charger), one concrete gripe (it only works bent at one exact angle), and a fresh comparison — the phone hiring a locksmith and charging rent for the sweet spot — instead of the usual battery complaint.

## How it works

`main.py` (Python 3, deterministic, no network, no randomness) writes the text above to `/output/entry.txt`, validating the 1–200 character gate first, and prints exactly the entry line to stdout.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
