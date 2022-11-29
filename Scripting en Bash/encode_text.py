import base64
#
#Obtenemos una frase desde el input principal
#
print ("Bienvenido a codificadorBase64 en python")
frase = input ("proporciona una frase para codificar: ")
#
#obtenemos los bytes de la frase
#
frase_bytes = frase.encode('ascii')
#
#Se calculan los bytes en base64
#
base64_bytes = base64.b64encode(frase_bytes)
#
#se genera mensaje en base64
#
base64_message = base64_bytes.decode('ascii')
print ("la frse codificada en Base 64 es: ")
print(base64_message)