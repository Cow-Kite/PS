T = int(input())

for num in range(1, T+1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]
    center = N//2
    total = 0

    for i in range(N):
        if i <= center:
            total += sum(farm[i][center - i: center + i + 1])
        else:
            offset = N - 1 - i
            total += sum(farm[i][center - offset: center + offset + 1])

    print(f'#%d %d' % (num, total))
