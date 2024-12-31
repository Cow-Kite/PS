def solution(arr, intervals):
    
    a = intervals[0][0]
    b = intervals[0][1]
    c = intervals[1][0]
    d = intervals[1][1]
    
    return arr[a:b+1]+arr[c:d+1]