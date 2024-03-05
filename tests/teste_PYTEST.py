import requests

class TestCursos:
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
    url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
    headers = {'Authorization': 'Token 107b3775b6668b6b80be07a8476b5c283936eb0b'}

    # def test_get_cursos(self):
    #     cursos = requests.get(url=self.url_base_cursos, headers=self.headers)
    #     assert cursos.status_code == 200

    # def test_get_curso(self):
    #     curso = requests.get(url=f'{self.url_base_cursos}5', headers=self.headers)
    #     assert curso.status_code == 200

    # def test_post_curso(self):
    #     novo = {"titulo":"Curso de Programação com Ruby", "url":"http://google3.com"}
    #     resultado = requests.post(url=self.url_base_cursos, headers=self.headers, data=novo)
    #     assert resultado.status_code == 201

    # def test_put_curso(self):
    #     novo = {"titulo": "Gerencia de projeto", "url": "http://www.geek10.com.br"}
    #     resultado = requests.put(url=f'{self.url_base_cursos}10/', headers=self.headers, data=novo)
    #     assert resultado.status_code == 200

    # def test_put_curso(self):
    #     resultado = requests.delete(url=f'{self.url_base_cursos}10', headers=self.headers)
    #     assert resultado.status_code == 204 