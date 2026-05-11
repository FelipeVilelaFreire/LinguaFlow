# TODO

## Modelo conversacional — regras definitivas

Todo exercício do Talkly segue um único padrão:

```
NPC fala → jogador escolhe o que DIZER → NPC reage
```

### Regras invioláveis

- Todo `multiple_choice` tem `npc` (quem fala) e `npc_reaction` (reação ao acerto)
- Opções são sempre o que o jogador DIRIA — nunca traduções soltas
- **Exceção S1 (narrativa)**: exercícios de compreensão inicial — opções em português porque o player ainda não sabe o idioma
- Sem `fill_blank`, `translate`, `reveal` como exercícios — apenas como elementos narrativos se necessário
- O NPC nunca desaparece — todas as 6 seções são conversação

### Ordem das seções (definitiva)

1. `narrativa` — imersão, você OUVE sem entender, exercícios de compreensão
2. `revisao_srs` — NPC passeia com você, revisa vocab anterior em conversa
3. `gramatica_narrativa` — NPC ENSINA explicitamente na história
4. `pratica_aplicada` — você USA o que aprendeu com pessoas novas
5. `reforco` — gramática flui naturalmente, menos aula, mais vida
6. `obstaculo` — fechamento do arco + gate (errar trava)

### Próximas fases a escrever

- Fase 2: Ostessa Carmela — aiuto, per favore, dove, taverna, mangiare — Grammar: dov'è
- Fase 3: Oste Stefano — pane, acqua, vino, formaggio, buono — Grammar: vorrei
- ... (fases 4–25 seguem o mesmo modelo conversacional)

### Fases automáticas vs. manuscritas

- `adventurePhaseMock.ts` = fases manuscritas (ricas, conversacionais)
- `phaseContentMock.ts` = fases 2–25 geradas automaticamente (protótipo)
- Quando uma fase for escrita manualmente, adicionar em `PHASES_CONTENT` em `adventurePhaseMock.ts`
