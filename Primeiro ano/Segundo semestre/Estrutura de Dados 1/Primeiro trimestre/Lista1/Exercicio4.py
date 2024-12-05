import string

def verifica_palindromo():
    frase = input("Digite a sua frase: ")
    
    fraselimpa = ''.join(char.lower() for char in frase if char not in string.punctuation and char != ' ')
    
    if fraselimpa == fraselimpa[::-1]:
        print("A frase é um palíndromo!")
    else:
        print("A frase não é um palíndromo.")

verifica_palindromo()
