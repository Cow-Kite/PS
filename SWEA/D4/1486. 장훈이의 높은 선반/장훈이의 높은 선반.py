T = int(input())

def dfs(n, sm):
    global ans
    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return

    dfs(n+1, sm+height[n])
    dfs(n+1, sm)

for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    ans = N * 10000
    dfs(0, 0)

    print(f'#{test_case} {ans}')