for x in range(80, 0, -1):
    sum = (3 * 80 ** 3 + x * 80 ** 2 + 7 * 80 + 5) + (1 * 80 ** 3 + 4 * 80 ** 2 + x * 80)
    if sum % 17 == 0:
        print(sum // 17)
        break