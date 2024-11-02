def solution(a, b):
    a = str(a)
    b = str(b)
    answer1 = int(a + b)
    answer2 = int(b + a)
    if answer1 >= answer2:
        return answer1
    return answer2