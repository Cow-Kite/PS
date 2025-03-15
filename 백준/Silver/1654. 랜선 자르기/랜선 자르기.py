k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]

low, high = 1, max(line)
result = 0

while low <= high:
    mid = (low+high) // 2
    count = 0

    for i in range(k):
        count += (line[i] // mid)

    if count >= n:
        result = mid
        low = mid + 1
    else:
        high = mid - 1

print(result)