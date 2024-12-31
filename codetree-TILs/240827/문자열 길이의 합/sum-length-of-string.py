n = int(input())
hap = 0
cnt = 0
for _ in range(n):
    arr = input()
    hap += len(arr)
    if arr[0] == 'a':
        cnt += 1

print(hap, cnt)