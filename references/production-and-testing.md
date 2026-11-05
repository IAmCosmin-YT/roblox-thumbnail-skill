# Production and testing

## What the study can establish

A finished image reveals composition and rendering cues, not a verifiable software history. Labels such as "render-like", "capture-like", "illustrated", and "graphic composite" describe appearances. They do not identify a specific artist, application, or use of generative AI. No source files or production interviews were supplied for the reviewed games.

The following are reproducible ways to obtain comparable visual effects. They are proposed workflows, not claims about how each competitor worked.

## Staged gameplay capture

Best when the game's real visual style is part of the appeal, assets already exist, or the scene needs recognizable gameplay geography.

1. Stage the actual action with the player's tools, reward, enemy, or vehicle. Find a frame where the relationship is unambiguous.
2. Move the camera closer than a normal gameplay camera when that makes the action readable. Remove unnecessary UI and debug elements. Preserve useful UI only when it proves the mechanic and survives reduction.
3. Separate foreground and background through lighting, distance, and camera angle. Take several compositions before committing to post-processing.
4. Adjust levels, local contrast, and color without obscuring the game. Build a deliberate square composition from the same subject, often with a closer camera.

Avoid a beautiful empty map view when the point of the game is interaction. Environment-led imagery works when the destination or atmosphere is the actual promise.

## Posed 3D artwork

Best for repeatable character staging, clean silhouettes, dramatic camera placement, and controlled lighting.

1. Use game-owned or licensed character and prop assets. Export from Studio and import into the chosen 3D program if needed. Keep textures and proportions consistent with the game.
2. Block the camera and subject sizes first. An oversize reward or enemy should express a real game aspiration or threat, not invent a mechanic.
3. Pose the whole body. Let hands, gaze, torso, and action lines connect the actor with the target. Check contact, grip, intersections, and disconnected limbs.
4. Use a key light to describe the form, restrained fill to retain information, and a rim or background value difference when separation needs it. Avoid making every surface glossy.
5. Render subject and background separately if independent adjustment helps. Add contact shadows so composited layers feel connected. Use effects around the meaningful action rather than everywhere.
6. Finish with selective contrast, edge cleanup, and a controlled color grade. Export separate square and landscape compositions.

Primary practitioner evidence: [Vioo's Studio-to-Blender GFX walkthrough](https://devforum.roblox.com/t/create-roblox-gfx-tutorial-blender-2881828329/890782) describes export, rigging, texture setup, lighting, camera and rendering. [Uhley's GFX advertisement walkthrough](https://devforum.roblox.com/t/intermediate-to-advanced-how-to-make-a-professional-looking-gfx-advertisement-in-blender/1249194) describes area/rim lighting, posing, rendering and post-processing. These are historical workflow examples, not current button-by-button Blender documentation and not evidence for the production of the sampled games.

## Illustration and graphic composites

Best for stylized enemies, anime character appeal, distinct faces, or a simple symbolic promise. Start with a silhouette and value sketch; resolve the focal expression and gesture before surface detail. Keep outlines and cutout edges coherent across layers. Integrate light direction, perspective, and shadow. Use typography or symbols to explain something specific rather than to fill empty space.

Generative tools can be part of a proposed production workflow when the user wants them, but visual smoothness or unusual anatomy alone is insufficient to identify an existing image as AI-generated. Fix asset fidelity, hands, prop contact, repeated forms, and unreadable lettering in any workflow.

## AI generation from game references

Use actual game captures to lock asset identities, and label each supplied image as an asset reference, approved style, positive composition reference or negative reference. For the owner's requested high/low-CCU workflow and approved examples, read [ai-artwork-production.md](ai-artwork-production.md). Translate references into explicit visual choices; image labels alone are not a useful prompt.

Match the requested production method. A complete AI-generated thumbnail can include text in one pass when the user permits it; separate VS halves and later typography are optional workflows. Generate square icon compositions separately. Preserve native output and be clear when exports are flattened rather than layered.

Before delivery, trace connected machinery and check prop contact, coherent limbs, repeated objects, exact lettering and crop margins at full size and feed size. For factories, check that belts and both rails remain continuous and enter aligned machine openings; repair accidental branches and unfinished tips. Use targeted edits to protect approved parts, then inspect the repair.

## Video thumbnails and vertical exports

For YouTube/Shorts tasks, use [youtube-and-shorts.md](youtube-and-shorts.md) to review the actual video hook, choose portrait versus landscape staging, preserve the owner avatar, and add artifact-free real-font lettering when text is wanted. The bundled typesetting helper exports a no-text master and transparent overlay. It does not repair subjects; semantic edits still belong in the image-generation workflow.

## Building a useful creative test

First define the variable. "Make it better" is not a hypothesis. Examples:
- A readable attack trajectory will attract combat players more effectively than a disconnected character portrait.
- A close-up signature enemy will communicate horror more quickly than a dark environment where the threat disappears.
- A visible earned transformation will communicate progression more clearly than a pile of unexplained rare items.
- A social scene will attract roleplay intent more effectively than a detached logo.

These are hypotheses; none has a guaranteed direction or lift. For testing a whole concept, change the promise or staging deliberately and attribute results to the whole concept. For learning about one element, hold the rest of the composition steady.

Keep image IDs, activation dates, surface, source, audience, impressions, clicks when available, plays, qualified plays, and downstream outcomes. Compare rates on matching populations and time ranges. Missing clicks mean CTR is unavailable; qualified plays are not clicks. Do not combine ad CTR with Home qPTR into one rate.

Roblox's personalization distributes traffic differently as it learns. Inspect audience segments and exposure before treating a raw aggregate winner as causal evidence. Low exposure can leave a promising variant uncertain. Sample sufficiency depends on the baseline rate, effect size, traffic stability, and desired confidence; do not prescribe a universal impression minimum or 24-hour verdict. Keep known good variants while introducing distinct alternatives when appropriate.

A click gain with worse early bounce or shorter sessions can mean the artwork attracts the wrong audience or overpromises. A lower rate can also accompany expansion to broader audiences. Interpret both with traffic mix and update timing.

## Official sources to refresh before execution

- [Icons](https://create.roblox.com/docs/production/publishing/experience-icons): square artwork and small-size legibility.
- [Thumbnails](https://create.roblox.com/docs/production/publishing/thumbnails): landscape assets, personalization, and thumbnail performance fields.
- [Discovery](https://create.roblox.com/docs/discovery): acquisition and post-join signals, originality, and accurate expectations.
- [Discovery FAQ](https://create.roblox.com/docs/discovery-faq): current platform explanations and changing recommendation behavior.

Sources accessed 17 October 2026. Platform details should be checked again for future publishing work.
