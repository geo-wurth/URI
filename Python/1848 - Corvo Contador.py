for i in range(3):
    valor = 0
    while True:
        corvo = list(map(str, input().split()))
        if corvo[0] == "caw":
            print(valor)
            break
        else:
            if corvo[0] == "--*":
                valor += 1
            elif corvo[0] == "-*-":
                valor += 2
            elif corvo[0] == "-**":
                valor += 3
            elif corvo[0] == "*--":
                valor += 4
            elif corvo[0] == "*-*":
                valor += 5
            elif corvo[0] == "**-":
                valor += 6
            elif corvo[0] == "***":
                valor += 7
            
