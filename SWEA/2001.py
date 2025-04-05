T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(N)]

    def fly(x, y):
        dead_fly = 0
        for i in range(x, x+M): # 3, 4
            for j in range(y, y+M): # 3, 4
                dead_fly += area[i][j]

        return dead_fly

    max_fly = 0

    for x in range(0, N-M+1): # 0, 1, 2, 3
        for y in range(0, N-M+1): # 0, 1, 2, 3
            max_fly = max(max_fly, fly(x, y))

    print(f'#{t} {max_fly}')
