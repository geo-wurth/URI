lados = list(map(int, input().split()))

if ((lados[0] < (lados[2] + lados[3])) and (lados[2] < (lados[0] + lados[3])) and (lados[3] < (lados[0] + lados[2]))):
    print("S")
elif ((lados[0] < (lados[1] + lados[3])) and (lados[1] < (lados[0] + lados[3])) and (lados[3] < (lados[0] + lados[1]))):
    print("S")
elif((lados[0] < (lados[1] + lados[2])) and (lados[1] < (lados[0] + lados[2])) and (lados[2] < (lados[0] + lados[1]))):
    print("S")
elif ((lados[1] < (lados[3] + lados[2])) and (lados[3] < (lados[1] + lados[2])) and (lados[2] < (lados[3] + lados[1]))):
     print("S")
else:
    print("N")
