with open("24-4643.txt") as f:
    num = '12'
    let = 'AB'
    k = 0
    kmax = 0
    s = f.readline()
    for i in range(0, len(s), 3):
        if s[i] in num and s[i + 1] in num and s[i + 2] in let:
            k += 1
        else:
            kmax = max(kmax, k)
            k = 0
print(kmax)