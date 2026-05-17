@echo off
setlocal EnableExtensions

set "PROJECT_PATH=%~dp0.."
set "CONDA_ENV=linguaflow"

where wt >nul 2>nul
if %errorlevel% neq 0 (
  echo Windows Terminal nao encontrado. Abrindo comandos em janelas separadas.
  start "backend" cmd /k "cd /d %PROJECT_PATH%\backend && conda activate %CONDA_ENV% && python manage.py runserver 8001"
  start "shared-core" cmd /k "cd /d %PROJECT_PATH%\packages\shared-core && npm run dev"
  start "web" cmd /k "cd /d %PROJECT_PATH%\web && npm run dev"
  start "mobile" cmd /k "cd /d %PROJECT_PATH%\mobile && npm run start"
  exit /b 0
)

wt ^
  new-tab --title "backend" -d "%PROJECT_PATH%\backend" cmd /k "conda activate %CONDA_ENV% && python manage.py runserver 8001" ^
  ; split-pane --title "shared-core" -d "%PROJECT_PATH%\packages\shared-core" cmd /k "npm run dev" ^
  ; new-tab --title "web" -d "%PROJECT_PATH%\web" cmd /k "npm run dev" ^
  ; split-pane --title "mobile" -d "%PROJECT_PATH%\mobile" cmd /k "npm run start" ^
  ; new-tab --title "legacy-web" -d "%PROJECT_PATH%\frontend-web" cmd /k "npm run dev"
