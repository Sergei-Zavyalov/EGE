import sys


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1) - 1


sys.setrecursionlimit(100000)
print(f(1000) // f(997))