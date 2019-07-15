mao = list(map(int, input().split()))
if mao[0] == mao[1]:
    print(mao[1])
elif mao[0] > mao[1]:
    print(mao[0])
else:
    print(mao[1])
