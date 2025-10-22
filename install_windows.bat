@echo off
setlocal

REM Windows installer for FTTH panel (ASCII-safe)

cd /d "%~dp0"

set "PYCMD="
where py >nul 2>nul
if %errorlevel% EQU 0 (
  set "PYCMD=py -3"
) else (
  where python >nul 2>nul
  if %errorlevel% EQU 0 (
    set "PYCMD=python"
  ) else (
    echo Python 3 not found. Install from https://www.python.org/downloads/windows/
    echo Check "Add Python to PATH" during setup. Then run this installer again.
    pause
    exit /b 1
  )
)

echo Using: %PYCMD%

if not exist ".venv" (
  echo Creating virtual environment .venv ...
  %PYCMD% -m venv ".venv"
  if ERRORLEVEL 1 (
    echo Failed to create virtual environment.
    pause
    exit /b 1
  )
) else (
  echo Using existing .venv
)

echo Upgrading pip ...
call ".venv\Scripts\python.exe" -m pip install --upgrade pip

if exist "requirements.txt" (
  echo Installing dependencies ...
  call ".venv\Scripts\python.exe" -m pip install -r "requirements.txt"
  if ERRORLEVEL 1 (
    echo Failed to install dependencies.
    pause
    exit /b 1
  )
) else (
  echo requirements.txt not found, skipping dependency install.
)

echo Initializing database ...
call ".venv\Scripts\python.exe" -c "import app; app.create_app(); print('DB_OK')"

echo.
echo Installation complete.
echo To start the server manually:
	echo   .venv\Scripts\python.exe app.py

set /p STARTNOW=Start server now [Y/N]: 
if /I "%STARTNOW%"=="Y" goto start
if /I "%STARTNOW%"=="S" goto start

echo Done.
pause
goto end

:start
echo Starting server at http://127.0.0.1:5000 ...
call ".venv\Scripts\python.exe" "app.py"

:end
endlocal
