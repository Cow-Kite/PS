from collections import deque
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1

queue = deque()

count = 0

for i in range(1, N+1):
    if not visited[i]:
        queue.append(i)

        while queue:
            num = queue.popleft()

            for j in range(1, N+1):
                if not visited[j] and graph[num][j] == 1:
                    visited[j] = True
                    queue.append(j)
                    

        count += 1

print(count)


