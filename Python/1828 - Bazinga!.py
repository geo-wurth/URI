casos = int(input())
for i in range(1, casos+1):
    jogo = list(map(str, input().split()))
    if jogo[0] == "pedra":
        if jogo[1] == "pedra":
            print("Caso #%d: De novo!" %i)
        elif jogo[1] == "papel":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "tesoura":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "lagarto":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "Spock":
            print("Caso #%d: Raj trapaceou!" %i)
            
    elif jogo[0] == "papel":
        if jogo[1] == "pedra":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "papel":
            print("Caso #%d: De novo!" %i)
        elif jogo[1] == "tesoura":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "lagarto":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "Spock":
            print("Caso #%d: Bazinga!" %i)

    elif jogo[0] == "tesoura":
        if jogo[1] == "pedra":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "papel":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "tesoura":
            print("Caso #%d: De novo!" %i)
        elif jogo[1] == "lagarto":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "Spock":
            print("Caso #%d: Raj trapaceou!" %i)

    elif jogo[0] == "lagarto":
        if jogo[1] == "pedra":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "papel":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "tesoura":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "lagarto":
            print("Caso #%d: De novo!" %i)
        elif jogo[1] == "Spock":
            print("Caso #%d: Bazinga!" %i)
            
    elif jogo[0] == "Spock":
        if jogo[1] == "pedra":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "papel":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "tesoura":
            print("Caso #%d: Bazinga!" %i)
        elif jogo[1] == "lagarto":
            print("Caso #%d: Raj trapaceou!" %i)
        elif jogo[1] == "Spock":
            print("Caso #%d: De novo!" %i)
