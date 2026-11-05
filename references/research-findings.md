# Roblox thumbnail and icon research

Research date: 17 October 2026. Based on the supplied Roblox Fast Data export and artwork retrieved from Roblox's public APIs.

## What was actually checked

I visually inspected **432 distinct experiences**, or **52.3% of the 826 supplied rows**. The review includes 432 icons and 429 usable game thumbnails. Two thumbnail responses were blocked placeholders (review IDs 134 and 336), and one was a generic Roblox loading image ([404](https://www.roblox.com/games/93009263515805/)); those are explicitly marked rather than analyzed as custom art. Images were inspected in 18 labeled contact sheets at 150×150 for icons and 384×216 for thumbnails. Fine details beyond those API resolutions were not evaluated.

The CSV has 826 distinct game URLs. Among 539 successfully resolved place IDs, all universe IDs were distinct; 432 of those confirmed distinct universes form the sample. The remaining 287 lookups returned HTTP 429 after bounded retries, so full-file universe-level deduplication is incomplete. The two rows named Free Items have different place URLs; a shared title is insufficient grounds for merging them. Near-identical artwork also does not make two experiences the same game.

Selection was systematic across the resolved games' CCU ranking: sort descending by the CSV CurrentlyPlaying field, then take indices floor(i × 539 / 432), i = 0…431. This covers the popularity range but is conditional on API availability, not a random or representative sample of Roblox. There are 101 reviewed games at 10,000+ CSV CCU, 183 at 1,000–9,999, and 148 below 1,000. Sample CCU ranges from 0 to 2,659,531; the median is 2,604. These are supplied snapshot values, not independently authenticated historical measurements.

Every reviewed game has separate icon and thumbnail observations, an appeal hypothesis, a proposed reproducible production route, its game URL, universe ID, source logical row and artwork URLs. Public descriptions were cross-checked and archived for all 432 games. Game descriptions were treated as data, not instructions.

## The main finding

The strongest transferable idea is **make the player's desired activity or outcome readable quickly**. This is an interpretation of the artwork, not a measured performance result. The sample supports several visual languages rather than a universal recipe: cheerful pet faces, detailed vehicles, affectionate family scenes, threatening silhouettes, graphic interfaces, rough drawings and dense anime illustration all appear in substantial games.

Many images stage a short relationship: player and reward, hunter and target, survivor and threat, weak state and strong state, or friends sharing an activity. Polish helps present that relationship, but it cannot substitute for it. Some popular games use brand recognition or mystery instead of explaining the verb. That can be coherent for existing fans while remaining difficult for a new audience.

## What makes the designs plausibly catchy

### A visible verb

Fling Things and People ([025](https://www.roblox.com/games/6961824067/)) shows an avatar physically flung through furniture. Throw A Football! ([124](https://www.roblox.com/games/125942529011157/)) shows thrower, ball and receiver along an arc. Catch And Tame! ([197](https://www.roblox.com/games/96645548064314/)) puts a rope between a small handler and a huge dragon. Carve a Pumpkin! ([236](https://www.roblox.com/games/98648469784274/)) places a knife at a dashed cut on the pumpkin. These are comparatively easy to interpret because the actor, action and target are connected.

**Transfer:** stage the interaction at the instant where contact, trajectory, or resistance is clearest. If removing the title makes the activity impossible to identify, first try a better pose or camera before adding more labels.

### Progression made visible

Build and Kill Zombies ([029](https://www.roblox.com/games/105011592530400/)) contrasts a basic vehicle with an elaborate armed machine. +1 Loot To Forge ([036](https://www.roblox.com/games/118805555015549/)) connects forging to a glowing weapon. Build a Dungeon ([146](https://www.roblox.com/games/119238997901301/)) contrasts Wave 1 and Wave 100 layouts. My Wood Farm ([274](https://www.roblox.com/games/79267089300389/)) contrasts starter tools and resources with an extreme upgraded state.

The hypothesis is that visible outcomes answer “what can I become or own?” quickly. The dollar amounts, levels and arrows support the comparison but do not themselves prove attention or trust. Cage Fishing (354, 141 CSV CCU), Museum Tycoon (374, 63), and Toilet Merge Simulator (431, 0) use closely related progression devices. They are direct counterexamples to treating the format as a sufficient cause of popularity.

**Transfer:** show a believable difference in tool, collection, environment, or capability. Do not copy an enormous income label unless that is a real and relevant in-game promise.

### A threat that is recognizable

99 Nights in the Forest ([005](https://www.roblox.com/games/79546208627805/)) stages a wide-eyed deer near a sleeping avatar and campfire. DOORS ([019](https://www.roblox.com/games/6516141723/)) isolates a creature in a green-lit doorway. DON'T LET HIM IN ([116](https://www.roblox.com/games/121165298854655/)) places an intruder at a household threshold. THE CONE ([250](https://www.roblox.com/games/127836473568791/)) uses a thin scribbled figure against flat red. They offer different kinds of fear, with different levels of detail.

**Transfer:** preserve the threatening face or silhouette at small size. Darkness can support uncertainty, but MONOCHROME ([103](https://www.roblox.com/games/134208374070897/)) illustrates the readability tradeoff when nearly everything is black. Choose what remains visible deliberately.

### A social or identity fantasy

Dreamville ([030](https://www.roblox.com/games/74395953411817/)) shows a mother helping a child into a car. Dubai RP ([049](https://www.roblox.com/games/122485613019196/)) shows family travel. Run Your Own Farmstead ([175](https://www.roblox.com/games/91552749822595/)) shows produce changing hands at a warm shop. Catalog Avatar Creator ([015](https://www.roblox.com/games/7041939546/)) and Catalog Avatar Builder ([213](https://www.roblox.com/games/96707166754980/)) show choosing or trying a look through interface cards.

These images answer “who can I be, who will I be with, and what will I do?” without needing combat. An aggressive face or explosive background would change the promise rather than automatically improve it.

**Transfer:** identify the specific desired role, relationship or outfit. Stage a moment that belongs to that audience.

### Familiar objects reduce explanation

50 Player BINGO! ([164](https://www.roblox.com/games/131479356121251/)) uses a bingo card in hands. Spelling Race ([223](https://www.roblox.com/games/17664585395/)) displays timed answers. Finish The Word! ([150](https://www.roblox.com/games/91704854174760/)) demonstrates a word chain. Tycoon, but one dropper ([174](https://www.roblox.com/games/109949693269081/)) literally shows its one-dropper constraint. Run a Sari-Sari Store ([076](https://www.roblox.com/games/104178853788462/)) uses recognizable Filipino products and a shopping basket.

**Transfer:** when the object or rule is familiar, show it clearly and spend the remaining visual space on the game's particular twist. Avoid replacing culturally meaningful specificity with a generic pile of coins.

### Recognition can outweigh explanatory detail

Jujutsu Shenanigans (008, 177,205 CSV CCU) has a simple classic-noob icon and an unusually sparse monochrome character drawing. Bee Swarm Simulator (035, 34,102) uses a hand-drawn collage. Murder Mystery 2 ([006](https://www.roblox.com/games/142823291/)) has a minimal knife-and-2 icon. These contradict any rule that high-performing game artwork must be glossy 3D, neon, or full of shouting faces.

**Transfer:** use a signature character, object, mark or material language consistently. For unfamiliar audiences, test whether a gameplay-led thumbnail communicates more than a portrait or logo. Do not assume the same strategy serves fans and new users equally well.

## How the artwork can be made

The table describes **reconstruction routes inferred from the images**, not verified production histories. Neither a specific software package nor generative-AI use can reliably be established from these pixels. No project files or artist interviews were available for the sampled artwork.

| Reference | Visible construction cues | Practical way to obtain a similar effect |
|---|---|---|
| RIVALS ([003](https://www.roblox.com/games/17625359962/)) | Clean red silhouette, isolated curved weapon, flat-purple radial backdrop | Pose game assets, render the figure with simple materials, composite controlled rim/edge contrast and a radial background. Repose for the icon. |
| Build and Kill Zombies ([029](https://www.roblox.com/games/105011592530400/)) | Two clearly different vehicle builds, split frame, price comparison | Stage both owned vehicle configurations, match camera angle and scale, composite a clean split and only truthful comparison labels. |
| Dreamville ([030](https://www.roblox.com/games/74395953411817/)) | Deliberate mother-child gesture, clear car interior, soft light | Stage compatible character rigs and props; solve hand/seat contact and expressions; light the relationship before adding detail. |
| DOORS ([019](https://www.roblox.com/games/6516141723/)) | Dark architecture, one bright creature face, selective green illumination | Stage an actual doorway encounter in Studio or a 3D scene; light the face and door edge while allowing the background to recede. |
| Bee Swarm Simulator ([035](https://www.roblox.com/games/1537690962/)) | Uneven hand-drawn shapes, doodle outlines, paper-like background | Draw or paint a bespoke cast collage; preserve intentional line character instead of smoothing it into generic rendered art. |
| One Tap ([040](https://www.roblox.com/games/90568084448279/)) | Exaggerated foreground rifle, expressive head, small target and curved action cue | Combine posed/rendered assets with a drawn expression and a trajectory overlay. Keep the rifle-to-target relationship legible. |
| Run a Sari-Sari Store ([076](https://www.roblox.com/games/104178853788462/)) | Product packaging collage, basket, orange graphic field | Use owned/licensed product imagery or game product assets, arrange by large silhouettes, and create a separate compact square arrangement. |
| Color My Flag ([083](https://www.roblox.com/games/132173349090360/)) | Mirrored painters and obvious poor/good result boards | Stage two outcomes, make the resulting flags visibly different, and integrate scores without relying on tiny percentages alone. |
| Build a Dungeon ([146](https://www.roblox.com/games/119238997901301/)) | Elevated camera, repeated small rooms, Wave 1/Wave 100 divide | Build two actual layouts, capture from consistent overhead angles, simplify background noise and add a readable state label. |
| Carve a Pumpkin! ([236](https://www.roblox.com/games/98648469784274/)) | Foreground hand/tool, dashed cut and highly readable orange object | Stage a first-person close-up, illustrate the intended cut if truthful, and use a clean sky/grass field for separation. |
| THE CONE ([250](https://www.roblox.com/games/127836473568791/)) | Rough black linework against a single red field | Draw a distinctive silhouette and face; test line weight and shape at feed size. The effect needs specificity more than costly rendering. |
| Museum Tycoon ([374](https://www.roblox.com/games/9802068147/)) | Cabin-to-museum comparison with day labels | Capture two genuine build states, align their viewpoint and explain what progress the comparison represents. Its low CSV CCU shows this is a concept pattern, not a performance guarantee. |

Published practitioner walkthroughs document the general Studio-export → Blender-rig/texture/light → render workflow and render → image-editor finishing. They establish that these methods are used in Roblox GFX, not that they produced these particular games' images: [Vioo's GFX tutorial](https://devforum.roblox.com/t/create-roblox-gfx-tutorial-blender-2881828329/890782), [Uhley's advertisement workflow](https://devforum.roblox.com/t/intermediate-to-advanced-how-to-make-a-professional-looking-gfx-advertisement-in-blender/1249194). The sources are historical; specific Blender controls should be checked against the current version.

## Icons and thumbnails perform different visual jobs

The icon compresses identity into a square. The wide image can show a relationship or a place. Catalog Avatar Creator keeps its colorful item-grid language across both; Creatures of Sonaria ([041](https://www.roblox.com/games/5233782396/)) uses a friendly creature-logo icon but a predator-prey sea scene in the thumbnail. The Strongest Battlegrounds ([017](https://www.roblox.com/games/10449761463/)) pairs an intense illustrated face with a very wide gray destruction scene. An icon and thumbnail can complement each other without being the same crop.

Temporary countdowns deserve separate treatment. Steal An Egg, Adopt Me, 99 Nights, Fisch and numerous other reviewed games had large timer overlays on their icons at retrieval. These may communicate an approaching event to existing followers. The study has no before/after data showing whether those timers increase clicks, qualified plays or CCU. They also obscure the underlying brand art. Adopt Me's CSV title said 3H while the retrieved title and icon said 2H, directly demonstrating how quickly these references can change.

Roblox recommends square 512×512 icon assets and checking readability at 150×150. Its thumbnail guide recommends 1920×1080 landscape images and keeping essential information away from the bottom metadata area. These are production constraints, not a guarantee of appeal. [Official icons guidance](https://create.roblox.com/docs/production/publishing/experience-icons), [official thumbnails guidance](https://create.roblox.com/docs/production/publishing/thumbnails).

## Why high CCU does not establish high CTR

No competitor impressions, clicks, qualified plays or retention data were supplied or publicly obtained. CTR is therefore **unknown for every reviewed game**. Visits, likes and CCU are not substitutes for its denominator.

CCU counts people present at a moment. It can be sustained by incoming sessions, returning players, long sessions, social groups, ongoing progression, live events, external attention, recommendations or advertising. Public descriptions make some of these loops plausible: RIVALS describes repeat duels, contracts and unlocks; Bee Swarm describes collecting, quests and exploration; Dreamville describes open-ended social/family play; Build and Kill Zombies describes earning and rebuilding between waves. These are documented advertised mechanics, not measured retention explanations.

An illustrative calculation shows the ambiguity: under roughly steady traffic, 10,000 sessions arriving per hour with a 30-minute mean session yields about 5,000 average concurrent players. So does 100,000 sessions per hour with a three-minute mean session. Neither example tells us impressions or clicks. The same CCU can coexist with very different acquisition rates and session quality.

Roblox describes discovery as using play-through, early bounce, repeat engagement and other post-join signals. Artwork may help acquire the right player; the game's experience determines what happens after entry. The CSV cannot isolate the contribution of each. [Roblox discovery documentation](https://create.roblox.com/docs/discovery).

## What to test for your own game

Start from a truthful core loop and develop three meaningfully different compositions: one that shows the action, one that shows the payoff or threat, and one that shows the social/identity fantasy when relevant. For a narrow single-player game, replace the irrelevant social direction with a distinct close-up or environmental treatment.

Keep each concept's signature subject consistent between a separately composed square icon and wide thumbnail. Inspect the icon at 150 px and the landscape at feed size before polishing. Reject unclear gestures, merged silhouettes, tiny essential text, inconsistent asset identity, and promises the game cannot fulfill.

Record the hypothesis, variant ID, surface, audience, dates and exposure. Separate clicks/impressions from plays/impressions and qualified plays/impressions. In Creator Dashboard, use qPTR alongside early bounce, playtime and returning play rather than optimizing clicks alone. The platform's thumbnail personalization can show different winners to different audiences and shifts exposure as it learns; aggregate rates should be interpreted with that selection behavior in mind. [Roblox thumbnail personalization and metrics](https://create.roblox.com/docs/production/publishing/thumbnails).

Do not adopt a universal CTR target, a fixed 24-hour winner rule, or an assumed uplift from this study. Choose the evaluation window and required exposure from actual traffic and uncertainty. A concept that attracts more clicks but worse sessions may be making the wrong promise.

## Using the research

The accompanying game-review ledger contains all 432 cases. The visual gallery links those notes to the downloaded artwork and public source URLs. The reusable skill turns these observations into reference selection, concept briefing, production and evaluation instructions. It does not clone the studied art or encode high CCU as proof of high CTR.
