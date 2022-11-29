#!/bin/bash
#Script netdiscover.sh
#1/10/22 - Gabriela Hermenegildo Otero
#
#Escaner de red basico en BASH 
#
#Determinando el segmento de red
which if config && { echo "comando ifconfig existe...";
			direccion_ip=`ifconfig |grep inet |grep -v "127.0.0.1" |awk '{ print $2}'`; 
			echo "Esta es tu direccion ip: $direccion_ip";
			subred=`ifconfig |grep inet |grep -v "127.0.0.1" |awk '{ print $2}'|awk -F. '{print $1"."$2"."$3"."}'`;
			echo "esta es tu subred: $subred";
			}\
			|| { echo "no existe el comando ifconfig...usando ip";
			direccion_ip=`ip addr show |grep -w inet | grep -v "127.0.0.1" |awk '{ print $2}'`;
			echo "esta es tu direccion ip: $direccion_ip";
			subred=`ip addr show |grep -w inet | grep -v "127.0.0.1" |awk '{ print $2}'|awk -F. '{print $1"."$2"."$3"."}'`;
			echo "esta es tu subred: $subred"; 
			}
for ip in {1..254}
do 
	ping -q -c 4 ${subred}${ip} > /dev/null
	if [ "$?" = 0 ]
	then 
		echo "host responde: ${subred}${ip}"
	fi 
done
