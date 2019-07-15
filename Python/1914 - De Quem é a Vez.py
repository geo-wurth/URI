casos = int(input())
for i in range(casos):
    Nomes = list(map(str, input().split()))
    Valores = list(map(int, input().split()))
    Valor = (Valores[0] + Valores[1]) % 2
    if Valor == 0:
        i = (Nomes.index("PAR")) - 1
        Ganhador = Nomes[i]
    else:
        i = (Nomes.index("IMPAR")) - 1
        Ganhador = Nomes[i]
    print(Ganhador)
