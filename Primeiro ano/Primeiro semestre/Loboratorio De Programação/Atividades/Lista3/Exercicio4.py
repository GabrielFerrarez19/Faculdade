while True:
    num = int(input("Digite um número para verificar seus divisores e se é primo: "))
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    
    print("Divisores de", num, ":", divisores)
    
    primo = True if len(divisores) == 2 else False
    if primo:
        print(num, "é um número primo.")
    else:
        print(num, "não é um número primo.")
    
    continuar = input("Deseja analisar outro número? (s/n): ")
    if continuar.lower() != 's':
        break
