n = int(input())

#for i in range(n):
for j in range(n, 0, -1):
    for h in range(j):
        print('*'*j, end=" ")
    print()