def solution(array, height):
    answer = 0
    for elem in array:
        if elem > height:
            answer += 1
    return answer