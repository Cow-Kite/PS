from collections import deque

n, m = map(int, input().split())
arts = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

count = 0
max_area = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arts[nx][ny] == 1:
                visited[nx][ny] = True
                area += 1
                queue.append((nx, ny))
    
    return area

for i in range(n):
    for j in range(m):
        if arts[i][j] == 1 and not visited[i][j]:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)