def solution(arr):
    answer = 0
    for num in arr:
        answer += num
    return answer / len(arr)