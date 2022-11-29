#Nombre: Gabriela Hermenegildo Otero
#matricula: 1990138
#
Clear-Host
Write-Host "Bienvenido a un ejemplo de codificacion/decodificacion base64 usando powershell " -ForegroundColor Green
Write-Host "codificando un archivo de texto"
#
#Se va a leer el contenido del archivo de texto
#
$inputfile = "C:\Users\gabri\OneDrive\Escritorio\secret.txt"
$fc = get-Content $inputfile
$GB = [System.Text.Encoding]::UTF8.Getbytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es: " $etext -ForegroundColor Green
#
#decodificando contento de un archivo
#
Write-Host "DECODIFICANDO el texto previo:"
[System.Text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" C:\Users\gabri\OneDrive\Escritorio\decode_secret.txt
$outfile12 = Get-Content C:\Users\gabri\OneDrive\Escritorio\decode_secret.txt
Write-Host "El texto decodificado es el siguiente: " -ForegroundColor Green
Write-Host "DECODIFICADO:" $outfile12