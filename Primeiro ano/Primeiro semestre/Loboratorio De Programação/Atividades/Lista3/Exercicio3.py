n = int(input("Digite o número para calcular a série de Fibonacci: "))

fibonacci = [0, 1]

for i in range(2, n+1):
    fib = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(fib)

print("A série de Fibonacci para o número", n, "é:")
for num in fibonacci[:n+1]:
    print(num, end=", ")
