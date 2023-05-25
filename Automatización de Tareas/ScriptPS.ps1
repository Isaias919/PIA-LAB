param(
    [Parameter(Mandatory)] [string]$ruta,
    [Parameter(Mandatory)] [string]$hora,
    [Parameter(Mandatory)] [string]$Tskpa,
    [Parameter(Mandatory)] [string]$Tskna,
    [Parameter(Mandatory)] [string]$dstion
     )

#ruta: C:\Users\braya\Desktop\SEND_SYSINFO.ps1
$tarea = New-ScheduledTaskAction PowerShell.exe -Argument $ruta
$trigger = New-ScheduledTaskTrigger -Once -At $hora
Register-ScheduledTask -Action $tarea -Trigger $trigger -TaskPath $Tskpa -TaskName $Tskna -Description $dstion