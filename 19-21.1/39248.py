def game19(heap, step):
    # 3 - шаг, на котором известен результат Вани (Не 2, а 3)
    if step == 3 and heap >= 64:
        return 1
    elif step == 3 and heap < 64:
        return 0
    elif heap >= 64 and step < 3:
        return 0
    else:
        # Чётный ход - ход Вани
        if step % 2 == 0:
            return game19(heap + 1, step + 1) or game19(heap * 3, step + 1)
        else:
            return game19(heap + 1, step + 1) and game19(heap * 3, step + 1)


def game20(heap, step):
    if step == 4 and heap >= 64:
        return 1
    elif step == 4 and heap < 64:
        return 0
    elif heap >= 64 and step < 4:
        return 0
    else:
        if step % 2 == 0:
            return game20(heap + 1, step + 1) and game20(heap * 3, step + 1)
        else:
            return game20(heap + 1, step + 1) or game20(heap * 3, step + 1)


def game21(heap, step):
    if (step == 3 or step == 5) and heap >= 64:
        return 1
    elif step == 5 and heap < 64:
        return 0
    elif heap >= 64 and step < 5:
        return 0
    else:
        if step % 2 == 0:
            return game21(heap + 1, step + 1) or game21(heap * 3, step + 1)
        else:
            return game21(heap + 1, step + 1) and game21(heap * 3, step + 1)


print(f'19: {[i for i in range(1, 64) if game19(i, 1)]}')
print(f'20: {[i for i in range(1, 64) if game20(i, 1)]}')
print(f'21: {[i for i in range(1, 64) if game21(i, 1)]}')


# --- II варинат решения ---

def game2(heap, moves, toWin):
    if heap >= 64:
        return moves % 2 == toWin % 2
    if moves == toWin:
        return 0
    h = [game2(heap + 1, moves + 1, toWin),
         game2(heap * 3, moves + 1, toWin)]
    return any(h) if (moves + 1) % 2 == toWin % 2 else all(h)


print('21: ', [s for s in range(1, 64) if not game2(s, 0, 2) and game2(s, 0, 4)])
