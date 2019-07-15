vetor = []
for i in range(0,100):
    vetor.append(float(input()))
    if vetor[i] <= 10:
        print("A[" + str(i) + "] = {:.1f}".format(vetor[i]))    
