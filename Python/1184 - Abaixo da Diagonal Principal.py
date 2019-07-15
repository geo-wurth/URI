matriz = [[0 for x in range(12)] for y in range(12)] 
calculo = str(input())
soma = 0
contador = 0
for i in range(12):
    for j in range(12):
        valor = float(input())
        if j < i:
            contador = contador + 1
            soma = soma + valor
        matriz[i][j] = valor
if calculo == "S":    
    print("{:.1f}".format(soma))
else:
    media = soma / contador
    print("{:.1f}".format(media))
