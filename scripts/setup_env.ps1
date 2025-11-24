<#
PowerShell environment setup script for the Bakery project.
Run from project root (where manage.py lives):

    .\scripts\setup_env.ps1

This will create a local virtual environment at `.venv`, activate it for the current session (if you allow script execution), and install packages from `requirements.txt`.
#>

Write-Host "Setting up virtual environment (.venv) and installing requirements..."

# Create venv
python -m venv .venv

# Try to activate PowerShell activation script for the current session
$activate = Join-Path -Path (Get-Location) -ChildPath ".venv\Scripts\Activate.ps1"
if (Test-Path $activate) {
    Write-Host "Activating virtual environment..."
    try {
        . $activate
    } catch {
        Write-Warning "Failed to activate automatically. Run '. .venv\Scripts\Activate.ps1' in PowerShell to activate the venv manually."
    }
} else {
    Write-Warning "Activation script not found at $activate"
}

Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Done. To activate the environment in PowerShell run:`n. .venv\Scripts\Activate.ps1`"
Write-Host "Then run the dev server with: `python manage.py runserver`"
