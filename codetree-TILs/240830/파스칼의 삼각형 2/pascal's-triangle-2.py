n = int(input())
arr = []
for i in range(n):
    arr.append([0] * (i + 1))
    for j in range(0, i+1):
        if j == 0 or j == i:
            arr[i][j] = 2
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    
for row in arr:
    for col in row:
        print(col, end=" ")
    print()