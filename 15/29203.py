for a in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if not((3*x + 7*y < a) or (x >= y) or (y > 6)):
                flag = False
    if flag:
        print(a)
        break
