n = int(input())
cnt = 0 
hap = 0

arr = list(map(int, input().split()))

for i in arr:
    if i % 7 == 0:
        cnt += 1
        hap += i

print(f'{cnt} {hap} {hap/cnt:.1f}')