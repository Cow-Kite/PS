N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for i in range(N):
    # 총감독관은 무조건 1명
    ans += 1
    if arr[i] > B:
        # 남은 인원만큼 부감독관 배치
        ans += (arr[i] - B + C - 1) // C

print(ans)