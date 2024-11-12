@echo off
:: Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not installed. Please install Git and try again.
    exit /b
)

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

:: Clone the GitHub repository
echo Cloning the Keylogger repository...
git clone https://github.com/ramprasathmk/keylogger.git

:: Navigate to the repository directory
cd keylogger

:: Create a virtual environment in the "env" folder
echo Creating virtual environment...
python -m venv env

:: Check if requirements.txt exists
if not exist requirements.txt (
    echo requirements.txt file not found. Skipping package installation.
) else (
    echo Installing packages from requirements.txt...
    env\Scripts\pip install -r requirements.txt
)

:: Activate the virtual environment
echo Activating virtual environment...
if "%ComSpec%"=="" (
    env\Scripts\Activate
) else (
    call env\Scripts\Activate
)

echo Virtual environment is activated.
