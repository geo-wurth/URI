casos = int(input())
for i in range(casos):
    caso = list(map(int, input().split()))
    conduite = caso[0] + caso[1]
    print(conduite)
