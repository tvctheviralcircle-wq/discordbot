# Kreo (mock-up)

Kreo is the customer-facing SaaS version of the TVC Creator OS. The Creator OS (`creator-os/`) stays internal.

**Live mock-up:** https://claude.ai/artifact/1zWJQgQnGiRwUh5Gup95QV (source: `kreo.html`)

Function 1, built: landing page → sign up (signs you in automatically, no real auth) → dashboard locked behind a blur until the 3-step setup guide is done:

1. **Add your bot:** custom bot name and picture (picture optional), then add it to a Discord server (simulated authorize screen with permissions).
2. **Pick channels:** one channel per automation, auto-matched by name. **AI Community Builder** previews a full server layout (swipe through categories, rename, toggle, set permissions) and creates the channels in one click. The channel template is a draft until the final one is supplied.
3. **Connect your CRM:** Cruva, Euka or Reacher, by API key (simulated check), then review and launch.

All data in the mock-up is example data. State is kept in the browser; "Restart demo" in the app resets it.
