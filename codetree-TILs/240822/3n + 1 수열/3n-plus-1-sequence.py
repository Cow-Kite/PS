N = int(input())
cnt = 0
while True:
    if N == 1:
        print(cnt)
        break
    if N % 2 == 0:
        N = N//2
    else:
        N = N * 3 + 1
    cnt += 1