N = int(input())
M = int(input())
X = list(map(int, input().split()))
left = 0
right = N

while left<=right:
    mid = (left+right)//2

    current = 0

    for x in X:
        if x-mid>current:
            break
        else:
            current = x + mid
    
    if current >= N:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)