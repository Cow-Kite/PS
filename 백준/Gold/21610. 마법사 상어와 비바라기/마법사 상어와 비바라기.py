N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clst1 = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2,1)] # 구름 초기 위치

di, dj = [0,0,-1,-1,-1,0,1,1,1],[0,-1,-1,0,1,1,1,0,-1]

for _ in range(M):
    D, S = map(int, input().split())
    clst2= [] # 이동한 구름 위치 좌표
    # 구름 이동 -> 구름 있는 자리에 물 증가 -> 구름 사라짐
    for ci, cj in clst1:
        ni, nj = (ci+di[D]*S+N)%N, (cj+dj[D]*S+N)%N
        arr[ni][nj]+=1 # 물 증가
        clst2.append((ni, nj))

    # 구름 이동한 위치에서 대각선 체크
    for ci, cj in clst2:
        for dii, djj in ((-1,-1),(-1,1),(1,-1),(1,1)):
            ni, nj = ci+dii, cj+djj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj]>0:
                arr[ci][cj]+=1

    # 전체 순회하면서 물이 2이상인 자리에 구름 발생 (물 -=2), 단 clst2는 제외
    clst1 = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>=2 and (i, j) not in clst2:
                arr[i][j]-=2
                clst1.append((i, j))

ans = 0
for lst in arr:
    ans += sum(lst)
print(ans)