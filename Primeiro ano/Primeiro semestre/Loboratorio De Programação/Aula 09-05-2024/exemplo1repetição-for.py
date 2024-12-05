import random

X=int(input("Digite a quantidade: "))
cont=1
#while cont <= X:
    #print(cont)
    #cont += 1
#for cont in range(1,X):   #for cont in range(1,X+1): #for cont in range(X):
    #print(cont)
soma=0
for _ in range(X):
    num = random.randint(1,10)
    soma+=num
    print(num)
    cont+=1
print("===================")
print(soma) 