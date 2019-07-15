while True:
    valores = list(map(int, input().split()))
    x = valores[0]
    y = valores[1]
    if x > y:
        print("Decrescente")
    elif x < y:
        print("Crescente")
    else:
        break
