from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

virus_positions = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]

def bfs(spread_lab):
    queue = deque(virus_positions) # virus start
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and spread_lab[nx][ny] == 0:
                spread_lab[nx][ny] = 2
                queue.append((nx, ny))
    
    return sum(row.count(0) for row in spread_lab)

max_safe_zone = 0

for walls in combinations(empty_spaces, 3):
    temp_lab = copy.deepcopy(lab)

    for x, y in walls:
        temp_lab[x][y] = 1

    safe_zone = bfs(temp_lab)

    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)