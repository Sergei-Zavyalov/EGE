for n in range(2000):
    k1 = 0
    k0 = 0
    binstr = str(bin(n))[2:]
    for i in range(len(binstr)):
        if i % 2 == 0 and binstr[i] == '0':
            k0 += 1
        else:
            if i % 2 == 1 and binstr[i] == '1':
                k1 += 1
    if abs(k1 - k0) == 5:
        print(n)
        break