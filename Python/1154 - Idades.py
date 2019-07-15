idade = int(input())
idades = [idade]
while idade > 0:
    idade = int(input())
    if idade < 0:
        break
    else:
        idades.append(idade)
soma = sum(idades) / len(idades)
print('{:.2f}'.format(soma))
