N, M, H = map(int, input().split())

def check():
    for sj in range(1, N+1): # 모든 sj값이 끝날때고 같아야댐
        j = sj
        for i in range(1, H+1):
            if arr[i][j]==1: # 오른쪽으로 이동
                j+=1
            elif arr[i][j-1] == 1: # 왼쪽으로 이동
                j-=1
        if j!=sj:
            return 0
    return 1

def dfs(n, s):
    global ans

    if n==cnt: # 모든 개수를 선택완료
        if check()==1:
            ans=1
        return

    for j in range(s, CNT):
        ti, tj = pos[j]
        #왼쪽도 사다리가 아니고, 오른쪽도 사다리가 아니면 놓는게 가능
        if arr[ti][tj-1] == 0 and arr[ti][tj+1] == 0:
            arr[ti][tj] = 1
            dfs(n+1, j+1)
            arr[ti][tj] = 0
arr = [[0]*(N+2) for _ in range(H+1)] # 좌우 공백 추가
# 사다리 입력 받기
for _ in range(M):
    ti, tj = map(int, input().split())
    arr[ti][tj] = 1

# 사다리 놓을 후보 저장
pos = []
for i in range(1, H+1):
    for j in range(1, N+1):
        if arr[i][j] == 0:
            pos.append((i, j))
CNT = len(pos)

# 추가하는 사다리 개수 0~3 실행 -> 안되면 -1이 정답
for cnt in range(4):
    ans = 0
    dfs(0, 0) # CNT개에서 cnt개수를 뽑는 모든 조합
    if ans == 1:
        ans = cnt
        break
else:
    ans = -1

print(ans)
