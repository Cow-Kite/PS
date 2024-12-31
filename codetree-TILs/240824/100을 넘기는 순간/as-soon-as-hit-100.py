n = int(input())
arr = list(map(int, input().split()))
cnt = 0
hap = 0
for i in arr:
    cnt += 1
    hap += i
    if i >= 100:
        print(hap)
        print(f'{hap/cnt:.1f}')
        break