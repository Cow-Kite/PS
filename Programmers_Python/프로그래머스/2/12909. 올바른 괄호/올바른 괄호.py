def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append(i)
        if i == ")":
            if answer:
                answer.pop()
            else:
                return False
    return not answer