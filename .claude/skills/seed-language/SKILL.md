---
name: seed-language
description: Generate a new LinguaFlow adventure seed for a language pair, using the existing ES A1 T1 seed as the structural model while preserving the canonical story, progression, item system, voice style, and Django seed architecture.
---

# Seed Language

Use this when creating a new adventure seed for a language pair such as `en -> de` or `pt -> it`.

## First Read

Read only what is needed:

- `docs/content/es-a1/story.md`: canonical narrative beats. Do not change the plot.
- `docs/content/es-a1/characters.md`: character roles and relationship arcs.
- `docs/content/es-a1/inventory-system.md`: chest, item, rarity, degraded-item rules.
- `backend/apps/adventure/seeds/es/chapter.py`: chapter-level structure.
- `backend/apps/adventure/seeds/es/voice.py`: localized voice profiles and NPC aliases.
- `backend/apps/adventure/seeds/es/phases/f01.py` through `f25.py`: section structure and pacing.
- `backend/apps/adventure/seeds/runner.py`: how section seeds are executed.
- `frontend-web/src/features/adventure/constants/characterAvatars.ts`: NPC-name to slug mapping used by section chat.
- `frontend-web/public/<lang>/characters/`: future character image folder.

## Output Architecture

Create the new language under:

```text
backend/apps/adventure/seeds/<target_lang>/
  __init__.py
  chapter.py
  voice.py
  phases/
    __init__.py
    f01.py
    ...
    f25.py
```

Keep Django commands thin:

```text
backend/apps/adventure/management/commands/seed_<target_lang>.py
backend/apps/adventure/management/commands/seed_<target_lang>_sections.py
```

The command files should only import/call seed code from `apps.adventure.seeds`.

Keep batch files language-scoped:

```text
backend/bats/padrao/       # shared backend tasks such as migrations
backend/bats/<target_lang>/ # language-specific setup/seed scripts
```

Root-level `.bat` files in `backend/` should stay as small compatibility shortcuts when needed.

Keep frontend character assets language-scoped:

```text
frontend-web/public/<target_lang>/characters/<character_slug>.png
frontend-web/public/<target_lang>/characters/<character_slug>.jpg
```

Also update `frontend-web/src/features/adventure/constants/characterAvatars.ts` with every localized display name and short alias used in section content. The slug must match the backend `AdventureCharacter.slug`.

## Non-Negotiable Rules

Narrative is immutable.
Keep the same 25 phase beats, milestones, emotional arc, mystery reveals, boss structure, and item system. Adapt culture, names, scenery, vocabulary, and grammar only.

Seed content must be editorial, not merely structural.
Do not satisfy a language seed by generating thin placeholder phases, generic repeated sections, or a factory that stamps the same exercise shape 25 times. The ES seed is the quality bar: each phase needs scene-specific narrative, character-specific dialogue, contextual exercises, emotional progression, and a clear transition. A structural scaffold is acceptable only as a temporary private drafting step; the final committed `f01.py` through `f25.py` files must contain materialized `SECTIONS` with phase-specific content.

Phase files must be adapted from the Spanish seed at equivalent density.
For every target phase file, open the matching Spanish source file (`seeds/es/phases/fXX.py`) and preserve its editorial shape: comparable number of beats, exercises, vocab lists, review loops, gated obstacles, NPC reactions, comments/intent, and transition beats. Do not compress a 700-line ES phase into a 70-line target phase. The target file may differ where the target language grammar requires it, but it must feel like the same lesson experience with the same narrative weight.

Translate/adapt the experience, not just the labels.
The expected workflow is: use the ES phase as the matrix, translate/adapt the scene into the source language for narration/help, rewrite NPC speech in the target language, replace vocabulary/options/word IDs with the target language, and keep the same teaching rhythm. A global search-and-replace is forbidden, but so is inventing a smaller generic phase from scratch.

Characters are language-local.
Every language seed gets its own localized cast names, titles, voice profiles, and future image identity. Preserve canonical roles and relationship arcs, but do not reuse Spanish names by default unless the target culture makes that name natural. Keep stable character slugs inside the language seed, and make sure any future image prompts/assets can map to those slugs.

The source language is the player's native language.
All `source_text`, explanations, bridge-character help, and translations use the source language. For `en -> de`, the bridge character helps in broken English. For `pt -> it`, the bridge character helps in broken Portuguese.

The target language is the immersion language.
NPC dialogue and exercise answers teach the target language. Target text must be natural, idiomatic, and level-appropriate.

The Other Foreigner must be a third lineage.
The James-equivalent cannot belong to either language of the pair. For `en -> de`, do not make him English, American, German, Austrian, or Swiss-German. Pick a plausible third lineage and adjust clues without changing his story role.

Grammar adapts, rhythm stays.
Do not copy Spanish grammar topics blindly. Map the target language's core A1 progression onto the same phase rhythm. Example: for German, distribute articles/gender, cases, verb-second order, separable verbs, modal verbs, and past exposure across the 25 phases without breaking the story beats.

Items and chests stay structurally identical.
Keep item moments, chest tiers, degraded items, boss rewards, word links, rarity spread, and inventory behavior. Change flavor and object names to fit the target culture.

## Generation Workflow

1. Identify `source_lang`, `target_lang`, language codes, chapter slug, target culture, and target A1 grammar pillars.
2. Build a phase grammar map from F1-F25, matching ES pacing but adapting to the target language.
3. Create a localized cast map: slugs, display names, roles, voice profiles, and future image identity notes.
4. Create `chapter.py` with languages, scenarios, phrases, phases, characters, phase-1 items, chest pool, degraded items, chest phases, and boss rewards.
5. Create `voice.py` with localized `VOICE_PROFILES`, including aliases used in section dialogue.
6. Draft a phase-by-phase content plan with story beats, NPCs, vocabulary, grammar, review words, item moments, and transition lines.
7. Create `phases/f01.py` through `f25.py`, each exporting materialized `SECTIONS`; each phase must be adapted from the matching ES `fXX.py` and kept at comparable editorial density. Do not leave phase files as one-line factory calls or short summaries.
8. Create thin management commands:
   - `seed_<target_lang>` seeds chapter data.
   - `seed_<target_lang>_sections --reset` seeds all 25 section files.
9. Create `backend/bats/<target_lang>/setup_<target_lang>.bat` and `seed_<target_lang>.bat` if the user wants runnable batch shortcuts.
10. Update `CHARACTER_AVATARS` and create `frontend-web/public/<target_lang>/characters/` so future images map cleanly.
11. Update root setup or docs only if the user asks to make the new seed part of the default setup.
12. Run Django checks/import checks if available.

## Quality Bar

Each phase must have:

- Six sections unless the existing ES structure clearly differs.
- Comparable size/depth to the matching ES phase. As a rough sanity check, a target phase should not be dramatically smaller than ES unless the source ES phase is itself short.
- Conversational exercises embedded in scene context, not dry quiz prompts.
- `npc`, `npc_reaction`, and pacing fields following the existing pattern.
- Review vocabulary from earlier phases.
- New vocabulary tied to the scene's action.
- A clean transition into the next phase.
- At least one phase-specific scene beat and one phase-specific NPC line in every section.
- No repeated generic filler such as "the same story beat continues here" as final seed content.

Every generated seed must be internally consistent:

- Slugs use the target language code.
- `word_id` values match target language vocabulary.
- `scenario_slug` values exist in `SCENARIOS`.
- Character first phases match canonical milestones.
- Character display names, `VOICE_PROFILES`, and future image identifiers are aligned.
- Every NPC name used in sections exists in `CHARACTER_AVATARS`.
- `public/<target_lang>/characters/` exists, even if final images are not generated yet.
- Phase numbers and section numbers are contiguous.
- `hydrate_section_content` remains the path for section content.

## Target-Specific Guidance

For `en -> de`:

- Use English source text and German target text.
- Use German grammar pacing based on gender/articles, nominative/accusative/dative exposure, verb-second order, modal verbs, separable verbs, negation, and simple past/perfect recognition.
- Keep the bridge character's English imperfect but understandable.
- Make the James-equivalent a third lineage, such as Portuguese, Italian, Polish, or French.

For `pt -> it`:

- Use Portuguese source text and Italian target text.
- Use Italian grammar pacing based on gender/articles, essere/avere, regular verbs, common irregulars, prepositions, possessives, passato prossimo exposure, and modal verbs.
- Keep the bridge character's Portuguese imperfect but understandable.

## Do Not

- Do not move seed data back into `management/commands`.
- Do not put every language's batch script in the backend root.
- Do not call a seed complete when it is only an architectural scaffold.
- Do not leave phase files as wrappers around a generic factory.
- Do not change the canonical story to fit the target culture.
- Do not make the teaching style generic or textbook-like.
- Do not remove item degradation, chest logic, or boss rewards.
- Do not create a language seed by global search-and-replace from Spanish.
