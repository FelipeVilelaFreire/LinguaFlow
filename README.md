# LinguaFlow

Plataforma de aprendizado de idiomas para estudo diario em situacoes reais.

## Estrutura

- `backend/`: Django + Django REST Framework.
- `frontend-web/`: React + Vite + Tailwind CSS.
- `frontend-admin/`: interface administrativa React.
- `docs/`: documentacao organizada por produto, conteudo, design, arquitetura e features.

## Documentacao

Comece por [`docs/README.md`](docs/README.md).

Documentos principais:

- Produto: [`docs/product/product-spec.md`](docs/product/product-spec.md)
- Conteudo ES A1: [`docs/content/es-a1/story.md`](docs/content/es-a1/story.md)
- Personagens ES A1: [`docs/content/es-a1/characters.md`](docs/content/es-a1/characters.md)
- Arquitetura backend: [`docs/architecture/backend.md`](docs/architecture/backend.md)
- Arquitetura frontend web: [`docs/architecture/frontend-web.md`](docs/architecture/frontend-web.md)

## Rodar Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_es_full
python manage.py runserver
```

API: `http://localhost:8000/api/`

## Rodar Frontend

```bash
cd frontend-web
npm install
npm run dev
```

App: `http://localhost:5173`
