T = int(input())

for num in range(1, T+1):
    N = int(input())
    arr = [0] * 101
    scores = list(map(int, input().split()))

    for score in scores:
        arr[score] = arr[score] + 1

    max_score = 0
    max_score_index = 0

    for i in range(len(arr)):
        if arr[i] >= max_score:
            max_score_index = i
            max_score = arr[i]

    print(f"#{num} {max_score_index}")