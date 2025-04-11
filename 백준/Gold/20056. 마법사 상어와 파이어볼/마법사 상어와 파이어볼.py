N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

for a in arr: # 좌표 맞추기
    a[0] -= 1
    a[1] -= 1

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]
    # 격자에 파이어볼 추가하기
    for r, c, m, s, d in arr:
        nr = (r + dr[d]*s) % N
        nc = (c + dc[d]*s) % N
        board[nr][nc].append((m, s, d))

    # 파이어볼 합치기
    arr = []
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue # 파이어볼 없으면 스킵
            if len(board[i][j])==1: # 파이어볼 하나라면 arr에 그대로 append
                m, s, d = board[i][j][0]
                arr.append([i, j, m, s, d])
            else: # 파이어볼 2개 이상
                sm, ss, dirs = 0, 0, []
                for m, s, d in board[i][j]:
                    sm += m
                    ss += s
                    dirs.append(d % 2)

                # 질량 나누기
                nm = sm//5
                if nm==0:
                    continue

                # 속력 나누기
                ns = ss // len(board[i][j])

                # 방향
                ndir = [0, 2, 4, 6] if all(x==dirs[0] for x in dirs) else [1, 3, 5, 7]

                # 파이어볼 리스트에 넣기
                for d in ndir:
                    arr.append([i, j, nm, ns, d])

print(sum(x[2] for x in arr))


