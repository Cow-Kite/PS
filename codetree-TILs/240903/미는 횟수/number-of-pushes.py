A = input()
B = input()

cnt = 0
while True:
    if cnt == len(A):
        cnt = -1
        break
    if A == B:
        break
    A = A[-1]+A[:-1]
    cnt += 1

print(cnt)