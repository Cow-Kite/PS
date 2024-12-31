x, y = map(int, input().split())

hap = 0 
cnt = 0

max_num = max(x, y)
min_num = min(x, y)
for i in range(min_num, max_num+1):
    if i % 5 != 0:
        hap += i
        cnt += 1

print(f'{hap} {hap/cnt:.1f}')