from urllib import response
import requests

#https://docs.github.com/es/developers/apps/building-oauth-apps/authorizing-oauth-apps

client_id = "ed8270db5c60e56e1ace"
client_scret = "dd62aadfcffd0b3414bc2cc78b19957de1f22937"
access_token = "73636373839303782032"
#armamos el url y entramos ahi encontraremos el code en la url cuando entremos code=2b5810790a1da56c92ce
#https://github.com/login/oauth/authorize?client_id=ed8270db5c60e56e1ace&scope=respo

code = '2b5810790a1da56c92ce'
url= 'https://github.com/login/oauth/access_token'
payload ={'client_id': client_id, 'client_secret': client_scret, 'code':code}
headers= {"Accept": 'application/json'}
response =requests.post(url, json=payload,headers=headers)

# Usamos el code que sacamos del url y ahora obtenemos el acces token
if response.status_code == 200:
    response_json = response.json()
    access_token = response_json['access_token']
    print(access_token)
else:
    print("No estoy mandando nada")

#Sacamos los repositorios entrando usando el token
url2 = 'repos'
headers2 = {'Authorization' : 'token 2321312312'}

response2 = requests.get(url2, headers=headers2)
if response2.status_code == 200:
    payload = response2.json()

    for project in payload:
        name = project['name']
        print(name)
else:
    print(response2.content)