valor = [None] * 5
cont_par = 0
cont_impar = 0
cont_pos = 0
cont_neg = 0
for x in range(5):
    valor[x] = float(input())
for y in valor:
    if ((y % 2) == 0):
        cont_par = cont_par + 1
    else:
        cont_impar = cont_impar + 1
    if y > 0:
        cont_pos = cont_pos + 1
    elif y < 0:
        cont_neg = cont_neg + 1
print(str(cont_par) + " valor(es) par(es)")
print(str(cont_impar) + " valor(es) impar(es)")
print(str(cont_pos) + " valor(es) positivo(s)")
print(str(cont_neg) + " valor(es) negativo(s)")
