N = list(map(int, input().split()))
A = N[0]
N = N[len(N)-1]
soma = 0

for i in range(N):
    soma += A
    A += 1
print(soma)
