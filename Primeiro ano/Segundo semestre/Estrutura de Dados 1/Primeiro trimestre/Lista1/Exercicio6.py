def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


alunos = [
    ("Ana", 85),
    ("Bruno", 90),
    ("Carlos", 75),
    ("Diana", 95),
    ("Eduardo", 80)
]


insertion_sort(alunos)

print("Essa e a lista ordenada em insertion sort:")

i =1 
for alunos in alunos:
    print(f"{i}. Nome:{alunos[0]}|Nota:{alunos[1]}")
    i+=1
