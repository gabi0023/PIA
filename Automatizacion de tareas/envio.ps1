#
##Script para programar envio de correo
#
#Nombre:Gabriela Hermenegildo Otero
#Matricula:1990138
#
$script= New-ScheduledTaskAction -Execute "powershell.exe" C:/Users/gabri/OneDrive/Escritorio/send_sysinfo.ps1
$hora=New-ScheduledTaskTrigger -Once -At 5:00pm
Register-ScheduledTask -Action $script -Trigger $hora -TaskPath "MisTareas" -TaskName "Envio sysinfo" -Description "Envio de informacion del sistema"