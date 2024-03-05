import requests


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

atualiza_curso = {"titulo": "Gerencia de projeto", "url": "http://www.geek3.com.br"}

resultado = requests.put(url=f'{url_base_cursos}10/', headers=headers, data=atualiza_curso)
print(resultado.json())


#testando o 200 do put
assert resultado.status_code == 200

# #Testando se o titulo retornado é o mesmo informado
# assert resultado.json()['titulo'] == atualiza_curso['titulo']