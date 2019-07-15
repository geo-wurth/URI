while True:
    try:
        caso = int(input())
        matriz = [[3 for x in range(caso)] for y in range(caso)]
        i = caso -1
        for linha in range(caso):
            for coluna in range(caso):
                if coluna == i:
                    matriz[linha][coluna] = 2
                elif linha == coluna:
                    matriz[linha][coluna] = 1
            i -= 1
        for i in range(caso):
            texto = ''
            for j in range(caso):
                texto += "%1g" %matriz[i][j]
            print(texto)
    except EOFError:
        break
