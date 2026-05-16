# Admin Architecture

LinguaFlow now has two admin surfaces.

## 1. Django Admin

URL:

```txt
http://localhost:8001/admin/
```

Purpose:

- direct database maintenance
- content inspection
- user and permission management
- emergency edits

Admin registrations are split by app:

```txt
backend/apps/accounts/admin.py
backend/apps/learning/admin.py
backend/apps/goals/admin.py
backend/apps/progress/admin.py
```

## 2. React Admin

Folder:

```txt
frontend-admin/
```

URL:

```txt
http://localhost:5178
```

Purpose:

- operational dashboard
- user overview
- study area overview
- content coverage overview

It authenticates through the normal JWT login endpoint:

```txt
POST /api/auth/login/
```

Then it reads staff-only endpoints:

```txt
GET /api/admin-dashboard/summary/
GET /api/admin-dashboard/users/
GET /api/admin-dashboard/goals/
GET /api/admin-dashboard/content/
```

The backend class is:

```txt
backend/apps/accounts/admin_api.py
```

All React Admin endpoints require:

```py
IsAdminUser
```

So the user must be staff/superuser.

## Why This Split

Django Admin is best for direct model management.

React Admin is best for product-facing operations: metrics, monitoring, support, and quick investigation without exposing raw model forms as the primary experience.
