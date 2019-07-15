matriz = [[0 for x in range(12)] for y in range(12)] 
calculo = str(input())
soma = 0
contador = 0
contador2 = 11
for linha in range(12):
    for coluna in range(12):
        valor = float(input())
        if coluna > contador2:
            contador = contador + 1
            soma = soma + valor
        matriz[linha][coluna] = valor
    contador2 = contador2 - 1
if calculo == "S":    
    print("{:.1f}".format(soma))
else:
    media = soma / contador
    print("{:.1f}".format(media))
