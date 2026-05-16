# LinguaFlow Admin Architecture

## Purpose

`frontend-admin` is a separate React application for staff and superusers. It is not part of the learner-facing `frontend-web` app.

The admin surface has two layers:

- Django Admin at `/admin/` for direct database maintenance.
- React Admin at `http://localhost:5178` for a cleaner operational dashboard.

## Runtime

```txt
frontend-admin
  -> Vite React app
  -> talks to backend /api/admin-dashboard/*
  -> requires a staff/superuser JWT
```

Default API base:

```txt
http://localhost:8001/api
```

Override with:

```txt
VITE_API_BASE_URL=http://localhost:8001/api
```

## Folder Structure

```txt
frontend-admin/
  src/
    components/
      DataTable.tsx
      StatCard.tsx
    services/
      api.ts
    styles/
      index.css
    types/
      admin.ts
    App.tsx
    main.tsx
```

## Backend Contract

The React admin uses `AdminDashboardViewSet` in:

```txt
backend/apps/accounts/admin_api.py
```

Routes:

```txt
GET /api/admin-dashboard/summary/
GET /api/admin-dashboard/users/
GET /api/admin-dashboard/goals/
GET /api/admin-dashboard/content/
```

All routes use:

```py
permission_classes = [IsAdminUser]
```

So the logged user must have `is_staff=True`.

## Current Screens

### Dashboard

Shows high-level metrics:

- users
- staff users
- active goals
- total goals
- languages
- scenarios
- lessons
- study days
- phrases
- completions
- favorites
- progress entries

### Users

Shows recent users with:

- id
- username
- email
- staff status
- active status
- goal count
- completion count

### Areas

Shows study goals with:

- user
- source and target language
- current level
- target level
- duration
- routine
- progress
- streak

### Content

Shows:

- languages
- scenarios
- phrase counts by course and level
- lesson totals
- study day totals

## Django Admin

Each backend app owns its own admin registration:

```txt
backend/apps/accounts/admin.py
backend/apps/learning/admin.py
backend/apps/goals/admin.py
backend/apps/progress/admin.py
```

This keeps database maintenance close to each domain app.

## Commands

Install dependencies:

```powershell
cd LinguaFlow/frontend-admin
npm install
```

Run admin frontend:

```powershell
npm run dev
```

Open:

```txt
http://localhost:5178
```

Backend requirements:

```powershell
cd LinguaFlow/backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The same superuser works for Django Admin and React Admin.
