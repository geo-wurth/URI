caso = int(input())
casos = [None] * caso
casos_in = 0
casos_out = 0

for x in range(caso):
    casos[x] = int(input())

for x in casos:
    if x in range(10,20):
        casos_in = casos_in + 1
    else:
        casos_out = casos_out + 1

print(str(casos_in) + " in")
print(str(casos_out) + " out")
