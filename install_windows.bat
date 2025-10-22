@echo off
SetLocal EnableExtensions EnableDelayedExpansion
title Instalador Panel FTTH (Flask)
chcp 65001 >nul

echo === Instalador Panel FTTH (Flask) ===

REM Ir al directorio del script
cd /d "%~dp0"

REM Detectar Python
set "PYCMD="
where py >NUL 2>&1
if %ERRORLEVEL%==0 set "PYCMD=py -3"
if not defined PYCMD (
  where python >NUL 2>&1
  if %ERRORLEVEL%==0 (
    set "PYCMD=python"
  ) else (
    echo No se encontro Python. Instale Python 3 desde https://www.python.org/downloads/windows/
    echo y marque la casilla "Add Python to PATH". Luego ejecute este instalador de nuevo.
    pause
    exit /b 1
  )
)

echo Usando: %PYCMD%

REM Crear entorno virtual si no existe
if not exist ".venv" (
  echo Creando entorno virtual .venv ...
  %PYCMD% -m venv ".venv"
  if ERRORLEVEL 1 (
    echo Error creando el entorno virtual.
    pause
    exit /b 1
  )
)

echo Actualizando pip ...
call ".venv\Scripts\python.exe" -m pip install --upgrade pip

echo Instalando dependencias ...
call ".venv\Scripts\python.exe" -m pip install -r "requirements.txt"
if ERRORLEVEL 1 (
  echo Error instalando dependencias.
  pause
  exit /b 1
)

echo Inicializando base de datos ...
call ".venv\Scripts\python.exe" -c "import app; app.create_app(); print('DB_OK')"

echo.
echo Instalacion completada.
echo Para iniciar el servidor manualmente:
echo   .venv\Scripts\python.exe app.py
echo.
set /p STARTNOW=¿Desea iniciar el servidor ahora? [S/N]: 
if /I "%STARTNOW%"=="S" goto start
if /I "%STARTNOW%"=="s" goto start

echo Listo. Puede cerrar esta ventana o iniciar el servidor cuando desee.
pause
goto end

:start
echo Iniciando servidor en http://127.0.0.1:5000 ...
call ".venv\Scripts\python.exe" "app.py"

:end
EndLocal
