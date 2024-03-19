[string]$py_version = python --version
$matches = $py_version | Select-String -Pattern "\d+" -AllMatches | ForEach-Object { $_.Matches.Value }

[int]$major = $matches[0]
[int]$minor = $matches[1]

if (($major -lt 3) -or ($major -eq 3 -and $minor -lt 10)) {
    Write-Host "✘ Please upgrade your Python version to 3.10 or later" -ForegroundColor red
    Break  # Terminate
}

if (-not (Test-Path "./.venv")) {
    Write-Host "Creating virtual environment (./.venv)..." -ForegroundColor cyan
    python -m venv ./.venv
    Write-Host "✔ Created virtual environment" -ForegroundColor green
}

./.venv/Scripts/activate
Write-Host "✔ Activated virtual environment" -ForegroundColor green

Write-Host "Installing requirements (./requirements.txt)...`n" -ForegroundColor cyan
pip install -r "./requirements.txt"

Write-Host "`n✔ Installed requirements" -ForegroundColor green
