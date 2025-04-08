# 핵심 포인트: 사람 -1, 비상구 -11
# 회전이나 이동시 narr 생성해서 수정한 후 다시 arr에 복사
# 사각형 범위 주의
# 회전 공식 

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1][j-1] -= 1

ei, ej = map(int, input().split())
ei, ej = ei-1, ej-1
arr[ei][ej] = -11

def find_square(arr):
    mn = N # N보다는 작을거니까
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람인 경우 거리 측정
                mn = min(mn ,max(abs(ei-i), abs(ej-j))) # 가로, 세로 길이 중 max값이랑 비교

    # 사각형 최소 길이를 찾았으니까 계속 순회하면서 길이가 L인 정사각형에 사람이랑 비상구가 있는지 체크
    for si in range(N-mn):
        for sj in range(N-mn):
            if si<=ei<=si+mn and sj<=ej<=sj+mn: # 비상구 있으면
                for i in range(si, si+mn+1):
                    for j in range(sj, sj+mn+1):
                        if -11<arr[i][j]< 0: # 사람이 있으면
                            return si, sj, mn+1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

ans = 0
cnt = M
for _ in range(K):
    # 모든 참가자 한 칸 이동
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11<arr[i][j]<0: # 사람인 경우에만 이동
                dist = abs(i-ei)+abs(j-ej)
                # 네 방향
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]<=0 and dist>(abs(ei-ni)+abs(ej-nj)):
                        ans += arr[i][j] # 정답 변수 (전체 이동거리)
                        narr[i][j] -= arr[i][j] # 사람이 있던 칸에서 이동했으니까 사람 수를 없애는 처리를 해줘야함
                        if arr[ni][nj] == -11: # 내가 이동하고자 하는 곳이 비상구라면
                            cnt += arr[i][j] # 사람 탈출
                        else: # 빈칸 또는 사람있는 자리라면
                            narr[ni][nj] += arr[i][j] # 들어온 인원 추가
                        break # 한 명의 사람은 한 턴에 한 칸만 이동 가능

    arr = narr # 이동한 지도 표시
    if cnt == 0: # 참가자가 다 탈출했다면,
        break # 종료

    # 회전
    si,sj,L = find_square(arr) # 비상구+사람 포함 최소 정사각형 찾기

    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si+i][sj+j] = arr[si+L-1-j][sj+i]
            if narr[si+i][sj+j] > 0:
                narr[si+i][sj+j] -= 1 # 벽이면 회전시 1 감소
    arr = narr
    ei, ej = find_exit(arr)

print(-ans)
print(ei+1, ej+1)
