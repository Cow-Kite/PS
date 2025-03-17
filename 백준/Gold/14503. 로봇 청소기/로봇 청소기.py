n, m = map(int, input().split())  # 방 크기 입력
x, y, d = map(int, input().split())  # 로봇 청소기 시작 위치와 방향
area = [list(map(int, input().split())) for _ in range(n)]  # 방 상태 입력

# 방향 설정 (북, 동, 남, 서)
fx = [-1, 0, 1, 0]
fy = [0, 1, 0, -1]

# 후진 방향 (현재 방향과 반대)
bx = [1, 0, -1, 0]
by = [0, -1, 0, 1]

count = 0  # 청소한 칸 개수

while True:
    # 현재 칸이 청소되지 않았다면 청소
    if area[x][y] == 0:
        count += 1
        area[x][y] = 2  # 청소된 칸을 2로 표시 (1: 벽, 0: 미청소, 2: 청소됨)

    # 주변 4칸 중 청소되지 않은 칸이 있는지 확인
    cleanable = False
    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향 회전
        nx, ny = x + fx[d], y + fy[d]

        if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
            x, y = nx, ny
            cleanable = True
            break  # 청소 가능한 곳 찾으면 이동 후 종료

    # 청소할 곳이 없다면 후진 시도
    if not cleanable:
        sx, sy = x + bx[d], y + by[d]
        if 0 <= sx < n and 0 <= sy < m and area[sx][sy] != 1:  # 벽이 아니면 후진
            x, y = sx, sy
        else:
            break  # 후진도 못 하면 종료

# 결과 출력
print(count)
