for n in range(1, 10000):
    binaryn = bin(n)[2:]
    binaryn = binaryn.replace('0', '2')
    binaryn = binaryn.replace('1', '0')
    binaryn = binaryn.replace('2', '1')
    binaryn = int(binaryn, 2)
    if n - binaryn > 37 and n % 2 == 1:
        print(n)
        break