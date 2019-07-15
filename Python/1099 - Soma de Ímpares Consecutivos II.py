caso = int(input())

for i in range(caso):
    casos = input()
    casos = casos.split()
    casos = list(map(int, casos))
    casos.sort()
    soma = 0
    for j in range(casos[0]+1,casos[1]):
        if (j % 2) != 0:
            soma = soma + j
    print(soma)
