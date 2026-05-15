# Language Seed Continuation

This document exists so the next Codex/Claude can continue the language seed work without repeating the same mistake.

## Current Goal

Create full adventure seeds for:

- `pt -> it`
- `en -> de`

The new seeds must not be short scaffolds. They must follow the Spanish ES A1 T1 seed as the editorial matrix.

Read `docs/content/seeds/ES_CANON_ADAPTATION.md` before continuing. It defines the hierarchy: ES A1 T1 is the operational canon; other languages are controlled adaptations of that canon.

## Core Rule

ES is the pillar. Target languages must copy the ES narrative structure, item structure, boss structure, character-role timing, and phase density. Only local names, cultural flavor, item flavor, target vocabulary, and teaching method change.

The teaching method must follow the language pair:

- `pt -> it`: Portuguese support/narration, Italian NPC speech/exercises, Italian A1 grammar pacing.
- `en -> de`: English support/narration, German NPC speech/exercises, German A1 grammar pacing.

Do not copy Spanish grammar topics blindly. Keep the ES story rhythm, but build the target-language grammar map correctly.

For each target phase file, open the matching Spanish file:

```text
backend/apps/adventure/seeds/es/phases/fXX.py
```

Then adapt it into the target language file:

```text
backend/apps/adventure/seeds/it/phases/fXX.py
backend/apps/adventure/seeds/de/phases/fXX.py
```

The target file must keep comparable density:

- same 6-section rhythm
- comparable number of beats
- contextual `multiple_choice` exercises
- `vocab_list` where ES has one
- `npc_reaction`
- gated obstacles
- review loops
- transition beats
- same narrative arc
- same item moments with valid backend tags
- same boss/reward shape

Do not generate a small generic phase. A 45k-character ES phase should not become a 5k-character target phase.

## What Is Done

Italian module 1 is expanded:

```text
backend/apps/adventure/seeds/it/phases/f01.py
backend/apps/adventure/seeds/it/phases/f02.py
backend/apps/adventure/seeds/it/phases/f03.py
backend/apps/adventure/seeds/it/phases/f04.py
backend/apps/adventure/seeds/it/phases/f05.py
```

Italian module 2 is expanded:

```text
backend/apps/adventure/seeds/it/phases/f06.py
backend/apps/adventure/seeds/it/phases/f07.py
backend/apps/adventure/seeds/it/phases/f08.py
backend/apps/adventure/seeds/it/phases/f09.py
backend/apps/adventure/seeds/it/phases/f10.py
```

Italian module 3 is expanded:

```text
backend/apps/adventure/seeds/it/phases/f11.py
backend/apps/adventure/seeds/it/phases/f12.py
backend/apps/adventure/seeds/it/phases/f13.py
backend/apps/adventure/seeds/it/phases/f14.py
backend/apps/adventure/seeds/it/phases/f15.py
```

Italian module 4 is expanded:

```text
backend/apps/adventure/seeds/it/phases/f16.py
backend/apps/adventure/seeds/it/phases/f17.py
backend/apps/adventure/seeds/it/phases/f18.py
backend/apps/adventure/seeds/it/phases/f19.py
backend/apps/adventure/seeds/it/phases/f20.py
```

Italian module 5 is expanded:

```text
backend/apps/adventure/seeds/it/phases/f21.py
backend/apps/adventure/seeds/it/phases/f22.py
backend/apps/adventure/seeds/it/phases/f23.py
backend/apps/adventure/seeds/it/phases/f24.py
backend/apps/adventure/seeds/it/phases/f25.py
```

These were rebuilt from the Spanish `f01`-`f25` matrix and are now roughly the same size/depth as ES:

- IT `f01` ~47k
- IT `f02` ~48k
- IT `f03` ~45k
- IT `f04` ~44k
- IT `f05` ~45k
- IT `f06` ~54k
- IT `f07` ~54k
- IT `f08` ~64k
- IT `f09` ~59k
- IT `f10` ~62k
- IT `f11` ~45k
- IT `f12` ~47k
- IT `f13` ~48k
- IT `f14` ~49k
- IT `f15` ~46k
- IT `f16` ~45k
- IT `f17` ~47k
- IT `f18` ~48k
- IT `f19` ~48k
- IT `f20` ~48k
- IT `f21` ~22k
- IT `f22` ~18k
- IT `f23` ~18k
- IT `f24` ~19k
- IT `f25` ~24k, with an expanded boss ending and T2 north-road hook

Basic cleanup already done:

- `word_id` values use `it_...`
- obvious Spanish character names were replaced
- `"corrict"` was corrected back to `"correct"`
- `Sally` is not used in T1 phase content
- `Chiara` remains the T1 equivalent of ES `Sofía`
- `Sally` is reserved as the future Italian equivalent of ES `Catalina`

## What Still Needs Work

Italian T1 is complete through `f25`.

ES study seed is no longer missing.

```text
backend/apps/learning/management/commands/seed_es_study.py
```

It creates ES study modules, 8 scenarios, 120 phrases, and 25 canonical StudyDays. The ES bats already call it. The remaining study-seed question is whether IT and DE should get equivalent `seed_it_study.py` and `seed_de_study.py` commands, ideally extracted into `backend/apps/learning/seeds/`.

German has now been rebuilt with the same operational rule:

- ES A1 T1 remains the matrix.
- DE is `en -> de`: English support/narration, German target speech/exercises.
- All 25 DE phase files are materialized and no longer short 6-7k scaffolds.
- DE was expanded again for density: current phase files average about 34.7k chars, with item-heavy phases around 54k-56k chars and final-season phases around 18k-35k chars.
- DE keeps 6 sections per phase, the same T1 canon milestones, mapped mochila/item moments, boss/reward shape, and T2 north-road hook.

Important Italian character mapping:

```text
ES Don Miguel       -> IT Antonio il Contadino
ES Miguel           -> IT Nico
ES Rosa             -> IT Giulia
ES Ernesto          -> IT Pietro
ES El Mercader      -> IT Il Mercante
ES El Vigilante     -> IT La Guardia
ES Señora Carmen    -> IT Bianca
ES Sofía            -> IT Chiara
ES María            -> IT Lucia
ES Doña Lucía       -> IT Donna Elena
ES El Alcalde       -> IT Il Podesta
ES El Inspector     -> IT L'Ispettore
ES James/future     -> IT Mateusz
ES Catalina/future  -> IT Sally
```

Known Italian editorial cleanup still useful before calling IT fully polished:

- Some minor NPC names in phase text still look like ES/PT leftovers and need editorial cleanup.
- F25 has the right boss/hook shape, but can still receive a final Italian editorial polish pass.

German phase files now rebuilt:

```text
de f01-f05
de f06-f10
de f11-f15
de f16-f20
de f21-f25
```

German is no longer the summarized scaffold version. It is structurally aligned with ES/IT, including 25 phases, 150 sections, 13 characters, 74 phrases, 48 chest items, 15 chest phases, 2 boss rewards, and mochila moments in F4/F7/F9/F12/F13/F21/F23/F24. Future editorial passes can still improve individual lines and idiomatic German.

## German Notes

German must be adapted for `en -> de`, so:

- narration/help/source text should be English
- target NPC speech should be German
- bridge character speaks imperfect but understandable English
- grammar pacing should be German-specific, not Spanish-specific
- preserve story rhythm while teaching German A1 concepts:
  - gender/articles
  - nominative/accusative exposure
  - verb-second order
  - negation
  - modal verbs
  - separable verbs
  - perfect/simple past exposure

German must not be treated as a direct Portuguese-to-Italian style adaptation. The source/help language is English, so all narration, explanations, bridge help, and translations must be English.

German character mapping currently used:

```text
ES Don Miguel       -> DE Elias der Bauer
ES Miguel           -> DE Otto
ES Rosa             -> DE Hanna die Baeckerin
ES Ernesto          -> DE Friedrich
ES El Mercader      -> DE Der Markthaendler
ES El Vigilante     -> DE Der Waechter
ES Señora Carmen    -> DE Greta
ES Sofía            -> DE Lina
ES María            -> DE Marta die Heilerin
ES Doña Lucía       -> DE Klara
ES El Alcalde       -> DE Der Vogt
ES El Inspector     -> DE Der Inspektor
ES James/future     -> DE Joao
```

## Files To Keep In Sync

When adding or changing characters, update:

```text
backend/apps/adventure/seeds/<lang>/content.py
backend/apps/adventure/seeds/<lang>/voice.py
frontend-web/src/features/adventure/constants/characterAvatars.ts
frontend-web/public/<lang>/characters/
```

When changing seed-generation rules, update:

```text
.claude/skills/seed-language/SKILL.md
```

## Validation Status

Latest local validation:

- `python -m py_compile` passed for DE `content.py`, `chapter.py`, and all `phases/f01.py` through `f25.py`.
- `backend/.venv/Scripts/python.exe manage.py check` passed.
- `backend/.venv/Scripts/python.exe manage.py migrate` was run because the local SQLite database was missing inventory columns.
- `backend/.venv/Scripts/python.exe manage.py seed_de` passed after the second DE expansion.
- `backend/.venv/Scripts/python.exe manage.py seed_de_sections --reset` passed after the second DE expansion and created 150 sections.

Useful commands from `backend/`:

```bat
py manage.py check
py manage.py seed_it
py manage.py seed_it_sections --reset
py manage.py seed_de
py manage.py seed_de_sections --reset
```

## Warning For The Next Agent

Do not call DE/IT complete just because they have 25 files. The first generated version had 25 files but was too short and generic. Completion means the target files are editorially comparable to ES phase-by-phase.
