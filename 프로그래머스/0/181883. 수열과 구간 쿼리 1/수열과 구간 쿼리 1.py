def solution(arr, queries):
    #answer = []
    for i in range(len(queries)):
        s = queries[i][0]
        e = queries[i][1]
        for j in range(s, e+1):
            arr[j] += 1
    return arr