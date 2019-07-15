def ordenarX(elem):
    return elem[0], elem[1]
def ordenarY(elem):
    return elem[1], elem[0]
while True:
    vetor = []
    vetor_y_exc = []
    vetor_x_exc = []
    try:
        casos = int(input())
    except ValueError or EOFError:
        break
    for i in range(casos):
        coordenadas = list(map(int, input().split()))
        vetor.append(coordenadas)
    vetor_y = sorted(vetor, key=ordenarY)
    vetor_x = sorted(vetor, key=ordenarX)
    '''for i in range(casos):
        vetor_y_exc.append(vetor_y[i][1])
        vetor_x_exc.append(vetor_x[i][0])'''
    contp2 = 0
    '''for i in range(vetor_y_exc[0]+1, vetor_y_exc[len(vetor_y_exc)-1]):'''
    for i in range(-200, 200):
        contp = 0
        '''x = vetor_x_exc[0]'''
        x = -1000
        y = None
        for j in vetor_x:
            if (j[1] == i - 1 or j[1] == i + 1) and j[0] >= x and contp == 0:
                y = j[1]
                x = j[0]
                contp += 1
            elif (j[1] == i - 1 or j[1] == i + 1) and j[1] != y and j[0] > x:
                y = j[1]
                x = j[0]
                contp += 1
        if contp > contp2:
            contp2 = contp
    print(contp2)
