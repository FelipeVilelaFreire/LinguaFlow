# Language Seed Continuation

This document exists so the next Codex/Claude can continue the language seed work without repeating the same mistake.

## Current Goal

Create full adventure seeds for:

- `pt -> it`
- `en -> de`

The new seeds must not be short scaffolds. They must follow the Spanish ES A1 T1 seed as the editorial matrix.

## Core Rule

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

These were rebuilt from the Spanish `f01`-`f05` matrix and are now roughly the same size/depth as ES:

- IT `f01` ~47k
- IT `f02` ~48k
- IT `f03` ~45k
- IT `f04` ~44k
- IT `f05` ~45k

Basic cleanup already done:

- `word_id` values use `it_...`
- obvious Spanish character names were replaced
- `"corrict"` was corrected back to `"correct"`
- `Sally` is not used in T1 phase content
- `Chiara` remains the T1 equivalent of ES `Sofía`
- `Sally` is reserved as the future Italian equivalent of ES `Catalina`

## What Still Needs Work

Continue Italian in 5-phase modules:

```text
it f06-f10
it f11-f15
it f16-f20
it f21-f25
```

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

After Italian is complete, redo German the same way:

```text
de f01-f05
de f06-f10
de f11-f15
de f16-f20
de f21-f25
```

German currently exists but is still a summarized scaffold compared with ES. It must be expanded phase-by-phase from the ES matrix.

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

Python/Django validation was not run in this environment because Python is not installed/configured here.

When available, run from `backend/`:

```bat
py manage.py check
py manage.py seed_it
py manage.py seed_it_sections --reset
py manage.py seed_de
py manage.py seed_de_sections --reset
```

## Warning For The Next Agent

Do not call DE/IT complete just because they have 25 files. The first generated version had 25 files but was too short and generic. Completion means the target files are editorially comparable to ES phase-by-phase.
