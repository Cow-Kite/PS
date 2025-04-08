from collections import deque
def bfs(si, sj):
    q = deque()
    v = [[0]*N for _ in range(N)]
    tlst = []

    # q에 데이터 삽입 v 표시
    q.append((si, sj))
    v[si][sj] = 1
    eat = 0

    while q:
        ci, cj = q.popleft()
        # eat == v[ci][cj]
        if eat == v[ci][cj]:
            return tlst, eat-1

        # 4방향, 범위내, 미방문, 조건 (나보다 같거나 작은 물고기)
        for di, dj in ((-1,0), (1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and shark >= arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                # 나보다 작은 물고기인 경우 tlst에 추가
                if shark > arr[ni][nj] > 0:
                    tlst.append((ni, nj))
                    eat = v[ni][nj]

    # 방문을 모두 끝낸경우
    return tlst, eat-1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            ci, cj = i, j
            arr[i][j] = 0

shark = 2
cnt = ans = 0
while True:
    tlst, dist = bfs(ci, cj)
    if len(tlst)==0: # 먹을 물고기 없음
        break
    tlst.sort(key=lambda x: (x[0], x[1])) # 행, 열 순위로 정렬
    ci, cj = tlst[0]
    arr[ci][cj] = 0 # 물고기 먹기
    cnt += 1
    ans += dist
    if shark == cnt:
        shark += 1
        cnt = 0

print(ans)