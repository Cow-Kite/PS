def solution(myString, pat):
    new = ""
    answer = 0
    for i in myString:
        if i == 'A':
            new += 'B'
        if i == 'B':
            new += 'A'
    if pat in new:
        answer = 1
    return answer