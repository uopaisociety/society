# AI Society brand instructions for agents

Read [README.md](README.md) and [tokens.json](tokens.json) before editing social copy or artwork. Use AI Society for short references, University of Portsmouth AI Society on formal materials, and @uopaisociety on social.

## A. Brand Voice & Anti-Slop Copywriting Protocol

- Write like a sharp technical founder or the society president messaging peers. Keep it brief, natural, grounded and direct. Use specific verbs and concrete outcomes.
- Never use “delve”, “unleash”, “revolutionize”, “game-changer”, “thrilled to announce”, “cutting-edge”, “embark”, “realm”, “tapestry”, “supercharge”, “calling all students”, “don't miss out” or “buckle up”.
- Never use em dashes for dramatic pauses. Use periods, commas or line breaks.
- Use at most two functional emojis in a message. The allowed set is 🎮, 👇, 👉, 📍, ⏰ and ⚡.
- Lead with what members build, touch or take home. For example, “Bring a laptop. We’ll build a simple chatbot and try each other’s demos.”

## B. Platform-Specific Rules

### 1. WhatsApp Community (Highest Priority Conversion Channel)

Every major WhatsApp announcement needs a 1600 × 800 (2:1) [banner](templates/whatsapp-banner-2x1.svg), [reminder](templates/whatsapp-reminder-2x1.svg) or [showcase](templates/whatsapp-showcase-2x1.svg). For Status use the shared [9:16 layout](templates/ig-story-status-9x16.svg). Pair a chat graphic with:

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

- Use 4:5 (1080 × 1350) for [portrait event posts](templates/ig-post-event-4x5.svg) and every slide in a [feed carousel](templates/). Use the [9:16 Story](templates/ig-story-status-9x16.svg) for vertical updates. Use a real screenshot in the rounded frame on showcase slides. Keep essential Story content within the safe insets and add the native link sticker in the app.
- Give a carousel one continuous background, split across the slides. Design it as a single canvas of N × 1080 by 1350 and crop it into N slides, using [ig-carousel-background-4x5.svg](templates/ig-carousel-background-4x5.svg) as the pattern. Keep text and logos inside each slide's safe insets and clear of the seams. Use cream lettering on the marine end and navy lettering on the cream end.
- Keep to one idea and at most 12 words of editable copy per slide, including logistics and CTA. Shorten the headline or CTA when adding room and time.
- Keep captions under 60 words. Put the hook on line one, follow with two sentences, give the date, time and location, and end with “Sign up via link in bio.”

### 3. LinkedIn (University of Portsmouth AI Society)

Use the 2400 × 1256 [Open Graph card](templates/social-og-card.svg) or 1600 × 800 [showcase banner](templates/whatsapp-showcase-2x1.svg). Write for industry partners, Gradcracker employers and student engineers. Lead with a shipped repo, practical engineering work, an observable workshop outcome or evidence of society activity. Use short paragraphs and one CTA.

### 4. Luma & GitHub Repositories

Luma is canonical for event dates, times, rooms and registration questions. GitHub is canonical for starter code and the live GitHub Pages demo. Before generating social copy or artwork, check that every template agrees on the date, 24-hour UK time, room code and destination URLs. Clear optional placeholder copy when a detail does not apply. Use confirmed logistics and live destinations in published artwork.

## C. Programmatic SVG-to-PNG Workflow for Agents

Work on a copy. Edit text by `id="slot-…"` or `data-slot` using an XML-aware parser. Keep the text editable, the slot IDs unique and the surrounding transforms and styles intact. Respect the per-slot character limit and check for overflow in the rendered PNG. Update the root title and description. For `slot-screenshot`, set the image `href` to an embedded PNG or JPEG data URI (up to 1 MB decoded), update the accessible label and retain the rounded `frame-clip` and border. Hide `screenshot-placeholder` for transparent screenshots. Use navy text and marks in the cream area and cream text and marks in the navy area. Keep text and logos clear of the gradient transition.

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

To export slide k from the panoramic carousel background, offset the viewBox by k × 1080 and render that window at 1080 × 1350. Change only the root width and viewBox. Leave the background rects and the grain filter at the full panorama width so the gradient stays one field.

```bash
k=0
python3 - "$k" <<'PY'
import pathlib, sys
k = int(sys.argv[1])
src = pathlib.Path("brand/templates/ig-carousel-background-4x5.svg")
text = src.read_text()
text = text.replace('width="4320"', 'width="1080"', 1)
text = text.replace('viewBox="0 0 4320 1350"', f'viewBox="{k * 1080} 0 1080 1350"', 1)
out = pathlib.Path("out")
out.mkdir(exist_ok=True)
slide = out / f"ig-carousel-bg-{k}.svg"
slide.write_text(text)
print(slide)
PY
npx --yes @resvg/resvg-js-cli@2.6.2-beta.1 --fit-width 1080 \
  out/ig-carousel-bg-$k.svg out/ig-carousel-bg-$k.png
```

The cropped file is a normal 1080 × 1350 SVG. The Playwright command above can screenshot it with `--viewport-size="1080,1350"`.

For scripted browser captures, await `document.fonts.ready` and verify the intended fonts loaded. Inspect the exported PNG for overflow, contrast, screenshot crop and safe-area fit. Compare it against the post and canonical event listing before publishing.
