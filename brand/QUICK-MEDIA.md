# Quick social templates

The everyday templates use the official **grainy navy mesh** and **grainy cream wash**. They reuse the original colour fields and noise recipe, with cream lettering over navy and navy lettering over cream. Use one gradient across all exports of an announcement, then alternate on the next post. A later reminder can change gradients and keep the same title and layout.

## Pick a template

| Where | Size | Editable SVGs |
| --- | --- | --- |
| WhatsApp chat, single-image X post, native LinkedIn image | 1500 × 900 (5:3) | [Navy](templates/quick/landscape-5x3-navy.svg) · [Cream](templates/quick/landscape-5x3-cream.svg) |
| Instagram feed and single slides | 1080 × 1350 (4:5) | [Navy](templates/quick/feed-4x5-navy.svg) · [Cream](templates/quick/feed-4x5-cream.svg) |
| Instagram Story and WhatsApp Status | 1080 × 1920 (9:16) | [Navy](templates/quick/story-9x16-navy.svg) · [Cream](templates/quick/story-9x16-cream.svg) |
| Luma event cover | 1080 × 1080 (1:1) | [Navy](templates/quick/luma-1x1-navy.svg) · [Cream](templates/quick/luma-1x1-cream.svg) |
| LinkedIn link preview image | 1200 × 627 | [Navy](templates/quick/link-1200x627-navy.svg) · [Cream](templates/quick/link-1200x627-cream.svg) |

Copy an SVG and edit the text in Inkscape or by `slot-…` ID. The displayed workshop is example content. Replace it, remove unused lines, and update the SVG title and description. The full art and logo are embedded. Install Inter Tight, Inter and JetBrains Mono locally for the intended type.

## What to put on the card

| Post | Visual | Accompanying copy |
| --- | --- | --- |
| Event announcement | What students will do, one useful detail, date and start time. Add a short room or building and “Sign up required” if confirmed and useful. | Explain the experience, eligibility and what to bring. Give one direct route to register. |
| Reminder or room change | Event title, confirmed time and latest room. Put the change on the first useful line. | Repeat the date, time and room in plain text. Include the event link or arrival instruction. |
| Recap or member project | Outcome or project name. Use a real photo or screenshot if it adds evidence. Remove event logistics. | Describe what happened, credit confirmed contributors and link the demo or repo if available. |
| Partner announcement | State the concrete thing students can access or do. Use approved partner artwork when needed. | Name the partner, say what they are contributing and give one next step. |

Give the headline the most space. Use one detail line to say who it is for, what to bring or what people will leave with. Put essential logistics in the caption or message as well as the card. Check the PNG at roughly 320 px wide, where it should still be clear what this is and when it happens. Use 4.5:1 as the minimum contrast for ordinary text. Check the lightest area behind cream text and the darkest area behind navy text on the rendered gradient. [Visual hierarchy](https://www.nngroup.com/articles/principles-visual-design/) · [Front-loading](https://service-manual.ons.gov.uk/content/writing-for-users/structuring-content) · [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)

## Adapt the copy to the platform

- **WhatsApp.** Use 5:3 for chat graphics. Keep the time, room and tappable link in the message. For Status, use the vertical layout and preview it in the app. [WhatsApp Status guidance](https://faq.whatsapp.com/643144237275579/)
- **X.** Lead with something people can make or try. Use the 5:3 card as a single photo, include one direct link and add concise alt text. Keep within the standard 280-character limit. [X photos](https://help.x.com/en/using-x/posting-gifs-and-pictures) · [X image descriptions](https://help.x.com/en/using-x/picture-descriptions)
- **Instagram.** Use one idea per slide. For registration, confirm the bio link for feed posts and reserve the lower Story area for the native link sticker. Use the 4:5 carousel layouts below.
- **LinkedIn.** Use the landscape card for a native image and the 1200 × 627 art for a link preview. Write about the student outcome or the specific partner contribution. Use an approved screenshot or photo when it adds proof. [LinkedIn preview guidance](https://www.linkedin.com/help/linkedin/answer/a566445/customize-the-image-and-title-of-a-linkedin-page-post-preview)
- **Luma.** Use the event title, optional short edition or topic, one image and the society mark. Use native event fields for date, time, venue and registration. [Luma event covers](https://help.luma.com/p/event-cover-images)

## Luma event covers

Use the 1080 × 1080 square. Lead with one or two short, left-aligned title lines. Add an edition or topic only if it helps identify the event. Let one real visual carry the lower half, such as a screenshot of what people will build or a portrait of the speaker. With no artwork supplied, the card uses the official wave. Use the original navy or cream gradient through the whole cover.

Luma recommends at least 800 × 800, minimal text and space around the edges for rounded corners. Keep the logo and the recognisable part of the visual inside the guide. Test the title and focal image in a small preview. Use the Luma listing for timing, eligibility, venue and signup. [Luma cover guidelines](https://help.luma.com/p/event-cover-images) · [Visual hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)

Use `detail` for the optional edition line and supply one PNG or JPEG if you have event artwork. The export centres and crops the image inside the rounded frame. Choose an image with its subject clear of the edges.

```bash
python3 brand/quick-media.py out/luma --brief brief.json --format luma-1x1 --cover-art artwork.png --png
```

## Instagram carousels

| Style | Opening | Inside slides | Closing |
| --- | --- | --- | --- |
| Navy covers and cream inside | Grainy navy cover with the hook | One wide grainy cream gradient, cropped into as many slides as the story needs | Grainy navy cover with one next step |
| All navy | Grainy navy cover with the hook | Slices of the same grainy navy gradient across the whole carousel | Final navy slice with one next step |

Write one idea per slide. Give the first slide the hook, use the middle slides for examples or steps, and put the next step on the last slide. For the mixed style, the cut from navy to cream at each cover is intentional. Inside, the SVGs share one gradient field and the PNG exporter renders that field once before it slices the slides. The grain continues across the swipe.

Use the [editable JSON example](examples/instagram-carousel.json) or ask Grok for a JSON array with one slide brief per item. Use at least three slides for navy covers with cream inside, or two for all navy. Use a fresh output folder for each export. Results are numbered in swipe order. Omit `--png` if you only need editable SVGs.

```bash
python3 brand/quick-media.py out/mixed --brief brand/examples/instagram-carousel.json --carousel navy-cream --png
python3 brand/quick-media.py out/navy --brief brand/examples/instagram-carousel.json --carousel all-navy --png
```

## Give Grok one campaign brief

> Read this page, the brand rules, the token file and the SVG masters. Use the confirmed facts below to write the requested captions and alt text. Return a visual JSON brief in the shape shown here. For an Instagram carousel, return an array of slide briefs and specify navy covers with cream inside or all navy. Keep headline wording and theme consistent across the exports. Confirm event logistics from Luma or the organiser. Flag conflicts and missing details that affect publishing. Use the actual SVG masters and logo artwork. If you use image generation for an illustration, add it separately and set all text and logos from the masters. Check the exported images and the actual signup route before marking the assets ready.

Include the audience, goal, confirmed event name, date, time, room, requirements, direct URL, requested channels and any approved media in your message to Grok. Keep operational details and links in the captions. Use this JSON shape for the cards. The array holds one or two short title lines. The other fields are optional.

```json
{
  "lead": "WORKSHOP",
  "title": ["Build a", "tiny game"],
  "detail": "No coding experience needed.",
  "when": "Thu 12 Mar · 18:30",
  "where": "Ravelin Library",
  "action": "Sign up required"
}
```

Run from the repository root with Python 3.10+.

```bash
python3 brand/quick-media.py out --brief brief.json --theme navy
python3 brand/quick-media.py out --brief brief.json --theme navy --png
```

The first command exports editable SVGs. The second also checks the rendered slots and exports PNGs using Inkscape. Use `--format landscape-5x3` to generate one size. The square cover uses the title, optional detail and one visual. The link card uses the title, category and detail. The generator is for text cards. For a photo or screenshot, use the existing [showcase templates](README.md#instagram) or attach real media alongside the card. Confirm crop, type, contrast, alt text and live links in each platform’s composer before publishing.

Before changing the templates, render one announcement, a room change, one recap without a footer and one long title. Check both gradients, the Story sticker area and every interior carousel seam. Keep the SVGs as the reusable outputs and regenerate them from the same source. [Cursor PStack](https://github.com/cursor/plugins/tree/main/pstack)
