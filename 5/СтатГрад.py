array = []
for n in range(15432098, 248456790):
    binaryn = bin(n)[2:]
    k = n
    for i in range(3):
        sumn = 0
        for j in range(len(str(k))):
            sumn += int(str(k)[j])
        if sumn % 2 == 1:
            binaryn += '1'
        else:
            binaryn += '0'
        k = int(binaryn, 2)
    R = int(binaryn, 2)
    if 123456789 < R < 1987654321:
        array.append(R)
print(len(set(array)))
