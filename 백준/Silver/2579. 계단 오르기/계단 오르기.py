num = int(input())

stairs = [0] * (num+1)
dp = [0] * (num+1)

for i in range(1, num+1):
    stairs[i] = int(input())

def up_stairs(num):
    if num == 1:
        return stairs[1]
    if num == 2:
        return stairs[1] + stairs[2]
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, num+1):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

    return dp[num]

print(up_stairs(num))

