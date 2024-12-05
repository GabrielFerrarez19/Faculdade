valor = float(input("Digite o valor do produto:"))

desconto = float(input("Digite a prcentagem de desconto"))

valorDesconto = (valor*desconto)/100

valorfinal = valor - valorDesconto

print(f"O valor final do produto dera de {valorfinal}")