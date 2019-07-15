for i in range(0,3,+1):
    for j in range(1+i,4+i,+1):
        print("I=" + str(i) + " J=" + str(j))
    if i < 2:
        for k in range(2,10,+2):
            for j in range(1+i,4+i,+1):
                print("I=" + str(i) + "." + str(k) + " J=" + str(j) + "." + str(k))
