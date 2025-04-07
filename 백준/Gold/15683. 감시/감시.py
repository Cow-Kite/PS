di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 90도씩 회전하기 때문에 상우하좌
cctv = [[], [1], [1, 3], [0, 1], [0, 1, 3], [0, 1, 2, 3]] # cctv 종류에 따른 보는 방향

def cal(tlst): # 사각지대 넓이 계산 하는 함수
    v = [[0]*(M+2) for _ in range(N+2)] # cctv로 봤는지 기록하는 변수
    for i in range(CNT):
        si, sj = lst[i] # cctv 좌표
        rot = tlst[i] # i번 cctv가 회전하는 정도 90도인지 180도인지 등
        type = arr[si][sj] # cctv 종류 1~5까지

        # type에 따라 모든 방향을 뻗어나가면서 v배열에 1로 표시를 할거야
        for dr in cctv[type]:
            dr = (dr+rot)%4
            ci, cj = si, sj
            while True:
                ci, cj = ci+di[dr], cj+dj[dr]
                if arr[ci][cj] == 6:
                    break
                v[ci][cj] = 1

        # 사각지대 넓이 카운트
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 0 and v[i][j] == 0:
                cnt += 1
    return cnt

def dfs(n, tlst):
    global ans
    if n == CNT: # 모든 cctv 방향 정하기 완료
        ans = min(ans, cal(tlst))
        return

    dfs(n+1, tlst+[0])
    dfs(n+1, tlst+[1])
    dfs(n+1, tlst+[2])
    dfs(n+1, tlst+[3])

N, M = map(int, input().split())

arr = [[6] * (M+2)] + [[6] + list(map(int, input().split())) + [6] for _ in range(N)] + [[6] * (M+2)]

lst = [] # cctv 좌표 저장
for i in range(1, N+1):
    for j in range(1, M+1):
        if 1<=arr[i][j]<=5:
            lst.append((i, j))

CNT = len(lst) # cctv의 개수
ans = N*M # 사각지대 넓이
dfs(0, []) # 0번 cctv부터 []: cctv 회전 리스트
print(ans)