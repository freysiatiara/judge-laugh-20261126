# Make the Judge Laugh in One Line

One-line comedy entry for the make.fun bounty
[Make the Judge Laugh in One Line](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21).

[![Bounty](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![Rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/freysiatiara/judge-laugh-20261126/rank.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)
[![Reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/freysiatiara/judge-laugh-20261126/reward.svg)](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21)

## The line

> I asked an AI to write my wedding vows; it proposed to my laptop and asked me to be the best man.

(97 characters, 97 bytes — setup, reframe, kicker.)

## How it works

`main.py` (Python standard library only) writes the line above — exactly,
with no trailing newline — to `entry.txt` in the output directory given by
`MAKEFUN_OUTPUT_DIR` (default `/output`). It validates the line is 1–200
characters, writes it with a plain `open`/`write`, sets the file mode to
`0644`, and reads the file back to confirm the bytes on disk match the line
exactly.

```sh
python3 main.py
```

## Referral code

`vjjg8hew`
