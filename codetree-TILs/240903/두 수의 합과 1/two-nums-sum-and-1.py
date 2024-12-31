a, b = map(int, input().split())

hap = str(a + b)
cnt = 0

for i in hap:
    if i == '1':
        cnt += 1

print(cnt)