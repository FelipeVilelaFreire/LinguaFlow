@echo off
chcp 65001 > nul
title Dev {{DISPLAY_NAME}}

:: ============================================================
:: {{DISPLAY_NAME}} — Daily dev startup
:: Tabs: Claude · Backend+SharedCore · Web+Mobile · (Admin if enabled)
::
:: CLAUDE: if Admin panel: no  →  remove the last `; new-tab ... frontend ...` line.
:: CLAUDE: if Admin panel: yes →  keep all lines below.
:: ============================================================

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
for %%I in ("%SCRIPT_DIR%") do set "SCRIPT_FOLDER=%%~nxI"
if /I "%SCRIPT_FOLDER%"=="bats" (
    for %%I in ("%SCRIPT_DIR%\..") do set "PROJECT_PATH=%%~fI"
) else (
    set "PROJECT_PATH=%SCRIPT_DIR%"
)

wt -d "%PROJECT_PATH%" cmd /k "claude" ^
   ; new-tab --title "backend+core" -d "%PROJECT_PATH%\backend" cmd /k "conda activate {{CONDA_ENV}} && python manage.py runserver" ^
   ; split-pane -V -d "%PROJECT_PATH%\packages\shared-core" cmd /k "yarn dev" ^
   ; new-tab --title "web+mobile" -d "%PROJECT_PATH%\web" cmd /k "npm run dev" ^
   ; split-pane -V -d "%PROJECT_PATH%\mobile" cmd /k "npx expo start" ^
   ; new-tab --title "admin" -d "%PROJECT_PATH%\frontend" cmd /k "npm run dev"

exit
