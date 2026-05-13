# 🧠 Product Logic Specification — Language Learning App

## 📌 Objetivo

Definir a lógica completa do sistema para evitar ambiguidades na implementação.

Este documento NÃO trata de design.
Apenas comportamento, fluxo e regras.

---

# 🌍 Conceitos Globais

## Usuário possui:

* source_language (ex: PT)
* target_language (ex: DE)
* goal (nível + duração)
* progresso

---

## Goal

* nível alvo (A1, A2…)
* duração (ex: 90 dias)
* start_date
* end_date
* total_phrases

---

## Progresso

Baseado em:

* frases aprendidas
* lições concluídas

---

# 🔄 Fluxo Principal

1. Usuário entra no app
2. Se não tiver goal → onboarding
3. Se tiver goal → vai para "Today"

---

# 📱 TELAS

---

# 1. Onboarding

## Objetivo:

Criar configuração inicial

## Passos:

### Step 1:

Selecionar source_language

### Step 2:

Selecionar target_language

### Step 3:

Selecionar:

* nível alvo
* duração

### Step 4:

Confirmar

## Ação final:

Criar Goal automaticamente

---

# 2. Home

## Objetivo:

Visão geral rápida

## Exibir:

* goal atual
* progresso (%)
* dias restantes
* streak
* lições concluídas

## Ação principal:

Ir para "Today"

---

# 3. Today (CORE)

## Objetivo:

Executar o estudo do dia

---

## Estrutura:

### Step 1 — Lesson

* carregar frases do dia
* executar fluxo de aprendizado

---

### Step 2 — Video

* exibir link
* usuário pode abrir ou pular

---

### Step 3 — Practice

* exercícios rápidos
* baseados nas frases do dia

---

## Regra:

Usuário pode completar mesmo sem vídeo

---

## Conclusão:

Marcar dia como completo

Atualizar:

* progresso
* streak

---

# 4. Lesson

## Objetivo:

Aprender frases

---

## Fluxo por frase:

1. Mostrar frase (target)
2. Usuário tenta entender
3. Revelar tradução
4. Mostrar frase source
5. Usuário escreve target
6. Validar resposta

---

## Regras:

* resposta pode ser aproximada (não precisa exata inicialmente)
* usuário pode avançar

---

# 5. Practice

## Objetivo:

Reforço rápido

---

## Tipos:

* traduzir
* completar
* escrever

---

## Regra:

Baseado nas frases do dia

---

# 6. Scenarios

## Objetivo:

Explorar por contexto

---

## Estrutura:

* lista de cenários
* cada cenário contém frases

---

## Ações:

* visualizar frase
* revelar tradução
* favoritar

---

# 7. Vocabulary

## Objetivo:

Revisão pessoal

---

## Conteúdo:

* frases favoritas

---

## Ações:

* remover
* revisar

---

# 8. Profile

## Objetivo:

Configurações do usuário

---

## Exibir:

* idiomas
* meta
* progresso
* stats

---

## Ações:

* editar meta
* resetar progresso (opcional)

---

# 📊 Regras de Progresso

## Cálculo:

progress = frases_aprendidas / total_frases

---

## Atualização:

Ao completar "Today":

* incrementar frases aprendidas
* incrementar lições
* atualizar %

---

# 🔥 Regras Importantes

* usuário NÃO pode ficar travado
* sempre pode avançar
* foco em fluxo contínuo

---

# 🚫 Fora do escopo (por enquanto)

* autenticação complexa
* IA avançada
* social features
* gamificação pesada

---

# 🎯 Objetivo final

Sistema simples, funcional e utilizável diariamente
