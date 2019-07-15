vetor = []
vetor2 = []
casos = int(input())
vetor = list(map(int, input().split()))
vetor2 = vetor.copy()
vetor2.sort()
print("Menor valor: " + str(vetor2[0]))
print("Posicao: " + str(vetor.index(vetor2[0])))
