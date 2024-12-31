arr = list(map(int, input().split()))

hap1 = 0
hap2 = 0

for i in range(0, len(arr)):
    if i % 2 == 0:
        hap1 += arr[i]
    else:
        hap2 += arr[i]

print(hap1 - hap2) if hap1 >= hap2 else print(hap2 - hap1)