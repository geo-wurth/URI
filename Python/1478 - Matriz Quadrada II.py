while True:
    caso = int(input())
    if (caso == 0):
        break
    matriz = [[0 for x in range(caso)] for y in range(caso)]
    for linha in range(caso):
        for coluna in range(caso):
            if linha == 0:
                matriz[linha][coluna] = coluna + 1
            elif coluna == 0:
                matriz[linha][coluna] = linha + 1
            elif matriz[linha-1][coluna-1] == 1:
                matriz[linha][coluna] = 1
            elif coluna > linha:
                matriz[linha][coluna] = matriz[linha][coluna-1] + 1
            else:
                matriz[linha][coluna] = matriz[linha-1][coluna] + 1
    for i in range(caso):
        texto = ''
        for j in range(caso):
            texto += " %3g" %matriz[i][j]
        print(texto[1:])
    print("")
