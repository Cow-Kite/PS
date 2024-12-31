a, b = map(int, input().split(" "))
hap = 0
cnt = 0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        hap+=i
        cnt+=1

print(hap, end=" ")
print(f'{hap/cnt:.1f}')