#!/bin/bash
#Script superscan.sh
#Gabriela Hermenegildo Otero 1990138
#
c=0
while [ $c != 5 ] ; do 
	echo "------------------"
	echo " Menu principal"
	echo "------------------"
	echo "1. Escaneo de red"
	echo "2. Escaneo individual"
	echo "3. Escaneo UDP"
	echo "4. Escaneo de script"
	echo "5. Salir"
	read -p "opcion [ 1 - 5 ] " c
	case $c in 
		1)/home/gabi/Escritorio/Escaneo-de-red.sh
		;;
		2)/home/gabi/Escritorio/Escaneo-individual.sh
		;;
		3)/home/gabi/Escritorio/Escaneo-udp.sh
		;;
		4)/home/gabi/Escritorio/Escaneo-de-script.sh
		;;
		5) echo "Adios, hasta la proxima"; exit 0 ;;
	esac 
done
