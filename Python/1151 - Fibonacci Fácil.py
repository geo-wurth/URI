N = int(input())
fibonacci = [0, 1, 1]
if (N == 0):
    print("0")
elif (N == 1):
    print("0 1")
elif (N == 2):
    print("0 1 1")
else:
    for i in range(3,N):
        proximo_fibonacci = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo_fibonacci)
    j = 0
    for i in fibonacci:
        if (j == (N-1)):
            print(i, end="\n")
        else:
            print(i, end=" ")
        j += 1
