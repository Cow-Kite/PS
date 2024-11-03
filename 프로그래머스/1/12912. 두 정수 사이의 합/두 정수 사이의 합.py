def solution(a, b):
    answer = 0
    num1 = max(a, b)
    num2 = min(a, b)
    for num in range(num2, num1+1):
        answer += num
    return answer