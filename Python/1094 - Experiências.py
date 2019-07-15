caso = int(input())
experimento = []
experimentos = []
ratos = []
coelhos = []
sapos = []

for i in range(caso):
    experimento = input()
    if 'C' in experimento:
        experimento = experimento.split()
        coelhos.append(int(experimento[0]))
        experimento = []
    elif 'R' in experimento:
        experimento = experimento.split()
        ratos.append(int(experimento[0]))
        experimento = []
    else:
        experimento = experimento.split()
        sapos.append(int(experimento[0]))
        experimento = []

print

experimento_ratos = sum(ratos)
experimento_coelhos = sum(coelhos)
experimento_sapos = sum(sapos)
experimento_total = experimento_coelhos + experimento_ratos + experimento_sapos
perc_ratos = (experimento_ratos / experimento_total) * 100
perc_coelhos = (experimento_coelhos / experimento_total) * 100
perc_sapos = (experimento_sapos / experimento_total) * 100

print("Total: " + str(experimento_total) + " cobaias")
print("Total de coelhos: " + str(experimento_coelhos))
print("Total de ratos: " + str(experimento_ratos))
print("Total de sapos: " + str(experimento_sapos))
print("Percentual de coelhos: {:.2f} %".format(perc_coelhos))
print("Percentual de ratos: {:.2f} %".format(perc_ratos))
print("Percentual de sapos: {:.2f} %".format(perc_sapos))
