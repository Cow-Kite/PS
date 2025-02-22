from collections import deque

M, N = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))


days = -1
while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = 1
                queue.append((nx, ny))

    days += 1

for row in tomato:
    if 0 in row:
        print(-1)
        exit()

print(days)
