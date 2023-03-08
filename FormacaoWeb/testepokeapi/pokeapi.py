import requests

cep = input()

r = requests.get(f'https://viacep.com.br/ws/{cep}/json')
r = r.text


