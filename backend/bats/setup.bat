@echo off
REM ============================================================================
REM  Talkly Backend - Setup Interativo
REM
REM  Sempre roda migrations. Depois voce escolhe qual seed rodar:
REM  1 = ES, 2 = IT, 3 = DE, 4 = tudo.
REM ============================================================================

pushd "%~dp0.."

echo.
echo === Talkly Backend Setup Interativo ===
echo.

echo Escolha o seed:
echo   1 - ES
echo   2 - IT
echo   3 - DE
echo   4 - Tudo
echo.
set /p CHOICE="Digite 1, 2, 3 ou 4: "

if "%CHOICE%"=="1" goto valid_choice
if "%CHOICE%"=="2" goto valid_choice
if "%CHOICE%"=="3" goto valid_choice
if "%CHOICE%"=="4" goto valid_choice

echo.
echo ERRO: escolha invalida.
popd
pause
exit /b 1

:valid_choice
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
echo [1/3] makemigrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERRO: makemigrations
    popd
    pause
    exit /b 1
)

echo.
echo [2/3] migrate...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERRO: migrate
    popd
    pause
    exit /b 1
)

echo.
echo [3/3] Seed selecionado...
python manage.py seed_languages 2>nul

if "%CHOICE%"=="1" goto seed_es
if "%CHOICE%"=="2" goto seed_it
if "%CHOICE%"=="3" goto seed_de
if "%CHOICE%"=="4" goto seed_all

:seed_es
call :run_es
goto done

:seed_it
call :run_it
goto done

:seed_de
call :run_de
goto done

:seed_all
call :run_es
if %errorlevel% neq 0 goto fail
call :run_it
if %errorlevel% neq 0 goto fail
call :run_de
if %errorlevel% neq 0 goto fail
goto done

:run_es
echo.
echo --- Seed ES aventura ---
python manage.py seed_es
if %errorlevel% neq 0 (
    echo ERRO: seed_es
    exit /b 1
)
echo.
echo --- Seed ES secoes (F1-F25) ---
python manage.py seed_es_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_es_sections
    exit /b 1
)
echo.
echo --- Seed ES estudo ---
python manage.py seed_es_study
if %errorlevel% neq 0 (
    echo ERRO: seed_es_study
    exit /b 1
)
exit /b 0

:run_it
echo.
echo --- Seed IT aventura ---
python manage.py seed_it
if %errorlevel% neq 0 (
    echo ERRO: seed_it
    exit /b 1
)
echo.
echo --- Seed IT secoes (F1-F25) ---
python manage.py seed_it_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_it_sections
    exit /b 1
)
echo.
echo --- Seed IT estudo ---
python manage.py seed_it_study
if %errorlevel% neq 0 (
    echo ERRO: seed_it_study
    exit /b 1
)
exit /b 0

:run_de
echo.
echo --- Seed DE aventura ---
python manage.py seed_de
if %errorlevel% neq 0 (
    echo ERRO: seed_de
    exit /b 1
)
echo.
echo --- Seed DE secoes (F1-F25) ---
python manage.py seed_de_sections --reset
if %errorlevel% neq 0 (
    echo ERRO: seed_de_sections
    exit /b 1
)
echo.
echo --- Seed DE estudo ---
python manage.py seed_de_study
if %errorlevel% neq 0 (
    echo ERRO: seed_de_study
    exit /b 1
)
exit /b 0

:fail
echo.
echo ERRO: setup interrompido.
popd
pause
exit /b 1

:done
echo.
echo === Setup concluido! ===
echo.

popd
pause
