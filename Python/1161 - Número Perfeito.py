caso = int(input())
for i in range(caso):
    N = list(map(float, input().split()))
    tempo = 0
    while N[0] <= N[1]:
        N[0] = int(N[0] + (N[0]*N[2]/100))
        N[1] = int(N[1] + (N[1]*N[3]/100))
        tempo += 1
        if tempo > 100:
            break
    if tempo > 100:
        print("Mais de 1 seculo.")
    else:
        print(str(tempo) + " anos.")
