@echo off
echo.
echo === Talkly Backend Setup ===
echo.

echo Ativando ambiente conda (linguaflow)...
call conda activate linguaflow
if %errorlevel% neq 0 (
    echo ERRO: nao foi possivel ativar o ambiente "linguaflow".
    echo Verifique se o conda esta instalado e o ambiente existe.
    pause
    exit /b 1
)

echo.
echo [1/8] Migrations...
python manage.py migrate
if %errorlevel% neq 0 ( echo ERRO: migrate && pause && exit /b 1 )

echo.
echo [2/8] Seed languages...
python manage.py seed_languages 2>nul
if %errorlevel% neq 0 ( echo AVISO: seed_languages nao encontrado, continuando... )

echo.
echo [3/8] Seed ES aventura (fases)...
python manage.py seed_es_full
if %errorlevel% neq 0 ( echo ERRO: seed_es_full && pause && exit /b 1 )

echo.
echo [4/8] Seed ES secoes fase 1...
python manage.py seed_es_sections
if %errorlevel% neq 0 ( echo ERRO: seed_es_sections && pause && exit /b 1 )

echo.
echo [5/8] Seed ES secoes fase 2...
python manage.py seed_es_f2_sections
if %errorlevel% neq 0 ( echo ERRO: seed_es_f2_sections && pause && exit /b 1 )

echo.
echo [6/8] Seed ES secoes fase 3...
python manage.py seed_es_f3_sections
if %errorlevel% neq 0 ( echo ERRO: seed_es_f3_sections && pause && exit /b 1 )

echo.
echo [7/8] Seed ES secoes fases 4 e 5...
python manage.py seed_es_f4_sections
if %errorlevel% neq 0 ( echo ERRO: seed_es_f4_sections && pause && exit /b 1 )
python manage.py seed_es_f5_sections
if %errorlevel% neq 0 ( echo ERRO: seed_es_f5_sections && pause && exit /b 1 )

echo.
echo [8/8] Seed ES estudo (modulos)...
python manage.py seed_es_study
if %errorlevel% neq 0 ( echo ERRO: seed_es_study && pause && exit /b 1 )

echo.
echo === Setup concluido! ===
echo.
