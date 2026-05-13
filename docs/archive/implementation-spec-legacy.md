# ⚙️ INSTRUÇÕES PARA IMPLEMENTAÇÃO

## 📌 Contexto

Este projeto é uma plataforma de aprendizado de idiomas focada em uso diário e situações reais.

O sistema deve ser:
- simples
- rápido
- funcional
- escalável

---

## 🧱 Stack obrigatória

### Frontend
- React
- Tailwind CSS
- Seguir arquitetura já existente do projeto (IMPORTANTE)
- Utilizar padrões de componentização (React Bits ou similar)

### Backend
- Django
- Django REST Framework
- API REST

---

## ❗ REGRAS IMPORTANTES

1. NÃO reinventar arquitetura frontend
2. Seguir estrutura já existente do projeto
3. Código deve ser modular e limpo
4. Evitar complexidade desnecessária
5. Priorizar funcionalidade sobre perfeição visual

---

## 🎯 FUNCIONALIDADES A IMPLEMENTAR

---

### 1. Sistema de Idiomas

O sistema deve suportar múltiplos idiomas:

- PT
- EN
- ES
- DE

Cada frase deve conter:
- source_language
- target_language
- source_text
- target_text
- categoria (opcional)

---

### 2. Modelos (Django)

Criar modelos:

#### Language
- code (PT, EN, ES, DE)
- name

#### Phrase
- source_language
- target_language
- source_text
- target_text
- category

#### UserProgress
- user
- phrase
- status (new, learning, mastered)

#### Favorite
- user
- phrase

---

### 3. API Endpoints

Criar endpoints:

- GET /phrases
- POST /phrases
- GET /phrases?category=
- POST /favorites
- GET /favorites
- GET /progress

---

### 4. Frontend - Estrutura

Criar layout com:

#### Sidebar
- Home
- Estudo Guiado
- Cenários
- Vocabulário

---

### 5. Página Estudo Guiado

Funcionalidade:

- mostrar frase
- botão: mostrar tradução
- botão: próxima
- alternar direção:
  - source → target
  - target → source

---

### 6. Página Cenários

- listar categorias
- clicar → ver frases daquele cenário

---

### 7. Página Vocabulário

- listar favoritos
- permitir revisão

---

### 8. Interações

- botão para favoritar frase
- feedback visual simples

---

## 🎨 UI / Design

- usar Tailwind
- layout limpo
- foco no conteúdo
- evitar excesso de cores
- componentes simples

---

## ⚡ PRIORIDADES

1. Estudo guiado funcionando
2. Sistema de frases
3. Favoritos
4. Cenários

---

## 🚫 NÃO FAZER AGORA

- autenticação complexa
- IA avançada
- animações complexas
- gamificação

---

## 🎯 OBJETIVO FINAL

Criar uma aplicação utilizável diariamente para aprendizado de idiomas, com foco em simplicidade, clareza e funcionalidade.