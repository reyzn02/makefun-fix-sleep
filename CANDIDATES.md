# Candidate lines — self-judge vs the judge brief

Judge order: (1) real patch note about fixing human sleep, (2) joke lands on
one read, (3) genuine changelog voice, (4) single line <160 chars,
(5) specific + surprising, not a flat "sleep is fixed".

| # | Line (chars) | Verdict |
|---|--------------|---------|
| 1 | Fixed a bug where humans woke up at 3 a.m. to replay every embarrassing thing they said in 2009. (96) | Strong. Relatable 3 a.m. replay, real changelog voice. But "woke up ... to replay" is a plain description; the joke has no twist beyond the image. |
| 2 | Sleep now saves correctly; previously, closing your eyes only paused the day. (76) | Charming save-game metaphor, terse voice. Joke is gentler and less specific — no concrete image, weaker on (5). |
| 3 | Fixed a bug where the brain opened a 3 a.m. support ticket titled 'remember that embarrassing thing from 2009?' (113) | Funny premise, but "titled ..." is wordy and half-explains the joke; loses to (1) on voice (3). |
| 4 | Fixed a bug where sleep would crash at 3 a.m. and reboot with every embarrassing memory from 2009 restored. (109) | Vivid crash/reboot image, strong voice. Close second — but "reboot with memories restored" takes a beat longer to parse than the winner. |
| 5 | Fixed a bug where humans dreamed in 240p; sleep now renders in full HD. (71) | Snappy, but dream quality is only loosely "fixing sleep" — weaker on (1) than the 3 a.m. lines. |
| 6 | Fixed an issue where sleep required 45 minutes of staring at the ceiling while the brain defragmented. (105) | Good defrag metaphor, but "staring at the ceiling" is a weaker, more generic image than the 2009 replay. |
| 7 | **WINNER** — Fixed a bug where the brain treated 3 a.m. as the ideal time to replay every embarrassing thing from 2009. (106) | Wins head-to-head: same relatable 3 a.m./2009 image as (1) and (4), but "treated ... as the ideal time" adds a deadpan twist — the bug is framed as the brain's *deliberate scheduling choice*, which is more surprising (5) and more changelog-dry (3) than a plain description, and it lands in one read (2). |

Winner (106 chars, 1 line) is the entry. v1 shipped candidate 1; v2 revises to candidate 7.

## Raised bar — candidates 8–12 + tournament (26 Nov, after repo created)

| # | Line (chars) | Verdict |
|---|--------------|---------|
| 8 | Fixed a bug where the human body treated 2 a.m. as the perfect time to remember every awkward thing ever said. (110) | Same frame as (7) but vaguer payoff ("every awkward thing ever said" vs dated "from 2009"). Loses to (7). |
| 9 | Sleep no longer crashes at 3 a.m. and reboots into a highlight reel of your most embarrassing moments. (102) | "Highlight reel" is a good image, but "crashes ... and reboots into" is clunkier than (7)'s deadpan. Loses to (7), narrowly. |
| 10 | Fixed a bug where the brain scheduled its weekly review of your worst moments for 3 a.m. every night. (101) | Clever corporate-retro joke, but more abstract than the visceral 2009 replay. Loses to (7). |
| 11 | Humans can now fall asleep without the brain running a full retrospective of every embarrassing thing since 2009. (113) | Decent, but "Humans can now..." is a weaker changelog opening than "Fixed a bug where...". Loses to (7) on voice (3). |
| 12 | **NEW WINNER** — Fixed a bug where closing your eyes opened a 45-minute loading screen titled 'Things You Said in 2009'. (103) | Beats (7) head-to-head: criteria (1), (3), (4) tied; on (2) the loading-screen title is a laugh-line, not just a smile; on (5) it packs two concrete images (45-minute loading screen + the titled 2009 reel) where (7) has one. Still unmistakably a sleep fix — closing your eyes *is* trying to sleep, and the loading screen *is* the insomnia delay. |

Tournament: (7) beat (8), (9), (10), (11); (12) beat (7) in the final. Winner: candidate 12, 103 chars, 1 line.

## Compete standard — fresh round (candidates 13–17) + tournament + beat-the-top

Fresh round, aiming to beat the v3 champion (12):

| # | Line (chars) | Verdict |
|---|--------------|---------|
| 13 | Fixed a bug where the brain's 'Do Not Disturb' mode only silenced sleep. (69) | Neat inversion, one-note, no concrete image. Loses on (5). |
| 14 | Fixed a bug where the brain treated bedtime as a group meeting to review every embarrassing thing from 2009. (109) | Good corporate frame, but "review every embarrassing thing" is the same 2009 joke with a weaker image than tabs. Loses to (16). |
| 15 | Fixed a bug where the dream server went down nightly at 3 a.m. and served a rerun of your most embarrassing moment instead. (118) | Good "dream server" premise, but "served a rerun" is wordier and slower than the tabs line. Loses to (16). |
| 16 | **NEW CHAMPION** — Fixed a bug where closing your eyes opened 47 browser tabs, all titled 'Things You Said in 2009'. (97) | Beats (12): same 2009 punch, but 47 titled tabs is more chaotic and vivid than a loading screen — wins on (5) specificity/surprise and on (2) the joke. Beats (17) on (1): it is anchored in the sleep act itself (closing your eyes), where the screensaver is only brain-adjacent. |
| 17 | Fixed a bug where the brain's screensaver was just you, age 14, saying something stupid in 2009. (99) | Close second. "Age 14, saying something stupid" is a huge laugh — arguably wins (2) by a hair — but loses to (16) on (1), which the brief weighs first: a screensaver is the brain idling, not sleep being fixed. |

Tournament: (16) beat (12) in the final, (17) the runner-up. Total candidates: 17 serious (12 + 5 fresh).

## Beat-the-top check (board-analysis.json, checked 2026-11-25T17:32Z)

Bar: Turning It Off top neighbors 66–69% win rate; Robot Romance neighbors ~57.2%.

- vs Turning It Off 68.1% — "I can hear your smoke alarm, ma'am — let's start simple: have you tried turning the router off and on again? The router. Not the house.": on pure joke it is a coin-flip (dialogue + escalation punchline vs deadpan image + count), but as a *patch note* (criterion 3, which our judge weighs) the champion is in-genre and tighter, and it clearly beats the rest of the band — "Turn the house off and on again" (59.7%), "Rebooted Myself Instead" (66.2%), "The hold music is doing its job" (67.5%). **Plausibly beats the band.**
- vs Robot Romance ~57.2% — "Are you a token? Because I would burn my whole context window just to keep talking to you." and the CAPTCHA pickup lines: one-note puns, no concrete scene, no surprise beyond the premise. The champion is more specific, more vivid, and more surprising. **Plausibly beats them.**
- vs the Cooking Game lesson (winner 89.5% = a deep specific world whose title enumerated the depth): at line scale the champion does the same thing — it is a specific world (47 titled tabs) with a count, not a generic claim. No generic line was submitted.

**Verdict: PASS — champion plausibly beats the top-neighbor bar. Proceed to submit pass.**
