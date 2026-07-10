# Post entry template

<!-- Install note (delete this comment when installing): write this file verbatim, minus
this comment, as <content>/TEMPLATE.md. The fenced block stays fenced in the installed
file — it keeps the template's frontmatter inert; post files are created by copying the
fence's CONTENTS, per the line below. -->

*Copy everything inside the code block below into `posts/YYYY-MM-DD-<platform>-<slug>.md`
and fill it in. Delete guidance comments as you go.*

---

```markdown
---
date: YYYY-MM-DD                  # publish date (planned date while draft)
platform: {{PLATFORM_PRIMARY}}    # x | reddit | tiktok | ...
account: personal-build-in-public # personal-build-in-public | brand
type: single                      # single | thread | reply
status: idea                      # idea | draft | posted
title: Short working title
post_url: null                    # fill after publishing
follow_up_of: null                # relative path to prior post file
follow_ups: []                    # filled in later as follow-up posts are created
assets: []                        # e.g. [../assets/<slug>/screenshot.png]
links: []                         # external links included in the post body
---

# <Title>

## Content

<For ideas: 2–3 lines — the hook, the receipt (screenshot/number/decision), the chain
it belongs to. For drafts/posted: the full text. For threads, number each post:>

**1/**
...

**2/**
...

## Metrics

| captured_at | views | likes | replies | reposts | bookmarks | profile visits | new follows |
|---|---|---|---|---|---|---|---|
| YYYY-MM-DD (~24h) | | | | | | | |
| YYYY-MM-DD (~7d)  | | | | | | | |

## Retro

**What worked:**
-

**What went wrong:**
-

**Lesson:** <one line — promote to PLAYBOOK.md if durable>
```
