def f(n, goal):
    if n > goal:
        return 0
    if n == goal:
        return 1
    else:
        return f(n + 3, goal) + f(n * 2, goal)

print(f(3, 27) * f(27, 63))