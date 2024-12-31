n = int(input())
num = False
for i in range(2, n):
    if n % i == 0:
        num = True

if num == True:
    print('C')
else:
    print('N')