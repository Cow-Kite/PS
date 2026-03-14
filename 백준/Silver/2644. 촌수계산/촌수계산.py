def bfs(si, ei):
    q = []
    q.append((si, 0))
    v[si] = 1

    while q:
        ci, dist = q.pop(0)
        if ci==ei:
            return dist
        for ni in adj[ci]:
            if not v[ni]:
                q.append((ni, dist+1))
                v[ni]=1
    return -1

N = int(input())
SH, EH = map(int, input().split())
E = int(input())

adj = [[] for _ in range(N+1)]
v = [0] * (N+1)
for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

ans = bfs(SH, EH)
print(ans)