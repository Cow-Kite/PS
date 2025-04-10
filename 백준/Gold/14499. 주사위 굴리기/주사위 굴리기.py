N, M, ci, cj, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(int, input().split()))

n1=n2=n3=n4=n5=n6=0
di, dj = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0] # 동서북남

# 명령방향대로 이동 후 처리
for dr in lst:
    # 이동 후 범위내이면 처리
    ni, nj = ci+di[dr], cj+dj[dr]
    if 0<=ni<N and 0<=nj<M:
        # 주사위 굴리기
        if dr==1:
            n1, n3, n4, n6 = n4, n1, n6, n3
        elif dr==2:
            n1, n3, n4, n6 = n3, n6, n1, n4
        elif dr==3:
            n1, n2, n5, n6 = n5, n1, n6, n2
        else:
            n1, n2, n5, n6 = n2, n6, n1, n5

        # 이동한 면이 0인지 확인
        if arr[ni][nj]==0:
            arr[ni][nj]=n6
        else:
            n6=arr[ni][nj]
            arr[ni][nj]=0
        ci, cj = ni, nj # 이동 처리
        print(n1)