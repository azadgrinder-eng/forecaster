# Registers a Windows scheduled task that runs run_daily.ps1 every day at the time below.
# Run once from this folder:  powershell -ExecutionPolicy Bypass -File setup_schedule.ps1
param([string]$At = "09:00")
$script = Join-Path $PSScriptRoot "run_daily.ps1"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$script`"" -WorkingDirectory $PSScriptRoot
$trigger = New-ScheduledTaskTrigger -Daily -At $At
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 3)
Register-ScheduledTask -TaskName "Forecaster daily run" -Action $action -Trigger $trigger -Settings $settings -Force | Out-Null
Write-Host "Scheduled 'Forecaster daily run' every day at $At (runs when you're logged in; catches up if the PC was off)."
Write-Host "Remove it with:  Unregister-ScheduledTask -TaskName 'Forecaster daily run'"
