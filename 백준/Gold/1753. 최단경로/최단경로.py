import heapq

INF = float('inf')
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def di(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        distance, now = heapq.heappop(q)
        if dist[now]<distance:
            continue
        for neighbor, weight in graph[now]:
            cost = distance+weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))

di(K)

for i in range(1, V + 1):
    print(dist[i] if dist[i] != INF else "INF")