n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(0, n):
    for j in range(0, n):
        if i%2==0:
            arr[i][j] = 1
        if j%2==1:
            arr[i][j] = 2

for row in arr:
    print(' '.join(map(str, row)))