import requests
import json
#nombre:gabriela hermenegildo otero
#matricula: 1990138
if __name__ == '__main__' :
    url='http://httpbin.org/post'
    argumentos={'nombre':'Gabriela','matricula':'1990138','curso':'Programacion para Ciberseguridad'}

    response =requests.post(url, params=argumentos)

    if response.status_code ==200:
        print(response.content)
