maxr = 0
for n in range(4,29):
    binary = bin(n)[2:]
    if binary.count('1') % 2 == 0:
        binary = "10" + binary[:-2] + "00"
    else:
        binary = "11" + binary[:-2] + "11"
    R = int(binary, 2)
    maxr = max(maxr, R)
print(maxr)