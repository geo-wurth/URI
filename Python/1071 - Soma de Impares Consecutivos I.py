caso = [None] * 2
soma = 0
for x in range(2):
    caso[x] = input()
caso.sort()
if int(caso[0]) == int(caso[1]):
    soma = 0
else:
    for x in range(int(caso[0])+1,int(caso[1])):
        if ((x % 2) != 0):
            soma = soma + x
print(soma)
