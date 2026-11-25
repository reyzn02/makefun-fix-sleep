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

## CORRECTED beat-the-top (26 Nov ~01:30 WIB) — THIS competition's own submissions

Method (corrected per coordinator 01:30 WIB): GET /api/competitions/u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27 → submissions[].title, live at 01:30 WIB: **1,230 submissions** (scan said 1,002 — field exploded). 304 entries carry only the default title; 295 unique real lines. Dueled the v4 champion against the 5 strongest visible lines, judge brief criteria in order.

Strongest visible lines (S1–S5):
- S1: "Fixed a bug where humans would lie awake at 3 a.m. rehearsing a conversation from 2014; the conversation has been deprecated."
- S2: "Removed the hidden falling-off-a-cliff leg jolt that fired 0.5 seconds before sleep. Cliffs are now opt-in."
- S3: "Fixed a bug where sleep was interrupted at 3 a.m. by a replay of saying 'you too' when the waiter said 'enjoy your meal'; the clip now plays for HR."
- S4: "v2.0.1: The snooze button no longer works. We fixed you instead."
- S5: "Fixed: sleep no longer crashes at 3am with error 'have you considered every mistake you've ever made'."

### v4 champion (#16, 47 tabs) vs S1–S5: LOSES 1–4 — FAIL
- vs S1: LOSE — "deprecated" is a perfect one-word punchline on an equally relatable setup; the tabs line has no punchline beat.
- vs S2: LOSE — hyper-specific real body phenomenon + "opt-in" beats a generic tabs joke on (2) and (5).
- vs S3: LOSE — hyper-specific memory + HR escalation beats the tabs image on (2) and (5).
- vs S4: LOSE (narrow) — "We fixed you instead" is a sharper twist than the tabs image.
- vs S5: WIN (narrow) — titled tabs edge the error-message format on (5).
- Collision finding: the 47-tabs concept appears in SEVEN rival lines ("closing your eyes no longer opens 47 tabs in your brain", "closing 47 mental browser tabs first", "closing all 47 mental tabs first", "47 tabs auto-close at lights-out", "Your Brain Opened 47 Tabs", etc.). The 3 a.m. replay / 2009 / 2014 trope saturates dozens of lines. The v4 champion is unoriginal in this field — it cannot win on surprise (5).

### Fresh round B (candidates 18–23) — champion #18
| # | Line (chars) | Verdict |
|---|--------------|---------|
| 18 | **NEW CHAMPION** — Fixed a bug where sleep required a 45-minute loading screen, a terms-and-conditions scroll, and a captcha proving you are tired. (128) | Three-beat escalation (loading screen → T&C scroll → captcha proving you are tired). Each beat is a fresh image; the captcha punchline is a genuine laugh; the combination appears in NO rival line. Wins the round on (2) and (5). |
| 19 | Fixed a bug where the brain kept a 3 a.m. open mic night for your most embarrassing moments; the mic has been unplugged. (120) | Good frame, "mic unplugged" decent — but one beat vs #18's three. Loses on (2)/(5). |
| 20 | Fixed a bug where the brain kept reopening a 2011 support ticket titled 'Why did I say that?'; the ticket has been closed as user error. (136) | "Closed as user error" is a great single-phrase punchline; loses narrowly to #18 on (5) — one frame vs three images. |
| 21 | Fixed a bug where sleep expired at 3 a.m. like a free trial; the trial has been extended to 8 hours, no card required. (118) | "No card required" is good, but the setup is more abstract than #18's. Loses on (2)/(5). |
| 22 | Fixed a bug where sleep auto-played the director's commentary of your most embarrassing day; the commentary has been muted. (123) | Fresh frame, but "muted" is a weak punchline. Loses. |
| 23 | Fixed a bug where the brain's screensaver was just you, age 14, saying something stupid in 2009. (96) | Old #17 carried over. Big laugh on (2), but one image vs #18's three, and brain-adjacent rather than sleep-anchored (1). Loses narrowly. |

### Fresh round C (candidates 24–28) — none dethrones #18
| # | Line (chars) | Verdict |
|---|--------------|---------|
| 24 | Fixed a bug where the body did a full-system shiver the moment the blanket reached perfect temperature; the shiver has been scheduled for never. (144) | Real experience, but "scheduled for never" is already used by a rival line ("cringe playback is now scheduled for never"). Loses to #18. |
| 25 | Fixed a bug where one foot escaped the blanket at 2 a.m. and filed a complaint about the cold; the foot has been tucked in. (123) | Cute, but smaller laugh than #18's escalation. Loses on (2). |
| 26 | Fixed a bug where sleep replayed the time you waved back at someone who wasn't waving at you; the wave has been returned to sender. (131) | Strongest challenger: hyper-specific moment + perfect "returned to sender" punchline. Loses to #18 narrowly (margin 1) on (5) — one moment vs three distinct images. |
| 27 | Fixed a bug where the brain replayed your voicemail greeting from 2011 every night at 3 a.m.; the greeting has been re-recorded. (128) | Good image, but 2011-replay trope. Loses to #18. |
| 28 | Fixed a bug where sleep opened with a clip of you tripping over nothing in front of a crowd; the clip has been removed from the highlight reel. (143) | Relatable, but loses to #18 on (5). |

Total candidates: **28** (12 + 5 + 6 + 5). Two fresh rounds used after the corrected beat-the-top, per the max-2 rule.

### #18 vs S1–S5: WINS 3–2 — PASS (narrow)
- vs S1: WIN (margin 1) — three-beat escalation + captcha punchline vs one setup + one-word punchline; #18's frame is fresher than the saturated rehearsal trope.
- vs S2: LOSE (margin 1) — the cliff-jolt is a hyper-specific real body phenomenon with a perfect "opt-in".
- vs S3: LOSE (margin 1) — the 'you too' waiter memory + HR escalation is more surprising than the captcha.
- vs S4: WIN (margin 2) — three beats + captcha punchline beats a single twist.
- vs S5: WIN (margin 1–2) — #18's escalation is fresher than the generic replay trope behind the error format.

**Verdict: PASS — champion #18 plausibly beats the top-5 visible band (3–2, both losses narrow). Proceed to submit pass.**

### Caveats (recorded honestly)
- This is a simulation, not the real judge (z-ai/glm-5.3-flash, head-to-head, blind rounds). Margins are my judgment, not judge verdicts.
- Dueled on submissions[].title — titles usually carry the line in this competition, but a title is not guaranteed to equal the entry text; 304 entries hide behind the default title and their texts are invisible.
- Field is 1,230 entries; the final heat takes only the top 500 on the dev board — the first hurdle is passing that cut, and dev-board scores are dense.
