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
