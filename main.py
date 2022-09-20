import requests
import json
if __name__ == '__main__':
    url='https://httpbin.org/get'
    args = {'nombre': 'Arturo', 'curso': 'python', 'nivel': 'basico'}
    response = requests.get(url,params=args)
    
    print(response)

    if response.status_code == 200:
        #print(response.content) #regresa el contenido de la url
        #response_json = response.json() #crea un diccionario
        #origin = response_json['origin']
        #print(origin)

        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)