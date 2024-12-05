from numerizer import numerize 
from deep_translator import GoogleTranslator

def escolher_lingua():
    linguas_disponiveis = GoogleTranslator().get_supported_languages(as_dict=True)
    print(linguas_disponiveis)


    print("Línguas disponíveis para tradução:")
    for nome_lingua in linguas_disponiveis:
        print(f"- {nome_lingua}")

    lingua_escolhida = input("Insira o nome da língua desejada: ").strip().title()

    if lingua_escolhida in linguas_disponiveis:
        sigla_lingua = linguas_disponiveis[lingua_escolhida]
        print(f"A língua escolhida foi '{lingua_escolhida}' com a sigla '{sigla_lingua}'.")
        return sigla_lingua
    else:
        print("Língua não encontrada. Por favor, insira um nome válido.")
        return None


sigla = escolher_lingua()
print(sigla)
tradutor = GoogleTranslator(suurce="pt", target=sigla)
texto = input("Digite um texto")
traduzido = tradutor.translate(texto)
print(traduzido)