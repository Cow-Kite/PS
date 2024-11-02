def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1