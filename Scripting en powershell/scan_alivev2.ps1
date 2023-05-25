$subred = (Get-NetRoute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "== Determinando tu Gateway ..."
Write-Host "Tu gateway: $subred"

$rango = $subred.Substring(0,$subred.IndexOf('.') + 1 + $subred.Substring($subred.IndexOf('.') +1).IndexOf('.') + 3 )
Write-Host "== Determinando tu rango de Subred ..."
echo $rango

$punto = $rango.EndsWith('.')
if ( $punto -like "False")
{
    $rango = $rango + '.'

}

$rango_ip = @(1..254)
Write-Output ""
Write-Host "-- Subred Actual: "
Write-Host "Escaneando: " -NoNewline ; Write-Host $rango -NoNewline; Write-Host "0/24" -ForegroundColor Red
Write-Output ""
foreach ( $r in $rango_ip)
{
    $actual = $rango + $r 
    $responde = Test-Connection $actual -Quiet -Count 1
    if ( $responde -eq "True" )
    {    
        Write-Output ""
        Write-Host "Host responde: "-NoNewline; Write-Host $actual -ForegroundColor Green
    }
}