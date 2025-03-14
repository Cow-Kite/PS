INF = float('inf') # 갈 수 없는 경우는 무한대 값으로 채우기

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수


graph = [[INF]*n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start-1][end-1] = min(graph[start-1][end-1], cost)

# 플로이드-워셜 알고리즘

for k in range(n): # 경유지
    for i in range(n): # 출발지
        for j in range(n): # 도착지
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()