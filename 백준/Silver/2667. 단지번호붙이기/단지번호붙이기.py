def bfs(si, sj):
    q = []
    v[si][sj] = 1
    q.append((si, sj))
    cnt=1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]==1 and v[ni][nj]==0:
                q.append((ni, nj))
                cnt += 1
                v[ni][nj]=1
    
    return cnt



N = int(input())
arr = [list(map(int, input())) for _ in range (N)]
v = [[0]*N for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if arr[i][j]==1 and v[i][j]==0:
            ans.append(bfs(i, j))

ans.sort()
print(len(ans), *ans, sep='\n')

