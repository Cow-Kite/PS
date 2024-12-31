n = int(input())
arr = list(map(int, input().split()))
k = int(input())
hap1=0
hap2=0

for i in arr:
    if k % i == 0:
        hap1 += i

    if i % k == 0:
        hap2 += i

print(hap1)
print(hap2)