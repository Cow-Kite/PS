def solution(myString):
    answer = []
    for part in myString.split("x"):
        if part:
            answer.append(part)
    answer.sort()
    return answer