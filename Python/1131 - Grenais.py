gremio = 0
inter = 0
grenais = 0
empate = 0
while True:
    gols = list(map(int, input().split()))
    if gols[0] > gols[1]:
        inter = inter + 1
    elif gols[0] < gols[1]:
        gremio = gremio + 1
    else:
        empate = empate + 1
    grenais = grenais + 1
    k = 0
    while k != 2 and k != 1:
        print("Novo grenal (1-sim 2-nao)")
        k = int(input())
    if k == 2:
        break
if inter > gremio:
    vencedor = "Inter"
elif inter < gremio:
    vencedor = "Gremio"
else:
    vencedor = "Nao houve vencedor"
print("{:1n} grenais".format(grenais))
print("Inter:{:1n}".format(inter))
print("Gremio:{:1n}".format(gremio))
print("Empates:{:1n}".format(empate))
print("{:1s} venceu mais".format(vencedor))
