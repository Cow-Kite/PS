n = int(input())

for i in range(0, n):
    for j in range(9-i, (9-i)-n, -1):
        if j <= 0:
            print(1, end = " ")
        else: 
            print(j, end = " ")
    print()