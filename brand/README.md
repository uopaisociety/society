# AI Society brand

Use **AI Society** in everyday copy, **University of Portsmouth AI Society** on formal materials, and **@uopaisociety** for the social handle. The society tagline is **GOOD IDEAS *BELONG HERE.***

## Visual identity

| Token | Colour | Use |
| --- | --- | --- |
| `marine-deep` | `#06283F` | Deep shadows in the marine mesh |
| `marine-navy` | `#073B5C` | Main blue, text and marks on cream |
| `slate-blue` | `#668998` | Soft blue highlights in the mesh |
| `cream` | `#F7F5F0` | Light end of the gradient, text and marks on navy |

The social pack uses three grainy backgrounds. **Marine** uses broad cream-tinted highlights over navy for bold headlines and opening slides. **Hybrid** follows the approved diagonal curve, with cream widening toward the lower right. On the carousel closing slide the same curve rotates toward the bottom to leave room for logistics. **Cream** uses a slate wash behind screenshots and information-heavy layouts. Use navy lettering on cream and cream lettering on marine, with the gradient transition clear of small text.

- **Headlines** use Inter Tight at 700 or 800 with −0.03em tracking. Use an italic accent line when it reads naturally.
- **Metadata** uses JetBrains Mono. Set times in 24-hour UK format.
- **Body copy** uses Inter at 400, 500 or 600. Keep it short enough to read at feed size.
- **Spacing** uses an 8 px base unit, 1.5 px hairlines and 2 px screenshot borders. See [tokens.json](tokens.json) for treatments, grain settings and per-format safe insets. Each template embeds its gradient and logo so it can render on its own. For editable examples of each background, open the WhatsApp reminder (marine), announcement (hybrid) or showcase (cream).

## Logos

| Asset | Use |
| --- | --- |
| [Wave mark](logos/logo-mark.svg) | Compact placements on dark surfaces |
| [Stacked logo](logos/logo-stacked.svg) | Standard signature on dark surfaces |
| [University lockup](logos/logo-lockup-uop.svg) | Formal event artwork and partnership material on dark surfaces |

The SVGs use the original wave-mark and lettering outlines. Give the logo breathing room and keep its proportions. The marine-navy [stacked logo](logo.svg) and [university lockup](lockup-uop.svg) are available for light backgrounds. Use the original [textured avatar](avatar-textured.svg) for profile pictures and the original [marine gradient](background.svg) where earlier collateral calls for it.

## WhatsApp

| Delivery | Template | Size | Treatment |
| --- | --- | --- | --- |
| Announce a workshop, collaboration or sign-up | [Announcement](templates/whatsapp-banner-2x1.svg) | 1600 × 800 | Hybrid |
| Send a day-of reminder or room change | [Reminder](templates/whatsapp-reminder-2x1.svg) | 1600 × 800 | Marine |
| Share a demo, member project or event recap | [Showcase](templates/whatsapp-showcase-2x1.svg) | 1600 × 800 | Cream |
| Cross-post a compact graphic | [Square announcement](templates/ig-post-square-1x1.svg) | 1080 × 1080 | Marine |
| Post to Status | [Story and Status](templates/ig-story-status-9x16.svg) | 1080 × 1920 | Marine |

Pair a chat graphic with short message copy and one tappable link or poll. For reminders, put the time and room in the message too.

## Instagram

| Delivery | Template | Size | Treatment |
| --- | --- | --- | --- |
| Standalone event or recruitment post | [Portrait event post](templates/ig-post-event-4x5.svg) | 1080 × 1350 | Cream |
| Short announcement or cross-post | [Square announcement](templates/ig-post-square-1x1.svg) | 1080 × 1080 | Marine |
| Story or vertical reminder | [Story and Status](templates/ig-story-status-9x16.svg) | 1080 × 1920 | Marine |
| Carousel opening hook | [01 · Hook](templates/ig-carousel-01-hook-4x5.svg) | 1080 × 1350 | Marine |
| Carousel screenshot or photo | [02 · Showcase](templates/ig-carousel-02-screen-4x5.svg) | 1080 × 1350 | Cream |
| Carousel agenda, highlights or prompts | [03 · Grid](templates/ig-carousel-03-grid-4x5.svg) | 1080 × 1350 | Cream |
| Carousel logistics and next step | [04 · CTA](templates/ig-carousel-04-cta-4x5.svg) | 1080 × 1350 | Hybrid |

Build a carousel with the hook first, the showcase or grid slides that fit the story, and one closing CTA. Use the portrait event post when a single image can carry the essential details. On Stories, keep text in the central area and add the link sticker in the app. The vertical template leaves 300 px at the top and bottom as working margins. Preview the final placement with the app controls visible.

## Other formats

| Delivery | Template | Size | Treatment |
| --- | --- | --- | --- |
| Luma event cover or presentation title slide | [Luma cover](templates/luma-cover-16x9.svg) | 1920 × 1080 | Marine |
| LinkedIn, GitHub or Open Graph link preview | [Social preview](templates/social-og-card.svg) | 2400 × 1256 | Hybrid |
| Students’ Union society page header | [UPSU header](templates/upsu-header.svg) | 1640 × 856 | Cream |

Fill the slots that suit the post and clear unused placeholders. For events, use the confirmed date, time, venue and direct link from the Luma listing. For demos, use the playable project link where available.

## Edit SVG slots

1. Copy the template to a campaign working file. Keep the root dimensions and `viewBox` so the output matches the platform.
2. Locate a text slot by its unique `id="slot-…"` or its corresponding `data-slot`. Change the element’s text content, keep it on one line and follow the nearby character limit. Use the numbered headline slots for separate lines. Keep the italic accent line short. XML-escape `&` and `<` when editing by hand.
3. On a showcase, set the `href` of `image#slot-screenshot` to a PNG or JPEG data URI (up to 1 MB decoded) and update its `aria-label`. Use the same crop as the frame. Keep `frame-clip`, the border and `preserveAspectRatio` intact. Use a screenshot of the actual project or demo. Hide `screenshot-placeholder` when using a transparent image so its guide does not show through.
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
