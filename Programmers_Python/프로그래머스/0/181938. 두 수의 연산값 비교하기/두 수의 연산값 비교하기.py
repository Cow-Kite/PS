def solution(a, b):
    num = 2 * a * b
    a, b = str(a), str(b)
    answer = max(int(a+b), num)
    return answer