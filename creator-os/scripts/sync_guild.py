"""Snapshot the Discord server for TVC Creator OS: channels (with whether the bot can view+post), roles.
Usage: python3 -I sync_guild.py <out.json>"""
import json, os, sys, urllib.request, datetime
G = os.environ.get("DISCORD_GUILD_ID", "1532483829300858920"); BOT = os.environ.get("DISCORD_BOT_ID", "1565126862714175620"); T = os.environ["DISCORD_BOT_TOKEN"]
def get(p):
    r = urllib.request.Request("https://discord.com/api/v10" + p, headers={"Authorization": "Bot " + T, "User-Agent": "TVC-Creator-OS (internal, 1.0)"})
    return json.load(urllib.request.urlopen(r, timeout=20))
ch, roles, me = get(f"/guilds/{G}/channels"), get(f"/guilds/{G}/roles"), get(f"/guilds/{G}/members/{BOT}")
guild = get(f"/guilds/{G}")
rp = {r["id"]: int(r["permissions"]) for r in roles}
base = rp[G]
for rid in me["roles"]: base |= rp.get(rid, 0)
admin = bool(base & 8)
def eff(c):
    if admin: return True
    p = base; ows = c.get("permission_overwrites", [])
    for o in ows:
        if o["id"] == G: p = (p & ~int(o["deny"])) | int(o["allow"])
    a = d = 0
    for o in ows:
        if o["id"] in me["roles"]: a |= int(o["allow"]); d |= int(o["deny"])
    p = (p & ~d) | a
    for o in ows:
        if o["id"] == BOT: p = (p & ~int(o["deny"])) | int(o["allow"])
    return bool(p & 1024 and p & 2048)
cats = {c["id"]: c["name"] for c in ch if c["type"] == 4}
lst = sorted(({"id": c["id"], "name": c["name"], "category": cats.get(c.get("parent_id"), "No category"), "canPost": eff(c), "pos": c.get("position", 0)} for c in ch if c["type"] in (0, 5)),
             key=lambda c: (c["category"] != "No category", c["category"], c["pos"]))
for c in lst: c.pop("pos")
doc = {"guildId": G, "guildName": guild["name"], "botName": get("/users/@me")["username"], "botId": BOT, "channels": lst,
       "roles": [r["name"] for r in roles if r["id"] != G], "syncedAt": datetime.datetime.now(datetime.UTC).isoformat()}
json.dump(doc, open(sys.argv[1], "w"))
print(len(lst), "channels;", sum(c["canPost"] for c in lst), "the bot can post in")
