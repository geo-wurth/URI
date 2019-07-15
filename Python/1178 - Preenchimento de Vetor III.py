casos = []
caso = float(input())
casos.append(caso)
print("N[0] = {:.4f}".format(casos[0]))
for i in range(1,100):
    casos.append(casos[i-1] / 2)
    print("N[" + str(i) + "] = {:.4f}".format(casos[i]))
