casos = []

for i in range(100):
    casos.append(int(input()))

casos_ordenados = casos[:]
casos_ordenados.sort()

print(casos_ordenados[99])
print(casos.index(casos_ordenados[99])+1)
