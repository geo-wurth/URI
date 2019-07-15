while True:
    caso = int(input())
    if (caso == 0):
        break
    matriz = [[0 for x in range(caso)] for y in range(caso)]
    for linha in range(caso):
        for coluna in range(caso):
            if linha == 0 and coluna == 0:
                matriz[linha][coluna] = 1
            elif coluna > linha:
                matriz[linha][coluna] = matriz[linha][coluna-1] * 2
            else:
                matriz[linha][coluna] = matriz[linha-1][coluna] * 2
    largura = len(str(matriz[caso-1][caso-1]))

    for i in range(caso):
        texto = ''
        for j in range(caso):
            texto += " {:{}n}".format(matriz[i][j], largura)
        print(texto[1:])
    print("")
