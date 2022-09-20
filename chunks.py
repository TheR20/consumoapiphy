from urllib import response
import requests
import json
#vamos a descargar un imagen
url = "https://i.imgur.com/lwLpNsW.jpeg"

response = requests.get(url, stream=True) #stream deja la conexion abierta
with open('image.jpg', 'wb') as file:
    for chunk in response.iter_content(): #toma toda la info y la convierte poco a poco 
        file.write(chunk)
response.close() #cierra la conexion
