#Nombre: Gabriela Hermenegildo Otero
#Matricula: 1990138
#
#importar modulos
import requests
import csv
from bs4 import BeautifulSoup
#Direccion de la pagina web
url= "http://quotes.toscrape.com/"
#ejecutar GET-request
response= requests.get(url)
#Analizar sintacticamente el archivo HTML de Beaautifulsoup del texto fuente
html= BeautifulSoup(response.text, 'html.parser')
#estraer todas las citas y autores del archivo HTML
quotes_html= html.find_all('span', class_="text")
authors_html=html.find_all('small',class_="author")
#crear una lista de las citas
quotes=list()
for quote in quotes_html:
    quotes.append(quote.text)
#Crear una lista de los autores
authors=list()
for author in authors_html:
    authors.append(author.text)
#para hacer el test: combinar y mostrar las entradas de ambas listas
for t in zip (quotes,authors):
    print(t)
#guardar las citas y los autores en el archivo csv en el directorio actual
#abrir el archivo con excell/libreOffice, etc
with open ('./citas_1990138.csv','w') as csv_file:
    csv_writer= csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes,authors))
