@echo off
REM ============================================================================
REM  Talkly Backend - Migrations
REM
REM  Cuida so do banco de dados, sem seeds.
REM  Rode sempre que mexer em models.py.
REM ============================================================================

pushd "%~dp0..\.."

echo.
echo === Talkly Backend - Migrations ===
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
echo [1/2] makemigrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERRO: makemigrations
    popd
    pause
    exit /b 1
)

echo.
echo [2/2] migrate...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERRO: migrate
    popd
    pause
    exit /b 1
)

echo.
echo === Migrations concluidas! ===
echo Banco sincronizado com os models.
echo.

popd
pause
