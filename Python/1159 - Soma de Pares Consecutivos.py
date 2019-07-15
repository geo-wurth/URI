teste = False
while teste is False:
    X = int(input())
    if X == 0:
        break
    elif X % 2 != 0:
        X += 1
    soma = 0
    k = 0
    for i in range(5):
        soma += X + k
        k += 2
    print(soma)
