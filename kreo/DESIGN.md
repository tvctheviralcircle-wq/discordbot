# Kreo design system

Kreo (the customer-facing version of the Creator OS) uses its own look, built on **Stageshow**'s craft rules
(`.claude/skills/stageshow`, MIT, by Benji Taylor). The TVC Creator OS and Pharmlitalia cards keep the TVC system in `/DESIGN.md`.

All values are tokens in the `:root` block at the top of `kreo/kreo.html`; components never use literal colours.

## The look
- **Ground and surfaces:** warm canvas `--color-background` (#f6f5f4), white surfaces lifted by a hairline ring and a soft shadow (`--shadow-window`), not borders. Floating things (menus, dialogs, drawers, toasts) use `--shadow-float`; the hero window `--shadow-hero`; a satellite card `--shadow-satellite`.
- **One accent:** Kreo rose `--color-primary` for the one main action and the chart highlight. Everything else is neutral (`--color-accent` is a dark gray). Status colours mean status only.
- **Type:** the system stack (SF Pro on Apple, Inter elsewhere), sentence case, -0.025em headings. Figures are sans with tabular digits; monospace only for code.
- **Controls:** filled primary button with a coloured soft shadow; white buttons with a ring; segmented controls are a well with a white thumb; toggles are iOS style (green when on); the selected nav item is a white pill on the canvas.
- **Avatars** take their own colour from `--av-1…6`; gray discs are filler only.
- **Icons:** Lucide 0.468.0 (ISC), one stroke, 16–18px. No sparkles or purple for AI features: the Community Builder uses `blocks`, the custom-automation AI uses `bot`.
- **Charts:** smooth line, gradient area fading to nothing, dashed faint gridlines, an end dot with a white ring.
- **Discord previews** stay in Discord's dark look so drafts match what will post.

## Marketing page
- **Hero:** a Stageshow-style demo in a browser window: the cursor approves a draft, the button confirms on itself, the count rolls, the Discord post rises in as a satellite and reactions count up. The next draft arriving is the visible cause of the reset. With reduced motion it shows the posted state as a still.
- **Feature bento:** canvas tiles, copy bottom-left, the product hung from the top and faded at its foot; real words only on what each tile is about.
