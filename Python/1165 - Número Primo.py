caso = int(input())
for i in range(caso):
    casos = int(input())
    primos = []
    for j in range(2,casos+1):
        if casos % j == 0:
            primos.append(j)
    if sum(primos) == casos:
        print(str(casos) + " eh primo")
    else:
        print(str(casos) + " nao eh primo")
