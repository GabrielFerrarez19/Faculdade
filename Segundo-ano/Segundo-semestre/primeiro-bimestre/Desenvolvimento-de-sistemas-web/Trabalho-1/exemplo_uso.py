
import requests
import json


BASE_URL = "http://localhost:8000"

def criar_categoria(nome):

    url = f"{BASE_URL}/categorias/"
    data = {"nome": nome}
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else response.text

def criar_produto(nome, preco, categoria_id):

    url = f"{BASE_URL}/produtos/"
    data = {
        "nome": nome,
        "preco": preco,
        "categoria_id": categoria_id
    }
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else response.text

def listar_categorias():

    url = f"{BASE_URL}/categorias/"
    response = requests.get(url)
    return response.json()

def listar_produtos():

    url = f"{BASE_URL}/produtos/"
    response = requests.get(url)
    return response.json()

def listar_produtos_por_categoria(categoria_id):

    url = f"{BASE_URL}/produtos/categoria/{categoria_id}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print("🚀 Exemplo de uso da API REST - Loja")
    print("=" * 50)
    
    print("\n💡 Para testar a API:")
    print("1. Execute: uvicorn main:app --reload")
    print("2. Acesse: http://localhost:8000/docs")
    print("3. Descomente o código acima e execute este arquivo")
