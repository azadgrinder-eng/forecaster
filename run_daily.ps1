# Daily harness run: resolve, collect today's markets, forecast them, update the scorecard.
# Scheduled by setup_schedule.ps1; safe to run by hand too.
$ErrorActionPreference = "Continue"
Set-Location -Path $PSScriptRoot
$env:PATH = "$env:USERPROFILE\.local\bin;$env:PATH"   # where the Claude Code installer puts claude.exe
$env:PYTHONIOENCODING = "utf-8"
New-Item -ItemType Directory -Force -Path logs | Out-Null
$log = "logs\daily-$(Get-Date -Format yyyy-MM-dd).log"
$python = if (Test-Path ".venv\Scripts\python.exe") { ".venv\Scripts\python.exe" } else { "python" }
& $python harness.py daily *>&1 | Tee-Object -FilePath $log -Append
