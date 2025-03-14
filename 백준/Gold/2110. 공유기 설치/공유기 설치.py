n, c = map(int, input().split())

houses = sorted(int(input()) for _ in range(n))

low, high = 1, houses[-1] - houses[0]
result = 0

while low <= high:
    mid = (low + high) // 2
    installed = houses[0] # 1
    count = 1


    for i in range(1, n):
        if houses[i] - installed >= mid: 
            installed = houses[i] # 공유기 하나 더 설치
            count += 1
    
    if count >= c: # 설치한 공유기 개수가 해야하는 개수보다 많다면 거리 증가
        result = mid
        low = mid + 1 
    else:
        high = mid - 1

print(result)