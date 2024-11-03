def solution(n):
    answer = []
    n = str(n)
    for i in n:
        answer.append(int(i))
    answer.sort(reverse=True)
    return int("".join(map(str, answer)))