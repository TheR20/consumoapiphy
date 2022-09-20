import requests
import json

url='https://httpbin.org/put'
payload = {'nombre': 'Arturo', 'curso': 'python', 'nivel': 'basico'}
headers = {'Conten-Type': 'application/json', 'access-toke': '12345' }
response = requests.put(url, json=payload, headers=headers) #manda en data el diccionario
print(response.url)

if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers
        server = headers_response['server']
        print(server)