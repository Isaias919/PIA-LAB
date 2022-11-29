clear-host
Write-Host "Bienvenido a un ejemplo de codificacion / decodificacion base64 usando powershell" -ForegroundColor Green
Write-host "Codificando un archivo de texto"

$inputfile = "C:\Users\Isaias\Documents\practica
$fc = get-content $inputfile
$GB = [System.text.Encoding]::UTF8.Getbytes($fc)
$etext = [System.Convert]::ToBase64String($GB)
Write-Host "El contenido del archivo CODIFICADO es:" $etext -ForegroundColor Green

Write-host "DECODIFICANDO el texto previo:"
[System.text.Encoding]::ASCII.GetString([System.Convert]::FromBase64String($etext)) | Out-File -Encoding "ASCII" C:\Users\Isaias\Documents\practica
$outfile12 = get-content C:\Users\Isaias\Documents\practica
Write-Host "El texto decodificado es el siguiente:" -ForegroundColor Green
Write-Host "DECODIFICADO:" $outfile12