def Calcula_media(lista):
    media = sum(lista)/ len(lista)
    print(f"A media foi de {media}")

print("NAME")
print(__name__)
if __name__ == "__main__":
    Calcula_media([1,2,3,4,5,6])
    Calcula_media([10,20,30])
    Calcula_media([100,200,300,400])
    Calcula_media([1000,2000,3000])

