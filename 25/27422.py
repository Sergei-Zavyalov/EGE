for i in range(174457, 174505):
    k = []
    count = 0
    for j in range(2, i//2+1):
        if i % j == 0:
            count += 1
    if count == 2:
        for j in range(2, i//2+1):
            if i % j == 0:
                k.append(j)
        print(k)
