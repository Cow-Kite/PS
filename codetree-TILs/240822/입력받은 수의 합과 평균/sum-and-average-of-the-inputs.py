n = int(input())
hap = 0

for i in range(0, n):
    num = int(input())
    hap += num

print(hap, end=" ")
print(f'{hap/n:.1f}')