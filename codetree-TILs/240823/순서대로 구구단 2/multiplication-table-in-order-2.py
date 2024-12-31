a, b = map(int, input().split())

if a >= b:
    for i in range(a, b-1, -1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}', end="  ")
            if j % 3 == 0:
                print()
        print()

else:
    for i in range(a, b+1):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}', end="  ")
            if j % 3 == 0:
                print()
        print()