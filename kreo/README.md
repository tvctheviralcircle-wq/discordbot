# Kreo (mock-up)

Kreo is the customer-facing SaaS version of the TVC Creator OS. The Creator OS (`creator-os/`) stays internal.

**Live mock-up:** https://claude.ai/artifact/1zWJQgQnGiRwUh5Gup95QV (source: `kreo.html`)

What's in the mock-up:

1. **Landing page and sign up:** sign up signs you in automatically (no real auth).
2. **Setup guide** (dashboard blurred until done):
   - **Add your bot:** custom name and picture, then "Add to Discord" opens the real Discord invite in a new tab (TVC bot `1565126862714175620`, permissions `335793232`). Back in Kreo the page waits, re-checks when you return to the tab, and has a Refresh button; then you confirm the server the bot was found in. Detection is simulated in the mock-up.
   - **Pick channels:** auto-matched per automation. The **AI Community Builder** uses the Pharmlitalia Creator Community's layout (emoji・name channels; GET STARTED, CREATOR HUB, SUPPORT, MULTI PLATFORM, plus `moderator-only`).
   - **Connect your CRM:** Cruva, Euka or Reacher by API key (simulated), then launch.
3. **App:** Dashboard (bento tiles: analytics peek, to-do, top creators, automations with on/off, coming up, community pulse, latest DMs), a custom date range picker (presets + two-month calendar), Analytics (Community and Overall/CRM tabs; creators table with CRM email and phone plus WhatsApp numbers found in DMs; creator drawer), Approvals, Automations (toggle, edit, run now) with a chat-based custom automation builder and live preview, Onboarding & DMs (inbox, questions, responses), Content, and Settings (workspace, bot & server, channels, CRM & data, team, notifications, billing).

All data is example data (fictional creators, 555 numbers, example.com emails). State is kept in the browser; "Restart demo" resets it.
