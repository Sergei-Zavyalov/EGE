n = 7 * 512**1912 + 6 * 64**1954 - 5 * 8**1991 - 4 * 8**1980 - 2022
count = 0
while n > 0:
    if n % 8 == 7:
        count += 1
    n = n // 8
print(count)
