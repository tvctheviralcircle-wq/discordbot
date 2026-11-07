---
version: alpha
name: "TVC Creator OS"
description: "TVC Creator OS design system: structure measured from cruva.com on 2026-11-07, identity (colours, fonts, buttons) is TVC's own. Not affiliated with Cruva."
colors:
  background: "#ffffff"
  surface: "#ffffff"
  surface-subtle: "#f8f6fa"
  text: "#2e2836"
  heading: "#1f1a24"
  text-muted: "#6e6678"
  text-subtle: "#8c8496"
  border: "#ece7f0"
  primary: "#b8336a"
  primary-foreground: "#ffffff"
  primary-tint: "#fbeff4"
  accent: "#4c3481"
  accent-tint: "#f4eefa"
  link: "#b8336a"
  focus: "#b8336a"
  success: "#2f7a4f"
  success-tint: "#e3f2e8"
  danger: "#b3364f"
  danger-tint: "#fbe4e8"
  surface-inverse: "#1f1a24"
  surface-inverse-foreground: "#ffffff"
  chart-1: "#b8336a"
  chart-2: "#4c3481"
  chart-3: "#a99bb5"
typography:
  display:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.02em
  h1:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  h2:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.02em
  h3:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.02em
  h4:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.02em
  h5:
    fontFamily: "\"Montserrat\", \"Arial Black\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "\"Poppins\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "\"Poppins\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 15.5px
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "\"Poppins\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "\"Poppins\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 14.5px
    fontWeight: 400
    lineHeight: 1.6
  code:
    fontFamily: "\"JetBrains Mono\", ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.55
  overline:
    fontFamily: "\"Poppins\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 9.5px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.04em
rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 10px
  2xl: 12px
  3xl: 20px
  full: 9999px
spacing:
  "0.5": 2px
  "0.75": 3px
  "1": 4px
  "1.25": 5px
  "1.5": 6px
  "1.75": 7px
  "2": 8px
  "2.25": 9px
  "2.5": 10px
  "3": 12px
  "3.5": 14px
  "4": 16px
  "4.5": 18px
  "5": 20px
  "5.5": 22px
  "6": 24px
  "7": 28px
  "8": 32px
  section: 80px
  section-alt: 60px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-foreground}"
    rounded: "{rounded.xl}"
    padding: "10px 18px"
    height: 40px
  button-primary-hover:
    backgroundColor: "#a32c5d"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.heading}"
    rounded: "{rounded.xl}"
    padding: "10px 16px"
    height: 40px
  button-secondary-hover:
    backgroundColor: "{colors.surface-subtle}"
  button-subtle:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.accent}"
    rounded: "{rounded.xl}"
    padding: "8px 14px"
    height: 36px
  button-subtle-hover:
    backgroundColor: "#ebe2f6"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: 14px
    padding: 20px
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    typography: "{typography.caption}"
    rounded: "{rounded.xl}"
    padding: "4px 12px"
    height: 40px
  badge:
    backgroundColor: "{colors.accent-tint}"
    textColor: "{colors.accent}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  link:
    textColor: "{colors.link}"
  band-inverse:
    backgroundColor: "{colors.surface-inverse}"
  page:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text}"
    typography: "{typography.body}"
  navigation:
    backgroundColor: transparent
    height: 69px
---

<!-- extract-design: the front matter above is generated from design-system/roles.json. Change roles.json, then run extract.mjs --rebuild to refresh it. The prose below is yours. -->

# TVC Creator OS design system

> Measured from https://cruva.com on 2026-11-07: 12 page visits (/, /case-studies, /blog, /pricing, /demo, /workflows, /meta-ads-programs, /full-pipeline-crm) at 1440px and 390px. The values are what the browser rendered. The names and the prose are judgment: check them against the screenshots in `design-system/source/screens/`. Inspired by cruva.com, not affiliated with it: never use its logo, illustrations, photos or words.

## Overview

TVC's own system for the Creator OS and other internal tools. The **structure** comes from measurements of cruva.com and its logged-in dashboard: the type scale, 4px spacing grid, radius scale, sidebar-plus-KPI-grid layout and sparkline cards. The **identity** is ours, from the Creator OS: a flat, all-white interface, plum-black text, lilac hairlines, solid rose (`{colors.primary}`) for the one main action and deep indigo (`{colors.accent}`) for secondary emphasis. Headings are Montserrat at weight 600, text is Poppins at 400–500, big figures are JetBrains Mono. Nothing glows or floats: cards are separated by hairlines, not shadows.

What was measured: a light interface on `#ffffff`, headings in `#1f1a24`, body text in `#2e2836`, and `#b8336a` for the main action. Type is Poppins and JetBrains Mono and Montserrat. Space runs on a 4px grid. Corners are 2px, 4px, 6px, 8px, 10px, 12px, 20px, and pills where the site uses them.

## Colors

| Token | Value | Use it for | On background |
|---|---|---|---|
| `{colors.background}` | `#ffffff` | the page; white everywhere, like the Creator OS | 1:1 |
| `{colors.surface}` | `#ffffff` | cards, panels, the sidebar and the top bar (same white as the page, separated by `{colors.border}` hairlines) | 1:1 |
| `{colors.surface-subtle}` | `#f8f6fa` | hover rows, table stripes, segmented-control tracks, quiet wells inside a card | 1.07:1 |
| `{colors.text}` | `#2e2836` | running copy and table cells | 14.26:1 |
| `{colors.heading}` | `#1f1a24` | headlines, card titles and big figures | 17.05:1 |
| `{colors.text-muted}` | `#6e6678` | card labels, descriptions, sub-heads, chart axis labels | 5.48:1 |
| `{colors.text-subtle}` | `#8c8496` | timestamps, placeholders and other tertiary copy only; fails AA for body text | 3.59:1 |
| `{colors.border}` | `#ece7f0` | every hairline: card edges, dividers, inputs, outline buttons | 1.22:1 |
| `{colors.primary}` | `#b8336a` | the one main action per view (Approve & Post, Save), the active nav item's text and dot, focus rings, the chart highlight | 5.65:1 |
| `{colors.primary-foreground}` | `#ffffff` | text and icons on `{colors.primary}` | 1:1 |
| `{colors.primary-tint}` | `#fbeff4` | the active nav item's background and selected chips | 1.12:1 |
| `{colors.accent}` | `#4c3481` | secondary emphasis: numbered discs, info pills, tags, the second chart series | 9.93:1 |
| `{colors.accent-tint}` | `#f4eefa` | background of `{colors.accent}` pills and quiet buttons (Settings) | 1.14:1 |
| `{colors.link}` | `#b8336a` | links in running text | 5.65:1 |
| `{colors.focus}` | `#b8336a` | the :focus-visible ring (2px) | 5.65:1 |
| `{colors.success}` | `#2f7a4f` | upward changes and “Posted / Allowlisted” states, as text on `{colors.success-tint}` | 5.23:1 |
| `{colors.success-tint}` | `#e3f2e8` | background of success pills and change chips | 1.16:1 |
| `{colors.danger}` | `#b3364f` | downward changes, errors, failed posts, as text on `{colors.danger-tint}` | 5.9:1 |
| `{colors.danger-tint}` | `#fbe4e8` | background of danger pills and change chips | 1.21:1 |
| `{colors.surface-inverse}` | `#1f1a24` | selected segments (7D / 14D) and the toast; never large areas | 17.05:1 |
| `{colors.surface-inverse-foreground}` | `#ffffff` | text on `{colors.surface-inverse}` | 1:1 |

For reference only (measured on cruva.com, not part of TVC's look; build with the roles above), the full palette (48 colours, most used first) is in `design-system/tokens.css` as `--color-<name>`: neutral-50 `#fafaff` (42.8%), slate-950 `#1a1a2e` (10.7%), slate-700 `#5b5b73` (7.4%), slate-950-2 `#0b0b18` (6.3%), neutral-100 `#e8e6f5` (9.1%), indigo-700 `#4c3df5` (3.9%), slate-500 `#8a8aa3` (2.5%), slate-950-3 `#20243b` (2.2%), indigo-600 `#6657df` (0.9%), white-a85 `#ffffffd9` (0.7%), ….

Gradients the site paints: `linear-gradient(rgb(248, 247, 255), rgb(244, 243, 255) 60%, rgb(248, 247, 255))`; `linear-gradient(rgb(232, 230, 245) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(90deg, rgb(232, 230, 245) 1px, rgba(0, 0, 0, 0) 1px)`; `linear-gradient(rgb(247, 246, 255) 0%, rgb(250, 251, 254) 100%)`.

- One `{colors.primary}` filled button per view. Everything else is the white outline button or the quiet `{colors.accent-tint}` button.
- Rose and indigo never fill large areas; they are for text, small fills, lines and dots. The page stays white.
- Change chips are always tinted pills: `{colors.success}` on `{colors.success-tint}`, `{colors.danger}` on `{colors.danger-tint}`, with ▲/▼ and a percentage.
- No gradients in UI chrome (this replaces both Cruva's indigo glows and the old Creator OS rose-to-indigo gradient).

## Typography

- **sans**: Poppins (free). Stack: `"Poppins", ui-sans-serif, system-ui, sans-serif`
- **mono**: JetBrains Mono (free). Stack: `"JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`
- **display**: Montserrat (free). Stack: `"Montserrat", "Arial Black", ui-sans-serif, system-ui, sans-serif`

| Token | Size | Phone | Line height | Tracking | Weight | Font |
|---|---|---|---|---|---|---|
| `{typography.display}` | 72px | 40px | 1.05 | -0.02em | 600 | display |
| `{typography.h1}` | 56px | 35.1px | 1.1 | -0.02em | 600 | display |
| `{typography.h2}` | 44px | same | 1.1 | -0.02em | 600 | display |
| `{typography.h3}` | 34px | 25px | 1.12 | -0.02em | 600 | display |
| `{typography.h4}` | 26px | 20px | 1.25 | -0.02em | 600 | display |
| `{typography.h5}` | 19px | same | 1.25 | -0.02em | 600 | display |
| `{typography.body-lg}` | 18px | same | 1.55 | 0 | 400 | sans |
| `{typography.body}` | 15.5px | same | 1.7 | 0 | 400 | sans |
| `{typography.body-sm}` | 15px | same | 1.65 | 0 | 400 | sans |
| `{typography.caption}` | 14.5px | same | 1.6 | 0 | 400 | sans |
| `{typography.code}` | 11px | same | 1.55 | 0 | 400 | mono |
| `{typography.overline}` | 9.5px | same | 1.55 | 0.04em | 400, uppercase | sans |

Weights in use: 400 (67.2%), 500 (15.7%), 600 (13.8%), 450 (1.8%), 700 (1%). Steps grow by about ×1.286.

- Headings in Montserrat 600, sentence case, gentle negative tracking (no tighter than -0.02em: Montserrat is wide). Never 800–900, never the black sticker style.
- Body and UI text in Poppins 400; labels and buttons 500–600. Avoid bold paragraphs.
- Figures that are the point of a card (GMV, counts, ROI) in JetBrains Mono with tabular numerals, `{colors.heading}`; their labels in Poppins, `{colors.text-muted}`.
- Small uppercase eyebrows (11px, +0.08em) in `{colors.primary}` above page titles.

## Layout

- Grid: none clear (spaces are loose; 4px is the nearest). Spacing steps: 2px, 3px, 4px, 5px, 6px, 7px, 8px, 9px, 10px, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 28px, 32px (`--space-<n>`, where n × 4 = px).
- Sections: 80px or 60px of vertical padding on desktop, 40px or 56px on phones.
- Content width: page 1240px, wide 1176px, narrow 760px (`--container-<name>`).
- Grids: 2 columns, 3 columns, 5 columns, 4 columns.
- The home page alternates bands: `#fafaff` → `#151729` → `#fafaff`.

- App layout: a white sidebar (about 248px) with a hairline right edge, a sticky top bar, then a 1180px content column with 16–22px gaps.
- KPI cards sit in an auto-fit grid (min 180–260px); each card: label top-left, change chip top-right, figure, then a sparkline with date ticks.
- Sections separate by space and hairlines only; no coloured bands.
- Everything is left-aligned in the app; centred text only in empty states.

## Elevation & Depth

| Token | Shadow |
|---|---|
| `--shadow-xs` | `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` |
| `--shadow-sm` | `rgba(255, 255, 255, 0.9) 0px 0px 0px 2px, rgba(76, 52, 129, 0.18) 0px 2px 6px 0px` |
| `--shadow-md` | `rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(76, 52, 129, 0.094) 0px 2px 7px 0px` |
| `--shadow-lg` | `rgba(36, 32, 74, 0.016) 0px 3px 8px 0px` |
| `--shadow-xl` | `rgba(255, 255, 255, 0.28) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset, rgba(184, 51, 106, 0.12) 0px 2px 3px 0px, rgba(184, 51, 106, 0.36) 0px 5px 12px -5px` |
| `--shadow-2xl` | `rgba(76, 52, 129, 0.07) 0px 6px 20px 0px, rgba(76, 52, 129, 0.05) 0px 2px 6px 0px` |
| `--shadow-ring` | `rgba(0, 0, 0, 0.03) 0px 0px 0px 1px` |

Effects: `filter: grayscale(1)`, `filter: grayscale(1) brightness(0.55) contrast(1.1)`, `filter: invert(0.36) sepia(0.82) saturate(19.95) hue-rotate(228deg) brightness(0.98) contrast(0.95)`, `filter: blur(60px)`.

- Cards, buttons and inputs are flat: a 1px `{colors.border}` and no shadow.
- Only things that float above the page get a shadow: menus, toasts and dialogs use `--shadow-2xl` (a faint plum tint).
- Hover is a colour change (`{colors.surface-subtle}` behind rows, a darker rose on the primary button), never a lift.

## Shapes

Radius scale: `{rounded.xs}` 2px, `{rounded.sm}` 4px, `{rounded.md}` 6px, `{rounded.lg}` 8px, `{rounded.xl}` 10px, `{rounded.2xl}` 12px, `{rounded.3xl}` 20px, `{rounded.full}` pill. Borders: 1px in `#ece7f0`.

## Components

### Buttons

- **primary** (“Get 14 Days Free”, ×7): `#4d3df5`, text `#ffffff`, 12px corners, 42px tall, padding 10/16/10/16, 14px weight 500, shadow `rgba(255, 255, 255, 0.28) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset, rgba(77, 61, 245, 0.12) 0px 2px 3px 0px, rgba(77, 61, 245, 0.36) 0px 5px 12px -5px`. Hover: a shadow. Focus: `2px solid rgb(77, 61, 245)`.
- **primary** (“Get Started”, ×4): `#4d3df5`, text `#ffffff`, 12px corners, 47px tall, padding 12/95/12/95, 15px weight 500, shadow `rgba(255, 255, 255, 0.28) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset, rgba(77, 61, 245, 0.12) 0px 2px 3px 0px, rgba(77, 61, 245, 0.36) 0px 5px 12px -5px`.
- **primary** (“Book a Demo”, ×3): `#4d3df5`, text `#ffffff`, 14px corners, 59px tall, padding 16/26/16/26, 16px weight 500, shadow `rgba(255, 255, 255, 0.28) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset, rgba(77, 61, 245, 0.12) 0px 2px 3px 0px, rgba(77, 61, 245, 0.36) 0px 5px 12px -5px`. Hover: a shadow. Focus: `2px solid rgb(77, 61, 245)`.
- **secondary** (“See how it works”, ×3): `#ffffff` with a 1px `#d8d5ee` border, text `#0b0b18`, 14px corners, 59px tall, padding 16/27/16/27, 16px weight 500. Hover: no visible change. Focus: `1px auto rgb(16, 16, 16)`.
- **secondary** (“Contact Sales”, ×2): `#ffffff` with a 1px `#d8d5ee` border, text `#0b0b18`, 12px corners, 49px tall, padding 12/97/12/97, 15px weight 500. Hover: no visible change. Focus: `1px auto rgb(16, 16, 16)`.
- **secondary** (“Select your region”, ×2): `#f8fafc` with a 1px `#d1d5db` border, text `#1e293b`, 9px corners, 36px tall, padding 8/13/8/13, 14px weight 400, shadow `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px`. Hover: no visible change. Focus: `1px auto rgb(16, 16, 16)`.

### Inputs

- `#f8fafc`, 1px `#d1d5db` border, 9px corners, 36px tall, placeholder `#6b7280`; focus `2px solid rgba(0, 0, 0, 0)` and `rgb(77, 61, 245) 0px 0px 0px 1px, rgba(0, 0, 0, 0.05) 0px 1px 2px 0px`.

### Cards

- ×5: `#ffffff` on `#fafaff`, 1px `#e8e6f5` border, 20px corners, 28px padding, shadow `rgba(70, 60, 180, 0.07) 0px 6px 20px 0px, rgba(70, 60, 180, 0.05) 0px 2px 6px 0px`.
- ×4: no fill on `#fafaff`, 1px `#e1e5f2` border, 16px corners, 25px padding.
- ×4: `#ffffff` on `#fafbff`, 1px `#e5e8f1` border, 11px corners, 12px padding.

### Navigation

69px tall, sticky, transparent.

### Badges

- “L3”: `#ede9fe`, text `#7c3aed`, 4px corners, 9.5px.
- “96% match”: `#f3f0ff`, text `#7c70b0`, 3px corners, 7px.

### Links

- standalone: `#1a1a2e`, no underline; hover `#1a1a2e`.
- standalone: `{colors.link}`, no underline; hover underline.

- **KPI card**: `{colors.surface}`, 14px corners, 1px `{colors.border}`, 20px padding; label `{typography.caption}` in `{colors.text-muted}`; change chip as a pill; figure in JetBrains Mono ~26px; sparkline as a 2px `{colors.primary}` line over a 10% tint fill, axis dates in `{colors.text-subtle}`.
- **Sidebar nav item**: 40px tall, 10px corners, icon + label in `{colors.text-muted}`; active = `{colors.primary-tint}` fill with `{colors.primary}` text and a filled dot; counts as small grey pills.
- **Tabs**: text tabs with a 2px `{colors.primary}` underline on the active one.
- **Segmented control**: `{colors.surface-subtle}` track; the active segment is white with `{colors.primary}` text (range pickers) or `{colors.surface-inverse}` (filters).
- **Discord preview**: drafts keep the dark Discord look so they match what will post; it is the only dark surface.

## Do's and Don'ts

### Do

- Use the tokens for every colour, size, space, radius and shadow. If a value is missing, add a token; don't hard-code it.
- Keep `{colors.primary}` for the one main action on a screen.
- Headings in `{colors.heading}`, running text in `{colors.text}`.
- Keep the page white and let hairlines do the separating.
- Use rose for one action and one highlight per view; use indigo for the rest of the emphasis.
- Put every important number in JetBrains Mono.
- Show change as tinted pills with ▲/▼.
- Use 10px corners on controls and 14px on cards.

### Don't

- Don't use cruva.com's logo, illustrations, photos, icons or copy. Draw your own.
- Don't copy Cruva's indigo `#4c3df5`, its glows or its lavender page: the structure is measured, the look is ours.
- Don't add gradients, glow shadows or heavy bold type.
- Don't put two filled rose buttons side by side.
- Don't use `{colors.text-subtle}` for anything someone has to read.

## Motion

`--duration-fast` 150ms, `--duration-base` 200ms, `--duration-slow` 800ms; easing `--ease-standard` `ease`, `--ease-alt-1` `cubic-bezier(0.4, 0, 0.2, 1)`. Transitions animate color, transform, border-color, box-shadow, opacity, background. The site respects `prefers-reduced-motion`; so should you.

## Iconography & Graphics

- Icons: line icons, strokes ≈ 1.75px at a 24px grid, round caps, round joins, drawn at 11px/15px/12px/14px (by size: 11px line 2.42px, 15px line 1.75px, 12px line 1.75px, 14px line 2.75px). They take the text colour (`currentColor`). See `design-system/source/screens/icons.png`.
- Chart colours, in order: `{colors.chart-1}` `#b8336a`, `{colors.chart-2}` `#4c3481`, `{colors.chart-3}` `#a99bb5` (`--color-chart-<n>`; the first is the highlight, the rest are context or more series). Gridlines in `#ece7f0`, labels in `#6e6678`.
- Icons: outline, about 1.75px at 24px, round caps and joins, in `{colors.text-muted}` (or `{colors.primary}` when active). No filled or duotone icons.
- Charts: area sparklines, 2px lines, 10% tint fills, `{colors.border}` gridlines; series order rose, indigo, lilac grey.
- Decoration is minimal: small numbered discs in `{colors.accent-tint}`, no illustrations, no 3D, no photos in the UI.

## Responsive Behavior

- Breakpoints: sm 521px, md 641px, lg 761px, xl 881px, 2xl 1001px (desktop-first (max-width queries)).
- On phones: display 72→40px, h1 56→35.1px, h3 34→25px, h4 26→20px.

## Known Gaps

- The site looks the same with dark mode on, so there's no dark theme to extract (it may switch with a toggle instead; see css.darkSelectors).
- The CSS has dark-mode selectors (.dark) but the page didn't switch with the system setting: dark mode is a toggle, or a class for dark sections only. Check the screenshots before adding a dark theme.
- Hover and focus states were measured on the most common buttons, links and fields only.
- The logged-in Cruva dashboard was seen in one screenshot (Dashboard → Analytics), not measured in a browser: tables, forms and dialogs there are unconfirmed.
- Montserrat and Poppins are TVC's choices, not measured; the type sizes are Cruva's measured scale.

## Files

- `design-system/tokens.css`: every token as a CSS custom property. Import it once, globally.
- `design-system/theme.css`: the same tokens as a Tailwind CSS v4 theme (`@import` it after Tailwind).
- `design-system/design.tokens.json`: W3C Design Tokens (2025.10) for Figma plugins, Style Dictionary or Terrazzo.
- `design-system/roles.json`: the choices behind the names. Change it and run `extract.mjs --rebuild`.
- `design-system/preview.html`: every token, a sample page built only from them, and the real site's screenshots.
