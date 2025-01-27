def solution(number, k):
    answer = ''
    stk = []
    
    for num in number:
        while stk and k > 0 and stk[-1] < num:
            stk.pop()
            k -= 1
        stk.append(num)
        
    stk = stk[:len(number)-k]
    return ''.join(stk)