X = int(input())
Z = X - 1
while Z <= X:
    Z = int(input())
contador = 1
soma = X
i = 1
while soma < Z:
    soma += X + i
    i += 1
    contador += 1
print(contador)
