for a in range(1000):
    state = True
    for x in range(1, 1000):
        if not(((x % 2 == 0) <= (not(x % 3 == 0))) or (x + a >= 100)):
            state = False
    if state:
        print(a)
        break
