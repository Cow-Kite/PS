def solution(n):
    answer = 0
    for elem in range(2, n+1, 2):
        answer += elem
    return answer