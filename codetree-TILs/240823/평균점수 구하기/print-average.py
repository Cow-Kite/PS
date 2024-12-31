arr = list(map(float, input().split()))

hap = 0
for i in arr:
    hap += i

print(f'{hap/len(arr):.1f}')