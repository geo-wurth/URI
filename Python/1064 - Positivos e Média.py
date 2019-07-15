valor = [None] * 6
cont = 0
media = 0
for x in range(6):
    valor[x] = float(input())
for y in valor:
    if y > 0:
        media = media + y
        cont = cont + 1
print(str(cont) + " valores positivos")
print(str(round((media / cont), 1)))
