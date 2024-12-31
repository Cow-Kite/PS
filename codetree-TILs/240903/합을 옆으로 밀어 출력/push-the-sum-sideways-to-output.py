n = int(input())

hap = 0

for _ in range(n):
    hap += int(input())

hap = str(hap)
print(hap[1:]+hap[0])