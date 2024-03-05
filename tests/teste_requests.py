import requests

#GET AVALIACOES

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# #Acessando status code da resposta
# print(avaliacoes.status_code)

# #Acessando dados da resposta em um dicionario python
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# #Acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# #Acessando a proxima pagina
# print(avaliacoes.json()['next'])

# #Acessando resultados
# print(avaliacoes.json()['results'])

# #Acessando primeiro resultado
# print(avaliacoes.json()['results'][0])

# #Acessando nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# #Get Avaliacao
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/3/')
# print(avaliacao.json())


#GET CURSOS

headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.json())
print(cursos.status_code)

