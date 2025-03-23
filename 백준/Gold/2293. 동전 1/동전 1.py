n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1 # 아무것도 선택하지 않는 방법 한 가지

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]

print(dp[k])