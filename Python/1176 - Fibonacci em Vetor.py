fibonacci = [0, 1]
caso = int(input())
for i in range(caso):
    casos = int(input())
    if casos > 1:
        if (len(fibonacci)-1) < casos:
            for j in range(len(fibonacci)-1,casos):
                proximo_fibonacci = fibonacci[j] + fibonacci[j-1]
                fibonacci.append(proximo_fibonacci)
    print("Fib(" + str(casos) + ") = " + str(fibonacci[casos]))
