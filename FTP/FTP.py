#Script para transferencia de FTP
#Objetivo: conectarse a servidor ftp y hacer un upload de un archivo
#19/11/2022 - Gabriela Hermenegildo Otero
#
#Importando modulo ftp
from ftplib import FTP
#
#Estableciendo conexion a un servidor
#
ftp=FTP("192.168.56.3")
#Accediendo con el usuario johnny
print(ftp.login("johnny", "1990138"))
#se mueve al directorio upload
print(ftp.cwd("upload"))
#Muestra lo que hay en el directorio actual
print(ftp.retrlines("LIST"))
#Se manda llamar un archivo
text_file=open(r"C:\Users\gabri\ADVERTENCIA.txt", "rb")
#se modifica el documento en caso de existir o se agrega uno nuevo 
print(ftp.storlines("STOR ADVERTENCIA.txt", text_file))
#Salimos del servidor
print(ftp.quit())