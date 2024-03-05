import requests, jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados)

#resultados primeira pessoa
primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeira)

#nome primeira pessoa
nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

#todos os nomes das pessoas que avaliaram o curso
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)