n  = int(input())
cnt = 0
hap = 0
for _ in range(n):
    num = int(input())
    hap += num
    cnt += 1 

avg = hap / cnt
print(f'{avg:.1f}')
if avg < 70:
    print('fail')