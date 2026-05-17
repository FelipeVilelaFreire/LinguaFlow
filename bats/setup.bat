@echo off
setlocal EnableExtensions

set "PROJECT_PATH=%~dp0.."
set "CONDA_ENV=linguaflow"

echo.
echo === Talkly Cross-Platform Setup ===
echo.

echo [1/5] Backend dependencies and database
pushd "%PROJECT_PATH%\backend"
call conda activate %CONDA_ENV%
if %errorlevel% neq 0 (
  echo ERRO: nao foi possivel ativar o ambiente conda "%CONDA_ENV%".
  popd
  exit /b 1
)
python manage.py migrate
if %errorlevel% neq 0 (
  echo ERRO: migrate falhou.
  popd
  exit /b 1
)
popd

echo.
echo [2/5] Shared-core dependencies
pushd "%PROJECT_PATH%\packages\shared-core"
if exist package-lock.json (
  npm install
) else (
  npm install
)
if %errorlevel% neq 0 (
  echo ERRO: npm install em packages\shared-core falhou.
  popd
  exit /b 1
)
npm run build
if %errorlevel% neq 0 (
  echo ERRO: build do shared-core falhou.
  popd
  exit /b 1
)
popd

echo.
echo [3/5] Web dependencies
pushd "%PROJECT_PATH%\web"
npm install
if %errorlevel% neq 0 (
  echo ERRO: npm install em web falhou.
  popd
  exit /b 1
)
popd

echo.
echo [4/5] Mobile dependencies
pushd "%PROJECT_PATH%\mobile"
npm install
if %errorlevel% neq 0 (
  echo ERRO: npm install em mobile falhou.
  popd
  exit /b 1
)
popd

echo.
echo [5/5] Legacy frontend-web dependencies
pushd "%PROJECT_PATH%\frontend-web"
npm install
if %errorlevel% neq 0 (
  echo ERRO: npm install em frontend-web falhou.
  popd
  exit /b 1
)
popd

echo.
echo === Setup concluido ===
echo Use bats\dev.bat para abrir o ambiente local.
echo.
pause
