matriz = [[0 for x in range(12)] for y in range(12)] 
linha = int(input())
calculo = str(input())
for i in range(12):
    for j in range(12):
        valor = float(input())
        matriz[i][j] = valor
soma = 0
for i in range(12):
    soma = soma + matriz[linha][i]
if calculo == "S":    
    print("{:.1f}".format(soma))
else:
    media = soma / 12
    print("{:.1f}".format(media))
