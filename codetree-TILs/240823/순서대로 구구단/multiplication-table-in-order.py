a, b = map(int, input().split())
if a <= b:
    for i in range(1, 10):
        for j in range(a, b+1):
            print(f'{j} * {i} = {i * j}', end = "  ")
        print()
else:
    for i in range(1, 10):
        for j in range(a, b-1, -1):
            print(f'{j} * {i} = {i * j}', end = "  ")
        print()