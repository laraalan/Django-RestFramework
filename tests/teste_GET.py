import requests


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

resultado = requests.get(url=url_base_cursos, headers=headers)
# print(resultado.json())

#testando se o endpoint está correto
assert resultado.status_code == 200

#testando a quantidade de registros
assert resultado.json()['count'] == 3

#testando o titulo do primeiro curso
assert resultado.json()['results'][0]['titulo'] == 'python'