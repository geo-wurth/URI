while True:
    caso = int(input())
    if (caso == 0):
        break
    matriz = [[0 for x in range(caso)] for y in range(caso)]
    if (caso % 2 == 0):
        meio = caso / 2
    else:
        meio = (caso + 1) / 2
    valor = 1
    acima = 0
    esquerda = 0
    abaixo = caso - 1
    direita = caso - 1
    while (valor <= meio):
        i = esquerda
        while (i <= direita):
            matriz[acima][i] = valor
            matriz[abaixo][i] = valor
            i+=1
        i = (acima + 1)
        while (i < abaixo):
            matriz[i][esquerda] = valor
            matriz[i][direita] = valor
            i+=1
        valor+=1
        acima+=1
        abaixo-=1
        esquerda+=1
        direita-=1    
    for i in range(caso):
        texto = ''
        for j in range(caso):
            texto += " %3g" %matriz[i][j]
        print(texto[1:])
    print("")
