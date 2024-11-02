def solution(n_str):
    answer = ''
    idx = 0
    
    for i in range(0, len(n_str)):
        if n_str[i] != '0':
            idx = i
            break
    
    answer = n_str[idx:]
    return answer