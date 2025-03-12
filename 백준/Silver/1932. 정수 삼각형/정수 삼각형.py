n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
if n == 1:
    print(arr[0][0])
    exit()

dp = [row[:] for row in arr]

for i in range(n-2, -1, -1):
    for j in range(len(arr[i])):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + arr[i][j]


print(dp[0][0])