def f(n, mult, goal):
    if n > goal or mult > 1:
        return 0
    if n == goal and mult == 1:
        return 1
    else:
        return f(n + 1, mult, goal) + f(n + 2, mult, goal) + f(n * 2, mult + 1, goal) + f(n * 3, mult + 1, goal)


print(f(1, 0, 10))