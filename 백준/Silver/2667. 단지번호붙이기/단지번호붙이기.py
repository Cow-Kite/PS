from collections import deque

N = int(input())

house = [[0] * (N) for _ in range(N)]

for i in range(N):
    line = input()
    for j in range(N):
        house[i][j] = int(line[j])

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * (N) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if house[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            count = 1

            while queue:
                x, y = queue.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < N and 0 <= ny < N:
                        if house[nx][ny] == 1 and not visited[nx][ny]:
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            count += 1
            
            result.append(count)


result.sort()
print(len(result))
print("\n".join(map(str, result)))