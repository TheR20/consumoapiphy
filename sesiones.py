import requests
url=''

session = requests.session()
session.auth = ('correo', 'contra')

response = session.get(url)
if response.ok:
    print(response.content)
    response = session.get('url con el codigo ')
    if response.ok:
        print(response.cookies)