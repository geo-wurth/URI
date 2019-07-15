while True:
    caso = int(input())
    if caso == 0:
        break
    resultado = []
    for i in range(1,caso+1,+1):
        resultado.append(i)
    print(str(' '.join(map(str, resultado))))
