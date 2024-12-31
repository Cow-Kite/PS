import math

def solution(n):
    
    num = int(math.sqrt(n))
    if num ** 2 == n:
        return 1
    else:
        return 2
    