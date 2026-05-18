@echo off
setlocal EnableExtensions
chcp 65001 >nul
title LinguaFlow dev launcher

set "PROJECT_PATH=%~dp0.."
for %%I in ("%PROJECT_PATH%") do set "PROJECT_PATH=%%~fI"
set "CONDA_ENV=linguaflow"

echo.
echo ============================================================
echo LinguaFlow - abrir ambiente dev
echo Projeto: "%PROJECT_PATH%"
echo ============================================================
echo.
echo Escolha o que abrir:
echo.
echo   1  - Web
echo        Backend + web
echo.
echo   2  - Mobile
echo        Backend + mobile
echo.
echo   3  - Admin
echo        Backend + admin
echo.
echo   4  - Web + Mobile
echo        Backend + web + mobile
echo.
echo   5  - Web + Admin
echo        Backend + web + admin
echo.
echo   6  - Mobile + Admin
echo        Backend + mobile + admin
echo.
echo   7  - Web + Mobile + Admin
echo        Backend + web + mobile + admin
echo.
echo   8  - Tudo com legado
echo        Backend + web + mobile + admin + frontend-web
echo.
echo   9  - Backend apenas
echo        Backend Django
echo.
set /p CHOICE="Digite uma opcao: "

set "OPEN_BACKEND=0"
set "OPEN_WEB=0"
set "OPEN_MOBILE=0"
set "OPEN_ADMIN=0"
set "OPEN_LEGACY=0"

if "%CHOICE%"=="1" (
  set "OPEN_BACKEND=1"
  set "OPEN_WEB=1"
) else if "%CHOICE%"=="2" (
  set "OPEN_BACKEND=1"
  set "OPEN_MOBILE=1"
) else if "%CHOICE%"=="3" (
  set "OPEN_BACKEND=1"
  set "OPEN_ADMIN=1"
) else if "%CHOICE%"=="4" (
  set "OPEN_BACKEND=1"
  set "OPEN_WEB=1"
  set "OPEN_MOBILE=1"
) else if "%CHOICE%"=="5" (
  set "OPEN_BACKEND=1"
  set "OPEN_WEB=1"
  set "OPEN_ADMIN=1"
) else if "%CHOICE%"=="6" (
  set "OPEN_BACKEND=1"
  set "OPEN_MOBILE=1"
  set "OPEN_ADMIN=1"
) else if "%CHOICE%"=="7" (
  set "OPEN_BACKEND=1"
  set "OPEN_WEB=1"
  set "OPEN_MOBILE=1"
  set "OPEN_ADMIN=1"
) else if "%CHOICE%"=="8" (
  set "OPEN_BACKEND=1"
  set "OPEN_WEB=1"
  set "OPEN_MOBILE=1"
  set "OPEN_ADMIN=1"
  set "OPEN_LEGACY=1"
) else if "%CHOICE%"=="9" (
  set "OPEN_BACKEND=1"
) else (
  echo.
  echo ERRO: opcao invalida.
  pause
  exit /b 1
)

set "WT_EXE="
where wt.exe >nul 2>nul
if not errorlevel 1 set "WT_EXE=wt.exe"
if "%WT_EXE%"=="" if exist "%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe" set "WT_EXE=%LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe"

if "%WT_EXE%"=="" (
  echo.
  echo ERRO: Windows Terminal ^(wt.exe^) nao encontrado no PATH.
  echo Instale o Windows Terminal ou adicione wt.exe ao PATH.
  pause
  exit /b 1
)

echo Abrindo os servicos em abas no Windows Terminal.
if "%OPEN_BACKEND%"=="1" call :open_tab "backend" "%PROJECT_PATH%\backend" "call conda activate %CONDA_ENV% && python manage.py runserver 8001"
if "%OPEN_WEB%"=="1" call :open_tab "web" "%PROJECT_PATH%\web" "npm run dev"
if "%OPEN_MOBILE%"=="1" call :open_tab "mobile" "%PROJECT_PATH%\mobile" "npm run start"
if "%OPEN_ADMIN%"=="1" call :open_tab "admin" "%PROJECT_PATH%\admin" "npm run dev"
if "%OPEN_LEGACY%"=="1" call :open_tab "legacy-web" "%PROJECT_PATH%\frontend-web" "npm run dev"
exit /b 0

:open_tab
set "TAB_TITLE=%~1"
set "TAB_PATH=%~2"
set "TAB_COMMAND=%~3"

start "" "%WT_EXE%" -w 0 new-tab --title "%TAB_TITLE%" -d "%TAB_PATH%" cmd.exe /d /k "%TAB_COMMAND%"
timeout /t 1 /nobreak >nul
exit /b 0
