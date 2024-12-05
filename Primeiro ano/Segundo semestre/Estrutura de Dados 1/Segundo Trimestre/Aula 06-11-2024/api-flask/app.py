from flask import Flask, request
from flask_cors import CORS

app = Flask("Minha API")
CORS(app) #ativar cors

@app.route("/")
def homepage():
    return "Hello World!"

@app.route("/soma")
def soma():
    s = 0
    for i in range(20):
        s += i
    return f"resultado = {s}"

#http://127.0.0.1:5000/multi?nome=jose&varx=8&vary=15
@app.route("/multi", methods={"GET"})
def mult():
    nome = request.args.get("nome")
    x = request.args.get("varx", type=float)
    y = request.args.get("vary") # y sera str
    y = float(y)
    resultado = x * y
    return f"Ola {nome}, o resultado é = {resultado}"

@app.route("/consulta", methods={"GET"})
def consulta_cadastro():
    documento = request.args.get("doc")
    resgistro = dados(documento)
    return resgistro


def dados(cpf):
    dados_pessoas={
        "00000000001": {
            "nome":"joão da Silva",
            "data_nascimento":"1990-05-20",
            "email":"joãodasilva@exemplo.com",
            },
            "00000000002": {
                "nome":"Maria Oliveira",
                "data_nascimento":"1985-09-20",
                "email":"mariaoliveira@exemplo.com",
            },
            "00000000003": {
                "nome":"Carlos Pereira",
                "data_nascimento":"1978-02-10",
                "email":"carlospereira@exemplo.com",
            },
            "00000000004": {
                "nome":"Ana costa",
                "data_nascimento":"1995-07-25",
                "email":"Anacosta@exemplo.com",
            },
            "00000000005": {
                "nome":"Paula Souza",
                "data_nascimento":"2000-11-30",
                "email":"PaulaSouzaa@exemplo.com",
            },
    } 
    vazio = {
        "nome":"Não encontrado",
        "data_nascimento":"Não encontrado",
        "email":"Não encontrado",
    }
    cliente = dados_pessoas.get(cpf,vazio)
    return cliente



if __name__ == "__main__":
    app.run(debug="True")