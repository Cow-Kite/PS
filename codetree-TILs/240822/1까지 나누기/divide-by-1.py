n = int(input())
cnt = 0

for i in range(1, n+1):
    cnt += 1
    n //= i
    if n <= 1:
        print(cnt)
        break