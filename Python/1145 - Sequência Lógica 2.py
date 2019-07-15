casos = list(map(int, input().split()))
for i in range(1,casos[1]+1,casos[0]):
    resultado = []
    if (i+1 == (casos[1])) and (i < (casos[1]+2)):
        for j in range(i,i+casos[0]-1):
            resultado.append(j)
    elif (i  == (casos[1])) and (i < (casos[1]+2)):
        for j in range(i,i+casos[0]-2):
            resultado.append(j)
    else:
        for j in range(i,i+casos[0]):
            resultado.append(j)
    print(str(' '.join(map(str, resultado))))
