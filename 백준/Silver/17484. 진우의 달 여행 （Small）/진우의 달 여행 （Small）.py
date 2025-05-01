from collections import deque

dirs = [(1, -1), (1, 0), (1, 1)]

def bfs(x, y):
    q = deque()
    INF = float('inf')
    cost = [[[INF]*3 for _ in range(M)] for _ in range(N)]
    min_cost = INF

    for d in range(3):
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            cost[nx][ny][d] = arr[x][y] + arr[nx][ny]
            q.append((nx, ny, cost[nx][ny][d], d))

    while q:
        x, y, cur_cost, prev_dir = q.popleft()
        if x == N - 1:
            min_cost = min(min_cost, cur_cost)
            continue

        for d in range(3):
            if d == prev_dir:
                continue

            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                new_cost = cur_cost + arr[nx][ny]
                if cost[nx][ny][d] > new_cost:
                    cost[nx][ny][d] = new_cost
                    q.append((nx, ny, new_cost, d))

    return min_cost
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

for j in range(M):
    temp = bfs(0, j)
    ans = min(ans, temp)

print(ans)