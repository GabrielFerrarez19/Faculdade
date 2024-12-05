while True:
    investimento_por_mes = float(input("Informe o valor a ser investido por mês: R$ "))
    taxa_juros_mensal = float(input("Informe a taxa de juros mensal em porcentagem: ")) / 100
    
    saldo_inicial = 0
    for mes in range(1, 13):
        saldo_inicial += investimento_por_mes
        saldo_inicial += saldo_inicial * taxa_juros_mensal
        
    print(f"Saldo do investimento após 1 ano: R$ {saldo_inicial:.2f}")
    
    continuar = input("Deseja processar mais um ano? (S/N): ")
    if continuar.lower() != 's':
        break
