n, k = map(int, input().split()) # n = 25, k = 3
count = 0

while True:
    target = (n//k) * k # 25 // 3 = 8 * 3 = 24
    count = n - target # count = 1 -> -1 하는 횟수
    n = target # n = 24
    if n < k: # 더 이상 나눌 수 없을 때까지
        break
    count += 1
    n //= k

count += n-1