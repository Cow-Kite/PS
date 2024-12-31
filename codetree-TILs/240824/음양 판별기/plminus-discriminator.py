n = int(input())

for _ in range(n):
    num = int(input())
    if num < 0:
        print('minus')
    elif num > 0:
        print('plus')
    else:
        print('zero')