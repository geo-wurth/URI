vetor = []
for i in range(10):
    vetor.append(int(input()))
    if vetor[i] <= 0:
        vetor[i] = 1
    print("X[" + str(i) + "] = " + str(vetor[i]))
