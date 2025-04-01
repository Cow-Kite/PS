N, M = map(int, input().split())

lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)

# 이분 탐색 결과 변수
result = right

# 이분 탐색 시작
while left <= right:
    mid = (left + right) // 2

    count = 1 # 블루레이 개수
    current_sum = 0 # 강의 길이

    for lecture in lectures:
        if current_sum + lecture <= mid:
            current_sum += lecture
        else:
            count += 1
            current_sum = lecture

    if count <= M:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)