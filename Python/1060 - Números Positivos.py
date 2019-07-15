valor = [None] * 6
cont = 0
for x in range(6):
    valor[x] = float(input())
for y in valor:
    if y > 0:
        cont = cont + 1
print(str(cont) + " valores positivos")
