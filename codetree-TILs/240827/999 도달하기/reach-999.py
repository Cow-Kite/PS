n = int(input())
arr = []
arr.append(1)
arr.append(n)
print(1, end=" ")
print(n, end=" ")
cnt = 0
i = 2
while cnt < 999:
    cnt = arr[i-1]+arr[i-2]
    arr.append(cnt)
    i += 1
    print(cnt, end=" ")