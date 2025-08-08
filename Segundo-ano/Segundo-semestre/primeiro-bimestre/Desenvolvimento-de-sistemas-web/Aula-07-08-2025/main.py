# Importa a classe FastAPI do framework FastAPI
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
app = FastAPI()

# Define uma rota GET para o caminho raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma resposta JSON com uma mensagem de saudação
    return {"message": "Hello World"}


