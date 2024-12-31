def solution(a, b, c):
    answer = 0
    if a == b and a != c:
        return (a+b+c) * (a*a+b*b+c*c)
    if a == c and a != b:
        return (a+b+c) * (a*a+b*b+c*c)
    if b == c and b != a:
        return (a+b+c) * (a*a+b*b+c*c)
    if a != b and a != c and b != c:
        return a+b+c
    if a == b and a == c:
        return (a+b+c) * (a*a+b*b+c*c) * (a*a*a+b*b*b+c*c*c)
    
    return answer