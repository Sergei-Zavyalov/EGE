for x in range(14):
    if (int(f'123{x}5', 15) + int(f'1{x}233', 15)) % 14 == 0:
        print((int(f'123{x}5', 15) + int(f'1{x}233', 15)) // 14)
        break
