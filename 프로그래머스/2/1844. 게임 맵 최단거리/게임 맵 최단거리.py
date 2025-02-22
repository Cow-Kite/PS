from collections import deque

def solution(maps):
    N, M = len(maps), len(maps[0])
    visited = [[False] * M for _ in range(N)]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
        
    if not visited[N-1][M-1]:
            return -1
    
    return maps[N-1][M-1]