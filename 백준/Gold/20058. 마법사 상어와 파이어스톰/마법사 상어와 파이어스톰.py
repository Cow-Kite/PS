N, Q = map(int, input().split())
N = 2**N
arr = [[0]*(N+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+2)]
lst = list(map(int, input().split()))
for L in lst:
    L = 2**L

    new = [[0]*(N+2) for _ in range(N+2)]
    for si in range(1, N+1, L):
        for sj in range(1, N+1, L):
            for i in range(L):
                for j in range(L):
                    new[si+i][sj+j] = arr[L-j-1+si][sj+i]
    arr = new

    # 네방향, 0이 2개 이상이면 얼음 -1 감소
    new = [x[:] for x in arr] # arr을 deepcopy
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j]==0: continue

            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if arr[i+di][j+dj] == 0:
                    cnt += 1
                    if cnt >= 2:
                        new[i][j]-=1 # 얼음 1녹임
                        break #다음위치로
    arr = new

def bfs(si, sj):
    q = []

    q.append((si, sj))
    v[si][sj]=1
    cnt = 1

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if v[ni][nj]==0 and arr[ni][nj]>0:
                q.append((ni, nj))
                v[ni][nj]=1
                cnt+=1
    return cnt

# 정답처리: 남은 얼음덩어리중 가장 큰 크기
v = [[0]*(N+2) for _ in range(N+2)]
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if v[i][j]==0 and arr[i][j]>0: # 미방문 얼음이면 탐색시작
            ans = max(ans, bfs(i, j))
print(sum(map(sum,arr)))
print(ans)
