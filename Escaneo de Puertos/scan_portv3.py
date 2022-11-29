#!/usr/bin/python
#
#Nombre: Gabriela Hermenegildo Otero
#Matricula: 1190138
#
# -*- coding: utf-8 -*-
#parte 1
#Importamos librerias necesarias
import sys
import threading
from socket import *
#parte 2
#creamos una funcion tcp_test la cual
#permite probar mediante socket los puertos
#abiertos, se le agregan lock.release()
def tcp_test(port):
    sock=socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result=sock.connect_ex((target_ip, port))
    if result==0:
        print("opened Port:", port)
#parte3
#establecemos el main del script
#guardamos en varibales host y portstrs
if __name__=='__main__':
    #portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs=sys.argv[2].split('-')
#parte4
#portstrs se convierte en lista al momento
#de hacer split y de ahi obtener dos valores
start_port=int(portstrs[0])
end_port=int(portstrs[1])
#parte 5
#usando la funcion gethostbyname se obtiene
#la direccion ip
target_ip=gethostbyname(host)
#parte 6
#se inica bucle para probar puertos
#usando la funcion tcp_test y generando
#un hilo por cada puerto a probar
hilos =[]
for port in range (start_port, end_port):
    hilo=threading.Thread(target=tcp_test, args=(port,))
    hilos.append(hilo)
    hilo.start()