import requests

url='http://httpbin.org/cookies'
cooki = {'my-cooki': 'true'}
response = requests.get(url,cookies=cooki)


if response.status_code == 200: #tambien se puede usar response.ok
    cookies = response.cookies
    print(cookies)
    print("El contenido es:")
    print(response.content)