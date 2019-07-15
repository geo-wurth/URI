while True:
    try:
        grupo = int(input())
        velocidades = list(map(int, input().split()))
        velocidades.sort(reverse=True)
        if velocidades[0] < 10:
            print(1)
        elif velocidades[0] >= 10 and velocidades[0] < 20:
            print(2)
        else:
            print(3)
    except EOFError:
        break
