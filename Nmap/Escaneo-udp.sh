#!/bin/bash
#
#Gabriela Hermenegildo Otero
#Escaneo udp
#
read -p  "ingresa la ip: " ip
nmap --script ssl-poodle $ip -oN Escaneo_udp.txt
