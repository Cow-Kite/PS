from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0]*M for _ in range(N)] # 공격한 턴수를 기록

def bfs(si, sj, ei, ej):
    q = deque()
    v = [[[] for _ in range(M)] for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = (si, sj)
    d = arr[si][sj] # 데미지

    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            arr[ei][ej] = max(0, arr[ei][ej]-d) # 목적지에 공격
            # 발자취따라서 공격
            while True:
                ci, cj = v[ci][cj]
                if (ci, cj) == (si, sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj]-d//2)
                fset.add((ci, cj))

        for di, dj in ((0,1), (1,0), (0,-1), (-1,0)):
            ni, nj = (ci+di)%N, (cj+dj)%M
            if len(v[ni][nj])==0 and arr[ni][nj] > 0: # 중요!!!! 미방문 칸이고, 포탑이여야돼
                q.append((ni, nj))
                v[ni][nj] = (ci, cj)
    return False

def bomb(si, sj, ei, ej):
    d = arr[si][sj]
    arr[ei][ej] = max(0, arr[ei][ej]-d)
    for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        ni, nj = (ei + di) % N, (ej + dj) % M
        if (ni, nj) != (si, sj):
            arr[ni][nj] = max(0, arr[ni][nj] - d // 2)
            fset.add((ni, nj))

for T in range(1, K+1):
    cnt = N*M
    for lst in arr:
        cnt -= lst.count(0)
    if cnt <= 1:
        break

    # 공격자 선정: 공격력 낮은, 가장 최근 공격자, 행+열(큰), 열(큰)
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            if mn > arr[i][j] or (mn == arr[i][j] and mx_turn < turn[i][j]) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si + sj < i + j) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and si + sj == i + j and sj < j):
                mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j  # si, sj 는 공격자


    # 공격 당할 포탑 선정: 공격력 높은-> 가장 오래전 공격자 -> 행+열(작은), 열(작은)
    mx, mn_turn, ei, ej = 0, T, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0: continue
            if mx < arr[i][j] or (mx == arr[i][j] and mn_turn > turn[i][j]) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and ei + ej > i + j) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and ei + ej == i + j and ej > j):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j  # ei, ej 공격당할 대상자

    arr[si][sj] += (N+M)
    turn[si][sj] = T # 중요!!!!!!!!! 이번 턴에 공격한다고 업데이트

    # 레이저 공격
    fset = set() # 공격 당한 모임
    fset.add((si, sj))
    fset.add((ei, ej)) # 중요!!!! 빼먹기 쉬움
    if bfs(si, sj, ei, ej) == False: # 레이저 공격 안되면 -> 포탄 공격으로
        bomb(si, sj, ei, ej)

    for i in range(N):
        for j in range(M):
            if (i, j) not in fset and arr[i][j] > 0:
                arr[i][j] += 1

print(max(map(max, arr)))
