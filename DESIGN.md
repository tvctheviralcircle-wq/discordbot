---
version: alpha
name: "cruva.com-inspired"
description: "A design system measured from cruva.com on 2026-11-07. Inspired by it, not affiliated with it."
colors:
  background: "#fafaff"
  text: "#1a1a2e"
  heading: "#0b0b18"
  text-muted: "#5b5b73"
  text-subtle: "#8a8aa3"
  border: "#e8e6f5"
  surface: "#ffffff"
  primary: "#4c3df5"
  primary-foreground: "#ffffff"
  link: "#4c3df5"
  focus: "#4d3df5"
  success: "#16a34a"
  surface-inverse: "#0b0b18"
  surface-inverse-foreground: "#ffffff"
  chart-1: "#4c3df5"
  chart-2: "#348c6d"
  chart-3: "#7c70b0"
typography:
  display:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -0.035em
  h1:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.04em
  h2:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.028em
  h3:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.025em
  h4:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.028em
  h5:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.02em
  body-lg:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 15.5px
    fontWeight: 400
    lineHeight: 1.7
  body-sm:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
  caption:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
    fontSize: 14.5px
    fontWeight: 400
    lineHeight: 1.6
  code:
    fontFamily: "\"JetBrains Mono\", ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.55
  overline:
    fontFamily: "\"Geist\", ui-sans-serif, system-ui, sans-serif"
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
    rounded: "{rounded.2xl}"
    padding: "10px 16px"
    height: 42px
  button-secondary:
    backgroundColor: "#ffffff"
    textColor: "{colors.heading}"
    rounded: 14px
    padding: "16px 27px"
    height: 59px
  button-subtle:
    backgroundColor: "#ffffff99"
    textColor: "{colors.heading}"
    rounded: "{rounded.2xl}"
    padding: "14px 21px"
    height: 52px
  button-subtle-hover:
    backgroundColor: "#ffffff"
  card:
    backgroundColor: "#ffffff"
    textColor: "{colors.text}"
    rounded: "{rounded.3xl}"
    padding: 28px
  input:
    backgroundColor: "{colors.background}"
    textColor: "#1e293b"
    typography: "{typography.caption}"
    rounded: 9px
    padding: "4px 12px"
    height: 36px
  badge:
    backgroundColor: "#ede9fe"
    textColor: "#7c3aed"
    rounded: "{rounded.sm}"
    padding: "2px 5px"
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

# cruva.com-inspired design system

> Measured from https://cruva.com on 2026-11-07: 12 page visits (/, /case-studies, /blog, /pricing, /demo, /workflows, /meta-ads-programs, /full-pipeline-crm) at 1440px and 390px. The values are what the browser rendered. The names and the prose are judgment: check them against the screenshots in `design-system/source/screens/`. Inspired by cruva.com, not affiliated with it: never use its logo, illustrations, photos or words.

## Overview

A light, airy SaaS interface: near-black type on a lavender-tinted white (`{colors.background}`), white cards with hairline lilac borders and soft 20px corners. Almost everything is neutral, so the single indigo (`{colors.primary}`) carries every call to action, the highlighted words in a headline, and the line icons. The bold thing is the headline: centred, 56–72px, weight 500–600 with very tight tracking (-0.035 to -0.04em), often with one phrase picked out in indigo. Numbers that matter (prices, live counts, “3,000+”) switch to JetBrains Mono, so data reads as data. One dark band (`#151729`, a navy with a faint indigo glow) breaks up the long home page for social proof.

What was measured: a light interface on `#fafaff`, headings in `#0b0b18`, body text in `#1a1a2e`, and `#4c3df5` for the main action. Type is Geist and JetBrains Mono. Space runs on a 4px grid. Corners are 2px, 4px, 6px, 8px, 10px, 12px, 20px, and pills where the site uses them.

## Colors

| Token | Value | Use it for | On background |
|---|---|---|---|
| `{colors.background}` | `#fafaff` | the page background on most pages | 1:1 |
| `{colors.text}` | `#1a1a2e` | body copy (paragraphs and lists) | 16.39:1 |
| `{colors.heading}` | `#0b0b18` | headings (h1–h6) | 18.77:1 |
| `{colors.text-muted}` | `#5b5b73` | 21% of text: secondary copy | 6.33:1 |
| `{colors.text-subtle}` | `#8a8aa3` | 6% of text: the quietest copy | 3.23:1 |
| `{colors.border}` | `#e8e6f5` | the most used border colour (by length) | 1.18:1 |
| `{colors.surface}` | `#ffffff` | panels and sections a step off the background | 1.04:1 |
| `{colors.primary}` | `#4c3df5` | the main buttons on the page you gave | 6.13:1 |
| `{colors.primary-foreground}` | `#ffffff` | text on primary buttons | 1.04:1 |
| `{colors.link}` | `#4c3df5` | links in running text | 6.13:1 |
| `{colors.focus}` | `#4d3df5` | the :focus-visible ring | 6.11:1 |
| `{colors.success}` | `#16a34a` | small positive tags only (“10% off”, upward deltas) as text on a pale green tint; never for body copy (3.17:1) | 3.17:1 |
| `{colors.surface-inverse}` | `#0b0b18` | the selected state of a segmented control (the active “Monthly” pill) and other small selected chips | 18.77:1 |
| `{colors.surface-inverse-foreground}` | `#ffffff` | text on `{colors.surface-inverse}` |  1.04:1 |

The full palette (48 colours, most used first) is in `design-system/tokens.css` as `--color-<name>`: neutral-50 `#fafaff` (42.8%), slate-950 `#1a1a2e` (10.7%), slate-700 `#5b5b73` (7.4%), slate-950-2 `#0b0b18` (6.3%), neutral-100 `#e8e6f5` (9.1%), indigo-700 `#4c3df5` (3.9%), slate-500 `#8a8aa3` (2.5%), slate-950-3 `#20243b` (2.2%), indigo-600 `#6657df` (0.9%), white-a85 `#ffffffd9` (0.7%), ….

Gradients the site paints: `linear-gradient(rgb(248, 247, 255), rgb(244, 243, 255) 60%, rgb(248, 247, 255))`; `linear-gradient(rgb(232, 230, 245) 1px, rgba(0, 0, 0, 0) 1px), linear-gradient(90deg, rgb(232, 230, 245) 1px, rgba(0, 0, 0, 0) 1px)`; `linear-gradient(rgb(247, 246, 255) 0%, rgb(250, 251, 254) 100%)`.

- `{colors.primary}` is the only saturated colour in the UI: the main button, the active link, focus rings, icons in feature lists, and one highlighted phrase per headline. Keep it to one filled button per view; the second action is the white outline button.
- `{colors.background}` is the page; `{colors.surface}` (white) is for cards and panels that sit on it. Don't swap them: white pages with lavender cards look wrong.
- `{colors.heading}` for headlines and big numbers, `{colors.text}` for running copy, `{colors.text-muted}` for card descriptions and sub-heads. `{colors.text-subtle}` fails AA for body text: use it only for captions, timestamps and placeholder-level copy.
- `{colors.border}` for every hairline: card edges, dividers, the faint background grid.
- Tints of the primary (`#f4f3ff`, `#ede9fe`) fill eyebrow pills and badges; the primary itself stays for text and icons on them.

## Typography

- **sans**: Geist (free). Stack: `"Geist", ui-sans-serif, system-ui, sans-serif`
- **mono**: JetBrains Mono (free). Stack: `"JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace`

| Token | Size | Phone | Line height | Tracking | Weight | Font |
|---|---|---|---|---|---|---|
| `{typography.display}` | 72px | 40px | 1.05 | -0.035em | 600 | sans |
| `{typography.h1}` | 56px | 35.1px | 1.1 | -0.04em | 500 | sans |
| `{typography.h2}` | 44px | same | 1.1 | -0.028em | 600 | sans |
| `{typography.h3}` | 34px | 25px | 1.12 | -0.025em | 600 | sans |
| `{typography.h4}` | 26px | 20px | 1.25 | -0.028em | 600 | sans |
| `{typography.h5}` | 19px | same | 1.25 | -0.02em | 600 | sans |
| `{typography.body-lg}` | 18px | same | 1.55 | 0 | 400 | sans |
| `{typography.body}` | 15.5px | same | 1.7 | 0 | 400 | sans |
| `{typography.body-sm}` | 15px | same | 1.65 | 0 | 400 | sans |
| `{typography.caption}` | 14.5px | same | 1.6 | 0 | 400 | sans |
| `{typography.code}` | 11px | same | 1.55 | 0 | 400 | mono |
| `{typography.overline}` | 9.5px | same | 1.55 | 0.04em | 400, uppercase | sans |

Weights in use: 400 (67.2%), 500 (15.7%), 600 (13.8%), 450 (1.8%), 700 (1%). Steps grow by about ×1.286.

- Headlines are sentence case, centred in heroes, weight 500–600 with tight negative tracking; they end with a full stop (“Plans built around your affiliate growth stage.”). Never bold 700 at display sizes.
- Body copy is weight 400 with generous line height (1.6–1.7) and a short measure (about 60–70 characters in heroes).
- Eyebrows above section titles are small uppercase labels with +0.04em tracking inside a lavender pill, led by a small indigo dot.
- Figures that are the point of a block (prices, GMV counters, stats) use `{typography.code}`'s family, JetBrains Mono, at heading sizes; labels next to them stay in Geist.

## Layout

- Grid: none clear (spaces are loose; 4px is the nearest). Spacing steps: 2px, 3px, 4px, 5px, 6px, 7px, 8px, 9px, 10px, 12px, 14px, 16px, 18px, 20px, 22px, 24px, 28px, 32px (`--space-<n>`, where n × 4 = px).
- Sections: 80px or 60px of vertical padding on desktop, 40px or 56px on phones.
- Content width: page 1240px, wide 1176px, narrow 760px (`--container-<name>`).
- Grids: 2 columns, 3 columns, 5 columns, 4 columns.
- The home page alternates bands: `#fafaff` → `#151729` → `#fafaff`.

- Lots of air: 80px between sections on desktop, and heroes with roughly 120px above the headline.
- Sections are separated by space alone, except one full-width dark band; there are no rules between sections.
- Heroes and section intros are centred; the content inside cards is left-aligned.
- Some hero areas sit on a faint 1px lilac grid (`#e8e6f5` lines) with a soft violet glow in one corner.

## Elevation & Depth

| Token | Shadow |
|---|---|
| `--shadow-xs` | `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` |
| `--shadow-sm` | `rgba(255, 255, 255, 0.9) 0px 0px 0px 2px, rgba(70, 60, 180, 0.18) 0px 2px 6px 0px` |
| `--shadow-md` | `rgba(255, 255, 255, 0.6) 0px 1px 0px 0px inset, rgba(185, 128, 24, 0.094) 0px 2px 7px 0px` |
| `--shadow-lg` | `rgba(36, 32, 74, 0.016) 0px 3px 8px 0px` |
| `--shadow-xl` | `rgba(255, 255, 255, 0.28) 0px 1px 0px 0px inset, rgba(255, 255, 255, 0.12) 0px 0px 0px 1px inset, rgba(77, 61, 245, 0.12) 0px 2px 3px 0px, rgba(77, 61, 245, 0.36) 0px 5px 12px -5px` |
| `--shadow-2xl` | `rgba(70, 60, 180, 0.07) 0px 6px 20px 0px, rgba(70, 60, 180, 0.05) 0px 2px 6px 0px` |
| `--shadow-ring` | `rgba(0, 0, 0, 0.03) 0px 0px 0px 1px` |

Effects: `filter: grayscale(1)`, `filter: grayscale(1) brightness(0.55) contrast(1.1)`, `filter: invert(0.36) sepia(0.82) saturate(19.95) hue-rotate(228deg) brightness(0.98) contrast(0.95)`, `filter: blur(60px)`.

- Cards lift very slightly: a hairline border plus `--shadow-2xl`, a soft indigo-tinted shadow. They never cast hard or grey shadows.
- The primary button has its own glow (`--shadow-xl`, an indigo drop with an inner highlight); outline buttons and inputs stay flat.
- The highlighted pricing card is marked by a primary border and a “MOST POPULAR” pill in `{colors.primary}`, not by a bigger shadow.

## Shapes

Radius scale: `{rounded.xs}` 2px, `{rounded.sm}` 4px, `{rounded.md}` 6px, `{rounded.lg}` 8px, `{rounded.xl}` 10px, `{rounded.2xl}` 12px, `{rounded.3xl}` 20px, `{rounded.full}` pill. Borders: 1px in `#e8e6f5`.

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
- standalone: `#4c3df5`, no underline; hover `#4c3df5`.

- **Eyebrow pill**: `{rounded.full}`, `#f4f3ff` fill, 1px `{colors.border}`, an indigo dot, then an uppercase `{typography.overline}`-style label in `{colors.primary}`.
- **Stat card**: a white `{colors.surface}` card, label in `{typography.h4}` weight 500 on the left, the number in JetBrains Mono at display size in `{colors.heading}` on the right, with a faint lavender gradient wash toward one edge.
- **Pricing card**: white, 20px corners, plan name `{typography.h5}`, description in `{colors.text-muted}`, price in JetBrains Mono, a 1px divider, then a checklist with small indigo check icons. The featured plan gets a 1px `{colors.primary}` border and a pill above it.
- **Segmented control**: a white pill track; the selected segment is `{colors.surface-inverse}` with white text; unselected segments are plain text with an optional `{colors.success}` discount tag.
- **Logo wall**: customer logos rendered in greyscale at a single height, in one row.

## Do's and Don'ts

### Do

- Use the tokens for every colour, size, space, radius and shadow. If a value is missing, add a token; don't hard-code it.
- Keep `{colors.primary}` for the one main action on a screen.
- Headings in `{colors.heading}`, running text in `{colors.text}`.
- Centre hero headlines and pick out one phrase in `{colors.primary}`.
- Put key numbers in JetBrains Mono.
- Use white cards with 1px lilac borders and 20px corners on the lavender page.
- Pair one filled primary button with one white outline button.
- Label sections with an eyebrow pill above the title.

### Don't

- Don't use cruva.com's logo, illustrations, photos, icons or copy. Draw your own.
- Don't add a second saturated colour for actions; green and amber appear only in tiny tags and star ratings.
- Don't use grey drop shadows or heavy elevation; shadows are indigo-tinted and faint.
- Don't set headlines in weight 700 or with default tracking.
- Don't put body copy in `{colors.text-subtle}`.
- Don't use sharp corners on cards or buttons (minimum 8px on anything clickable).

## Motion

`--duration-fast` 150ms, `--duration-base` 200ms, `--duration-slow` 800ms; easing `--ease-standard` `ease`, `--ease-alt-1` `cubic-bezier(0.4, 0, 0.2, 1)`. Transitions animate color, transform, border-color, box-shadow, opacity, background. The site respects `prefers-reduced-motion`; so should you.

## Iconography & Graphics

- Icons: line icons, strokes ≈ 1.75px at a 24px grid, round caps, round joins, drawn at 11px/15px/12px/14px (by size: 11px line 2.42px, 15px line 1.75px, 12px line 1.75px, 14px line 2.75px). They take the text colour (`currentColor`). See `design-system/source/screens/icons.png`.
- Chart colours, in order: `{colors.chart-1}` `#4c3df5`, `{colors.chart-2}` `#348c6d`, `{colors.chart-3}` `#7c70b0` (`--color-chart-<n>`; the first is the highlight, the rest are context or more series). Gridlines in `#e8e6f5`, labels in `#5b5b73`.
- Icons are outline only, about 1.75px at 24px, round caps and joins, slightly rounded rectangles; usually in `{colors.primary}` in feature lists and in `{colors.text-subtle}` when decorative. No filled or duotone icons.
- Decoration is soft and abstract: a faint square grid, blurred violet/indigo radial glows (`filter: blur(60px)`), gentle lavender gradients. No 3D, isometric scenes or stock illustration.
- Product UI shown as clean white cards rather than screenshots with chrome. Charts use the chart colours with `{colors.border}` gridlines.

## Responsive Behavior

- Breakpoints: sm 521px, md 641px, lg 761px, xl 881px, 2xl 1001px (desktop-first (max-width queries)).
- On phones: display 72→40px, h1 56→35.1px, h3 34→25px, h4 26→20px.

## Known Gaps

- The site looks the same with dark mode on, so there's no dark theme to extract (it may switch with a toggle instead; see css.darkSelectors).
- The CSS has dark-mode selectors (.dark) but the page didn't switch with the system setting: dark mode is a toggle, or a class for dark sections only. Check the screenshots before adding a dark theme.
- Hover and focus states were measured on the most common buttons, links and fields only.
- This measures Cruva's public marketing site. The logged-in Cruva dashboard (behind sign-in) couldn't be measured; it likely shares these tokens, but table, sidebar and form styles there are unconfirmed.
- The dark band on the home page is a section style, not a dark theme.

## Files

- `design-system/tokens.css`: every token as a CSS custom property. Import it once, globally.
- `design-system/theme.css`: the same tokens as a Tailwind CSS v4 theme (`@import` it after Tailwind).
- `design-system/design.tokens.json`: W3C Design Tokens (2025.10) for Figma plugins, Style Dictionary or Terrazzo.
- `design-system/roles.json`: the choices behind the names. Change it and run `extract.mjs --rebuild`.
- `design-system/preview.html`: every token, a sample page built only from them, and the real site's screenshots.
