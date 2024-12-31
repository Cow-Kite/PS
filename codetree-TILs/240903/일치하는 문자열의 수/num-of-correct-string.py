n, A = input().split()
cnt = 0

for _ in range(int(n)):
    a = input()
    if a == A:
        cnt += 1

print(cnt)