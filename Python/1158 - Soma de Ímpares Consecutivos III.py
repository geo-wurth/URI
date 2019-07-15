caso = int(input())
for i in range(caso):
    N = list(map(int, input().split()))
    if N[0] % 2 == 0:
        N[0] = N[0] + 1
    k = 0
    soma = 0
    for j in range(N[1]):
        soma += N[0] + k
        k += 2
    print(soma)
