def solution(array):
    answer = array[0]
    index = 0
    for i in range(1, len(array)):
        if answer < array[i]:
            answer = array[i]
            index = i
    
    answer2 = [answer, index]
    return answer2