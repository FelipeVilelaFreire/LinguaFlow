# Talkly — Design Prompts

Prompts prontos para gerar as telas no Stitch ou Claude Design.
Mobile first sempre — desktop é aprimoramento, não base.

---

## Como usar

- **Stitch:** cole o prompt completo. Ele não conhece o projeto.
- **Claude Design:** cole o prompt + os 3 arquivos de design system (colors.ts, studyAreaTheme.ts, globals.css).

---

## Regras fixas para todas as telas

```
Bottom navigation — sempre presente nas telas principais (5 abas):
  Home | Aventura | Estudo | Vocabulário | Perfil
  Ícones + labels, altura mínima 56px
  Aba ativa: cor primária teal (#14b8a6)
  Fundo: branco, borda top sutil

Mobile first:
  - Layout coluna única
  - Botões mínimo h-14 (56px)
  - Sem interações hover-only
  - Safe area no bottom e top

Telas fullscreen de aventura:
  - Quebram o layout normal
  - Sem bottom nav visível
  - Fundo escuro, tons âmbar/dourado
```

---

## Telas Prontas

---

### 1. AuthScreen

**Para o Stitch:**
```
Design a mobile login/signup screen for a language learning app called Talkly.

The app teaches languages through RPG adventure — medieval world, epic atmosphere,
but the auth screen should feel clean and trustworthy, not gamified.

Visual direction:
- Primary color: teal (#14b8a6)
- Background: very light slate (#f8fafc)
- Cards: white, subtle shadow, 8px border radius
- Typography: Inter, clean and modern
- Mobile first, single column layout

Screen content:
- App logo/name "Talkly" at the top with a small flame or sword icon
- Tagline: "Aprenda idiomas vivendo a história"
- Toggle tabs: "Entrar" / "Criar conta"
- Fields: email + password (login) or username + email + password (signup)
- Primary CTA button: full width, teal, rounded 8px, height 56px
- Subtle link below: "Esqueci a senha" (login) or terms text (signup)

No bottom navigation on this screen.
Mood: clean, modern, slightly epic. Trust and simplicity.
```

---

### 2. OnboardingScreen

**Para o Stitch:**
```
Design a mobile onboarding flow for a language learning RPG app called Talkly.
Multi-step setup shown once after account creation. No bottom navigation.

Visual direction:
- Primary color: teal (#14b8a6)
- Background: very light slate (#f8fafc)
- Cards: white, subtle shadow, 8px border radius
- Typography: Inter, clean and modern
- Mobile first, single column
- Progress indicator at top (Step X of 5)
- Back arrow top left

Show all 5 steps as separate screens:

STEP 1 — Idioma base
Title: "Qual é o seu idioma?"
Subtitle: "O app vai te explicar tudo nesse idioma"
Two large selection cards:
  🇧🇷 Português (selected — teal border + soft teal background)
     "Explicações e traduções em português"
  🇺🇸 English
     "Explanations and translations in English"
CTA bottom: "Continuar" — teal, full width, 56px

STEP 2 — Idioma alvo
Title: "O que você quer aprender?"
Subtitle: "Escolha o idioma da sua aventura"
Two large selection cards:
  🇩🇪 Alemão (selected)
     "Vila Medieval · A história começa aqui"
  🇪🇸 Espanhol
     "Em breve"
CTA: "Continuar"

STEP 3 — Nível atual
Title: "Qual é o seu nível hoje?"
Subtitle: "Sem pressão — você pode mudar depois"
Three selection cards stacked:
  "Estou começando do zero" (selected)
  "Já sei o básico (A1)"
  "Tenho alguma base (A2)"
CTA: "Continuar"

STEP 4 — Rotina de estudo
Title: "Quando você quer estudar?"
Subtitle: "Sua rotina, seu ritmo"
Days of week selector: SEG TER QUA QUI SEX SAB DOM
  (SEG QUA SEX selected — teal background)
Session duration pills: 15min / 30min (selected) / 45min / 60min
Estimated time below:
  "No seu ritmo, você chega no A1 em cerca de 6 meses"
Small note: "Você pode estudar qualquer dia — só vamos te lembrar nesses"
CTA: "Continuar"

STEP 5 — Modo de aprendizado
Title: "Como você quer aprender?"
Subtitle: "Você pode mudar isso no perfil a qualquer momento"
Two large cards stacked:

  Card 1 — Aventura (badge "Recomendado")
  ⚔ icon
  "Modo Aventura"
  "Aprenda vivendo a história. Narrativa, boss, itens e emoção real."
  Teal border, soft teal background

  Card 2 — Estudo
  📚 icon
  "Modo Estudo"
  "Direto ao ponto. Explicação + exercícios, sem narrativa."
  Default card

CTA: "Começar minha aventura" or "Começar meus estudos"

Mood: welcoming, clear, one decision per step.
```

---

### 3. HomeScreen

**Para o Stitch:**
```
Design a mobile home/dashboard screen for a language learning RPG app called Talkly.

Visual direction:
- Primary color: teal (#14b8a6)
- Background: very light slate (#f8fafc)
- Cards: white, subtle shadow, 8px border radius
- Typography: Inter, semibold titles, medium body
- Mobile first, single column

Screen content (top to bottom):

1. Top header
   - Left: flame icon + "Talkly"
   - Right: area badge "PT → DE · A1" in soft teal background

2. Hero card (main, prominent)
   - Small label: "Vila Medieval · Temporada 2"
   - Chapter progress bar: 60% teal
   - Large CTA: "Continuar Aventura" — full width, teal, 56px
   - Below: "Fase 3 de 15 · O Mercado"
   - Estimated time: "~10 min"

3. Stats row (3 equal cards)
   - 🔥 Streak: "7 dias"
   - 📖 Frases: "47 aprendidas"
   - ⭐ Nível: "A1"

4. Study session card
   - Label: "Sessão do dia"
   - "Hoje é dia de estudo · Segunda"
   - Secondary button: "Revisar frases"

5. Next session card (when not a study day)
   - "Próxima sessão: Quarta-feira"
   - "Descanse hoje — você merece"

6. Bottom navigation
   Home (active — teal) | Aventura | Estudo | Vocabulário | Perfil
   Icons + labels, white background, top border

Mood: motivating, clear, user knows exactly what to do next.
```

---

### 4. AdventureScreen (intro épica)

**Para o Stitch:**
```
Design a mobile fullscreen adventure intro screen for a language learning RPG app called Talkly.

This is the most epic screen in the app. It should feel like entering a real RPG world.

Visual direction:
- Fullscreen dark background: deep gradient #0a0200 → #1c0c00 → #3d1a00
- Warm amber/gold accents: #f59e0b, #fbbf24, #fde68a
- NO teal on this screen — this is the adventure world
- Mobile first, fullscreen — NO top header, NO white cards
- Content anchored to bottom, atmospheric space above

Screen content (bottom to top):

1. Bottom CTA button
   - "Continuar Aventura" — full width, amber #f59e0b, white text, 56px
   - Sword ⚔ icon on left

2. Season/phase progress above button
   - Row of dots: 15 dots total, 8 amber filled, 7 dark
   - "Temporada 2 · Fase 8 de 15"

3. Boss preview card (dark, red tones)
   - Skull icon in red
   - "BOSS DA TEMPORADA 2"
   - "Hakon, o Mercador Hostil"
   - "Ele te aguarda ao final desta temporada"
   - Dark red background #450a0a, red border

4. Chapter title (dominant, middle-upper area)
   - Small label top: "A1 · ALEMÃO" amber uppercase tracked
   - Large title: "Vila Medieval" white, 40px bold
   - Subtitle: "Um forasteiro sem memória aprende a sobreviver" amber/75 opacity

5. Atmospheric glow
   - Radial gradient amber glow at top center: rgba(217,119,6,0.15)
   - Subtle vignette at edges

Bottom navigation:
   Dark version — bg #0a0200
   Home | Aventura (active — amber) | Estudo | Vocabulário | Perfil

Mood: cinematic, epic, immersive. Like the opening of a medieval RPG game.
```

---

## Telas a fazer

- [ ] AdventureChapterScreen (mapa de temporadas)
- [ ] AdventurePhaseScreen (narrativa + exercícios)
- [ ] AdventureBossScreen (batalha HP)
- [ ] StudyScreen (sessão de estudo)
- [ ] VocabularyScreen (flashcards e favoritos)
- [ ] AccountScreen / Perfil
- [ ] HistoryScreen
