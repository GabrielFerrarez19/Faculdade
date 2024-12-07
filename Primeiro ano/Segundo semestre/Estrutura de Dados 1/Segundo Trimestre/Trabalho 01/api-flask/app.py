from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask("Minha API")
CORS(app) # Ativa cors
@app.route("/")
def index():
    return "Hello World!"

@app.route("/consulta" , methods=["GET"])
def consulta_cadastro():
    documento = request.args.get("doc")
    registro = dados(documento)
    return registro

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    try:
        payload = request.get_json()
        if not payload or "cpf" not in payload or "dados" not in payload:
            return jsonify({"error": "Requisição inválida"}), 400

        cpf = payload.get("cpf")
        valores = payload.get("dados")

        if not salvar_dados(cpf, valores):
            return jsonify({"error": "Erro ao salvar os dados"}), 500

        return jsonify({"message": "Dados cadastrados com sucesso"}), 201
    except Exception as e:
        print(f"Erro interno no servidor: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500


def carregar_arquivo():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../api-flask/dados.json")
    try:
        with open(caminho_arquivo, "r") as arq:
            return json.load(arq)
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando um novo arquivo.")
        return {}  # Retorna um dicionário vazio se o arquivo não existir
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return {}
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo: {e}")
        return {}

    
def gravar_arquivo(dados):
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../api-flask/dados.json")
    try:
        with open(caminho_arquivo, "w") as arq:
            json.dump(dados, arq, indent=4)
        print("Dados armazenados com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")
        return False


def salvar_dados(cpf, registro):
    dados_pessoas = carregar_arquivo()
    if not isinstance(dados_pessoas, dict):
        print("Erro: Estrutura de dados inválida ao carregar o arquivo.")
        return False

    dados_pessoas[cpf] = registro
    sucesso = gravar_arquivo(dados_pessoas)
    if not sucesso:
        print("Erro ao gravar os dados no arquivo.")
        return False

    return True


def dados(cpf):
    dados_pessoas = carregar_arquivo()
    vazio = {
        "nome": "não encontrado",
        "data_nascimento": "não encontrado",
        "email": "não econtrado",
    }
    cliente = dados_pessoas.get(cpf, vazio)
    return cliente


if __name__ == "__main__":
     app.run()

    