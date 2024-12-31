def solution(n):
    
    for num in range(6, 6*n+1, 6):
        if num % n == 0:
            return num//6
    