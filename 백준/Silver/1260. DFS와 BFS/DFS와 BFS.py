from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def BFS(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(1, N+1):
            if graph[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

def DFS(start):
    stack = [start]
    visited = [False] * (N + 1)
    result = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            result.append(v) 

            for i in range(N, 0, -1):
                if graph[v][i] == 1 and not visited[i]:
                    stack.append(i) 

    print(" ".join(map(str, result)))

DFS(V)
BFS(V)  