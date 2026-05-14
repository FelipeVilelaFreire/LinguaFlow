@echo off
REM ============================================================================
REM  Talkly Backend - Seed DE
REM
REM  Populates only EN -> DE content. Does not run migrations.
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

echo.
echo [1/3] Seed languages...
python manage.py seed_languages 2>nul

echo.
echo [2/3] Seed DE aventura...
python manage.py seed_de
if %errorlevel% neq 0 (
    echo ERRO: seed_de
    popd
    pause
    exit /b 1
)

echo.
echo [3/3] Seed DE secoes (F1-F25)...
python manage.py seed_de_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_de_sections
    popd
    pause
    exit /b 1
)

echo.
echo === Seed DE concluido! ===
echo.

popd
pause
