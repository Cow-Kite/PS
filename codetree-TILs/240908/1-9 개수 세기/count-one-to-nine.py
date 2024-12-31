n = int(input())

arr = list(map(int, input().split()))
count = [0] * 9
for elem in arr:
    count[elem-1] += 1

for i in range(9):
    print(count[i])