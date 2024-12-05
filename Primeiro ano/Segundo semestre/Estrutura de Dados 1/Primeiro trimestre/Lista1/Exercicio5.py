import unicodedata
import re

def remover_acentos_e_caracteres_especiais(texto):
    texto_sem_acentos = unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8')

    texto_sem_caracteres_especiais = re.sub(r'[^a-zA-Z0-9\s]', '', texto_sem_acentos)

    return texto_sem_caracteres_especiais


texto = "Olá, mundo! Como está você?"
resultado = remover_acentos_e_caracteres_especiais(texto)
print(resultado)  

def selection_sort(L):
    for i in range(len(L)-1):
        menor = i 
        for j in range(i+1, len(L)):
            if L[menor] > L[j]:
                menor = j
        L[i], L[menor] = L[menor], L[i]
        print(L)  
    return L


produtos=[]
inserir = 's'
while inserir.lower() == 's':
  item = {}
  item['nome'] = input('Digite o nome do produto: ')
  item['preco'] = float(input('Digite o preço do produto: '))
  item['qtd'] = int(input('Digite a quantidade do produto: '))
  produtos.append(item)
  inserir = input('Deseja inserir mais um produto? [S/N]')

print("\nProdutos cadastrados:")
print(produtos)