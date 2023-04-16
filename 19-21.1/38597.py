def game(heap, moves, toWin):
    if heap >= 29:
        return moves % 2 == toWin % 2
    if moves == toWin:
        return 0
    h = [game(heap + 1, moves + 1, toWin),
         game(heap * 2, moves + 1, toWin)]

    return any(h) if (moves + 1) % 2 == toWin % 2 else all(h)


print('19: ', min(s for s in range(1, 28) if not game(s, 0, 1) and game(s, 0, 2)))
print('20: ', [s for s in range(1, 28) if not game(s, 0, 1) and game(s, 0, 3)])
print('21: ', [s for s in range(1, 28) if not game(s, 0, 2) and game(s, 0, 4)])
