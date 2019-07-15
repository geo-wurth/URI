caso = int(input())
casos = []

for x in range(1,caso+1):
    casos.append(int(input()))

for x in casos:
    if (x == 0):
        print("NULL")
    if (x % 2 == 0) and (x > 0):
        print("EVEN POSITIVE")
    if (x % 2 == 0) and (x < 0):
        print("EVEN NEGATIVE")
    if (x % 2 != 0) and (x > 0):
        print("ODD POSITIVE")
    if (x % 2 != 0) and (x < 0):
        print("ODD NEGATIVE")
