matriz = [[0 for x in range(12)] for y in range(12)] 
calculo = str(input())
soma = 0
contador = 0
exclusivo_maior = 11
exclusivo_menor = 0
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if (coluna < exclusivo_maior) and (coluna > exclusivo_menor):
            contador = contador + 1
            soma = soma + valor
        matriz[linha][coluna] = valor
    exclusivo_maior = exclusivo_maior - 1
    exclusivo_menor = exclusivo_menor + 1
if calculo == "S":    
    print("{:.1f}".format(soma))
else:
    media = soma / contador
    print("{:.1f}".format(media))
