@echo off
REM ============================================================================
REM  Talkly Backend - Idioma ES
REM
REM  Roda o setup completo do Espanhol: migrations + seed ES + secoes + estudo.
REM ============================================================================

pushd "%~dp0..\.."

echo.
echo === Talkly Backend Setup - ES ===
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
echo [3/5] Seed ES aventura...
python manage.py seed_es
if %errorlevel% neq 0 (
    echo ERRO: seed_es
    popd
    pause
    exit /b 1
)

echo.
echo [4/5] Seed ES secoes (F1-F25)...
python manage.py seed_es_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_es_sections
    popd
    pause
    exit /b 1
)

echo.
echo [5/5] Seed ES estudo...
python manage.py seed_es_study
if %errorlevel% neq 0 (
    echo ERRO: seed_es_study
    popd
    pause
    exit /b 1
)

echo.
echo === Setup ES concluido! ===
echo ES A1 T1: F1 a F25.
echo.

popd
pause
exit /b 0
