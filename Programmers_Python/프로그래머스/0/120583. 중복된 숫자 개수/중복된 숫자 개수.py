def solution(array, n):
    answer = 0
    for elem in array:
        if elem == n:
            answer += 1
    return answer