# AI Society brand

Use **AI Society** in everyday copy, **University of Portsmouth AI Society** on formal materials, and **@uopaisociety** for the social handle. The tagline is **GOOD IDEAS *BELONG* HERE.** Set GOOD IDEAS and HERE. in upright bold off-white and BELONG in bold italic frosted steel.

## Visual identity

| Role | Tokens | Use |
| --- | --- | --- |
| 85% atmospheric navy | `bg-abyss` `#062338`, `bg-petrol` `#0B3550`, `bg-glow` `#1E5678` | Deep edges, main surface and directional glow |
| 10% neutral contrast | `fg-white` `#F7F6F2`, `fg-steel` `#B8CAD6`, `surface-chalk` `#F2F5F7`, `border-subtle` `rgba(184, 202, 214, 0.22)` | Headlines, italic emphasis, cool chalk screenshot slides and hairlines |
| 5% accents | `accent-amber` `#FFC83D`, `accent-cyan` `#38BDF8` | Small event or technical accents |

Use the proportions as a visual guide across a campaign. A full chalk showcase slide gives the screenshot room within a mostly navy carousel. Keep the accent colours away from full surfaces.

- **Headlines** use Inter Tight at 700 or 800 with −0.03em tracking. Use uppercase and a single italic steel line where emphasis helps.
- **Metadata** uses JetBrains Mono. Set times in 24-hour UK format.
- **Body copy** uses Inter at 400, 500 or 600. Keep it short enough to read at feed size.
- **Backgrounds** combine a petrol-navy radial gradient, a lower glow and 4% SVG grain. Keep text and the logo on separate layers above the grain.
- **Spacing** uses an 8 px base unit, 1.5 px hairlines and 2 px screenshot borders. Per-format safe insets and the other source values are in [tokens.json](tokens.json). SVGs carry local copies of the token values for independent rendering. Update both when changing the system.

## Logos

| Asset | Use |
| --- | --- |
| [Wave mark](logos/logo-mark.svg) | Compact placements on dark surfaces |
| [Stacked logo](logos/logo-stacked.svg) | Standard signature on dark surfaces |
| [University lockup](logos/logo-lockup-uop.svg) | Formal event artwork and partnership material on dark surfaces |

The SVGs use the original wave-mark and lettering outlines. Give the logo breathing room and keep its proportions. The marine-navy [stacked logo](logo.svg) and [university lockup](lockup-uop.svg) are available for light backgrounds. Use the original [textured avatar](avatar-textured.svg) for profile pictures and the original [marine gradient](background.svg) where earlier collateral calls for it.

## Templates

| Template | Size | Use |
| --- | --- | --- |
| [WhatsApp banner](templates/whatsapp-banner-2x1.svg) | 1600 × 800 | Announcement or reminder with one CTA |
| [WhatsApp showcase](templates/whatsapp-showcase-2x1.svg) | 1600 × 800 | Copy and a playable demo screenshot |
| [Instagram 01 · Hook](templates/ig-carousel-01-hook-4x5.svg) | 1080 × 1350 | Open with one clear idea |
| [Instagram 02 · Screenshot](templates/ig-carousel-02-screen-4x5.svg) | 1080 × 1350 | Show the product or game on cool chalk |
| [Instagram 03 · Grid](templates/ig-carousel-03-grid-4x5.svg) | 1080 × 1350 | Four prompts, features or tracks |
| [Instagram 04 · CTA](templates/ig-carousel-04-cta-4x5.svg) | 1080 × 1350 | Date, logistics and action with the university lockup |
| [Luma cover](templates/luma-cover-16x9.svg) | 1920 × 1080 | Event cover or presentation title slide |
| [Social OG card](templates/social-og-card.svg) | 2400 × 1256 | Open Graph, LinkedIn and GitHub link previews |
| [UPSU header](templates/upsu-header.svg) | 1640 × 856 | Centred tagline and logo for variable header crops |

The sample copy uses Flappy AI Jam. Its screenshot slots contain a rendered frame from the [Flappy AI Jam starter](https://github.com/uopaisociety/flappy-ai-jam/blob/main/index.html). Replace event details from the canonical Luma listing before publication. Use the playable GitHub Pages URL for demos. The sample registration URL points to the society’s Luma profile and the optional room and time slots are blank.

## Edit SVG slots

1. Copy the template to a campaign working file. Keep the root dimensions and `viewBox` so the output matches the platform.
2. Locate a text slot by its unique `id="slot-…"` or its corresponding `data-slot`. Change the element’s text content, keep it on one line and follow the nearby character limit. Use the numbered headline slots for separate lines. Keep the italic accent line short. XML-escape `&` and `<` when editing by hand.
3. On a showcase, replace the `href` of `image#slot-screenshot` with a PNG or JPEG data URI (up to 1 MB decoded) and update its `aria-label`. Use the same crop as the frame. Keep `frame-clip`, the border and `preserveAspectRatio` intact. Use a screenshot of the actual demo.
4. Update the root `title` and `desc` to match the finished artwork. Render at the exact target size and inspect the text, screenshot crop, contrast and platform safe area. Shorten text that exceeds its space, including wide characters within the suggested limit. Preview the UPSU upload on mobile and desktop because the viewport crop can vary.
5. Keep a usable CTA in the accompanying post. URLs rendered into PNG artwork are plain text.

## Render a PNG

Run from the repository root. Use the dimensions of the chosen template. Install Inter Tight, Inter and JetBrains Mono locally for resvg to use the specified fonts. SVGs also declare fallback families.

```bash
mkdir -p out
npx --yes @resvg/resvg-js-cli@2.6.2-beta.1 --fit-width 1600 \
  brand/templates/whatsapp-banner-2x1.svg out/wa-banner.png
```

Headless Chromium can load the Google Fonts import when network access is available. Install the browser once with `npx playwright install chromium`.

```bash
mkdir -p out
npx playwright screenshot --viewport-size="1600,800" --wait-for-timeout=1500 \
  "file://$(pwd)/brand/templates/whatsapp-banner-2x1.svg" out/wa-banner.png
```

For automated Chromium exports that require exact typography, await `document.fonts.ready` and verify that the intended fonts loaded before capturing. Use local installs when exporting offline. See [AGENTS.md](AGENTS.md) for platform copy and publishing rules.
