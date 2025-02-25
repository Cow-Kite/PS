from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

color_blind = []
for row in grid:
    new_row = []
    for c in row:
        if c == 'G':
            new_row.append('R')
        else:
            new_row.append(c)
    color_blind.append(new_row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(grid):
    count = 0
    visited = [[False] * (N) for _ in range(N)]
    queue = deque()

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))

                count += 1
    return count

print(bfs(grid))
print(bfs(color_blind))

