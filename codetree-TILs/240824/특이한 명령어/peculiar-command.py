n = int(input())
for _ in range(n):
    arr = input().split()
    if arr[2] == 's':
        print(int(arr[0])*int(arr[1]))
    elif arr[2] == 't':
        print((int(arr[0])*int(arr[1]))/2)