n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in arr:
    if i == 0:
        break
    cnt+=1

print(arr[cnt-1]+arr[cnt-2]+arr[cnt-3]+arr[cnt-4]+arr[cnt-5])