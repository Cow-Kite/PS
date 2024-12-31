def solution(s):
    answer = list(map(int, s.split()))
    min_val = min(answer)
    max_val = max(answer)
    return f'{min_val} {max_val}'