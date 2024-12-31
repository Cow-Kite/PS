arr = list(map(int, input().split()))

hap = 0
cnt = 0
for num in arr:
    if num >= 250:
        break
    hap += num    
    cnt += 1

print(f'{hap} {hap/cnt:.1f}')