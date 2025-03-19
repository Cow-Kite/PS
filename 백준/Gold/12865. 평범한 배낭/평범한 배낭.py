n, k = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (k+1)

for weight, value in items:
    for w in range(k, weight - 1, -1): # 7 -> 6 -> 5 -> 4 -> ...
        dp[w] = max(dp[w], dp[w-weight] + value)

print(dp[k])