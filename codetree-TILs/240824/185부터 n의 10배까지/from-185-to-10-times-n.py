n = int(input()) * 10 
hap = 0
cnt = 0
for i in range(185, n+1):
    hap += i
    cnt += 1

print(f'{hap} {hap/cnt:.1f}')