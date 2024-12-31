N, M = map(int, input().split())

A = [i for i in range(1, N+1)]

for i in range(M):
    start, end = map(int, input().split())
    temp = A[start-1:end]
    temp.reverse()
    A[start-1:end] = temp

for i in range(N):
    print(A[i], end=' ')