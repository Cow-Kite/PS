def dfs(c):
    ans_dfs.append(c)
    v[c] = 1

    for n in adj[c]:
        if v[n]==0:
            dfs(n)

def bfs(s):
    q = []
    q.append(s)
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]:
                v[n] = 1
                q.append(n)
                ans_bfs.append(n)
                
N, M, V = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

# 오름차순 정렬
for i in range(1, N+1):
    adj[i].sort()

# 방문 체크 배열
v = [0] * (N+1)
ans_dfs = []
dfs(V)

v = [0] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)