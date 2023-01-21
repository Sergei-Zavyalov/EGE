nmin = int("10000", 9)
nmax = int("88888", 9)
k = 0
for n in range(nmin, nmax):
    n9 = ''
    while n > 0:
        n9 += str(n % 9)
        n //= 9
    n9 = n9[::-1]
    if int(n9[0]) % 2 == 0:
        if n9.count('3') <= 1:
            if n9[len(n9) - 1] != '1' and n9[len(n9) - 1] != '8':
                k += 1
print(k)
