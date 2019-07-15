pares = []
impares = []
for i in range(15):
    caso = int(input())
    if caso % 2 == 0:
        pares.insert(len(pares),caso)
    else:
        impares.insert(len(impares),caso)
    if len(pares) == 5:
        for j in range(5):
            print("par[" + str(j) + "] = " + str(pares[j]))
        pares = []
    if len(impares) == 5:
        for j in range(5):
            print("impar[" + str(j) + "] = " + str(impares[j]))
        impares = []
for j in range(len(impares)):
    print("impar[" + str(j) + "] = " + str(impares[j]))
for j in range(len(pares)):
    print("par[" + str(j) + "] = " + str(pares[j]))
