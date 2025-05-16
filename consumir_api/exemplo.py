import requests


def exemplo_cep():
    cep = '01001000'
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        print(f'Logradouro: {dados["logradouro"]}')
        print(f"Cidade: {dados['localidade']} - {dados['uf']}")
        print(f'cep: {dados["cep"]}')
        print(f'bairro: {dados["bairro"]}')
        print(f'ddd: {dados["ddd"]}')

    else:
        print({'erro':response.status_code})


def exemplo_get():
    url="https://jsonplaceholder.typicode.com/posts/1"

def exemplo_put():
    url="https://jsonplaceholder.typicode.com/posts/1"

def exemplo_post():
    url="https://jsonplaceholder.typicode.com/posts"
