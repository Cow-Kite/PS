N, MM, H, K = map(int, input().split())
M = (N+1)//2
arr = []
for _ in range(MM):
    arr.append(list(map(int, input().split())))

tree = set()
for _ in range(H):
    i,j = map(int, input().split())
    tree.add((i, j))
# 좌 우 하 상
di = [0, 0, 1, -1]
dj = [-1, 1, 0, 0]
opp = {0:1, 1:0, 2:3, 3:2}

# 상 우 하 좌
tdi = [-1, 0, 1, 0]
tdj = [0, 1, 0, -1]
mx_cnt, cnt, flag, val = 1, 0, 0, 1
ti, tj, td = M, M, 0
ans = 0

for k in range(1, K+1):
    # 도망자 동시 이동
    for i in range(len(arr)):
        if abs(arr[i][0]-ti)+abs(arr[i][1]-tj)<=3: #술래 범위 내라면 이동
            ni, nj = arr[i][0]+di[arr[i][2]], arr[i][1]+dj[arr[i][2]]
            if 1<=ni<=N and 1<=nj<=N:
                if(ni, nj)!=(ti, tj): # 범위 내고 술래랑 겹치지 않을때
                    arr[i][0], arr[i][1] = ni, nj # 도망자가 이동한 거 체크
            else: # 범위 밖이면, 방향 바꿔서 이동
                nd = opp[arr[i][2]]
                ni, nj=arr[i][0]+di[nd], arr[i][1]+dj[nd]
                if(ni, nj)!=(ti, tj):
                    arr[i] = [ni, nj, nd] # 도망자 이동한 거와 방향 바꾼거 체크
    # 술래 이동
    cnt += 1
    ti, tj = ti+tdi[td], tj+tdj[td]
    if (ti, tj) == (1, 1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td=2 # 방향도 아래로 바꾸기
    elif (ti, tj) == (M, M):
        mx_cnt, cnt, flag, val = 1, 0, 0, 1
        td=0 # 방향도 위로 바꾸기
    else:
        if cnt==mx_cnt: # 방향 바꿔
            cnt=0 # 초기화
            td=(td+val)%4 # 1씩 더하기 -> 방향 바꿈
            if flag==0:
                flag=1
            else:
                flag=0
                mx_cnt+=val

    # 도망자 잡기
    tset = set(((ti, tj), (ti+tdi[td], tj+tdj[td]), (ti+tdi[td]*2, tj+tdj[td]*2)))
    for i in range(len(arr)-1, -1, -1):
        if (arr[i][0],arr[i][1]) in tset and(arr[i][0],arr[i][1]) not in tree:
            arr.pop(i)
            ans+=k

    if not arr:
        break

print(ans)
