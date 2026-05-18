@echo off
REM ============================================================================
REM  Talkly Backend - Setup opcional de audio da aventura ES
REM
REM  Baixa Piper localmente, baixa vozes gratuitas do rhasspy/piper-voices,
REM  grava backend\.env para laboratorio/dev. O uso normal continua no browser.
REM ============================================================================

setlocal EnableExtensions
set NO_PAUSE=0
set AUTO_YES=0
if /I "%~1"=="--no-pause" set NO_PAUSE=1
if /I "%~1"=="--yes" set AUTO_YES=1
if /I "%~2"=="--no-pause" set NO_PAUSE=1
if /I "%~2"=="--yes" set AUTO_YES=1

pushd "%~dp0..\..\backend"

echo.
echo === Setup Adventure TTS DEV - ES ===
echo.
echo Este passo baixa arquivos grandes da internet:
echo   - Piper Windows: cerca de 23 MB
echo   - Vozes ES Piper: dezenas/centenas de MB no total
echo.
if "%AUTO_YES%"=="1" goto confirmed
set /p CONFIRM_TTS="Continuar com download/configuracao automatica? (S/N): "
if /I not "%CONFIRM_TTS%"=="S" goto done

:confirmed

echo.
echo Ativando ambiente conda (linguaflow)...
call conda activate linguaflow
if %errorlevel% neq 0 (
    echo ERRO: nao foi possivel ativar o ambiente "linguaflow".
    goto fail
)
set PYTHONIOENCODING=utf-8

set "PIPER_VERSION=2023.11.14-2"
set "PIPER_URL=https://github.com/rhasspy/piper/releases/download/%PIPER_VERSION%/piper_windows_amd64.zip"
set "TTS_HOME=%USERPROFILE%\.codex\memories\linguaflow-tts"
set "PIPER_ZIP=%TTS_HOME%\piper_windows_amd64.zip"
set "PIPER_ROOT=%TTS_HOME%\piper-runtime"
set "PIPER_EXE=%PIPER_ROOT%\piper\piper.exe"
set "PIPER_EXE_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\piper-runtime\piper\piper.exe"
set "MODELS_DIR=%TTS_HOME%\models"
set "LOCAL_MODELS_DIR=%CD%\tts_models\piper"

if not exist "%TTS_HOME%" mkdir "%TTS_HOME%"
if not exist "%PIPER_ROOT%" mkdir "%PIPER_ROOT%"
if not exist "%MODELS_DIR%" mkdir "%MODELS_DIR%"

if exist "%PIPER_EXE%" (
    echo.
    echo Piper ja encontrado: %PIPER_EXE%
) else if exist "%CD%\tools\piper\piper\piper.exe" (
    echo.
    echo Copiando Piper para caminho sem acento: %PIPER_ROOT%
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Copy-Item -LiteralPath '%CD%\tools\piper\piper' -Destination '%PIPER_ROOT%\piper' -Recurse -Force"
    if %errorlevel% neq 0 goto fail
) else (
    echo.
    echo Baixando Piper...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri '%PIPER_URL%' -OutFile '%PIPER_ZIP%'"
    if %errorlevel% neq 0 goto fail

    echo Extraindo Piper...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Expand-Archive -LiteralPath '%PIPER_ZIP%' -DestinationPath '%PIPER_ROOT%' -Force"
    if %errorlevel% neq 0 goto fail
)

call :download_voice "es_ES-davefx-medium"   "es/es_ES/davefx/medium"
if %errorlevel% neq 0 goto fail
call :download_voice "es_ES-sharvard-medium" "es/es_ES/sharvard/medium"
if %errorlevel% neq 0 echo AVISO: voz es_ES-sharvard-medium nao baixou. Usando fallback.
call :download_voice "es_ES-mls_9972-low"    "es/es_ES/mls_9972/low"
if %errorlevel% neq 0 echo AVISO: voz es_ES-mls_9972-low nao baixou. Usando fallback.
call :download_voice "es_ES-mls_10246-low"   "es/es_ES/mls_10246/low"
if %errorlevel% neq 0 echo AVISO: voz es_ES-mls_10246-low nao baixou. Usando fallback.
call :download_voice "es_ES-carlfm-x_low"    "es/es_ES/carlfm/x_low"
if %errorlevel% neq 0 echo AVISO: voz es_ES-carlfm-x_low nao baixou. Usando fallback.
call :download_voice "es_MX-ald-medium"      "es/es_MX/ald/medium"
if %errorlevel% neq 0 echo AVISO: voz es_MX-ald-medium nao baixou. Usando fallback.
call :download_voice "es_MX-claude-high"     "es/es_MX/claude/high"
if %errorlevel% neq 0 echo AVISO: voz es_MX-claude-high nao baixou. Usando fallback.
call :download_voice "es_AR-daniela-high"    "es/es_AR/daniela/high"
if %errorlevel% neq 0 echo AVISO: voz es_AR-daniela-high nao baixou. Usando fallback.

set "VOICE_DEFAULT=%MODELS_DIR%\es_ES-davefx-medium.onnx"
set "VOICE_DON_MIGUEL=%VOICE_DEFAULT%"
set "VOICE_MIGUEL=%VOICE_DEFAULT%"
set "VOICE_ROSA=%VOICE_DEFAULT%"
set "VOICE_CARMEN=%VOICE_DEFAULT%"
set "VOICE_SOFIA=%VOICE_DEFAULT%"
set "VOICE_MARIA=%VOICE_DEFAULT%"
set "VOICE_ALCALDE=%VOICE_DEFAULT%"
set "VOICE_VIGILANTE=%VOICE_DEFAULT%"
set "VOICE_INSPECTOR=%VOICE_DEFAULT%"

if exist "%MODELS_DIR%\es_ES-mls_9972-low.onnx" set "VOICE_MIGUEL=%MODELS_DIR%\es_ES-mls_9972-low.onnx"
if exist "%MODELS_DIR%\es_ES-mls_9972-low.onnx" set "VOICE_VIGILANTE=%MODELS_DIR%\es_ES-mls_9972-low.onnx"
if exist "%MODELS_DIR%\es_ES-sharvard-medium.onnx" set "VOICE_ROSA=%MODELS_DIR%\es_ES-sharvard-medium.onnx"
if exist "%MODELS_DIR%\es_ES-sharvard-medium.onnx" set "VOICE_SOFIA=%MODELS_DIR%\es_ES-sharvard-medium.onnx"
if exist "%MODELS_DIR%\es_ES-mls_10246-low.onnx" set "VOICE_MARIA=%MODELS_DIR%\es_ES-mls_10246-low.onnx"
if exist "%MODELS_DIR%\es_ES-carlfm-x_low.onnx" set "VOICE_CARMEN=%MODELS_DIR%\es_ES-carlfm-x_low.onnx"

set "VOICE_DEFAULT_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-davefx-medium.onnx"
set "VOICE_DON_MIGUEL_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_MIGUEL_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_ROSA_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_CARMEN_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_SOFIA_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_MARIA_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_ALCALDE_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_VIGILANTE_ENV=%VOICE_DEFAULT_ENV%"
set "VOICE_INSPECTOR_ENV=%VOICE_DEFAULT_ENV%"

if exist "%MODELS_DIR%\es_ES-davefx-medium.onnx" set "VOICE_MIGUEL_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-davefx-medium.onnx"
if exist "%MODELS_DIR%\es_ES-mls_9972-low.onnx" set "VOICE_VIGILANTE_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-mls_9972-low.onnx"
if exist "%MODELS_DIR%\es_ES-sharvard-medium.onnx" set "VOICE_ROSA_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-sharvard-medium.onnx"
if exist "%MODELS_DIR%\es_ES-sharvard-medium.onnx" set "VOICE_SOFIA_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-sharvard-medium.onnx"
if exist "%MODELS_DIR%\es_ES-mls_10246-low.onnx" set "VOICE_MARIA_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-mls_10246-low.onnx"
if exist "%MODELS_DIR%\es_ES-carlfm-x_low.onnx" set "VOICE_CARMEN_ENV=%USERPROFILE%\.codex\memories\linguaflow-tts\models\es_ES-carlfm-x_low.onnx"

echo.
echo Gravando backend\.env com modelos DEV locais...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$envPath='%CD%\.env'; $lines=@('ADVENTURE_TTS_ENABLED=false','ADVENTURE_TTS_PROVIDER=piper','ADVENTURE_TTS_PIPER_EXE=%PIPER_EXE_ENV%','ADVENTURE_TTS_PIPER_DEFAULT_MODEL=%VOICE_DEFAULT_ENV%','ADVENTURE_TTS_PIPER_MODEL_DON_MIGUEL=%VOICE_DON_MIGUEL_ENV%','ADVENTURE_TTS_PIPER_MODEL_MIGUEL=%VOICE_MIGUEL_ENV%','ADVENTURE_TTS_PIPER_MODEL_ROSA=%VOICE_ROSA_ENV%','ADVENTURE_TTS_PIPER_MODEL_CARMEN=%VOICE_CARMEN_ENV%','ADVENTURE_TTS_PIPER_MODEL_SOFIA=%VOICE_SOFIA_ENV%','ADVENTURE_TTS_PIPER_MODEL_MARIA=%VOICE_MARIA_ENV%','ADVENTURE_TTS_PIPER_MODEL_ALCALDE=%VOICE_ALCALDE_ENV%','ADVENTURE_TTS_PIPER_MODEL_VIGILANTE=%VOICE_VIGILANTE_ENV%','ADVENTURE_TTS_PIPER_MODEL_INSPECTOR=%VOICE_INSPECTOR_ENV%'); Set-Content -LiteralPath $envPath -Value $lines -Encoding UTF8"
if %errorlevel% neq 0 goto fail

echo.
echo Conferindo vozes configuradas...
python manage.py generate_adventure_audio --lang ES --voices
if %errorlevel% neq 0 goto fail

echo.
if "%AUTO_YES%"=="1" goto done
set /p GENERATE_NOW="Gerar cache WAV DEV da aventura ES agora? (S/N): "
if /I "%GENERATE_NOW%"=="S" (
    python manage.py generate_adventure_audio --lang ES --provider piper
    if %errorlevel% neq 0 goto fail
)

:done
echo.
echo === Setup Adventure TTS DEV finalizado ===
echo.
popd
if "%NO_PAUSE%"=="0" pause
exit /b 0

:fail
echo.
echo ERRO: setup de audio nao foi concluido.
echo O jogo continua funcionando com a voz padrao do navegador.
echo.
popd
if "%NO_PAUSE%"=="0" pause
exit /b 1

:download_voice
set "VOICE_NAME=%~1"
set "VOICE_PATH=%~2"
set "VOICE_MODEL=%MODELS_DIR%\%VOICE_NAME%.onnx"
set "VOICE_JSON=%MODELS_DIR%\%VOICE_NAME%.onnx.json"
set "LOCAL_VOICE_MODEL=%LOCAL_MODELS_DIR%\%VOICE_NAME%.onnx"
set "LOCAL_VOICE_JSON=%LOCAL_MODELS_DIR%\%VOICE_NAME%.onnx.json"
set "VOICE_BASE=https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/%VOICE_PATH%/%VOICE_NAME%"

if exist "%VOICE_MODEL%" (
    echo Voz ja encontrada: %VOICE_MODEL%
) else if exist "%LOCAL_VOICE_MODEL%" (
    echo Copiando voz para caminho sem acento: %VOICE_NAME%.onnx
    copy /Y "%LOCAL_VOICE_MODEL%" "%VOICE_MODEL%" >nul
    if %errorlevel% neq 0 exit /b 1
) else (
    echo Baixando voz: %VOICE_NAME%.onnx
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri '%VOICE_BASE%.onnx' -OutFile '%VOICE_MODEL%'"
    if %errorlevel% neq 0 exit /b 1
)

if exist "%VOICE_JSON%" (
    echo Config da voz ja encontrada: %VOICE_JSON%
) else if exist "%LOCAL_VOICE_JSON%" (
    echo Copiando config para caminho sem acento: %VOICE_NAME%.onnx.json
    copy /Y "%LOCAL_VOICE_JSON%" "%VOICE_JSON%" >nul
    if %errorlevel% neq 0 exit /b 1
) else (
    echo Baixando config: %VOICE_NAME%.onnx.json
    powershell -NoProfile -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri '%VOICE_BASE%.onnx.json' -OutFile '%VOICE_JSON%'"
    if %errorlevel% neq 0 exit /b 1
)
exit /b 0
