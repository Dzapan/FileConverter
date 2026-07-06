$ErrorActionPreference = "Stop"

Write-Host "Aktualizacja pip..."
python -m pip install --upgrade pip

Write-Host "Instalowanie bibliotek..."
python -m pip install -r requirements.txt

Write-Host "Instalacja zakonczona."