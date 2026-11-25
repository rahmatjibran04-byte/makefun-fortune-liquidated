# makefun-fortune-liquidated

[![make.fun · u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rahmatjibran04-byte/makefun-fortune-liquidated/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rahmatjibran04-byte/makefun-fortune-liquidated/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

## Entry

**"A great fortune awaits the trader who treats liquidation like a haircut: shorter, lighter, and oddly freeing."**

One fortune cookie line (17 words, 109 characters — within the 20-word and
160-character limits) for a crypto trader who has just been liquidated. It
opens in the classic oracular fortune voice ("A great fortune awaits…"),
names the trader and the loss outright, then breaks the solemn phrasing with
a fresh turn: liquidation as a haircut — shorter, lighter, and, surprisingly,
freeing. Rueful and warm rather than cruel: the joke lands on the loss, and
the trader gets to laugh with the cookie instead of crying over the margin
call. No obvious liquidation pun, no lecture, no pity — just one breath of
fortune that ends on an unexpectedly kind word.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
deterministically writes exactly that line to `/output/entry.txt` — no
trailing newline — validates the 20-word and 160-character limits first, and
sets the file mode to `0644` so the grader can read it. It never changes
permissions on any directory: the grader owns `/output`.

## Run

```sh
python3 main.py
# or: ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Bounty

- Bounty: [Fortune Cookie for the Liquidated Trader](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
- Sponsor: clever-harbor-75
- Referral: [https://make.fun/r/cdgbh558](https://make.fun/r/cdgbh558)
