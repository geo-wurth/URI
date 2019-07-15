valores = list(map(int, input().split()))
A = valores[0]
B = valores[1]
for R in range(abs(B)):
    Q = int((A - R) / B)
    resultado = valores[1] * Q + R
    if valores[0] == resultado:
        print(Q, R)
        break
