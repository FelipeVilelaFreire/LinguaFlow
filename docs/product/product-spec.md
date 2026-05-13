# Talkly — Product Spec

## Identidade

**Nome:** Talkly
**Tagline:** Aprenda idiomas vivendo a história
**Foco inicial:** Português → Alemão (A1)
**Público:** Dev solo agora. Futuro: equipe com professores criando conteúdo.

---

## Conceito Central

O Talkly resolve o gap do Duolingo: exercício aleatório sem explicação real.

- **Modo Estudo:** Duolingo com explicação gramatical antes dos exercícios
- **Modo Aventura:** tudo do Estudo com narrativa, emoção, itens e boss

Um único conteúdo. Um único progresso. Dois modos de viver a mesma jornada.

---

## Estrutura de Conteúdo

```
Capítulo (nível CEFR — ex: A1 = Vila Medieval)
  └── Temporada (ex: Chegada ao Vilarejo)
        └── Fase (ex: Saudações básicas — ~10 frases)
```

**Por fase:**
- Explicação gramatical/contextual breve
- ~10 frases
- Exercícios variados: múltipla escolha → preencher lacuna → digitar

**Por temporada (só Aventura):**
- 4 fases normais + 1 fase Boss
- Boss testa todas as frases das 4 fases anteriores

**Por capítulo:**
- 5 temporadas (~50 fases)
- Recompensa do boss final carrega para o próximo capítulo

---

## Os Dois Modos

### Modo Estudo
```
Explicação da frase/gramática
        ↓
Exercícios (múltipla escolha → lacuna → digitar)
        ↓
Fase concluída → próxima desbloqueada
        ↓
Temporada concluída → próxima temporada
```
- Sem narrativa
- Sem itens
- Sem boss
- Sem HP
- Limpo e direto — foco total no aprendizado

### Modo Aventura
```
Narrativa de entrada (contexto da história)
        ↓
Mesma explicação do Estudo
        ↓
Mesmos exercícios — com contexto da história
        ↓
Acerta frase → item desbloqueado no inventário
        ↓
Fase concluída → próxima no mapa
        ↓
Fase 5 da temporada = BOSS
  → Barra de HP do boss + barra de HP do jogador
  → Acerta → dano no boss
  → Erra → perde HP
  → Vence → recompensa + próxima temporada
  → Perde → refaz frases erradas → tenta de novo
```

---

## O Que É Igual nos Dois Modos

| Elemento | Estudo | Aventura |
|---|---|---|
| Conteúdo das fases | ✓ | ✓ |
| Explicação gramatical | ✓ | ✓ |
| Tipos de exercício | ✓ | ✓ |
| Progresso unificado | ✓ | ✓ |
| Narrativa | ✗ | ✓ |
| Itens/inventário | ✗ | ✓ |
| Boss com HP | ✗ | ✓ |

---

## Progressão Unificada

Uma métrica só independente do modo:

| Ação | O que avança |
|---|---|
| Completar fase | +frases vistas |
| Acertar exercício | +frases consolidadas |
| Passar na temporada | +temporada concluída |
| Qualquer atividade no dia programado | +streak |

---

## Rotina de Estudo

O usuário define no onboarding:
- Dias da semana (ex: Seg, Qua, Sex)
- Duração da sessão (15 / 30 / 45 / 60 min)
- Ou modo avulso (sem agenda fixa)

**Nos dias programados:** app mostra "Hoje é dia de estudo" na Home.
**Nos dias de folga:** app disponível mas não cobra. Zero punição. Vocabulário livre para revisar.
**Streak:** quebra só se não fizer nada nos dias programados.

---

## Os 4 Fluxos de Usuário

### Fluxo 1 — Só Estudo
```
Onboarding → modo Estudo
      ↓
Home → sessão disponível
      ↓
Fase: explicação + exercícios
      ↓
Conclui temporada → próxima desbloqueada
      ↓
(Sem boss, sem narrativa, sem itens)
```

### Fluxo 2 — Só Aventura
```
Onboarding → modo Aventura
      ↓
AdventureScreen → tela épica
      ↓
Transição imersiva → mapa
      ↓
Fase: narrativa + explicação + exercícios + itens
      ↓
Fase 5 → Boss com HP
      ↓
Vence → recompensa → próxima temporada
```

### Fluxo 3 — Estudo → Aventura
```
Usuário estava no Estudo, decide migrar
      ↓
App detecta progresso e pergunta:

"Você já completou o equivalente à Temporada 1 e 2."

[ Jogar desde o início ]
→ passa pelas fases já feitas mais rápido
→ menos exercícios, mais narrativa
→ vive a história completa

[ Continuar da Temporada 3 ]
→ app mostra resumo narrativo das temporadas 1 e 2
→ entra direto na Temporada 3
→ inventário populado retroativamente com frases já aprendidas
```

### Fluxo 4 — Aventura → Estudo
```
Usuário na Aventura, não quer mais narrativa
      ↓
Perfil → "Usar modo Estudo"
      ↓
Progresso carrega completamente
Fases anteriores: concluídas
Fase atual: continua de onde parou, sem narrativa
      ↓
Boss da temporada vira: série de exercícios (sem HP)
      ↓
Pode voltar para Aventura a qualquer momento
```

---

## Telas do App

### Fora das abas
- **Auth:** login + cadastro numa tela só
- **Onboarding:** idioma base → idioma alvo → nível atual → meta → rotina → modo (Estudo ou Aventura)

### 5 Abas

**Home**
- Progresso do capítulo atual (barra + %)
- Streak
- Botão principal: Continuar Aventura / Sessão do dia
- Stats: frases aprendidas, dias seguidos, nível
- Badge "Hoje é dia de estudo" quando aplicável

**Aventura**
- AdventureScreen: intro épica fullscreen (escura, âmbar)
- AdventureChapterScreen: lista de temporadas → mapa de fases
- Fase: narrativa → exercícios → conclusão
- Boss: UI especial com barras de HP

**Estudo**
- Sessão do dia
- Revisão das frases vistas na Aventura (ou direto pelo modo Estudo)
- Tipos: múltipla escolha → lacuna → digitar
- Conclusão com streak

**Vocabulário**
- Frases favoritas
- Flashcard flip para revisão
- Filtro por temporada/capítulo

**Perfil**
- Nome e conta
- Área ativa + trocar modo (Estudo/Aventura)
- Histórico de sessões por mês
- Configurações: idioma da interface, logout

---

## Loop Central de Aprendizado

```
Aventura/Estudo → conhece frases novas com contexto
        ↓
Exercícios → pratica ativamente
        ↓
Dias seguintes → estudo revisa as mesmas frases
        ↓
Boss (Aventura) / Conclusão de temporada (Estudo) → prova que dominou
        ↓
Próxima temporada desbloqueada
```

---

## MVP vs Futuro

| MVP | Futuro |
|---|---|
| Auth + Onboarding | Perfil com foto |
| Modo Estudo completo | Inventário com efeitos reais |
| Aventura com temporadas + boss | Poderes por categoria gramatical |
| Conteúdo real A1 alemão (5 temporadas) | Áudio e pronúncia |
| Vocabulário/favoritos | Multiplayer / ranking |
| Perfil básico + troca de modo | A2, B1, B2... |
| Migração Estudo ↔ Aventura | Professores criando conteúdo |

---

## Princípios que Não Mudam

1. **Um conteúdo, dois modos** — nunca fragmentar o progresso
2. **Explicação antes do exercício** — diferencial real do Duolingo
3. **Boss não deixa mentir** — só na Aventura, testa de verdade
4. **Dias de folga não punem** — streak quebra só nos dias programados
5. **Migração preserva progresso** — trocar de modo nunca perde o que foi feito
6. **Mobile first** — desktop é aprimoramento
