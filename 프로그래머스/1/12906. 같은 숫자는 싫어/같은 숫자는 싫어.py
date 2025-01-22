def solution(arr):
    answer = []
    no = arr[0]
    answer.append(no)
    
    for i in range(1, len(arr)):
        if arr[i] != no:
            answer.append(arr[i])
        no = arr[i]
        
    return answer
    