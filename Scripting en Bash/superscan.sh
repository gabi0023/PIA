#!/bin/bash
#Script superscan.sh
#1/10/22 - Gabriela Hermenegildo Otero
#
date 
echo "----------------"
echo " Menu principal"
echo "----------------"
echo "1. Netdiscover"
echo "2. portscanv1"
echo "3. welcome"
echo "4. Exit"
read -p "opcion [ 1 - 4 ] " c
case $c in 
	1)/home/gabi/Escritorio/netdiscover.sh ;;
	2) /home/gabi/Escritorio/portscanv1.sh;;
	3)/home/gabi/Escritorio/welcome.sh;;
	4)echo "Adios"; exit 0;;
esac 
