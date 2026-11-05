# YouTube devlogs and vertical covers

Read for this owner's Roblox devlog thumbnails, 9:16 Shorts covers, supplied-video batches, or requests to match the studied Dani references. These are owner preferences and observed production lessons from October–November 2026, not universal design rules or measured performance claims. Current user instructions take precedence.

## Establish the video's hook

Inspect the supplied video's dimensions/duration and sample its actual frames, then consult its project script or aligned narration when available. Review the payoff and result before choosing copy. For a short clip, spread samples across its entire duration; for longer videos, include the opening, important mechanics, reveal and ending. Do not say you watched/listened to the whole video if you reviewed contact sheets and text only.

A batch needs a distinct visual premise per video, not the same monster with four new titles. Reuse palette, avatar identity, contour treatment and typography as a family. Show the specific action, mistake or question:
- One red room requested → several red doorways.
- AI-generated monsters → recognizable creature and relevant tool mark.
- Paying for Roblox ads → money directed toward Roblox, not an invented earnings result.
- Repeated coding limits → depleted battery as an editorial metaphor, not a fake usage screenshot.
- Cupid linking to Golem → clear heart-arrow relationship.
- Ascend unlocks → actual new workers and progression.

Do not add Robux to every Roblox thumbnail. Coins imply an economy/earnings hook and compete with faces, threats and AI marks. They fit an actual ads/earnings story; for a horror-building story, the monster and reaction may carry the promise better. Distinguish ad budget from spend and earnings; the Breakerline video mentions a $20 ad budget but recorded spend was about $8.37. Do not label the whole budget as money lost.

## Owner's avatar and visual preferences

When the creator is shown, use the supplied avatar rather than an unrelated worker or generic human. Durable identity reference: [owner-avatar.png](../assets/creator-thumbnail-examples/owner-avatar.png). Do not depend on clipboard/Temp paths.

The avatar has a green dinosaur hat with ivory forehead teeth and dark green ridge, green curled moustache, beige cylindrical head with a small black sparkle marking near the mouth, black/green sweater with green/pink pixel design and white/mint bands, dark green pants and black/white shoes. Preserve clothing/accessories while using the requested **classic blocky R6 body**: one cuboid torso, two single rigid cuboid arms rotated at shoulders and two straight box legs. Beige hand color is an end section of the arm block. Avoid human fingers, separate fists, C-shaped hands, bent elbows and detached cuffs. Hat/moustache can retain their accessory shapes.

Check the whole shoulder-to-arm-to-prop chain. A block touching a lever must meet the handle naturally without the lever passing through it; a raised arm must have the same coherent geometry. If “left hand” is ambiguous, inspect both hands and fix inconsistent geometry without changing the avatar identity.

The owner explicitly likes crisp white silhouettes around focal NPCs/objects, usually with a fine dark outer edge. They requested brighter blue/cyan backgrounds for the recent devlogs and Breakerline covers. Keep the subject's actual colors and enough fill light; a horror scene does not need to become a muddy dark poster. These palette choices are local preferences, not required for every game.

The owner rejected bland static laptop/avatar lineups and shiny generic AI artwork. The studied Dani references use exaggerated scale, diagonal action, clear actor/target relationships, selective blur, outlined cutouts, red arrows and short comic headlines. Transfer those visible decisions; adding saturation and a logo alone does not match them. An earlier successful thumbnail is style evidence, not a request to repeatedly copy its monitor-breakout composition. Do not reuse Dani's face, characters, exact layout or invented comments.

## References and game truth

When the user supplies a reference collection, inspect all supplied images. The 11 supplied Dani thumbnails were reviewed in the 23 October project. Their thumbnails establish appearance, not private CTR. For the Roblox study's high/low comparison workflow, use the sets in [ai-artwork-production.md](ai-artwork-production.md); the related Breakerline set used eight positive IDs 003,005,009,010,014,016,018,019 and eight negative IDs 361–368. These dated CCU categories do not rank YouTube thumbnails or predict click-through rates.

Read existing project notes for local constraints such as text-free artwork, rejected concepts and existing output versions. Current direct user requests override notes. Inspect source models/screenshots when available; Studio access is optional when footage already supplies the needed asset identity. Preserve existing Play sessions and avoid changing the place merely to inspect a reference.

Breakerline's Drifter is a tall dark workwear figure with reflective pale bands, cap and black face; light stops its movement. The Surveyor is a cable-suspended dark core with a red scanner eye and pale angular clawed limbs; moving while it scans is dangerous. Preserve recognizable creature features rather than substituting a fashionable horror mascot. Current game assets can change; refresh references when needed.

Use actual tool icons when relevant: Claude for coding-assistant context, ForgeGUI for generated asset context, Roblox for the platform/ads topic. Store a usable source image and provenance. Do not approximate a logo by code-drawing a generic star or pay for generation just to retrieve a brand asset.

## Typography and aspect-specific composition

The owner flagged generated-letter artifacts. For text-bearing YouTube/Shorts covers, default to **ImageGen artwork without text, then real-font typesetting**. If the requested cover is text-free, keep it text-free. Earlier permission for whole-image lettering remains an option when explicitly preferred; do not force extra passes on every task.

Bangers gave the recent covers a narrow comic treatment; a licensed copy is bundled at [Bangers-Regular.ttf](../assets/fonts/Bangers/Bangers-Regular.ttf) with [OFL.txt](../assets/fonts/Bangers/OFL.txt). Use short strong words, high-contrast fill and a dark outline. Do not generate a baked-in headline and then cover its malformed letters with new text.

For **9:16**, compose vertically from the start and export 1080×1920. Reserve actual clean headline space before generation, often about the top 15–20%, but adapt after seeing the result. Keep essential faces/headlines away from right-side controls and the lower region; about 10% right and 12% bottom were useful working margins, not permanent platform specifications. A generated image can ignore the requested headroom: measure the actual free area, recompose when necessary, and never hide a face under text. Inspect at 360×640 and 180×320.

For **16:9**, compose around the main action, preserve a 1920×1080 master and optionally a 1280×720 JPEG upload version. Check 384×216 and smaller. Do not crop a landscape image into a portrait cover as the default workflow. Do not carry a previous request's aspect ratio into a new request.

Reusable finishing helper: [typeset_thumbnail.py](../scripts/typeset_thumbnail.py). It adds real-font text to generated artwork and exports separate layers; it does not generate or repair subjects. Requires Pillow. Example config:

```json
{
  "source": "C:/project/artwork.png",
  "output_dir": "C:/project/thumbnail-v2",
  "stem": "video-cover",
  "size": [1080, 1920],
  "headline": {
    "lines": [
      {"text": "OUT OF", "color": "#ffffff"},
      {"text": "CREDITS!", "color": "#fff224"}
    ],
    "box": [70, 35, 940, 300],
    "max_font": 235,
    "min_font": 70,
    "stroke": 9,
    "gap": 12
  }
}
```

Run `python scripts/typeset_thumbnail.py --config C:/project/config.json` from this skill folder. Use `"headline": null` for text-free exports. Set `"size": [1920,1080]` and an appropriate box for landscape. The box is a measured free region, not a template to blindly apply. The helper refuses clipping/unfit copy and existing output filenames; version the output folder.

## Revisions and delivery

For targeted edits, provide the latest no-text master and lock all unrelated elements. Fix hands/background with ImageGen, then reapply the original typography layer or layout so it cannot mutate. A caption correction alone can use the real-font layer.

Keep native originals, no-text art, transparent text overlay, layout/config, font/license, exact prompts and reduced previews. These are separate layers, not a claimed multilayer PSD. A batch benefits from a labeled contact sheet and an archive in addition to individual ready-to-use links. Save selected assets in the actual project, preserve previous versions, and provide each requested file rather than only a preview.

Local examples retained for visual comparison:
- [Breakerline corrected blue-background composition](../assets/creator-thumbnail-examples/breakerline-blue.jpg): user requested this background/hand revision.
- [Four vertical promo covers](../assets/creator-thumbnail-examples/breakerline-promos.jpg): delivered set, not a recorded explicit approval or measured winner.
- [Ascend and Cupid vertical covers](../assets/creator-thumbnail-examples/ascend-cupid.jpg): delivered set, same evidence limitation.

The original editable deliveries live under the corresponding local video projects' thumbnails/ folders. Store new evidence as examples only when useful, and distinguish direct approval from simply having delivered a draft.

