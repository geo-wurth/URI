while True:
    try:
        caso = int(input())
        matriz = [[0 for x in range(caso)] for y in range(caso)]
        meio = int(caso / 2)
        comeca = int(caso / 3)
        i = caso -1
        for linha in range(caso):
            for coluna in range(caso):
                if linha == meio and coluna == meio:
                    matriz[linha][coluna] = 4
                elif linha >= comeca and linha < caso - comeca and coluna >= comeca and coluna < caso - comeca:
                    matriz[linha][coluna] = 1

                elif coluna == i:
                    matriz[linha][coluna] = 3
                elif linha == coluna:
                    matriz[linha][coluna] = 2
            i -= 1
        for i in range(caso):
            texto = ''
            for j in range(caso):
                texto += "%1g" %matriz[i][j]
            print(texto)
        print()
    except EOFError:
        break
