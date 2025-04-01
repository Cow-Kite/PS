N = int(input()) # 굴다리 길이
M = int(input()) # 가로등 개수

light = list(map(int, input().split()))

left = 1
right = N

while left <= right:
    mid = (left + right) // 2

    current = 0 # 현재까지 밝은 위치치

    for x in light:
        if x - mid > current:
            break # 못 밝힌 부분이 있음
        else:
            current = x + mid

    if current >= N:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
