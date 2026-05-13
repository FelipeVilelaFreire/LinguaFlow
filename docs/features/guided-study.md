# 📘 Daily Study System (Core Tab) — "Today"

## 🎯 Objetivo

A aba **Today (Estudo Guiado)** é o coração da plataforma.

Ela responde a pergunta:

> **“O que eu preciso fazer HOJE para evoluir no idioma?”**

Essa aba deve ser:
- extremamente simples
- visualmente agradável
- fluida (transições suaves)
- rápida (sem fricção)

---

## 🧠 Filosofia

> "Menos escolha, mais execução"

O usuário NÃO deve pensar.
Ele apenas:
1. abre o app
2. clica em "Começar"
3. segue o fluxo

---

## 🧱 Estrutura da Página

## 📅 Header

- Título:
  `Day 07 — Restaurant Basics`

- Subtítulo:
  `~15 min session`

- Progress bar:
  - Lição
  - Vídeo
  - Reforço

---

## 🟢 1. Lesson (Core Learning)

### Objetivo:
Aprendizado ativo (input + output)

### Estrutura:

#### Step 1 — Input
- Mostrar frase (target language)
- Exemplo:
  `Ich hätte gern ein Wasser`

- Botão:
  `Show Translation`

#### Step 2 — Reveal
- Tradução aparece com animação suave
  `Eu gostaria de uma água`

#### Step 3 — Active Recall
- Mostrar:
  `Eu gostaria de uma água`

- Input:
  usuário escreve em alemão

#### Step 4 — Feedback
- ✔️ Correct
- ❌ Try again

#### Step 5 — Variation (opcional)
- Pequenas variações da frase

---

## 🎥 2. Video (Support)

### Objetivo:
Contexto real

### Estrutura:

- Card com:
  - título do vídeo
  - duração (~10min)

- Botão:
  `Watch Video`

- Ação:
  abrir link (YouTube)

---

## 🔵 3. Reinforcement (Practice)

### Objetivo:
Fixação rápida

### Tipos:

- tradução rápida
- completar frase
- escrever

### Duração:
3–5 min

---

## ✅ 4. Completion

- Tela simples:
  `Day Completed 🎉`

- Feedback:
  - streak atualizado
  - progresso avançado

---

# 🎨 Design & UX (CRÍTICO)

## ⚡ Princípio principal

> O app deve ser leve, fluido e recompensador

---

## 🔄 Transições (INSPIRAÇÃO: Duolingo)

### IMPORTANTE:
As transições são fundamentais para retenção.

---

## Tipos de transição:

### 1. Entre steps da lição
- slide horizontal
- duração: 200–300ms
- easing suave

---

### 2. Mostrar tradução
- fade + slight slide up
- sensação de “revelação”

---

### 3. Feedback (acerto/erro)
- micro animação:
  - shake (erro)
  - pop (acerto)

---

### 4. Progressão
- progress bar animando
- leve incremento visual

---

## 🧩 Componentização (React)

Usar componentes pequenos:

- `LessonCard`
- `PhraseDisplay`
- `TranslationReveal`
- `InputBox`
- `FeedbackBadge`
- `ProgressBar`
- `VideoCard`

---

## 🎨 Estilo Visual

### Cores:
- fundo: claro (#f9f9f9)
- texto: escuro (#111)
- destaque: verde (sucesso), vermelho (erro)

---

### Tipografia:
- fonte limpa (Inter)
- frase grande (foco)

---

### Layout:
- centralizado
- largura limitada
- espaçamento confortável

---

## 🧠 Micro UX (MUITO IMPORTANTE)

- clique sempre gera resposta visual
- nenhuma ação “morta”
- sempre feedback

---

## 🔥 Regra de ouro

> Se não for prazeroso usar, está errado

---

# 🤖 Diretrizes para Claude Code

## 🎯 Objetivo

Implementar essa aba com foco em:

- fluidez
- simplicidade
- responsividade
- UX moderna

---

## ⚠️ Regras obrigatórias

1. Usar React + Tailwind
2. Seguir arquitetura existente
3. Componentização clara
4. Código limpo e reutilizável
5. Priorizar UX sobre complexidade

---

## 🎬 Animações

Utilizar:
- CSS transitions (Tailwind)
- ou Framer Motion (preferencial)

---

## 📌 Implementar:

- fluxo completo da lição
- sistema de steps
- animações suaves
- progress tracking local

---

## 🚫 Não fazer:

- lógica complexa de backend
- gamificação pesada
- features extras

---

## 🏁 Resultado esperado

Uma experiência que:

- lembra o Duolingo em fluidez
- é mais direta e focada
- incentiva uso diário