def solution(n, times):
    low = min(times)
    high = max(times) * n
    
    while low <= high:
        mid = (low+high) // 2
        count = sum(mid // time for time in times)
        
        if count >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return answer 