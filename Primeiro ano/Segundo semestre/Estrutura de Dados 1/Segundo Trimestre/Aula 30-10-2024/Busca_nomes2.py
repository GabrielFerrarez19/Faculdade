import requests
import busca_seuqnecial

def busca_nomes(qnt=20):
    url = f"https://gerador-nomes.wolan.net/apelidos/{qnt}"
    response = requests.get(url) 
    resultado = response.json()
    return resultado

if __name__ == "__main__":
    lista_nomes = busca_nomes()
    print(lista_nomes)
    aux = input("Digite o nome procurado: ")
    indice = busca_seuqnecial.busca_sequencial(lista_nomes, aux)
    if indice >= 0:
        print(f"{aux} esta no   indice {indice}")
    else:
        print(f"{aux} não esta na lista")

