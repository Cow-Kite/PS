from collections import deque

N, M = map(int, input().split())

miro = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    line = input()
    for j, value in enumerate(line, start=1):
        miro[i][j] = int(value)

visited = [[False] * (M+1) for _ in range(N+1)]

queue = deque([(1, 1)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    visited[x][y] = True

    if x == N and y == M:
        print(miro[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 1 or nx > N or ny < 1 or ny > M:
            continue

        if miro[nx][ny] == 0 or visited[nx][ny]:
            continue
        
        miro[nx][ny] = miro[x][y] + 1
        visited[nx][ny] = True
        queue.append((nx, ny))
