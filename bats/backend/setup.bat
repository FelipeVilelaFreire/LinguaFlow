@echo off
REM ============================================================================
REM  Talkly Backend - Setup Interativo
REM
REM  Sempre roda migrations. Depois voce escolhe qual seed rodar:
REM  1 = ES, 2 = IT, 3 = DE, 4 = tudo.
REM ============================================================================

pushd "%~dp0..\..\backend"

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
if %errorlevel% neq 0 goto fail
goto done

:seed_it
call :run_it
if %errorlevel% neq 0 goto fail
goto done

:seed_de
call :run_de
if %errorlevel% neq 0 goto fail
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
if "%CHOICE%"=="1" call :optional_es_audio
if "%CHOICE%"=="4" call :optional_es_audio
echo.
echo === Setup concluido! ===
echo.

popd
pause
exit /b 0

:optional_es_audio
echo.
echo --- Audio opcional da aventura ES ---
echo Uso normal recomendado: deixar desativado e usar a voz padrao do navegador.
echo Piper fica como laboratorio/dev para testar vozes em /aventura/mapa/dev.
set /p AUTO_TTS_SETUP="Abrir configuracao DEV do Piper mesmo assim? (S/N): "
if /I "%AUTO_TTS_SETUP%"=="S" (
    call "%~dp0tts.bat" --yes --no-pause
    if %errorlevel% neq 0 (
        echo AVISO: a configuracao automatica de audio falhou ou ficou incompleta.
        echo O setup principal ja foi concluido; o jogo ainda usa a voz do navegador como fallback.
        exit /b 0
    )
)
echo.
echo Mostrando vozes DEV configuradas:
python manage.py generate_adventure_audio --lang ES --voices
echo.
set /p GENERATE_ES_AUDIO="Gerar cache DEV de audio ES agora? (S/N): "
if /I not "%GENERATE_ES_AUDIO%"=="S" exit /b 0
echo.
echo Gerando cache de audio ES...
python manage.py generate_adventure_audio --lang ES --provider piper
if %errorlevel% neq 0 (
    echo AVISO: nao foi possivel gerar todos os audios agora. O setup principal ja foi concluido.
)
exit /b 0
