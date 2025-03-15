n = int(input())
area = list(map(int, input().split()))

price = int(input())

if sum(area) <= price:
    print(max(area))
    exit()

low, high = 1, max(area)
result = 0

while low <= high:
    mid = (low+high)//2
    max_price = 0

    for i in range(n):
        if area[i] >= mid:
            max_price += mid
        else:
            max_price += area[i]

    if max_price <= price:
        low = mid + 1
        result = mid
    else:
        high = mid - 1

print(result)