# AI Society brand instructions for agents

Read [README.md](README.md) and [tokens.json](tokens.json) before editing social copy or artwork. Use AI Society for short references, University of Portsmouth AI Society on formal materials, and @uopaisociety on social.

## A. Brand Voice & Anti-Slop Copywriting Protocol

- Write like a sharp technical founder or the society president messaging peers. Keep it brief, natural, grounded and direct. Use specific verbs and concrete outcomes.
- Never use “delve”, “unleash”, “revolutionize”, “game-changer”, “thrilled to announce”, “cutting-edge”, “embark”, “realm”, “tapestry”, “supercharge”, “calling all students”, “don't miss out” or “buckle up”.
- Never use em dashes for dramatic pauses. Use periods, commas or line breaks.
- Use at most two functional emojis in a message. The allowed set is 🎮, 👇, 👉, 📍, ⏰ and ⚡.
- Lead with what members build, touch or take home. For example, “You get a plain Flappy Bird and 30 minutes. Prompt a boss fight or webcam controls, then we play every game live on the projector.”

## B. Platform-Specific Rules

### 1. WhatsApp Community (Highest Priority Conversion Channel)

Every major WhatsApp announcement needs a 1600 × 800 (2:1) [banner](templates/whatsapp-banner-2x1.svg) or [showcase](templates/whatsapp-showcase-2x1.svg). Pair it with:

1. A one-line hook that says what is happening and when.
2. Two or three short lines describing what participants do and what they need. Use “No coding needed, just bring a laptop” when that is accurate.
3. A logistics block with 📍 room/building and ⏰ time when the event is within 48 hours.
4. One CTA at the bottom. Use the direct Luma link, a playable GitHub Pages link or a native WhatsApp poll.

| When | Message |
| --- | --- |
| T−7 days | Teaser, 2:1 banner and a native WhatsApp poll |
| T−5 days | Sign-ups open, Luma link, 2:1 banner and prerequisite checklist such as a GitHub account or student AI tools |
| T−2 days | Starter repo or playable teaser with a 2:1 showcase banner using the actual screenshot |
| Day of, T−3 hours | Short reminder with the time, 2:1 banner, location and a charger reminder |

### 2. Instagram (@uopaisociety)

- Use a four- or five-slide 1080 × 1350 carousel from [the Instagram templates](templates/). Alternate atmospheric navy with cool chalk showcase slides containing a real screenshot inside the rounded navy frame.
- Keep to one idea and at most 12 words of editable copy per slide, including logistics and CTA. Shorten the headline or CTA when adding room and time.
- Keep captions under 60 words. Put the hook on line one, follow with two sentences, give the date, time and location, and end with “Sign up via link in bio.”

### 3. LinkedIn (University of Portsmouth AI Society)

Use the 2400 × 1256 [Open Graph card](templates/social-og-card.svg) or 1600 × 800 [showcase banner](templates/whatsapp-showcase-2x1.svg). Write for industry partners, Gradcracker employers and student engineers. Lead with a shipped repo, practical engineering work, an observable workshop outcome or evidence of society activity. Use short paragraphs and one CTA.

### 4. Luma & GitHub Repositories

Luma is canonical for event dates, times, rooms and registration questions. GitHub is canonical for starter code and the live GitHub Pages demo. Before generating social copy or artwork, check that every template agrees on the date, 24-hour UK time, room code and destination URLs. Leave optional template logistics blank until confirmed.

## C. Programmatic SVG-to-PNG Workflow for Agents

Work on a copy. Edit text by `id="slot-…"` or `data-slot` using an XML-aware parser. Keep the text editable, the slot IDs unique and the surrounding transforms and styles intact. Respect the per-slot character limit and check for overflow in the rendered PNG. Update the root title and description. For `slot-screenshot`, replace the image `href` with an embedded PNG or JPEG data URI (up to 1 MB decoded), update the accessible label and retain the rounded `frame-clip` and border.

Run from the repository root. Set the width or viewport to the template’s native dimensions. Use local installs of Inter Tight, Inter and JetBrains Mono with resvg.

```bash
mkdir -p out
npx --yes @resvg/resvg-js-cli@2.6.2-beta.1 --fit-width 1600 \
  brand/templates/whatsapp-banner-2x1.svg out/wa-banner.png
```

For the Chromium path, install the browser with `npx playwright install chromium`. The import requires network access unless the fonts are installed locally.

```bash
mkdir -p out
npx playwright screenshot --viewport-size="1600,800" --wait-for-timeout=1500 \
  "file://$(pwd)/brand/templates/whatsapp-banner-2x1.svg" out/wa-banner.png
```

For scripted browser captures, await `document.fonts.ready` and verify the intended fonts loaded. Inspect the exported PNG for overflow, contrast, screenshot crop and safe-area fit. Compare it against the post and canonical event listing before publishing.
