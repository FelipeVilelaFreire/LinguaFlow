@echo off
pushd "%~dp0..\.."
echo.
echo === Talkly Backend Setup - IT ===
call conda activate linguaflow
if %errorlevel% neq 0 ( echo ERRO: conda activate linguaflow && popd && pause && exit /b 1 )
python manage.py makemigrations
if %errorlevel% neq 0 ( echo ERRO: makemigrations && popd && pause && exit /b 1 )
python manage.py migrate
if %errorlevel% neq 0 ( echo ERRO: migrate && popd && pause && exit /b 1 )
python manage.py seed_languages 2>nul
python manage.py seed_it
if %errorlevel% neq 0 ( echo ERRO: seed_it && popd && pause && exit /b 1 )
python manage.py seed_it_sections --reset
if %errorlevel% neq 0 ( echo ERRO: seed_it_sections && popd && pause && exit /b 1 )
echo.
echo === Setup IT concluido! ===
popd
pause
