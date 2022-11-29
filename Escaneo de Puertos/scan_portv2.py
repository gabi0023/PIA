#!/usr/bin/python
#
#Nombre: Gabriela Hermenegildo Otero
#Matricula: 1190138
#
# -*- coding: utf-8 -*-
#Parte 1
#importamos librerias necesarias
import socket
#parte 2
#Se define la funcion scan con la cual se
#utilizan sockets para probar los diferentes puertos
def scan (addr, port):
    #creando un nuevo socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Estableciendo el timeout para el nuevo objeto tipo socket
    socket.setdefaulttimeout(1)

    #conexion exitosa devuelve 0. Devuelve error en caso contrario
    result = socket_obj.connect_ex((addr, port)) #direccion y puerto en tupla

    #se cierra el objeto
    socket_obj.close()

    return result
#parte 3
#lista de puertos a escanear
ports = [21,22,25,80]
#parte 4
#bucle por todas las ip del rango 192.168.0.*
for i in range(1, 255):
    addr = "192.168.1.{}".format(i)
    for port in ports:
        result = scan(addr, port)
        if result == 0:
            print(addr, port, "OK")
        else:
            print(addr, port, "Failed")
