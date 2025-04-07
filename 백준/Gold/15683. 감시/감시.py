di = [-1,0,1,0]
dj = [0,1,0,-1] # 상우하좌
cctv = [[], [1], [1,3], [0,1], [0,1,3], [0,1,2,3]]

def cal(tlst):
    v = [[0]*(M+2) for _ in range(N+2)]
    #  모든 cctv에 대해서 처리
    for i in range(CNT):
        si, sj = lst[i]
        rot = tlst[i]
        type = arr[si][sj]

        # type에 따라 모든 방향을 뻗어가면서 v[] 1표시
        for dr in cctv[type]:
            dr = (dr+rot)%4
            ci, cj = si, sj
            while True:
                ci, cj = ci+di[dr], cj+dj[dr]
                if arr[ci][cj] == 6:
                    break
                v[ci][cj] = 1

    # 사각지대(0이고, 미방문) 개수 카운트
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 0 and v[i][j] == 0:
                cnt += 1
    return cnt

def dfs(n, tlst):
    global ans
    if n == CNT: # 모든 cctv 방향 정하기 원료
        ans = min(ans, cal(tlst))
        return
    dfs(n+1, tlst+[0]) #   0도 회전
    dfs(n+1, tlst+[1]) #  90도 회전
    dfs(n+1, tlst+[2]) # 180도 회전
    dfs(n+1, tlst+[3]) # 270도 회전

N, M = map(int, input().split())
# 벽 6번으로 가장 자리 막음
arr = [[6] * (M+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]

lst = [] # cctv 좌표 저장
for i in range(1, N+1):
    for j in range(1, M+1):
        if 1<=arr[i][j]<=5:
            lst.append((i, j))

CNT = len(lst)
ans = N*M
dfs(0, [])
print(ans)