while True:
    valores = list(map(int, input().split()))
    x = valores[0]
    y = valores[1]
    if x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    elif x > 0 and y < 0:
        print("quarto")
    else:
        break
