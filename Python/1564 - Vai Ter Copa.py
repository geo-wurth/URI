while True:
    try:
        caso = int(input())
        if (caso == 0):
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break
