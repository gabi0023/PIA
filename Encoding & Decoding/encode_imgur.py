import requests
# Para hacer un request a un sitio
#
#nombre:Gabriela Hermenegildo otero
#matricula:1990138
#
import base64
#para encode/decode en base64
from requests import Response
#
##Para descargargar la imagen del sitio
#
if __name__=='__main__':
    url= 'https://i.imgur.com/LWc9gko.png'

    Response: Response = requests.get(url, stream=True)
    with open('stones.jpg', 'wb') as file_down:
        for chunk in Response.iter_content():
            file_down.write(chunk)
    Response.close()
#
##para codificar la imagen
#
with open ('stones.jpg','rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data= base64.b64encode(binary_file_data)
    base64_messsage=base64_encoded_data.decode('utf8')

    print (base64_messsage)