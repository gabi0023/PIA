#!/bin/bash
#
#Gabriela Hermenegildo Otero
#Escaneo individual
#
read -p  "ingresa la ip: " ip
nmap -v -A $ip -oN Escaneo_individual.txt
