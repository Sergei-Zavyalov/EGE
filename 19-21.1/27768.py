def game(heap, heap2, moves, toWin):
    if heap + heap2 >= 84:
        return moves % 2 == toWin % 2
    if moves == toWin:
        return 0
    h = [game(heap + 1, heap2, moves + 1, toWin),
         game(heap, heap2 + 1, moves + 1, toWin),
         game(heap * 2, heap2, moves + 1, toWin),
         game(heap, heap2 * 3, moves + 1, toWin)]

    return any(h)


def game2(heap, heap2, moves, toWin):
    if heap + heap2 >= 84:
        return moves % 2 == toWin % 2
    if moves == toWin:
        return 0
    h = [game2(heap + 1, heap2, moves + 1, toWin),
         game2(heap, heap2 + 1, moves + 1, toWin),
         game2(heap * 2, heap2, moves + 1, toWin),
         game2(heap, heap2 * 3, moves + 1, toWin)]

    return any(h) if (moves + 1) % 2 == toWin % 2 else all(h)


print('19: ', min(s for s in range(1, 68) if not game(16, s, 0, 1) and game(16, s, 0, 2)))
print('20: ', [s for s in range(1, 68) if not game2(16, s, 0, 1) and game2(16, s, 0, 3)])
print('21: ', [s for s in range(1, 68) if not game2(16, s, 0, 2) and game2(16, s, 0, 4)])

