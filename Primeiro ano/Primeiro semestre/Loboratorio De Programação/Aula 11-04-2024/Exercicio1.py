peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = (peso/altura**2)


print (imc)
if imc < 18.5:
    print("Voce esta abaixo do peso")
elif imc > 18.5 and imc < 24.9:
    print("Voce esta saldavel")
elif imc > 25.0 and imc < 29.9:
    print("Voce esta com peso em acesso")
elif imc > 30.0 and imc < 34.9:
    print("voce esta no nivel de obesidade grua 1")
elif imc > 35.5 and imc < 39.9:
    print("voce esta no nivel de obesidade grua 2(severa)")
elif imc > 40.0:
    print("voce esta no nivel de obesidade grua 3(morbida)")