hap = 0
cnt = 0
for i in range(0, 10):
    n = int(input())
    if n >= 0 and n <= 200:
        hap += n
        cnt += 1

print(hap, end=" ")
print(f'{hap/cnt:.1f}')