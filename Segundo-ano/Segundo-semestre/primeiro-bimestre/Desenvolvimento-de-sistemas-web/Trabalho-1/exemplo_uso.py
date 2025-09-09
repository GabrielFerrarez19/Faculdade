"""
Exemplo de uso da API REST - Loja
Este arquivo demonstra como usar a API para criar categorias e produtos
"""

import requests
import json

# URL base da API
BASE_URL = "http://localhost:8000"

def criar_categoria(nome):
    """Criar uma nova categoria"""
    url = f"{BASE_URL}/categorias/"
    data = {"nome": nome}
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else response.text

def criar_produto(nome, preco, categoria_id):
    """Criar um novo produto"""
    url = f"{BASE_URL}/produtos/"
    data = {
        "nome": nome,
        "preco": preco,
        "categoria_id": categoria_id
    }
    response = requests.post(url, json=data)
    return response.json() if response.status_code == 201 else response.text

def listar_categorias():
    """Listar todas as categorias"""
    url = f"{BASE_URL}/categorias/"
    response = requests.get(url)
    return response.json()

def listar_produtos():
    """Listar todos os produtos"""
    url = f"{BASE_URL}/produtos/"
    response = requests.get(url)
    return response.json()

def listar_produtos_por_categoria(categoria_id):
    """Listar produtos de uma categoria específica"""
    url = f"{BASE_URL}/produtos/categoria/{categoria_id}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print("🚀 Exemplo de uso da API REST - Loja")
    print("=" * 50)
    
    # Exemplo de uso (descomente para testar)
    """
    # Criar categorias
    print("📁 Criando categorias...")
    cat1 = criar_categoria("Eletrônicos")
    cat2 = criar_categoria("Roupas")
    print(f"Categoria criada: {cat1}")
    print(f"Categoria criada: {cat2}")
    
    # Criar produtos
    print("\n📦 Criando produtos...")
    prod1 = criar_produto("Smartphone", 999.99, 1)
    prod2 = criar_produto("Notebook", 2500.00, 1)
    prod3 = criar_produto("Camiseta", 49.90, 2)
    print(f"Produto criado: {prod1}")
    print(f"Produto criado: {prod2}")
    print(f"Produto criado: {prod3}")
    
    # Listar categorias
    print("\n📋 Listando categorias...")
    categorias = listar_categorias()
    print(json.dumps(categorias, indent=2, ensure_ascii=False))
    
    # Listar produtos
    print("\n📋 Listando produtos...")
    produtos = listar_produtos()
    print(json.dumps(produtos, indent=2, ensure_ascii=False))
    
    # Listar produtos por categoria
    print("\n📋 Produtos da categoria Eletrônicos...")
    produtos_eletronicos = listar_produtos_por_categoria(1)
    print(json.dumps(produtos_eletronicos, indent=2, ensure_ascii=False))
    """
    
    print("\n💡 Para testar a API:")
    print("1. Execute: uvicorn main:app --reload")
    print("2. Acesse: http://localhost:8000/docs")
    print("3. Descomente o código acima e execute este arquivo")
