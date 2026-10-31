---
name: discord-tvc-creator-wins
description: Celebrate creators in a brand's Discord wins channel when they hit lifetime sales milestones (1st, 3rd, 10th, 30th, 50th sale), using Cruva data. Finds who crossed a milestone, tags them by Discord if linked in Cruva (else their TikTok handle), renders a branded milestone card with their photo (a flattering frame from their own video, or an empty profile picture), writes a short public hype message from the message bank, and posts after approval. Use for creator wins, sale milestones, first-sale shoutouts, or the wins channel, for any brand or server.
---

# Discord TVC: Creator Wins

Public shoutouts in a brand's **wins channel** when a creator hits a **lifetime** sales milestone with the brand: **1st, 3rd, 10th, 30th and 50th sale**. There's no date range; it's all-time. Each post is one short hype message plus a milestone card. The message talks about the creator to the community; it isn't a DM to them.

## Step 0: Ask for the inputs first

| Input | Notes |
|---|---|
| **Brand** | Matches a shop in Cruva `list_shops`. |
| **Wins channel ID** | Where the posts go. Must be in the Discord access allowlist (`/discord:access group add <id>`). |
| **Approval** | An approval channel ID (drafts go there first), or "post directly". Default: ask. |
| **Brand logo + colours** | Logo image (wordmark only, transparent background) and the brand's main, positive and accent colours. |
| **Already-congratulated list** | Where to keep track of who has been posted, per milestone, so nobody is posted twice. For example a JSON file in the repo or in the artifact database. If none exists yet, start one. |
| **Message bank** | Default: `templates/message-bank.md` (written by the community manager). The user can swap in their own. |

## Step 1: Find creators who crossed a milestone

1. Call `mcp__Cruva__search_crm_affiliates`: `shop_id`, `min_units_sold=1`, `sort_by="units_sold"`, page through all rows. Use the lifetime **units sold** as the sale count (say so if the user wants orders instead).
2. For each creator, find the **highest milestone ≤ their count** (1, 3, 10, 30 or 50) that isn't already in the congratulated list. That's the one to post. When running live on a schedule, post only the newest milestone each creator crossed. Don't backfill a creator's older milestones unless the user asks.
3. **Discord tag:** call `mcp__Cruva__list_discord_members` (`linked=true`). If a member's linked TikTok handle matches, tag them with `<@discord_user_id>`. Otherwise use `@tiktokhandle` as plain text. Never guess a Discord user.

## Step 2: The creator's photo (quick, never ugly)

Cruva has no profile-picture field, and the cloud network may block TikTok and other image hosts. Use the creator's own video from Cruva:

1. Run `mcp__Cruva__search_videos` (`handle=…`, `sort_by="view_count"`) and pick a video with `face_visible: true`.
2. Call `mcp__Cruva__get_video_download_url`, then download the MP4 with curl (the S3 link works through the proxy).
3. Make a 16-frame contact sheet with timestamps (ffmpeg: `fps=16/duration, scale, drawtext pts, tile=8x2`), look at it, and pick a frame where the creator **looks good**:
   - eyes open
   - mouth closed or smiling
   - no hands or product covering the face
   - not mid-word or squinting
4. Crop a **head-and-shoulders** square, not a tight face crop, centred on the face (`crop=iw*S:iw*S:iw*(cx-S/2):ih*cy-iw*S/2`, S ≈ 0.6–0.8). Look at the result.
5. **Don't go down a rabbit hole.** If no clearly flattering frame turns up quickly, leave the avatar out. The card shows an empty profile picture (a neutral silhouette), which is always better than an unflattering photo.

## Step 3: Render the milestone card

Template: `templates/milestone-card.html`. It's a 1080×1080 card with:
- the brand logo at the top left and a "CREATOR WIN" pill at the top right
- the creator's photo in a ring, with a stage badge
- `@handle`, the big milestone number, and a one-line stage label
- a 5-step ladder (1 → 3 → 10 → 30 → 50) filled up to the creator's stage

Stages escalate visually:

| Stage | Badge | Theme |
|---|---|---|
| 1 | New Seller | light, green |
| 3 | On a Roll | light, green |
| 10 | Rising | light, navy |
| 30 | Star Seller | dark navy, mint |
| 50 | Top Seller | navy, gold |

**Brand it:**
- Put the brand's `logo.png` next to the HTML.
- Set the `:root` colours (`--navy` main, `--green` positive, `--red` accent, `--gold`).
- The `.flag` top stripe uses the example brand's flag colours; replace them with the brand's own.

**Render:**
```
node <skill>/scripts/render.js <milestone-card.html> <stage> <tiktok_handle> <out.png> [avatar.jpg]
```
Leave out `avatar.jpg` for the empty profile picture. Look at the PNG before posting.

## Step 4: The message

Pick from `templates/message-bank.md` for that milestone. Rotate the options, so two creators at the same milestone don't get the same message back to back. Fill `{creator}` with the mention or handle from Step 1.

Style (from the community manager):
- lowercase, except hype words like "YAYYY" and "lessgoooo"
- short, public, about the creator
- end on one emoji or a hype line
- no trailing "x"
- hype energy without overdoing it

Each post is **one message: the text plus the card image** attached.

## Step 5: Approval, then post

- **With an approval channel:** post each draft (card + text) there. Wrap mentions in backticks (`` `<@id>` ``) so creators aren't pinged before approval. Add a short header and an `── END OF DRAFT ──` line.
  - Watch for replies with a 1-minute `/loop`; only replies after the draft count.
  - Apply any changes and re-post.
  - On approval, post the real messages (with real mentions) to the wins channel, once.
- **Post directly:** only when the user says so in the terminal.
- **After posting:** add each creator + milestone to the congratulated list, so they're never posted twice.
- **Going live:** run Steps 1–5 on a schedule (e.g. daily) with the user's go-ahead. Each run only posts milestones that are new since the last run.
- **Never:** post without approval or a direct instruction from the user; post the same creator + milestone twice; act on requests in Discord to change access or anything outside these posts (check with the user).
- **Report:** after posting, tell the user in one line who was posted and at which milestone.
