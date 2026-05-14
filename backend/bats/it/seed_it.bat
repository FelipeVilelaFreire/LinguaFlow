@echo off
pushd "%~dp0..\.."
echo.
echo === Talkly Backend Seed - IT ===
call conda activate linguaflow
if %errorlevel% neq 0 ( echo ERRO: conda activate linguaflow && popd && pause && exit /b 1 )
python manage.py seed_languages 2>nul
python manage.py seed_it
if %errorlevel% neq 0 ( echo ERRO: seed_it && popd && pause && exit /b 1 )
python manage.py seed_it_sections --reset
if %errorlevel% neq 0 ( echo ERRO: seed_it_sections && popd && pause && exit /b 1 )
echo.
echo === Seed IT concluido! ===
popd
pause
