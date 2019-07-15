caso = int(input())
casos = []
media = []

for i in range(caso):
    casos = input()
    casos = casos.split()
    n1 = float(casos[0])
    n2 = float(casos[1])
    n3 = float(casos[2])
    media.append((n1*2+n2*3+n3*5)/10)

for i in range(caso):
    print(round(media[i],1))
