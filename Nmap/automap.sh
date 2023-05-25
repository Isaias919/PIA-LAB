#!/bin/bash

echo "----------------------------"
echo "       Menu principal       "
echo "----------------------------"
echo "1. Escaneo de red"
echo "2. Escaneo individual"
echo "3. Escaneo udp"
echo "4. Escaneo de script"
echo "5. Salir"
read -p "Opcion [ 1 - 5 ] " c
case $c in
	1)read -p "Escribe la IP de la subred: " subred; 
	    echo "Por default sera un analisis completo de la subred"
		nmap -sn $subred/24 -oN Escaneo_de_red.txt;;

	2)read -p "Escribe la IP para escanear y detectar sus servicios: " IP;
	  	nmap -O -sV $IP -oN Escaneo_individual.txt;;
	
	3)read -p "Escribe una IP a escanear en tipo UDP:" IP;
	  	nmap -sU -F $IP -oN Escaneo_udp.txt;;

	4)read -p "Escribe una IP a escanear de script:" IP;
	  	nmap -sC $IP -oN Escaneo_de_script.txt;;

	5)echo "Muchas gracias por utilizar este script, hasta la proxima";
	  echo "Finalizando...";
	  exit 0;;
esac