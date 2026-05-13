# Talkly — Roadmap 1 Semana

## O que já está pronto
- Auth, design system, tema teal, roteamento manual
- Adventure: intro → transição imersiva → mapa de fases → narrativa → exercício → boss → conclusão
- Home, Study, Vocabulary, Profile (funcionais)
- Backend: Django + DRF, auth, models Adventure (Chapter → Phase → Phrase)
- CLAUDE.md com design system completo para uso em qualquer IA

---

## Dia 1 — Temporadas no backend
> Desbloqueia tudo. Sem isso nada adianta.

A estrutura atual é `Chapter → Phase`. Precisa virar `Chapter → Season → Phase`.

- [ ] Criar model `AdventureSeason` no Django
- [ ] Atualizar serializers e views da adventure API
- [ ] Rodar migration
- [ ] Atualizar seed do A1 com 5 temporadas reais (nomes, narrativa de cada uma)

**Entregável:** API retornando `chapter → seasons → phases` funcionando.

---

## Dia 2 — UI de Temporadas no frontend
> Com o backend pronto, mostrar temporadas antes do mapa de fases.

- [ ] `AdventureChapterScreen` mostra lista de temporadas (cards com progresso)
- [ ] Clicar numa temporada abre o mapa de fases daquela temporada
- [ ] Temporadas bloqueadas até completar a anterior

**Entregável:** Navegação completa `intro → temporadas → mapa → fase`.

---

## Dia 3 — Batalha com o Boss
> A fase mais impactante. Diferencia o Talkly de qualquer outro app.

- [ ] UI especial para fases boss: barra de HP do inimigo + HP do jogador
- [ ] Acertou → animação de dano no boss
- [ ] Errou → animação de dano no jogador
- [ ] Boss derrotado → tela de vitória dramática com a recompensa da temporada

**Entregável:** Boss funcionando de forma diferente das fases normais.

---

## Dia 4 — Conteúdo real do A1
> Seed completo com conteúdo de verdade, não dados de teste.

- [ ] 5 temporadas com nome e narrativa coerente
- [ ] 10 fases por temporada = 50 fases no A1
- [ ] Cada fase com ~15 frases reais de alemão A1
- [ ] Narrativa de cada fase conectada à história da temporada
- [ ] Boss da Temporada 5 com frases de revisão do nível inteiro

**Entregável:** A1 jogável do início ao fim com conteúdo real.

---

## Dia 5 — HomeScreen + Perfil
> Com conteúdo existindo, a Home fica rica de verdade.

- [ ] HomeScreen redesenhada (prompt já gerado em docs/archive/design-system-context-legacy.md)
- [ ] Perfil: meta ativa, histórico de fases, streak real
- [ ] Onboarding: fluxo de criação de meta revisado e polido

**Entregável:** App com cara de produto, não de protótipo.

---

## Dia 6 — Vocabulário + Estudo Guiado
> As duas abas que complementam a aventura.

- [ ] Flashcards funcionando com frases aprendidas na aventura
- [ ] Favoritos salvando e carregando corretamente
- [ ] Estudo guiado do dia conectado ao progresso real do usuário

**Entregável:** Loop completo — aprende na aventura → revisa no vocabulário → pratica no estudo.

---

## Dia 7 — Polish, testes e deploy
> Não adicionar nada novo. Só fechar.

- [ ] Testar todos os fluxos do início ao fim
- [ ] Corrigir o que quebrar
- [ ] Revisar transições e estados vazios
- [ ] Deploy (se tiver servidor configurado)

**Entregável:** App funcionando de ponta a ponta, pronto para mostrar.

---

## Regras para não perder tempo

**Não faça antes da hora**
Inventário, poderes, magias, sistema de atributos — isso é semana 2+. Está documentado em `docs/product/game-concept.md`. Não vai sumir.

**Ordem importa**
Backend antes do frontend. Se o Dia 1 não estiver sólido, o Dia 2 vira retrabalho.

**Uma coisa por dia**
Cada dia tem um entregável claro. Não misture dias.

**Divida o trabalho com a IA corretamente**
- Decisões de conteúdo (narrativa, nomes, frases) → você
- Código (models, views, componentes) → Claude

---

## O que vem depois (Semana 2+)
Documentado em `docs/product/game-concept.md`:
- Sistema de inventário (palavras aprendidas = itens desbloqueados)
- Alimentação como vocabulário passivo (Apfel, Wasser, Brot)
- Poderes por categoria gramatical
- Atributos do personagem (HP, Stamina, Power, Wisdom)
- Conteúdo A2, A3, B1...
