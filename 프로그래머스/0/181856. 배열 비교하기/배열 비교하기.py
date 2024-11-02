def solution(arr1, arr2):
    answer = 0
    num1, num2 = 0, 0
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            answer = 1
        elif len(arr1) < len(arr2):
            answer = -1
        else:
            answer = 0
    else:
        for i in arr1:
            num1 += i
        for i in arr2:
            num2 += i
            
        if num1 > num2:
            answer = 1
        elif num1 < num2:
            answer = -1
        else:
            answer = 0
    return answer