@echo off
REM ============================================================================
REM  Talkly Backend - Idioma IT
REM
REM  Roda o setup completo do Italiano: migrations + seed IT + secoes.
REM ============================================================================

pushd "%~dp0..\.."

echo.
echo === Talkly Backend Setup - IT ===
echo.

echo Ativando ambiente conda (linguaflow)...
call conda activate linguaflow
if %errorlevel% neq 0 (
    echo ERRO: nao foi possivel ativar o ambiente "linguaflow".
    echo Verifique se o conda esta instalado e o ambiente existe.
    popd
    pause
    exit /b 1
)
set PYTHONIOENCODING=utf-8

echo.
echo [1/5] Migrations (makemigrations + migrate)...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERRO: makemigrations
    popd
    pause
    exit /b 1
)

python manage.py migrate
if %errorlevel% neq 0 (
    echo ERRO: migrate
    popd
    pause
    exit /b 1
)

echo.
echo [2/5] Seed languages...
python manage.py seed_languages 2>nul

echo.
echo [3/5] Seed IT aventura...
python manage.py seed_it
if %errorlevel% neq 0 (
    echo ERRO: seed_it
    popd
    pause
    exit /b 1
)

echo.
echo [4/5] Seed IT secoes (F1-F25)...
python manage.py seed_it_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_it_sections
    popd
    pause
    exit /b 1
)

echo.
echo [5/5] Seed ES estudo mantido separado.
echo Study modules for IT are not created yet.

echo.
echo === Setup IT concluido! ===
echo IT A1 T1: F1 a F25.
echo.

popd
pause
