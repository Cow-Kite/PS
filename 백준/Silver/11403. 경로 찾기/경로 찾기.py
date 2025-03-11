N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            # k를 중간 노드로 놓고, i -> k -> j이면, i -> j도 갈 수 있음
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for row in arr:
    print(*row)