valor = [None] * 5
cont = 0
for x in range(5):
    valor[x] = float(input())
for y in valor:
    if ((y % 2) == 0):
        cont = cont + 1
print(str(cont) + " valores pares")
