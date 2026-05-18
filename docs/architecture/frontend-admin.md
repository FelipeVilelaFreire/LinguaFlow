# LinguaFlow Admin Architecture

## Purpose

`admin/` is the separate React application for staff and superusers. It is not part of the learner-facing `web/` app.

The admin surface has two layers:

- Django Admin at `/admin/` for direct database maintenance.
- React Admin at `http://localhost:5178` for operational workflows, content inspection, adventure entities and business planning.

## Runtime

```txt
admin/
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

## Current Structure

```txt
admin/
  src/
    admin/
      AdminApp.tsx
      apps/
        dashboard/config.tsx
        users/config.tsx
        goals/config.tsx
        content/config.tsx
        learning/config.tsx
        adventure/config.tsx
        progress/config.tsx
        business-plan/config.tsx
        system/config.tsx
      ini/config/endpoints.ts
      shared/
        components/
        services/
        types.ts
        utils/
    styles/index.css
```

## Rules

- Admin remains separate from `web/`.
- Admin apps are config-driven under `admin/src/admin/apps/**`.
- Visible admin text comes from `STRINGS.admin.*` in shared-core.
- Admin CSS uses `--admin-*` variables.
- No Tailwind in `admin/`.
- API endpoints are centralized in `admin/src/admin/ini/config/endpoints.ts`.
- Backend endpoints remain protected by `IsAdminUser`.

## Current Apps

- Dashboard.
- Users.
- Goals/areas.
- Content catalog.
- Learning/study.
- Adventure, including phases, characters and items.
- Progress.
- Business plan.
- System/Django app map.

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
GET /api/admin-dashboard/learning-detail/
GET /api/admin-dashboard/adventure/
GET /api/admin-dashboard/progress/
```

All routes use:

```py
permission_classes = [IsAdminUser]
```

## Commands

Install dependencies:

```powershell
cd LinguaFlow/admin
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

Build:

```powershell
npm run build
```

Backend requirements:

```powershell
cd LinguaFlow/backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The same superuser works for Django Admin and React Admin.

## Remaining Admin Work

- Add real CRUD mutations per entity.
- Add generic detail page.
- Add form builder.
- Add trash/history apps after backend soft-delete/audit endpoints exist.
- Turn `business-plan` from static scenario table into editable assumptions and cashflow model.
