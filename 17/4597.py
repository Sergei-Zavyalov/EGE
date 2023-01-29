k = 0
maxs = 0
mins = 100001
with open('17-4597.txt') as f:
    s = f.readlines()
    for i in range(len(s)):
        mins = min(mins, int(s[i]))
    for i in range(len(s) - 1):
        if int(s[i]) % 117 == mins or int(s[i + 1]) % 117 == mins:
            k += 1
            maxs = max(maxs, int(s[i]) + int(s[i + 1]))
print(k, maxs)