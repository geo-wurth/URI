S = 0
j = 1
k = 1
for i in range(1,19):
    S += (j / k)
    j = j + 2
    k = k * 2
print('{:.2f}'.format(S))
