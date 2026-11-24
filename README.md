# The Funniest Out-of-Office

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/aechoasisvers-a11y/makefun-funniest-out-of-office/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/aechoasisvers-a11y/makefun-funniest-out-of-office/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

A make.fun entry for [The Funniest Out-of-Office](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf): one line of an out-of-office auto-reply, the funniest we can make it.

## Entry

> "I'm out until Monday. I left my inbox in charge and it's already asking for a raise."

84 characters, one line, no trailing newline.

## How it works

`main.py` (pure stdlib Python 3.13) writes the line above to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), with a gate self-check (1–140 characters, not whitespace-only, one line, no leading/trailing whitespace) and a post-write verification that re-reads the file and asserts the bytes on disk exactly match the intended text.

Run it:

```sh
python3 main.py
```
