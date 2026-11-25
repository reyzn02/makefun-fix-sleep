#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

v2: self-judged winner of 7 candidates (see CANDIDATES.md). The v1 line
("humans woke up at 3 a.m. to replay...") was solid but flat; the v2 line
keeps the same joke and adds a deadpan twist -- the brain *treated* 3 a.m.
as "the ideal time", which is both more specific and more changelog-dry.

v3 (raised bar: 12 candidates, tournament self-judge): the winner is a
new line -- a 45-minute loading screen titled 'Things You Said in 2009'.
It beat the v2 line head-to-head on the joke landing (criterion 2) and on
surprise/specificity (criterion 5): two concrete images instead of one,
same deadpan changelog voice, still unmistakably a sleep fix.

v4 (compete standard: beat-the-top vs live board): fresh round of 5 more
candidates, tournament re-run. Champion: 47 browser tabs, all titled
'Things You Said in 2009'. It beat the v3 line on specificity (criterion
5 -- the count 47 plus the titled tabs is a more chaotic, more vivid image
than a loading screen) and beat the v2 screensaver-style runner-up on
criterion 1 (it is anchored in the sleep act itself: closing your eyes).
Beat-the-top check vs live top neighbors (board-analysis.json): plausibly
beats the Turning It Off 66-68% band and the Robot Romance ~57% band --
see CANDIDATES.md for the head-to-head evidence.

Writes one line of patch notes announcing that human sleep has been
fixed, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Gate: exactly one line, 1-160 characters, not only whitespace.
"""

import os
import sys

ENTRY = "Fixed a bug where closing your eyes opened 47 browser tabs, all titled 'Things You Said in 2009'."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    line = ENTRY.strip()
    if not line or "\n" in line or len(line) > 160:
        print("gate failed: entry must be one line of 1-160 chars", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
