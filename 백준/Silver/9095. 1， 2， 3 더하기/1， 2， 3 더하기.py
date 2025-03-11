T = int(input())

def solution(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N == 3:
        return 4
    
    arr = [0] * (N+1)
    arr[1], arr[2], arr[3] = 1, 2, 4

    for i in range(4, N+1):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

    return arr[N]


for _ in range(T):
    print(solution(int(input())))