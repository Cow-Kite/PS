from collections import deque

C = int(input())
N = int(input())

graph = [[0] * (C + 1) for _ in range(C + 1)]

for _ in range(N):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

queue = deque([1])
count = 0
visited = [False] * (C + 1)

while queue:
    visited[1] = True
    v = queue.popleft()

    for i in range(1, C+1):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
            count += 1

print(count)

