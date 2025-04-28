N = int(input())

arr = list(map(int, input().split()))
M = int(input())

left = 1
right = max(arr)
cost = 0

while left<=right:
    mid = (left+right)//2
    total = 0
    
    for price in arr:
        if price <= mid:
            total += price
        else:
            total += mid
    
    if total <= M:
        left = mid+1
        cost = mid
    else:
        right = mid-1

print(cost)