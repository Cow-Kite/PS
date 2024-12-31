n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    if i%2==0:
        for j in range(m):
            arr[i][j] = cnt
            cnt += 1
    if i%2==1:
        for k in range(m-1, -1, -1):
            arr[i][k] = cnt
            cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end= " ")
    print()