N = int(input())
for i in range(1, N+1):
    a = int(input())
    if a % 3 == 0 and a % 2 == 1:
        print(a)