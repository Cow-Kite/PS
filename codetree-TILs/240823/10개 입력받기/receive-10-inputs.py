arr = list(map(int, input().split()))
cnt = 0
hap = 0
for i in arr:
    if i == 0:
        break
    hap += i
    cnt += 1

print(f'{hap} {hap/cnt:.1f}')