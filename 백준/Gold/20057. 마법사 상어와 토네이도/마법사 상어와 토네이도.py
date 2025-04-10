N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mul=[ 2,10, 7, 1, 5,10, 7, 1, 2, 0]     #  %비율 => 100으로 나눠야 함
ai=[[-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0],
    [ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1]]
aj=[[ 0,-1, 0, 1,-2,-1, 0, 1, 0,-1],
    [-2,-1,-1,-1, 0, 1, 1, 1, 2, 0],
    [ 0, 1, 0,-1, 2, 1, 0,-1, 0, 1],
    [ 2, 1, 1, 1, 0,-1,-1,-1,-2, 0]]

di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]
cnt_mx = 1
ci = cj = N//2
ans = dr = cnt = flag = 0

while (ci,cj)!=(0,0):
    ci, cj = ci+di[dr], cj+dj[dr]

    # ci, cj 기준좌표 중심으로 모래량 계산 추가, 범위 밖이면 ans에 추가
    if arr[ci][cj]>0: # 모래가 있을때만 진행
        val = arr[ci][cj] # 기준좌표 모래량
        arr[ci][cj] = 0
        sm = 0

        for i in range(10):
            ni, nj = ci+ai[dr][i], cj+aj[dr][i] # 좌표 계산
            t = (val*mul[i])//100 # 소수점이하 버림
            if i==9: # 나머지 모래
                t=val-sm
            if 0<=ni<N and 0<=nj<N:
                arr[ni][nj]+=t
            else:
                ans+=t
            sm+=t

    cnt += 1
    if cnt==cnt_mx:
        cnt=0
        dr = (dr+1)%4 # 방향은 매번 바뀜
        if flag==0:   # 1, 1, 2, 2, 3, 3... 두 번마다 칸수 이동하는 증가
            flag=1
        else:
            flag=0
            cnt_mx+=1
print(ans)