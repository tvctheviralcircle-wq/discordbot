"""Post approved TVC Creator OS drafts to Discord as the bot.

Usage: python3 -I post_drafts.py <draft.json> [...]
Only posts to channels on the bot's allowlist (access.json groups, or ALLOWED_CHANNEL_IDS).
Each file is a draft document saved from the page's "drafts" collection (fields: channel, text).
Prints one JSON line per draft: {id, ok, messageUrl | error}.
"""
import json, os, sys, urllib.request, urllib.error

GUILD = os.environ.get("DISCORD_GUILD_ID", "1532483829300858920")
TOKEN = os.environ["DISCORD_BOT_TOKEN"]
ACCESS = os.path.expanduser("~/.claude/channels/discord/access.json")
# The allowlist comes from the Discord plugin's access.json, or from ALLOWED_CHANNEL_IDS (comma-separated)
# when the plugin isn't configured in this environment.
if os.path.exists(ACCESS):
    allowed = set(json.load(open(ACCESS)).get("groups", {}))
else:
    allowed = {c.strip() for c in os.environ.get("ALLOWED_CHANNEL_IDS", "").split(",") if c.strip()}

for path in sys.argv[1:]:
    doc = json.load(open(path))
    did, d = doc.get("id") or os.path.basename(path)[:-5], doc.get("data", doc)
    ch, text = d.get("channel", ""), (d.get("text") or "")[:2000]
    if ch not in allowed:
        print(json.dumps({"id": did, "ok": False, "error": "Channel isn't on the allowlist"})); continue
    body = json.dumps({"content": text, "allowed_mentions": {"parse": []}}).encode()
    req = urllib.request.Request(f"https://discord.com/api/v10/channels/{ch}/messages", data=body, method="POST",
                                 headers={"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json", "User-Agent": "TVC-Creator-OS (internal, 1.0)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            m = json.load(r)
        print(json.dumps({"id": did, "ok": True, "messageUrl": f"https://discord.com/channels/{GUILD}/{ch}/{m['id']}"}))
    except urllib.error.HTTPError as e:
        print(json.dumps({"id": did, "ok": False, "error": f"Discord said {e.code}: {e.read().decode()[:200]}"}))
