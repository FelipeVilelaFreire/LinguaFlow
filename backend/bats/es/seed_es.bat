@echo off
REM ============================================================================
REM  Talkly Backend - Seed ES
REM
REM  Popula somente o conteudo ES. Nao roda migrations.
REM ============================================================================

pushd "%~dp0..\.."

echo.
echo === Talkly Backend Seed - ES ===
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
echo [1/4] Seed languages...
python manage.py seed_languages 2>nul

echo.
echo [2/4] Seed ES aventura...
python manage.py seed_es
if %errorlevel% neq 0 (
    echo ERRO: seed_es
    popd
    pause
    exit /b 1
)

echo.
echo [3/4] Seed ES secoes (F1-F25)...
python manage.py seed_es_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_es_sections
    popd
    pause
    exit /b 1
)

echo.
echo [4/4] Seed ES estudo...
python manage.py seed_es_study

echo.
echo === Seed ES concluido! ===
echo.

popd
pause
