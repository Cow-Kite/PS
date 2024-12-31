n = int(input())

for i in range(0, n):
    count = 2 * (n-i)
    print('*'*count)

for j in range(n-2, -1, -1):
    count = 2 * (n-j)
    print('*'*count)