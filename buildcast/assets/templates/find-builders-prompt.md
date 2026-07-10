# Prompt: find active accounts to reply to

*Reusable prompt for a logged-in browser-agent session (Antigravity, Comet, or similar).
Timelines and search require login, so this step cannot run headless. Re-run weekly to
refresh WATCHLIST.md; the daily habit is replying, not re-searching.*

*Adapt the search queries in the prompt to the platform and niche before running.*

---

```
I'm {{OWNER}} ({{HANDLE}} on {{PLATFORM_PRIMARY}}), building "{{PROJECT}}" in public —
{{PITCH}}

My niche: {{NICHE}}.

Task: using the platform (I'm logged in), find 25 accounts worth replying to daily.
Search for recent posts (last 7 days) under queries relevant to my niche — e.g.
"build in public", "building in public", "indie hacker", "shipped", "side project",
"solo founder", plus 3–4 queries specific to what {{PROJECT}} does — and browse
quote-networks and reply sections of good posts you find; the best accounts are often
found replying to each other.

Include an account only if ALL of these hold:
- Posted original content (not just replies/reposts) at least 3 times in the last 7 days.
- Between ~500 and ~30,000 followers — big enough to have a community, small enough that
  a good reply from me gets seen and answered.
- Their replies section shows real conversation (they answer people who reply to them).
- They post about building something specific — a product, a tool, an experiment — not
  motivational filler or growth-hacking content.

Hard exclusions:
- Follow-for-follow / "drop your project below" engagement farmers.
- Accounts whose feed is mostly threads of recycled advice ("10 lessons from...").
- Crypto/trading-signal accounts, giveaway accounts, and anything that buys engagement.
- Accounts inactive for 5+ days.

Output: a markdown table sorted by relevance to my niche, with columns:
| Handle | Followers | What they're building | Post frequency | Why relevant |
| Link to one recent post of theirs I could reply to substantively today |

Below the table, add a short "start here" note: the 5 accounts where my first reply is
most likely to start a real conversation, and for each, what angle I could take based on
their recent post (a genuine reaction or question — never generic praise, never a pitch
for {{PROJECT}}).
```
