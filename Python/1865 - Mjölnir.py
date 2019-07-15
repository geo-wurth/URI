casos = int(input())
for i in range(casos):
    teste = list(map(str, input().split()))
    if teste[0] == "Thor":
        print("Y")
    else:
        print("N")
