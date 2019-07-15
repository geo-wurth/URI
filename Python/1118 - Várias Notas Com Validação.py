loop = 1
while loop == 1:
    while True:
        x = float(input())
        if 0 > x  or x > 10:
            print("nota invalida")
        else:
            break
    while True:
        y = float(input())
        if 0 > y or y > 10:
            print("nota invalida")
        else:
            break
    print("media = {:.2f}".format(((x + y) / 2)))
    k = 0
    while k != 2 and k != 1:
        print("novo calculo (1-sim 2-nao)")
        k = int(input())
    if k == 2:
        break
