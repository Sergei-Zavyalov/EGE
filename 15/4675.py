for a in range(1, 100000):
    flag = True
    for x in range(1, 1000):
        if not(((x % 6 == 0) <= (not (x % 10 == 0))) or (x + a > 121)):
            flag = False
    if flag:
        print(a)
        break