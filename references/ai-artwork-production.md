# AI artwork production and Emotion Factory preferences

Read this for AI-generated Roblox thumbnails/icons, especially when continuing the owner's Emotion Factory project. The owner requested these defaults during the 17 October 2026 session. Later user instructions override them. The visual preferences below describe an approved direction, not measured artwork performance.

For YouTube devlogs, vertical covers and the owner's current creator-avatar/typography preferences, read [youtube-and-shorts.md](youtube-and-shorts.md). User-supplied creator references govern those style tasks; do not force Roblox CCU groups onto a supplied YouTube reference set.

## Reference selection and prompting

For this owner's Roblox competitor-library workflow, visually inspect at least eight distinct games in each positive and negative set per concept group. Use only high snapshot-CCU examples for positive references and only low snapshot-CCU examples for negative references, as the owner requested. For square icons, inspect eight high-CCU icons and eight low-CCU icons separately; landscape images do not count as icon references. Reuse a relevant reviewed set across related variants; choose another set when the motivation or composition changes. Do not silently reduce the count if sources are missing; state the limitation.

Choose a clear high/low separation within the available dated study; record IDs, titles, source board, snapshot CCU and specific visual observations. The sets below use high examples at roughly 20,000+ CCU and low examples below 100 in this particular snapshot. Those are selection bounds for this session, not universal popularity thresholds. Low-CCU images can contain good artwork. Negative prompts should name an observed issue relevant to the new concept, not condemn everything in the low set.

Prepare labeled contact boards that keep the actual artwork legible. Label positive and negative roles explicitly in the prompt; otherwise an image model can imitate the undesirable board. Positive and negative boards together count as the requested underlying unique images, not merely two references. Borrow visual decisions, never competitor branding, characters, prices or unsupported claims.

| Concept group | Positive thumbnail review IDs | Negative thumbnail review IDs |
|---|---|---|
| Worker interaction/conflict | 014,020,025,030,038,040,054,060 | 363,365,367,368,398,400,407,432 |
| Reward/progression | 001,011,012,024,031,036,043,053 | 367,396,398,400,401,405,422,430 |
| Automated/offline factory | 029,033,037,038,044,048,056,057 | 365,368,387,388,389,407,412,429 |
| Square icons (all three concepts) | 003,008,009,014,018,025,033,056 | 365,367,368,387,396,407,430,432 |

Resolve these IDs through [visual-index.md](visual-index.md) and [game-review-ledger.md](game-review-ledger.md). They are starting sets, not compulsory choices for unrelated games. All CCU labels are the supplied historical snapshot; they do not establish CTR, qPTR, artistic quality or causation.

In the current archived 1698 x 2160 contact sheets, each cell is 566 x 270. For review ID n: sheet = floor((n-1)/24)+1; cell column = ((n-1)%24)%3; row = floor(((n-1)%24)/3). Relative to the cell's top-left, the landscape crop is (170,46)-(554,262); the icon crop is (8,79)-(158,229). Verify dimensions before reusing these coordinates.

Use a small number of well-labeled image inputs: actual game asset sheet, user-approved style image, positive board, negative board. Combine landscape and icon panels into each role board when necessary to fit the available tool's reference limit. The session's ImageGen tool accepted at most five paths; treat that as an observed environment limit, not a permanent API specification.

## Approved Emotion Factory direction

The game combines worker personalities with cube production, conveyor progression and offline earnings. Show a real interaction or reward rather than an empty factory overview.

- Plain Roblox R6 blocks, cylindrical heads, simple drawn face decals, recognizable accessories, smooth plastic and ordinary bright daylight.
- Navy belts with gold rails, turquoise machinery, cyan-framed transparent cubes with flat liquid filling, green stud ground and a simple sawtooth factory.
- The owner especially likes clean white silhouette outlines around focal NPCs and objects that need emphasis. Include this preference in future thumbnail and icon prompts: a crisp, consistent white contour that separates the selected subject from the background and stays legible at feed size. Apply it selectively to the important characters/reward; preserve facial details and object edges, and avoid turning the outline into a diffuse glow.
- Close, purposeful poses and broad color shapes. Keep effect count low. Reject gratuitous glossy metal, realistic fabric/skin, ornate armor, nebula interiors, cinematic golden bloom and decorative swirls unless later requested.
- Text can be generated with the full image. Use brief contextual speech bubbles such as "STOP TALKING!" or flat white/black outlined comic type such as "COSMIC!". Avoid making every concept a full-width puffy extruded headline. Specify exact spelling, placement and safe margins.
- Generate complete VS compositions in one pass when requested. Separate halves, renders, typography passes and layers are useful only when the user wants that control. The owner explicitly allowed whole-image AI generation after initially requesting separate halves.
- Recompose square icons independently. Favor one large face plus a signature product, or two contrasting faces plus one small product. Text-free icons worked as a direction in this session; they are not a universal requirement. Create icons only when requested.

User-approved source examples, retained as visual references:
- [Worker conflict / STOP TALKING](../assets/emotion-factory-examples/approved-stop-talking.jpg)
- [Cosmic reward](../assets/emotion-factory-examples/approved-cosmic.jpg)
- [Offline concept, original with conveyor defect](../assets/emotion-factory-examples/approved-offline-with-defect.jpg)
- [Offline geometry repair](../assets/emotion-factory-examples/offline-repaired.jpg) is a repair example, not a separately recorded user approval.

Original Studio asset references:
- [Worker identities](../assets/emotion-factory-examples/actual-workers.jpg)
- [Cosmic and GoldenChild](../assets/emotion-factory-examples/actual-cosmic.jpg)
- [Lazy and Golden Robot](../assets/emotion-factory-examples/actual-lazy-goldenrobot.jpg)

View the relevant examples before matching them. Prefer fresh captures when the project's assets have changed. Grumpy has a brown beret, red torso, brown suspenders and black bow tie; Yapper has a purple fedora and purple torso; Listener has cyan headphones and a teal torso. Lazy has a blue sleep cap with white band/pompom and blue slippers. Golden Robot has a yellow dome/antenna, two cyan visor eyes and a red/green/blue-button chest control panel. The Cosmic cube has a dark spiked frame, purple transparent faces, thin orange seams and one pale pink orbit. Preserve these distinctive parts rather than inventing generic replacements.

## Geometry repair and delivery

Trace every visible conveyor as a physical object from input to output. Check both rails, slat direction, support, machine tunnel alignment and the route behind occlusions. Reject unfinished visible tips, missing rail sections, disconnected tracks, accidental junctions and cubes floating or clipping through machinery. A conveyor continuing outside the frame is acceptable; an exposed broken stub is not. Keep workers beside the mechanism. Check two attached block arms, coherent shoulders and original hand style; do not invent human fingers on plain R6 limbs.

Inspect full size, landscape at about 384 x 216 and 240 x 135, icons at 150 x 150 and optionally 64 x 64. Repair a specific defect with an image-edit prompt that locks approved characters, expression, text and framing; then inspect the new output again. Do not assume a successful generation means geometry passed.

When using Studio, inspect the connected place and mode before staging. Preserve existing Play sessions; do not stop Play merely to capture references. Respect current permission for the selected public place versus a copy. In this session, "idkk" was the staging copy; that name does not authorize edits to any future connection. Restore temporary camera, UI, lighting and device settings after captures.

Save selected native originals and requested exports, exact prompts, source/reference IDs and small previews. Python is suitable for routine resizing, packaging and separately requested text finishing; use the image tool for semantic image repairs. Do not describe flattened AI artwork as a layered PSD. Preserve real layers or separate passes only when produced. Package the requested variants without overwriting earlier approved sets.

