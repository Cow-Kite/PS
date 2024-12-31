n = int(input())
arr = list(map(int, input().split()))
hap = 0
for i in range(1, n, 2):
    hap += arr[i]

print(f'{hap} {hap/(n//2):.1f}')