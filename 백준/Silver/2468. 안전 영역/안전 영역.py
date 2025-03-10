from collections import deque

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, area))
max_safe_areas = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > h:
                queue.append((nx, ny))
                visited[nx][ny] = True

for h in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_area_count = 0

    for i in range(N):
        for j in range(N): 
            if not visited[i][j] and area[i][j] > h:
                bfs(i, j, h, visited)
                safe_area_count += 1

    max_safe_areas = max(max_safe_areas, safe_area_count)

print(max_safe_areas)

