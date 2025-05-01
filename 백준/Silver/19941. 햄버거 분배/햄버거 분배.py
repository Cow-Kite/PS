H, K = map(int, input().split())
arr = list(input().strip())
eat = [False] * H

ans = 0
for i in range(H):
    # 햄버거라면 넘어가기
    if arr[i] == 'H':
        continue
    # 사람이라면 먹는 거 체크
    left = max(0, i-K)
    right = min(H-1, i+K)
    for j in range(left, right+1):
        if arr[j] == 'H' and not eat[j]:
            ans += 1
            eat[j] = True
            break
print(ans)