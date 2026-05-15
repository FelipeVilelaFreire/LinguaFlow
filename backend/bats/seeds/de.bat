@echo off
REM ============================================================================
REM  Talkly Backend - Seed DE
REM
REM  Popula o conteudo EN -> DE. Roda migrations antes porque aventura usa
REM  tabelas de skills, baus e maestria por usuario.
REM ============================================================================

pushd "%~dp0..\.."

echo.
echo === Talkly Backend Seed - DE ===
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
echo [1/5] Migrate banco...
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
echo [3/5] Seed DE aventura...
python manage.py seed_de
if %errorlevel% neq 0 (
    echo ERRO: seed_de
    popd
    pause
    exit /b 1
)

echo.
echo [4/5] Seed DE secoes (F1-F25)...
python manage.py seed_de_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_de_sections
    popd
    pause
    exit /b 1
)

echo.
echo [5/5] Seed DE estudo...
python manage.py seed_de_study
if %errorlevel% neq 0 (
    echo ERRO: seed_de_study
    popd
    pause
    exit /b 1
)

echo.
echo === Seed DE concluido! ===
echo.

popd
pause
