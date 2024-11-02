def solution(numLog):
    answer = ''
    operation_map = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range(1, len(numLog)):
        num = numLog[i] - numLog[i-1]
        answer += operation_map[num]
    return answer