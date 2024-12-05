import random 

mao =["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]


while len(mao) > 0:

    sorteia = random.randint(0, 13)

    print ("seleciona" , end="")

    print (mao[sorteia])  

    del mao[sorteia]

    print (mao)
    

    