def solution(num_list):
    answer1 = 1
    answer2 = 0
    
    for i in num_list:
        answer1 *= i
        answer2 += i
    answer2 *= answer2
    return 1 if answer1 < answer2 else 0
   