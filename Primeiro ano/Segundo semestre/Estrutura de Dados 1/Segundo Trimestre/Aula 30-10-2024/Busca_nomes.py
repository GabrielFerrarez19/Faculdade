# biblioteca que permite fazer requisições (solicitações)
import requests
import busca_seuqnecial

def busca_nomes(qnt=20):
    url = f"https://gerador-nomes.wolan.net/apelidos/{qnt}"
    response = requests.get(url) 
    resultado = response.json()
    return resultado

def busca_ibge():
    url = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/"
    response = requests.get(url)
    # print(response)
    resultado = response.json()

    lista_nomes = []
    for i in range(len(resultado)):
        elemento = resultado[i]
        nome = elemento["nome"]
        lista_nomes.append(nome)
    return lista_nomes

if __name__ == "__main__":
    lista_nomes = busca_nomes()
    print(lista_nomes)
    aux = input("Digite o nome procurado: ")
    indice = busca_seuqnecial.busca_sequencial(lista_nomes,"GABRIEL")
    if indice >= 0:
        print(f"{aux} esta na indice {indice}")
    else:
        print(f"{aux} não esta na lista")