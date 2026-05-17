@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul
title LinguaFlow setup from zero

rem ============================================================
rem LinguaFlow - one-time setup from zero
rem Target architecture:
rem   backend/              Django source of truth
rem   packages/shared-core/ Shared business logic
rem   web/                  Next.js render-only app
rem   mobile/               Expo render-only app
rem   frontend-web/         Legacy Vite app kept during migration
rem ============================================================

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
for %%I in ("%SCRIPT_DIR%\..") do set "PROJECT_PATH=%%~fI"

set "CONDA_ENV=linguaflow"
set "PYTHON_VERSION=3.12"
set "BACKEND_PORT=8001"

echo.
echo ============================================================
echo LinguaFlow - setup do zero
echo Projeto: "%PROJECT_PATH%"
echo Conda env: %CONDA_ENV%
echo ============================================================

call :require_command conda "Conda nao encontrado no PATH. Abra pelo Anaconda Prompt ou rode conda init primeiro."
if errorlevel 1 exit /b 1

call :require_command npm "npm nao encontrado no PATH. Instale Node.js LTS antes de continuar."
if errorlevel 1 exit /b 1

echo.
echo [1/7] Preparando ambiente Conda...
call conda env list | findstr /R /C:"^%CONDA_ENV% " /C:"^%CONDA_ENV%$" >nul 2>nul
if errorlevel 1 (
  echo Criando env "%CONDA_ENV%" com Python %PYTHON_VERSION%...
  call conda create -n %CONDA_ENV% python=%PYTHON_VERSION% -y
  if errorlevel 1 (
    echo ERRO: falha ao criar o ambiente Conda "%CONDA_ENV%".
    exit /b 1
  )
) else (
  echo Env "%CONDA_ENV%" ja existe.
)

call conda activate %CONDA_ENV%
if errorlevel 1 (
  echo ERRO: nao foi possivel ativar "%CONDA_ENV%".
  exit /b 1
)

echo.
echo [2/7] Instalando backend Django...
pushd "%PROJECT_PATH%\backend"
if not exist requirements.txt (
  echo ERRO: backend\requirements.txt nao encontrado.
  popd
  exit /b 1
)
python -m pip install --upgrade pip
if errorlevel 1 (
  echo ERRO: nao foi possivel atualizar pip.
  popd
  exit /b 1
)
pip install -r requirements.txt
if errorlevel 1 (
  echo ERRO: pip install -r requirements.txt falhou.
  popd
  exit /b 1
)
if exist .env.example if not exist .env (
  copy .env.example .env >nul
  echo Criado backend\.env a partir de backend\.env.example.
)
popd

echo.
echo [3/7] Rodando migrations do backend...
pushd "%PROJECT_PATH%\backend"
python manage.py migrate
if errorlevel 1 (
  echo ERRO: python manage.py migrate falhou.
  popd
  exit /b 1
)
popd

echo.
echo [4/7] Instalando e buildando shared-core...
pushd "%PROJECT_PATH%\packages\shared-core"
call npm install
if errorlevel 1 (
  echo ERRO: npm install em packages\shared-core falhou.
  popd
  exit /b 1
)
call npm run build
if errorlevel 1 (
  echo ERRO: npm run build em packages\shared-core falhou.
  popd
  exit /b 1
)
popd

echo.
echo [5/7] Instalando web Next.js...
pushd "%PROJECT_PATH%\web"
if exist .env.example if not exist .env.local (
  copy .env.example .env.local >nul
  echo Criado web\.env.local a partir de web\.env.example.
)
call npm install
if errorlevel 1 (
  echo ERRO: npm install em web falhou.
  popd
  exit /b 1
)
popd

echo.
echo [6/7] Instalando mobile Expo...
pushd "%PROJECT_PATH%\mobile"
if exist .env.example if not exist .env (
  copy .env.example .env >nul
  echo Criado mobile\.env a partir de mobile\.env.example.
)
call npm install
if errorlevel 1 (
  echo ERRO: npm install em mobile falhou.
  popd
  exit /b 1
)
popd

echo.
echo [7/7] Instalando frontend-web legado...
if exist "%PROJECT_PATH%\frontend-web\package.json" (
  pushd "%PROJECT_PATH%\frontend-web"
  if exist .env.example if not exist .env (
    copy .env.example .env >nul
    echo Criado frontend-web\.env a partir de frontend-web\.env.example.
  )
  call npm install
  if errorlevel 1 (
    echo ERRO: npm install em frontend-web falhou.
    popd
    exit /b 1
  )
  popd
) else (
  echo frontend-web nao encontrado; pulando legado.
)

echo.
echo ============================================================
echo Setup concluido.
echo.
echo Arquitetura pronta:
echo - backend: fonte da verdade em Django
echo - packages\shared-core: logica compartilhada
echo - web: app Next.js novo
echo - mobile: app Expo novo
echo - frontend-web: legado temporario durante a migracao
echo.
echo Comandos de desenvolvimento:
echo - bats\dev.bat
echo - backend: cd backend ^& conda activate %CONDA_ENV% ^& python manage.py runserver %BACKEND_PORT%
echo - shared-core: cd packages\shared-core ^& npm run dev
echo - web: cd web ^& npm run dev
echo - mobile: cd mobile ^& npm run start
echo ============================================================
echo.

set /p OPEN_DEV="Abrir o ambiente dev agora? (S/N): "
if /I "%OPEN_DEV%"=="S" (
  call "%PROJECT_PATH%\bats\dev.bat"
)

pause
exit /b 0

:require_command
where %~1 >nul 2>nul
if errorlevel 1 (
  echo ERRO: %~2
  exit /b 1
)
exit /b 0
