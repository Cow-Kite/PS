cnt1 = 0
cnt2 = 0

n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i % 5 == 0: 
        cnt1 += 1
    if i % 7 == 0 :
        cnt2 += 1

print(cnt1)
print(cnt2)