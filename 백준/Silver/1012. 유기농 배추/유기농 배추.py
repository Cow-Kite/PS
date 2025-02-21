from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# Test case 
for _ in range(T):
    M, N, K = map(int, input().split())
    
    bat = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    worm = 0
    queue = deque()

    # 배추 위치
    for _ in range(K):
        x, y = map(int, input().split())
        bat[y][x] = 1

    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    a, b = queue.popleft()
                    for h in range(4):
                        nx = a + dx[h]
                        ny = b + dy[h]

                        if 0 <= nx < N and 0 <= ny < M and bat[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True

                worm += 1

    print(worm)
    