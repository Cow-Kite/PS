arr = list(map(int, input().split()))

cnt = 0
hap = 0

for i in arr:
    if i == 0:
        for j in range(cnt, cnt-4, -1):
            hap += arr[j]
        break
    cnt+=1
print(hap)