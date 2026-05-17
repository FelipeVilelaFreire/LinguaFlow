@echo off
chcp 65001 > nul
title Setup {{DISPLAY_NAME}} - Aguarde...

:: ==========================================
:: {{DISPLAY_NAME}} — One-time setup script
:: Stack: Django + shared-core + Next.js + React Native (Expo)
:: ==========================================

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
for %%I in ("%SCRIPT_DIR%") do set "SCRIPT_FOLDER=%%~nxI"
if /I "%SCRIPT_FOLDER%"=="bats" (
    for %%I in ("%SCRIPT_DIR%\..") do set "PROJECT_PATH=%%~fI"
) else (
    set "PROJECT_PATH=%SCRIPT_DIR%"
)

echo.
echo ==========================================
echo [1/5] Criando ambiente Conda ({{CONDA_ENV}})...
echo ==========================================
call conda create -n {{CONDA_ENV}} python=3.12 -y

echo.
echo ==========================================
echo [2/5] Instalando dependencias do backend...
echo ==========================================
cd /d "%PROJECT_PATH%\backend"
call conda activate {{CONDA_ENV}}
pip install -r requirements.txt
if not exist .env copy .env.example .env

echo.
echo ==========================================
echo [3/5] Criando banco {{DB_NAME}} e rodando migrations...
echo ==========================================
psql -U postgres -c "CREATE DATABASE {{DB_NAME}};" 2>nul
python manage.py migrate

echo.
echo ==========================================
echo [4/5] Buildando shared-core (THE BRAIN)...
echo ==========================================
cd /d "%PROJECT_PATH%\packages\shared-core"
call yarn install
call yarn build

echo.
echo ==========================================
echo [5/5] Instalando dependencias do web e mobile...
echo ==========================================
cd /d "%PROJECT_PATH%\web"
if not exist .env.local copy .env.example .env.local
call npm install

cd /d "%PROJECT_PATH%\mobile"
if not exist .env copy .env.example .env
call npm install

:: ============================================================
:: --- ADMIN BLOCK START ---
:: CLAUDE: if Admin panel: no  →  delete this entire block (from START to END).
:: CLAUDE: if Admin panel: yes →  keep this block.
:: ============================================================
echo.
echo ==========================================
echo [Extra] Instalando dependencias do admin (frontend/)...
echo ==========================================
cd /d "%PROJECT_PATH%\frontend"
if not exist .env copy .env.example .env
call npm install
:: --- ADMIN BLOCK END ---
:: ============================================================

echo.
echo ==========================================
echo INSTALACAO CONCLUIDA!
echo Criando o superusuario do Django agora...
echo ==========================================
cd /d "%PROJECT_PATH%\backend"
python manage.py createsuperuser

echo.
echo ==========================================
echo Tudo pronto. Abrindo ambiente de trabalho...
echo ==========================================
pause

:: ============================================================
:: Windows Terminal layout:
::   Tab 1: Claude
::   Tab 2 "backend+core": Backend (top) + Shared-core watch (bottom)
::   Tab 3 "web+mobile":   Web (top) + Mobile (bottom)
::   Tab 4 "admin":        Admin (only if Admin panel: yes)
::
:: CLAUDE: if Admin panel: no  →  remove the last `; new-tab ... frontend ...` line.
:: CLAUDE: if Admin panel: yes →  keep all lines below.
:: ============================================================
wt -d "%PROJECT_PATH%" cmd /k "claude" ^
   ; new-tab --title "backend+core" -d "%PROJECT_PATH%\backend" cmd /k "conda activate {{CONDA_ENV}} && python manage.py runserver" ^
   ; split-pane -V -d "%PROJECT_PATH%\packages\shared-core" cmd /k "yarn dev" ^
   ; new-tab --title "web+mobile" -d "%PROJECT_PATH%\web" cmd /k "npm run dev" ^
   ; split-pane -V -d "%PROJECT_PATH%\mobile" cmd /k "npx expo start" ^
   ; new-tab --title "admin" -d "%PROJECT_PATH%\frontend" cmd /k "npm run dev"

exit
