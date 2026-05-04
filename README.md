# LinguaFlow

Plataforma de aprendizado de idiomas para estudo diário em situações reais.

## Estrutura

- `backend/`: Django + Django REST Framework.
- `frontend-web/`: React + Vite + Tailwind CSS.
- `docs/`: especificações do produto e arquitetura.

## Rodar Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_content
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
