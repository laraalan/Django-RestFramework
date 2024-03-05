import requests


url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

deleta_curso = {"titulo": "Gerencia de projeto", "url": "http://www.geek3.com.br"}

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

#testando o 204 do delete
assert resultado.status_code == 204

# #Testando se o tamanho do resultado é 0
assert len(resultado.text) == 0