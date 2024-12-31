def solution(s):
    answer = ''
    num = len(s) // 2
    if not len(s) % 2:
        answer = s[num-1] + s[num] 
    else:
        answer = s[num]
    return answer