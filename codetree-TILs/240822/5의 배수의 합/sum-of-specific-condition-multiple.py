a, b = map(int, input().split(" "))
hap = 0
j = min(a,b)
h = max(a,b)
for i in range(j, h+1):
    if i % 5 == 0:
        hap += i

print(hap)