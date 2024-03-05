import requests


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

novo_curso = {"titulo": "Gerencia de projeto", "url": "http://www.geek2.com.br"}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)
print(resultado)

#testando o 201 do post
assert resultado.status_code == 201

#Testando se o titulo retornado é o mesmo informado
assert resultado.json()['titulo'] == novo_curso['titulo']