# TVC Creator OS

**Live page (Pharmlitalia Creator Community, server `1532483829300858920`):** https://claude.ai/artifact/BS8LJGntohfJ4aQ95E41cb  
Request processor scheduled task: `trig_01KELia3YQ5dRjxgUqtfMJoH` (on demand, bound to the Creator OS session; posts with the Discord plugin and reacts 🔥 🤍 🚀 📈). Bot: `1565126862714175620`.

Internal TVC dashboard hosted as a Claude artifact: live Cruva analytics, Discord community health, and six Discord bot automations with approve-and-post.

The full build and replication guide is the Claude doc "TVC Creator OS: Build and Replication Guide". This folder holds what that guide tells you to copy.

| File | What it is |
| --- | --- |
| `tvc-creator-os.html` | The whole page. Publish it as a Claude artifact with the capabilities listed in the guide. |
| `request-processor-prompt.md` | The scheduled task prompt that lets the page's buttons reach a Claude session, which posts to Discord. |
| `scripts/sync_guild.py` | Reads your Discord server (channels with bot access, roles) into the JSON the page's `discord` collection expects. |
| `scripts/post_drafts.py` | Posts approved drafts to Discord as the bot, only to allowlisted channels. |

Both scripts need `DISCORD_BOT_TOKEN` in the environment, plus `DISCORD_GUILD_ID` (and `DISCORD_BOT_ID` for `sync_guild.py`) when you use a different server or bot. Run them with `python3 -I`.

Values to change in `tvc-creator-os.html` for a new account: `TRIGGER_ID` (your scheduled task) and `BOT_CLIENT_ID` (only if you use a different Discord bot).
