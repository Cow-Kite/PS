n = int(input())
arr = list(map(float, input().split()))
hap = 0
for i in arr:
    hap += i

print(f'{hap/n:.1f}')