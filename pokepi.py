from ast import arg
from unittest import result
from urllib import response
from webbrowser import get
import requests


def get_pokemon(url='https://pokeapi.co/api/v2/pokemon-form', offset=0):
    arg = {'offset' : offset} if offset else {}
    response = requests.get(url, params=arg)

    if response.status_code == 200:
        payload = response.json()
        result = payload.get('results',[])
        if result:
            for pokemon in result:
                name = pokemon['name']
                print(name)

        next = input('Quieres mas pokemon? [Y/N]')
        if next == 'y':
            get_pokemon(offset=offset+20)

get_pokemon()