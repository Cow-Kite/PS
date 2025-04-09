# 백트래킹도 되고 dp도 되는데, dp가 훨씬 효율적
N = int(input())

T = [0]*N
P = [0]*N
dp = [0]*(N+1) # 초기값 때문에

for i in range(N):
    T[i], P[i] = map(int, input().split())

for i in range(N-1, -1, -1): # 뒤에서 앞으로
    if i + T[i] <= N:        # 기간 내 상담 완료 가능
        dp[i] = max(dp[i+T[i]]+P[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])