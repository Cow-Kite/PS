n = int(input())
hap = 0
for i in range(1, n):
    if n % i == 0:
        hap += i

if hap == n:
    print('P')
else:
    print('N')