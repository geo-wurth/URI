valores = list(map(int, input().split()))
if valores[0] > valores[1] and valores[1] <= valores[2]:
    print(":)")
elif valores[0] < valores[1] and valores[1] >= valores[2]:
    print(":(")
elif valores[0] < valores [1] and valores[1] < valores[2] and valores[1] - valores[0] > valores[2] - valores[1]:
    print(":(")
elif valores[0] < valores [1] and valores[1] < valores[2] and valores[1] - valores[0] <= valores[2] - valores[1]:
    print(":)")
elif valores[0] > valores[1] and valores[1] > valores[2] and valores[1] - valores[0] < valores[2] - valores[1]:
    print(":)")
elif valores[0] > valores[1] and valores[1] > valores[2] and valores[1] - valores[0] >= valores[2] - valores[1]:
    print(":(")
elif valores[0] == valores[1] and valores[1] < valores[2]:
    print(":)")
else:
    print(":(")
