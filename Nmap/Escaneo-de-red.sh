#!/bin/bash
#
#Gabriela Hermenegildo Otero
#Escaneo de red 
#
read -p  "ingresa la subred: " subred
nmap -sn $subred -oN Escaneo_de_red.txt
