for x in range(9):
    for y in range(9):
        if (int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)) % 61 == 0:
            print((int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)) // 61)