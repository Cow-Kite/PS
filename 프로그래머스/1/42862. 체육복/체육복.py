def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve = set(reserve) - set(lost)
    
    for num in sorted(reserve):
        if num-1 in lost_set:
            lost_set.remove(num-1)
        elif num+1 in lost_set:
            lost_set.remove(num+1)
            
    return n - len(lost_set)