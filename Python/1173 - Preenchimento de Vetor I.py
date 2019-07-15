vetor = []
vetor.append(int(input()))
for i in range(10):
    vetor.append(vetor[i]*2)
    print("N[" + str(i) + "] = " + str(vetor[i]))    
