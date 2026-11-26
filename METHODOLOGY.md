# Methodology — bounty #43: Make the AI Judge Laugh: Office Jokes

Competition: `u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a`
($5, free entry, deadline 2026-11-26T14:40:00Z / 22:40 CST 26 Nov).
The entry is one joke about office life, a single line under 200 characters,
written by the program `main.py` to `/output/entry.txt`. A judge model
(z-ai/glm-5.3-flash) compares jokes two at a time under the brief published
with the bounty, in this order:

1. A genuine one-line joke about office life (not a slogan, caption or
   stray observation).
2. A real turn or surprise at the end.
3. Recognition — the truth of the office in it, so the laugh comes with a
   wince.
4. Tight wording, every word earning its place.
5. Freshness — not the obvious Monday morning or photocopier line.

An exact tie on judge win rate goes to the smaller text (fewer bytes), then
to the earlier receipt — so the line is kept as short as the joke allows.
Blind rounds run: nothing is judged on submit; the final round is the
deadline. The top 500 entrants on the dev board go on to the final heat.

## Competitor study (titles only, never copied)

The public submissions feed was read for titles only (source is withheld;
entry texts were not fetched). 1,000 titles (of ~8,096 submissions) were
counted by angle:

| Angle | Titles / 1,000 |
|---|---|
| Meeting / email ("per my last email", reply-all, standup, sync, calendar) | 176 — the most crowded by far |
| Printer | 37 |
| Performance review / promotion / raise | 32 |
| Boss / manager | 29 |
| HR | 17 |
| Lunch / fridge | 13 |
| Overtime / burnout / vacation | 13 |
| Plant | 12 |
| Open plan / desk | 10 |
| IT / password / wifi / Excel | 8 |
| Chair | 6 |
| Corporate speak (synergy, circle back, bandwidth) | 5 |
| Fridge thief | 5 |
| Birthday / cake | 5 |
| Quick question | 4 |
| Group chat / Slack | 4 |
| Fire drill | 3 |
| Commute / parking | 3 / 2 |
| Intern | 2 |
| Microwave | 2 |
| Water cooler | 2 |
| Coffee | 2 |
| Badge / access card | 1 |
| Out of office | 1 |
| Payroll | 1 |
| Toilet / bathroom | 1 |
| Lift / elevator | **0** |
| Thermostat / air conditioning | **0** |
| Dress code | 0 |
| Sick day | 0 |
| Team building | 0 |
| Reception | 0 |
| Cleaner | 0 |

154 of the 1,000 titles were generic ("Office joke", the bounty title
itself). Conclusion: meetings/emails, the printer, the boss and the
performance review are saturated — any line there has to beat hundreds of
near-identical takes. The lift, the thermostat, the sick day, team
building, the receptionist and the cleaner are effectively untouched.
The lift was chosen: every office worker knows the lift that stops at
every floor, and no title in the sample used it.

## Candidates — written fresh in this session, scored 0–50

Each candidate scored out of 10 on the five brief criteria, in order:
real joke / turn / recognition / tightness / freshness. Character counts
were measured programmatically, never by hand.

| # | Candidate | R | T | Rec | Tight | Fresh | Total | Chars |
|---|---|---|---|---|---|---|---|---|
| 1 | The lift stops at every floor except the top one. Same as my career. | 9 | 8 | 9 | 10 | 9 | **45** | 68 |
| 2 | Our lift has been 'out of order' so long it's now the longest-running project in the company — and the only one with no meetings about it. | 8 | 7 | 7 | 6 | 8 | 36 | 139 |
| 3 | I take the stairs now. The lift and my promotion both stopped moving in 2023. | 8 | 8 | 8 | 8 | 8 | 40 | 80 |
| 5 | The thermostat has two settings: Arctic research station and 'someone from Finance changed it again'. | 8 | 7 | 8 | 7 | 9 | 39 | 107 |
| 7 | I wore a coat indoors today. The thermostat is the only thing in this office with real power. | 8 | 8 | 8 | 8 | 9 | 41 | 94 |
| 8 | The air con is so cold HR sent a memo about 'appropriate indoor clothing' — for July. | 7 | 6 | 7 | 7 | 9 | 36 | 88 |
| 9 | My access badge opens every door in the building except the one to my career. | 9 | 9 | 9 | 9 | 9 | **45** | 77 |
| 10 | My badge photo is from my first day. Security still waves me through — apparently I've changed less than the org chart. | 7 | 7 | 7 | 6 | 8 | 35 | 122 |
| 11 | I lost my badge twice this week. Facilities replaced it faster than IT ever fixed my laptop, so now I know who actually runs this place. | 8 | 7 | 8 | 6 | 8 | 37 | 142 |
| 12 | The fire drill has perfect attendance, because the alarm is the only deadline anyone in this office respects. | 9 | 9 | 9 | 8 | 8 | 43 | 109 |
| 13 | The fire drill is the one office event nobody schedules a meeting to plan. | 7 | 7 | 7 | 8 | 8 | 37 | 74 |
| 14 | During the fire drill, everyone suddenly knows exactly where the exits are — the same people who can't find the shared drive. | 8 | 8 | 8 | 6 | 8 | 38 | 123 |
| 15 | I called in sick and my manager replied 'feel better!' then CC'd me on three urgent emails. | 9 | 8 | 10 | 8 | 9 | **44** | 91 |
| 16 | Our sick-day policy is simple: you may rest, provided your inbox doesn't notice you're gone. | 8 | 8 | 9 | 8 | 9 | 42 | 94 |
| 17 | The team-building day taught us to trust each other. It did not teach anyone to reply to my emails. | 7 | 6 | 7 | 7 | 9 | 36 | 104 |
| 18 | We did a trust fall at the team-building day. I fell. Nobody caught me. HR called it 'a learning outcome'. | 9 | 9 | 8 | 7 | 9 | 42 | 107 |
| 19 | The company spent thousands on a team-building retreat and all I learned is that Dave from Sales can't read a map — or a room. | 8 | 7 | 7 | 6 | 8 | 36 | 131 |
| 20 | The receptionist knows everyone's name, birthday and coffee order. She runs this company; the CEO just has the parking space. | 8 | 8 | 8 | 7 | 9 | 40 | 131 |
| 21 | Our receptionist greets the CEO by his first name and the rest of us by our badge numbers. Fair — she signs for all our parcels. | 8 | 7 | 8 | 7 | 9 | 39 | 131 |
| 22 | The cleaner has seen my desk at its worst and still says good morning. She deserves the promotion more than any of us. | 7 | 7 | 8 | 7 | 9 | 38 | 121 |
| 23 | The office cleaner empties my bin every night, which is more closure than any project here has ever had. | 9 | 9 | 8 | 8 | 9 | 43 | 105 |
| 24 | The dress code says 'smart casual', which in this office means a blazer over the same shirt you've worn since Tuesday. | 8 | 7 | 8 | 7 | 9 | 39 | 115 |
| 25 | HR updated the dress code to 'smart casual'. Nobody knows what it means, so everyone just wears black and hopes. | 7 | 6 | 7 | 8 | 9 | 37 | 110 |
| 26 | The only promotion I've ever received is a parking space — two floors further from the entrance than my old one. | 9 | 9 | 8 | 8 | 8 | 42 | 113 |
| 27 | I got to the office at 7 a.m. for a parking space. The early bird gets the worm; the early employee gets a 40-minute walk from the overflow car park. | 8 | 7 | 7 | 6 | 8 | 36 | 152 |
| 28 | Payroll got my salary right for the first time in six months. I checked twice — I thought it was a phishing email. | 9 | 9 | 8 | 8 | 9 | 43 | 114 |
| 29 | Someone keeps leaving the bathroom door open. Facilities calls it 'an open-plan initiative'. | 8 | 8 | 7 | 8 | 9 | 40 | 93 |
| 30 | The office bathroom has a sign saying 'please be considerate'. It has been ignored longer than any email I've ever sent. | 7 | 7 | 7 | 7 | 9 | 37 | 118 |
| 31 | Whoever reheats fish in the office microwave has done more damage to team morale than any restructure. | 9 | 8 | 9 | 8 | 8 | 42 | 106 |
| 32 | The microwave has a sign: 'clean up after yourself'. It's been there since 2019. So has the smell. | 7 | 6 | 7 | 7 | 8 | 35 | 91 |
| 33 | The office plant has outlived three managers and two restructures. It's now our longest-serving employee, and the only one never asked to do more with less. | 8 | 8 | 8 | 7 | 7 | 38 | 159 |
| 34 | I watered the office plant and it perked up. That's the fastest positive feedback anyone has ever received here. | 8 | 8 | 8 | 8 | 7 | 39 | 106 |
| 35 | My chair squeaks every time I lean back, so the whole floor knows exactly when I've given up for the day. | 9 | 8 | 9 | 9 | 8 | 43 | 101 |
| 36 | A colleague stopped by for a 'quick question'. Forty minutes later I understood why our meetings have agendas and my desk doesn't. | 8 | 7 | 8 | 6 | 8 | 36 | 129 |

## Head-to-head — why the winner wins

Top of the table: #1 lift/career (45), #9 badge/career (45), #15 sick-day
CC (44), then #12 fire drill, #23 cleaner, #28 payroll, #35 chair (43).

- **#1 vs #9:** both end on the same turn — the career that won't open.
  Same punchline family, so only one can stand. #1 is tighter (68 vs 77
  chars), its angle is fresher (lift 0 titles vs badge 1), and its
  two-beat structure ("…top one. Same as my career.") lands the turn as
  a deadpan punch rather than a clause. #1 wins.
- **#1 vs #15:** #15 has the single best recognition score (10/10 — every
  office worker has been CC'd while sick). But its vehicle is email, the
  most crowded angle in the field (176/1,000 titles), so its freshness
  is borrowed, not real; the judge's criterion 5 and the head-to-head
  field punish it. #1 wins.
- **#1 vs #12 / #23 / #28 / #35:** all four are strong jokes, but #1
  beats each on total score and is the shortest of the top group — and
  the competition's tie-break rewards fewer bytes. #1 wins.

## Refinements of the winner — kept or rejected, with reasons

- A. `The lift stops at every floor except the top one. Same as my career.`
  (68 chars) — the base line. Kept as the reference.
- B. `Our lift stops at every floor but the top. Same as my career.`
  (61 chars) — **CHOSEN.** Seven characters tighter than A with the same
  joke; "Our" puts the speaker inside the office, which anchors
  criterion 1 (a joke about office life) without spending a setup word;
  "but the top" is the tightest correct phrasing. Fewer bytes also helps
  the competition's byte tie-break.
- C. `The lift goes to every floor except the top. So does my career.`
  (63 chars) — rejected. "Goes to" loses the recognition inside "stops
  at every floor" (the lift that stops everywhere is itself an office
  truth); the turn is no stronger for the swap.
- D. `The lift stops at every floor except the top one — just like my career.`
  (71 chars, 73 bytes) — rejected. Wordier, and "just like" is a weaker,
  more explanatory connector than the deadpan "Same as my career."; the
  em dash also costs bytes.
- "…Same as my career prospects." — rejected. "Prospects" explains what
  "career" already says; the shorter noun lands harder.

## The winning line (61 characters, 61 bytes, no trailing newline)

> Our lift stops at every floor but the top. Same as my career.

Why it fits the brief, criterion by criterion: (1) a genuine one-line
joke about office life — lift plus career, nothing else; (2) the turn
lands in the last five words, where "the top" stops meaning a floor and
starts meaning a career ceiling; (3) recognition — the lift that stops
at every floor and the promotion that never comes are both daily office
truths, and the laugh comes with a wince; (4) tight — 61 characters,
every word earning its place, no setup longer than it needs; (5) fresh —
the lift angle appeared in 0 of 1,000 sampled competitor titles, against
176 for meetings/emails.

## Program

`main.py` is deterministic: it holds the line as a constant, checks it is
1–199 characters and a single line, and writes exactly those bytes to
`/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` for local tests), mode
0644, no trailing newline. `test_determinism.sh` runs it twice into two
directories and diffs the outputs byte for byte.
