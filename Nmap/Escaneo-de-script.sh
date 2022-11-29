#!/bin/bash
#
#Gabriela Hermenegildo Otero
#Escaneo de script
#
read -p  "ingresa la ip: " ip
echo "Escribe el nombre del script que se va a utilizar: "
echo "consejo prueba con: ssl-ccs-injection"
read script
nmap --script $script $ip -oN Escaneo_de_script.txt
