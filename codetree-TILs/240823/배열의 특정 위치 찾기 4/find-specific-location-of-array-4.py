arr = list(map(int, input().split()))
hap = 0
cnt = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        hap += i
        cnt += 1

print(f'{cnt} {hap}')