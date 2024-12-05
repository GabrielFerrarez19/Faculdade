import os
import unicodedata

# Função para remover acentos e caracteres especiais
def remover_acentos(palavra):
    return ''.join(ch for ch in unicodedata.normalize('NFD', palavra)
                   if unicodedata.category(ch) != 'Mn')

# Mensagem de abertura
print("********** JOGO DA FORCA **********")

# Captura da palavra secreta
palavra_secreta_original = input("Digite a palavra secreta: ").strip().upper()
palavra_secreta = remover_acentos(palavra_secreta_original).upper()

# Limpar a tela
os.system('cls' if os.name == 'nt' else 'clear')

# Inicialização das estruturas
letras_certas = ['_' if letra.isalpha() else ' ' for letra in palavra_secreta]
acertou = False
errou = False
erros = 0
tentativas = []

# Jogo da forca
while not acertou and not errou:
    # Mostrar o estado atual da palavra secreta
    print("Palavra: " + ' '.join(letras_certas))
    
    # Captura da letra do jogador
    tentativa = input("Digite uma letra: ").strip().upper()
    
    # Verificar se a entrada é válida (uma letra)
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Entrada inválida. Digite apenas uma letra.")
        continue
    
    # Verificar se a letra já foi tentada
    if tentativa in tentativas:
        print(f"Você já tentou a letra '{tentativa}'.")
        continue
    
    # Adicionar a letra às tentativas
    tentativas.append(tentativa)
    
    # Verificar se a letra está na palavra secreta
    if tentativa in palavra_secreta:
        print(f"A letra '{tentativa}' está na palavra secreta!")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == tentativa:
                letras_certas[i] = tentativa
    else:
        print(f"A letra '{tentativa}' não está na palavra secreta.")
        erros += 1
    
    # Verificar se todas as letras foram descobertas
    if '_' not in letras_certas:
        acertou = True
    # Verificar se o jogador perdeu
    elif erros >= 6:
        errou = True

# Fim do jogo
print("\nFim do jogo!")
if acertou:
    print("Parabéns! Você descobriu a palavra secreta: " + palavra_secreta_original)
else:
    print("Você perdeu! A palavra secreta era: " + palavra_secreta_original)