# 📚 Content Generation & Population System

## 📌 Objetivo

Criar um sistema no backend responsável por:

1. Gerar conteúdo educacional (frases, lições, cenários)
2. Popular automaticamente o banco de dados
3. Simular um curso completo de idioma

---

# 🧠 Filosofia

O conteúdo deve ser:

* prático
* baseado em situações reais
* progressivo (A1 → A2)
* reutilizável

---

# 🗂 Estrutura de Pastas

```
backend/
  content/
    generators/
    seeds/
    scenarios/
```

---

# 🧱 Estrutura de Conteúdo

---

## 1. Cenários

Cada cenário representa um contexto real.

Exemplos:

* restaurant
* market
* transport
* university
* housing

---

## 2. Frases

Cada frase deve conter:

* source_language
* target_language
* source_text
* target_text
* scenario
* difficulty (A1, A2…)

---

## 3. Lições

Cada lição contém:

* lista de frases
* tema (ex: pedir comida)
* ordem progressiva

---

## 4. Study Days

Cada dia contém:

* 1 lição
* 1 vídeo (opcional)
* exercícios baseados nas frases

---

# 🤖 Geração de Conteúdo (IA)

O sistema deve gerar conteúdo automaticamente.

---

## Regras para IA:

A IA deve agir como:

> um professor de idiomas focado em situações reais

---

## Exemplo de geração:

### Input:

* idioma: alemão
* nível: A1
* cenário: restaurante

---

### Output esperado:

10–20 frases úteis, como:

* “Ich hätte gern ein Wasser”
* “Die Rechnung, bitte”

---

## Regras:

* frases curtas
* uso real
* evitar frases genéricas
* incluir variações

---

# 🌱 Sistema de Seeds

Criar arquivos de população:

```
backend/content/seeds/
  seed_german_a1.py
  seed_scenarios.py
```

---

## seed_scenarios.py

* cria cenários básicos

---

## seed_german_a1.py

* cria frases A1
* organiza por cenário
* cria lições
* cria study days

---

# ⚙️ Execução

Criar comando Django:

```
python manage.py seed_content
```

---

## Esse comando deve:

1. Criar cenários
2. Criar frases
3. Criar lições
4. Criar study days

---

# 📊 Volume de Conteúdo

Para A1:

* ~300 frases
* 20–30 lições
* 30–60 study days

---

# 🎯 Qualidade do Conteúdo

* deve parecer um curso real
* não apenas frases aleatórias
* progressão lógica

---

# ⚠️ Regras Importantes

* evitar duplicação
* manter consistência
* manter contexto

---

# 🚀 Evolução futura

* geração dinâmica com IA
* personalização por usuário
* ajuste de dificuldade

---

# 🏁 Resultado esperado

Um sistema onde:

* o backend já vem populado
* o usuário já pode estudar imediatamente
* o conteúdo é rico e estruturado
