n = int(input())
T = []
P = []

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n+2)

for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i-1])
    

    if i + T[i-1] - 1 <= n:
        dp[i + T[i-1]] = max(dp[i + T[i-1]], dp[i] + P[i-1])

print(max(dp))