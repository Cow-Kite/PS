hap = 0
cnt = 0

n = int(input())
arr = list(map(int, input().split()))

for elem in arr:
    if hap > 200:
        break
    hap += elem
    cnt += 1

print(hap)
print(f'{hap/cnt:.1f}')