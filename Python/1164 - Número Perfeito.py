caso = int(input())
for i in range(caso):
    casos = int(input())
    divisores = []
    for j in range(1,casos-1):
        if casos % j == 0:
            divisores.append(j)
    if sum(divisores) == casos:
        print(str(casos) + " eh perfeito")
    else:
        print(str(casos) + " nao eh perfeito")
