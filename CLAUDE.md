# discordbot

Discord community automations for TVC brand communities, built on Cruva data. Skills live in `.claude/skills/`.

## Pharmlitalia Creator Community

- **Discord server ID: `1532483829300858920`** (Pharmlitalia Creator Community).
- All Pharmlitalia automations, channels, schedules and state (`config/pharmlitalia-*.json`) belong to this server only. Never post them to, or mix them with, another server. A different brand or server gets its own config file.
- Approval (moderators): `1532483951007105240`. Every draft goes here first.
- Destinations: winning angle `1533830710937256087`, viral hooks `1534655536602026164`, creator wins `1533831170108952596`, leaderboard `1550255413558116492`.
- Cruva shop: Pharmlitalia `6a33383f8957ff1cdc980fe1`. Time zone: America/New_York.
- Creators not linked to Discord in Cruva: write their TikTok username as plain `@handle` text, no mention.
- After posting to any destination channel, react to the main message of each post with 🔥 🤍 🚀 📈.
- Viral hooks: pick the most-viewed relevant video for the week; Cruva AI analysis isn't required (no invented quotes without a transcript).
- Creator OS dashboard: https://claude.ai/artifact/BS8LJGntohfJ4aQ95E41cb (source `creator-os/`). Page buttons fire `trig_01KELia3YQ5dRjxgUqtfMJoH`; process its `requests` per that task's prompt, Pharmlitalia server only.

## Two-way approvals (moderator chat + Creator OS)

Every scheduled draft can be approved in either place; whichever comes first posts it, once.

1. **Drafting:** after posting a draft to the moderator channel, also add it to the Creator OS `drafts` collection (ArtifactData `set`, url https://claude.ai/artifact/BS8LJGntohfJ4aQ95E41cb). Doc id: `<automation>-<week start or creator>-<rank or milestone>`, e.g. `viral_hooks-2026-10-25-2`, `wins-michelleleannefashion-3`. Fields: guild `1532483829300858920`, automation (`winning_content` | `viral_hooks` | `wins` | `leaderboard`), name, channel (destination id), channelName, status `pending`, test `false`, source `schedule`, createdAt, approvalMessageIds, history, messages `[{text, images, files}]` with the FINAL texts (real @here and mentions, no draft header or backticks), images = card PNGs uploaded with the Artifact tool (`asset: true`), files = local PNG paths, and `text` = all texts joined. Save the doc id as `os_draft_id` in the pending entry in `config/pharmlitalia-pending.json`.
2. **Approved in the moderator chat:** first read the OS draft. If it's already `posted`, don't post again; just clean up the pending entry. Otherwise set it to `posting`, post, then set `posted` with messageUrl and a history line "Approved in moderator chat by <name>".
3. **Approved in Creator OS** (request `post`, not a test): check the pending entry is still pending, post the OS draft's messages (they include any edits made in the OS) to the destination, react 🔥 🤍 🚀 📈, move the entry to `posted` in the pending file, commit, and reply in the moderator chat under the draft: "approved in creator os, live in <#channel>".
4. **Changes requested in the moderator chat:** re-post the draft there and update the OS draft's messages too. **Rejected in Creator OS** (request `reject`): remove the pending entry and say so under the draft in the moderator chat.

## Design system
Before any UI work, read DESIGN.md. Build only from its tokens (design-system/tokens.css, or the Tailwind theme in design-system/theme.css). Never hard-code a colour, font size, radius or shadow; if a value is missing, add a token. Check new screens against design-system/preview.html. (Inspired by cruva.com's measured design, not affiliated; existing Pharmlitalia cards and the Creator OS page keep their own looks unless asked.)
