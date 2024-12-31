n = int(input())
num = 1000
cnt = 0 
hap = 0
even = 2

while num > n:
    num -= even
    hap += even
    cnt += 1
    even += 2

print(cnt, hap)