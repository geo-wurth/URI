x = True
while True:
    casos = list(map(int, input().split()))
    casos.sort()
    resultado = []
    for i in range(casos[0],casos[1]+1):
        if i <= 0:
            x = False
            break
        resultado.append(i)
    if x == False:
        break
    print(str(' '.join(map(str, resultado))) + " Sum=" + str(sum(resultado)))
