import math
while True:
    caso = list(map(int, input().split()))
    if caso[0] == 0:
        break
    lado_terreno = int(math.sqrt(caso[0] * caso[1] / (caso[2] / 100)))
    print(lado_terreno)
