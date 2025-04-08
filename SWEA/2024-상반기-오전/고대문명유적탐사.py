def rotate(arr, si, sj): # 90도 회전하는 동작
     narr = [x[:] for x in arr]
     for i in range(3):
         for j in range(3):
             narr[si+i][sj+j] = arr[si+3-j-1][sj+i]
     return narr

def bfs(arr, v, si, sj, clr):
    q = []
    sset = set()
    cnt = 0

    q.append((si, sj))
    v[si][sj] = 1
    sset.add((si, sj))
    cnt += 1

    while q:
        ci, cj = q.pop(0)
        # 네방향, 미방문, 조건
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = 1
                sset.add((ni, nj))
                cnt += 1

    if cnt >= 3: # 유물이면: cnt 리턴 + clr == 1이면 0으로 clear
        if clr==1:
            for i, j in sset:
                arr[i][j] = 0
        return cnt
    else: # 3개미만이면 유물이 아니니까 0리턴
        return 0


def count_clear(arr, clr):
    v = [[0]*5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5): # 미방문인경우 같은 값이면
            if v[i][j] == 0:
                # 같은 값이면, 3개 이상인 경우
                t = bfs(arr, v, i, j, clr)
                cnt += t
    return cnt


K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []

for _ in range(K): # K턴 만큼 진행
    # 탐사 진행
    mx_cnt = 0
    for rot in range(1, 4): # 회전수
        for sj in range(3): # 열
            for si in range(3): # 행 작은 순서대로
                # rot 횟수만큼 90도 시계방향 회전 -> narr
                narr = [x[:] for x in arr] # 회전은 새로운 배열 생성해서 복사해
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                # 유물 개수 카운트
                t = count_clear(narr, 0)
                if mx_cnt < t:     # 최대개수 찾았다 -> 상태 보존
                    mx_cnt = t
                    marr = narr

    # 유물이 없으면 즉시 종료
    if mx_cnt == 0:
        break

    # 연쇄획득
    cnt = 0
    arr = marr
    while True:
        t = count_clear(arr, 1)
        if t == 0:
            break    # 연쇄획득 종료 -> 다음 턴으로 이동
        cnt += t # 획득한 유물 개수 누적

        # arr의 0값인 부분 리스트에서 순서대로 추가
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    ans.append(cnt) # 이번턴 연쇄획득한 개수 추가

print(*ans)
