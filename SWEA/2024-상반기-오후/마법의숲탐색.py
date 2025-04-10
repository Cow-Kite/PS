R, C, K = map(int, input().split())
unit = [list(map(int, input().split())) for _ in range(K)]
arr = [[1] + [0]*C + [1] for _ in range(R+3)] + [[1]*(C+2)]
exit_set = set() # 출구 기록

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

ans = 0 # 정답 변수
num = 2 # 골렘 번호 (arr에 기록)

def bfs(si, sj):
    q = []
    v = [[0]*(C+2) for _ in range(R+4)]
    mx_i=0
    q.append((si, sj))
    v[si][sj]=1

    while q:
        ci, cj = q.pop(0)
        mx_i = max(mx_i, ci)
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj
            if v[ni][nj]==0:
                if arr[ci][cj] == arr[ni][nj]: # 같은 골렘이라면
                    q.append((ni, nj))
                    v[ni][nj] = 1
                elif (ci, cj) in exit_set and arr[ni][nj] > 1: # 현재 위치가 출구이고, 다음 위치가 다른 골렘이라면
                    q.append((ni, nj))
                    v[ni][nj] = 1
    return mx_i-2

for cj, dr in unit:
    ci = 1
    while True:
        if arr[ci + 1][cj - 1] + arr[ci + 2][cj] + arr[ci + 1][cj + 1] == 0:
            ci += 1
        elif (arr[ci - 1][cj - 1] + arr[ci][cj - 2] + arr[ci + 1][cj - 1] + arr[ci + 1][cj - 2] + arr[ci + 2][
            cj - 1]) == 0:
            ci+=1
            cj-=1
            dr = (dr-1)%4 # 골렘 출구 위치 바뀜
        elif (arr[ci - 1][cj + 1] + arr[ci][cj + 2] + arr[ci + 1][cj + 1] + arr[ci + 1][cj + 2] + arr[ci + 2][
            cj + 1]) == 0:
            ci+=1
            cj+=1
            dr = (dr+1)%4
        else: # 끝까지 이동한 경우
            break

    # 골렘을 지도에 표시
    if ci<4: # 골렘의 일부가 지도밖에 있다 -> 지도와 변수 리셋
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit_set=set()
        num=2
    else: # 지도에 골렘을 추가하고, 출구 정보도 저장
        arr[ci+1][cj]=arr[ci-1][cj]=num
        arr[ci][cj-1:cj+2]=[num]*3
        num+=1 #다음 골렘으로 ㄱㄱ
        exit_set.add((ci+di[dr], cj+dj[dr]))

        ans+=bfs(ci, cj) # 정령들이 최종적으로 위치한 행
print(ans)
