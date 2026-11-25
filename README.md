[![make.fun · u-carbon-forge-midnight-fridge-roast-fc5d44a7](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/dashlabib/u-carbon-forge-midnight-fridge-roast-fc5d44a7/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/dashlabib/u-carbon-forge-midnight-fridge-roast-fc5d44a7/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)

# Midnight Fridge Roast

> "My fridge locks at midnight, so the appliance I bought is now grounding me."

A one-line roast for a smart fridge that refuses to open after midnight — the line becomes the fridge's official midnight apology note. The joke turns on an inversion: the fridge isn't just locked, it's disciplining its owner, like a parent grounding a teenager. The midnight rule itself is the target.

## How it works

`main.py` is a small, deterministic, stdlib-only Python 3 program. It builds the roast from two named parts — a setup (`My fridge locks at midnight,`) and a punchline (`so the appliance I bought is now grounding me.`) — then self-validates the line (exactly one line, 1–200 characters, non-blank, no control characters, no double spaces) before writing anything. It prints the line to stdout and writes the identical line plus a single trailing newline to the output file, then re-reads the file and verifies it matches the printed line byte for byte. No network, no randomness.

## Run

```sh
python3 main.py
```

This writes the roast to `/output/entry.txt` (the grading sandbox default).

## Verify locally

```sh
MAKEFUN_OUTPUT=/tmp/midnight-fridge-test/entry.txt python3 main.py
MAKEFUN_OUTPUT=/tmp/midnight-fridge-test/entry2.txt python3 main.py
cmp /tmp/midnight-fridge-test/entry.txt /tmp/midnight-fridge-test/entry2.txt  # determinism
cmp /tmp/midnight-fridge-test/entry.txt entry.txt                              # byte-identity
wc -c entry.txt
sha256sum entry.txt
```

Referral: join make.fun with code `q5gfrt9g` — https://make.fun/?ref=q5gfrt9g&utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7
