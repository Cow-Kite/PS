from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dest = [[-1] * m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j))
            dest[i][j] = 0
        if arr[i][j] == 0:
            dest[i][j] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1 and dest[nx][ny]==-1:
                dest[nx][ny] = dest[x][y]+1
                q.append((nx, ny))

for i in range(n):
    for j in range(m):
        print(dest[i][j], end=' ')
    print()