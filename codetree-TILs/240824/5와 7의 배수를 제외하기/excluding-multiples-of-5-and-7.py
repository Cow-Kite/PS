n = int(input())
arr = list(map(int, input().split()))
cnt = 0
hap = 0
for i in arr:
    if i % 5 == 0 or i % 7 == 0:
        continue
    hap += i
    cnt += 1

print(hap)
print(f'{hap/cnt:.1f}')