def solution(hp):
    answer = 0
    five = hp // 5
    hp = hp % 5
    
    three = hp // 3
    hp = hp % 3
    
    one = hp // 1
    
    answer = five + three + one
    return answer