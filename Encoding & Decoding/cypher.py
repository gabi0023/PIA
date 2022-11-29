#importamos fernet desde cryptography
#nombre:gabriela Hermenegildo Otero
#matricula:1990138
#
import cryptography
from cryptography.fernet import Fernet
#Definicion del funcion genwrite que genera una llave para cifrado
def genwrite():
    key = Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)
#llamamos a la funcion para generar el archivo "pass.key" que contiene la llave
genwrite()
#definicion de la funcion call_key con la cual leemos el contenido del archivo "pass.key"
def call_key():
    return open ("pass.key","rb").read()
#
#ahora ciframos un mensaje almacenado y codificado previamente
key= call_key()
banner ="Hola, mundo".encode()
a = Fernet (key)
coded_banner =a.encrypt(banner)
print(coded_banner)
#
#Ahora desciframos el mensaje previamente cifrado
key =call_key()
b=Fernet(key)
decoded_banner=b.decrypt(coded_banner)
print(decoded_banner)
#
#fin del script