T = int(input())

for num in range(1, T+1):
    D, H, M = map(int, input().split())

    target = (11 - 11) * 1440 + (11 - 0) * 60 + (11 - 0)
    time = (D - 11) * 1440 + H * 60 + M

    if time < target:
        print(f'#{num} -1')
    else:
        print(f'#{num} {time - target}')