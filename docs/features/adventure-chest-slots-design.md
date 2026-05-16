# Adventure Chest Slots Design

Registro da decisao de produto/design para a tela `/aventura/baus`.

## Modelo de baus

O LinguaFlow deve usar um modelo inspirado em jogos como Clash Royale, mas sem copiar a limitacao mais frustrante:

- O jogador pode guardar quantos baus quiser.
- Apenas 2 baus podem estar com timer ativo ao mesmo tempo.
- Um bau `ready` ainda ocupa slot ate ser coletado.
- Os baus guardados continuam visiveis e nao sao descartados quando os slots estao cheios.
- Ao iniciar abertura, o bau guardado deve subir visualmente para um dos 2 slots.

Essa regra evita perda de recompensa por falta de espaco, mas ainda cria uma decisao leve de gerenciamento: escolher quais baus abrir agora.

## Referencia: Clash Royale

Clash Royale usa slots limitados de bau:

- O jogador ganha baus ao jogar.
- Os baus entram em slots visiveis.
- Cada bau tem um tempo de desbloqueio.
- O jogador escolhe um bau para iniciar o timer.
- Quando o timer acaba, o bau fica pronto para abrir.

A forca do design vem menos da regra em si e mais do polimento:

- artes 2D fortes para baus, cartas, moedas e recompensas;
- UI com profundidade, sombras, bordas grossas e brilhos;
- animacoes curtas com entrada, pulso, abertura e revelacao;
- audio, vibracao e particulas para reforcar feedback.

## Direcao para LinguaFlow

Nao devemos copiar Clash Royale ou Duolingo 1:1. A melhor direcao e um estilo proprio:

- aventura calma;
- RPG de aprendizado;
- baus bonitos, mas menos agressivos visualmente;
- slots claros e legiveis;
- microanimacoes suaves;
- recompensa com sensacao de conquista;
- consistencia com `strings.xxx` e `routes.xxx`.

O objetivo e parecer um produto de aprendizado com camada de jogo, nao um clone de jogo mobile.

## Chance de espelhar o nivel visual

Usando apenas React e CSS, sem assets dedicados:

- Nota realista: 5/10.
- Conseguimos layout, slots, timers, brilho, movimento e feedback basico.
- Ainda tende a parecer um web app gameficado.

Usando React, CSS e SVGs/ilustracoes simples:

- Nota realista: 6.5/10.
- Ja melhora bastante a identidade visual.
- Ainda falta riqueza artistica e motion mais elaborado.

Usando React, assets bons, particulas, sons e animacoes:

- Nota realista: 8/10.
- A experiencia pode ficar com cara de jogo de verdade.
- E o melhor custo-beneficio para o LinguaFlow.

Igual ao nivel de Clash Royale ou Duolingo:

- Nota realista: 9-10/10.
- Exige tempo dedicado para ilustracao, motion design, audio, UX e refinamento.
- Nao e impossivel, mas nao vem so de programacao.

## Implementacao atual

Estado desejado da tela:

- topo com 2 slots de abertura;
- baus `opening` e `ready` aparecem nesses slots;
- lista de baus `stored` aparece abaixo;
- botao de iniciar abertura fica desabilitado quando os 2 slots estao ocupados;
- animacao `chest-slot-arrive` mostra o bau entrando no slot.

Regra de backend:

- `stored`: bau guardado, nao ocupa slot;
- `opening`: bau com timer ativo, ocupa slot;
- `ready`: bau pronto para coletar, ocupa slot;
- `claimed`: bau coletado, sai dos ativos;
- `discarded`: bau descartado, sai dos ativos.

## Proximas melhorias possiveis

- Criar assets proprios de bau por raridade.
- Adicionar particulas leves quando o bau entra no slot.
- Adicionar estado visual diferente para bau pronto.
- Adicionar som curto ao iniciar abertura e ao coletar.
- Melhorar a revelacao da recompensa com uma tela pequena de premio.
- Adicionar tooltip ou texto compacto explicando os 2 slots.
