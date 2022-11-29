#limpiando pantalla
Clear-Host
#Mensaje de bienvenida
Write-Host "Ejemplo de codificador Base64 en Powershell" -ForegroundColor Yellow
Write-Host "Escribe una frase a codificar: " -ForegroundColor Yellow
#solicitando la entrada de una cadena de texto
$frase = Read-Host
#Codificando en Base64 y guardando resultado en una cadena
$encod = [convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes(($frase)))
#imprimiendo la salida
Write-Host "La frase escrita en Base64 es: " -ForegroundColor Green
Write-Output $encod