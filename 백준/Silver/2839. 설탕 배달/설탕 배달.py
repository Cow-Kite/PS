N = int(input())

count = 0

while N > 2:
    if N % 5 == 0:
        count += (N // 5)
        print(count)
        exit()

    N -= 3
    count += 1

if N == 0:
    print(count)
else:
    print(-1)