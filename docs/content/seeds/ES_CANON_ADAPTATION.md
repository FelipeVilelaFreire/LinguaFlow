# ES Canon Adaptation Rules

This document defines the editorial hierarchy for LinguaFlow/Talkly A1 adventure seeds.

## Canon Hierarchy

The Spanish A1 T1 implementation is the operational canon for adventure seed generation.

Primary canon files:

- `docs/content/seeds/T1-ES-A1-COMPLETA.md`
- `docs/content/es-a1/story.md`
- `docs/content/es-a1/characters.md`
- `docs/content/es-a1/inventory-system.md`
- `backend/apps/adventure/seeds/es/chapter.py`
- `backend/apps/adventure/seeds/es/phases/f01.py` through `f25.py`

When another language is created or repaired, the Spanish seed is not inspiration. It is the matrix.

## What Must Stay The Same

Every target language must preserve:

- 25 phases for T1.
- The same phase-by-phase narrative arc.
- The same character roles and relationship arcs.
- The same timing for major character entries.
- The same mystery reveals and letter progression.
- The same boss structure and final seasonal hook.
- The same item system shape: phase-1 items, chest pool, degraded items, item moments, chest phases, and boss rewards.
- Comparable editorial density to the matching ES phase.
- Six sections per phase unless the ES source phase itself differs.
- Contextual exercises attached to scenes, not generic textbook prompts.

Target files should feel like the same season played in another cultural/language skin.

## What May Change

Only these layers should be localized:

- Character display names, titles, and slugs.
- Cultural setting and object flavor.
- NPC voice style, as long as the universal role stays intact.
- Item names and item descriptions.
- Grammar pacing and language teaching choices.
- Source-language narration, explanations, helper text, and translations.
- Target-language dialogue, vocabulary, answers, and `word_id` values.

Do not change the plot to fit the target culture. Change the costume, not the skeleton.

## Teaching Pair Rule

The source language is the player's native/help language.
The target language is the immersion/learning language.

Examples:

| Pair | Source/help text | Target/NPC speech | Important adaptation |
|---|---|---|---|
| `pt -> it` | Portuguese | Italian | Teach Italian through Portuguese support. Bridge character may speak broken Portuguese. |
| `en -> de` | English | German | Teach German through English support. Bridge character may speak broken English. |

This means `en -> de` must not copy the same explanations as `pt -> it`.
The story rhythm stays aligned to ES, but the pedagogy must respect the learner pair.

## Grammar Adaptation Rule

Do not copy Spanish grammar topics blindly.

The ES phase is the rhythm and narrative matrix. The target language defines the grammar map.

Examples:

- German must prioritize article gender, nominative/accusative exposure, verb-second order, negation, modal verbs, separable verbs, and simple past/perfect recognition.
- Italian must prioritize gender/articles, essere/avere, regular verbs, common irregulars, prepositions, possessives, passato prossimo exposure, and modal verbs.

The learner should encounter a natural A1 path for the target language while moving through the same ES story beats.

## T1 Canon Milestones

Target languages must preserve these T1 milestones:

| Phase | Canon requirement |
|---|---|
| F1-F5 | Arrival, survival, first ally, unreadable letter, basic social/commercial vocabulary. |
| F6 | First visible sign that a learned word affects the world. Local companion enters. |
| F8 | Hidden villain/Marta-equivalent enters as trusted healer and recognizes the protagonist. |
| F11-F15 | Authority pressure grows. Local legal/social status becomes the conflict. |
| F14 | Hidden villain is present and observing the protagonist's growth. |
| F19 | Letter becomes partially readable after enough mastery. |
| F21-F24 | Direct preparation for the authority conflict and boss. |
| F25 | T1 boss, conscious consequence of word-power, boss rewards, letter fragment, and hook into T2. |

## Character Role Map

Names change by language. Roles do not.

| Universal role | ES reference | Entry |
|---|---|---|
| Bridge/best friend | Miguel | T1 F2 |
| Local believer | Sofia | T1 F6 |
| Hidden villain/healer | Maria | T1 F8 |
| Love interest/second bearer | Catalina | T1 cameo, active T2 F3 |
| Practical ally | Rodrigo | T2 F6 |
| Explainer/other foreigner | James | T3 F2 |
| Letter guardian | Valentina | Via letter T1-T5, appears T5 |
| T1 authority boss | El Alcalde | T1 F11-F25 |

The James-equivalent must come from a third lineage, not from either language in the pair.

## Inventory And Item Rules

The item system is part of the canon and must not be simplified away.

Target languages must preserve:

- `PHASE1_ITEMS`
- `CHEST_POOL`
- `DEGRADED`
- `CHEST_PHASES`
- `BOSS_REWARDS`
- All ES `item_moment` placements and their narrative purpose.

Important implementation rule: backend item tags are system constants and are not localized.

Use the backend tags exactly:

- `comida`
- `bebida`
- `arma`
- `documento`
- `moneda`
- `remedio`
- `comum`

Localized item names may be Italian, German, French, etc., but `item_tag` must remain one of the backend constants.

## Phase Adaptation Workflow

For each target phase:

1. Open `backend/apps/adventure/seeds/es/phases/fXX.py`.
2. Identify the ES phase's story beat, NPCs, exercises, review loops, item moments, and transition.
3. Map character names using the target language cast map.
4. Rewrite source/help text in the source language.
5. Rewrite NPC speech and answers in the target language.
6. Replace vocabulary and `word_id` values with target-language vocabulary.
7. Adapt grammar to the target language's A1 path.
8. Preserve section count, gated section behavior, `npc_reaction`, `vocab_list`, transition beats, and density.
9. Validate imports and Django seed execution.

Do not use global search-and-replace as the main generation method.
Do not create short generic phases.

## Completion Checklist

A target T1 is complete only when all of this is true:

- `f01.py` through `f25.py` exist and are editorially comparable to ES.
- Each phase has the same high-level narrative purpose as ES.
- Major character entries happen in the canon phases.
- F25 includes boss resolution, boss rewards, letter progression, and T2 hook.
- Item moments use valid backend tags.
- Chest pool is rich enough to support the same gameplay shape as ES.
- Character names in sections match seeded characters, voice aliases, and frontend avatar mappings.
- Source/help language matches the learning pair.
- Target dialogue and exercise answers are natural A1 for the target language.
- Django checks and seed commands pass.

