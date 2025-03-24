from collections import deque

n, m = map(int, input().split())

maps = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

# 보물 위치 찾는 함수
def find(i, j):
    visited = [[-1] * m for _ in range(n)]
    visited[i][j] = 0
    
    queue = deque([(i, j)])
    max_dist = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and maps[nx][ny] == 'L':
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                max_dist = max(max_dist, visited[nx][ny]) # visited 배열 업데이트 하면서, max 거리 업데이트

    return max_dist

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'L':
            count = max(count, find(i, j))

print(count)