# TODO

## Mock — Phase 1 sections precisam de revisão completa

A ordem das seções está errada e o conteúdo precisa ser reescrito para refletir o modelo definitivo.

### Ordem correta das seções (CLAUDE.md já atualizado)

1. `narrativa` — imersão, vocab aparece sem explicação
2. `revisao_srs` — narrativa + prática do vocab da fase anterior
3. `gramatica_narrativa` — NPC ensina explicitamente (estava na posição 4)
4. `pratica_aplicada` — prática intensa com NPC presente (estava na posição 3)
5. `reforco` — narrativa usa o que foi ensinado na S3
6. `obstaculo` — fechamento do arco + gate

### Arco narrativo correto para Fase 1

- S1: Você chega, Giovanni te aborda, ouve palavras sem entender
- S2: Giovanni passeia com você pelo borgo, revisa o vocab em conversa
- S3: Giovanni para na praça e ENSINA 'mi chiamo' explicitamente
- S4: Você vai ao mercado e USA 'mi chiamo' com Lucia (aplica o que aprendeu em S3)
- S5: Encontra Marco e Sofia nas ruas — gramática flui naturalmente
- S6: Guarda no portão — fechamento + gate

### Regras que o mock deve seguir

- Sem `fill_blank`, `translate`, `reveal` como exercícios
- Todo exercício = NPC fala → jogador responde ou demonstra compreensão
- Chat conversacional em TODAS as seções (o NPC nunca desaparece)
- `word_id` + `tier: "bronze"` nos exercícios de vocabulário
