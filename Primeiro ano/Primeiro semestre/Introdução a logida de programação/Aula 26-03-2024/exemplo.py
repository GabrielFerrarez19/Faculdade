lista1=["teste","abobrinha","bolacha"]
print(f"Lista1={lista1}")
del lista1[0]
print(F"lista1={lista1}")

for i in range(0,11):
    print(f"Linha numero {i}")



lista2=[1,2,3,4,5,6,7,8,9]
        


#for x in range(1,1000001):
     #print(F"contagem: {x}")


#x = 0 

#while x < 10:
    #x=int(input("Digite um valor: "))

senha = "123456"
m = ""
while m != senha:
    m=input("Digite a senha: ")


#nota = float(input("Digite a nota (0-100):"))
#while nota < 0 or nota > 100:
 #   nota = float(input("Nota invalida. Tente novamente: "))
  #  #print(f"Nota invalida: {nonta}. Tente novamente")
#print(f"A nota válida foi: {nota}")
    

while True:
    n = int(input("Digite um numero inteiro: "))
    print(f"Voce digitou {n}")
    if n == 9:
        print("Parabens, agora podemos sair do loop")
        break