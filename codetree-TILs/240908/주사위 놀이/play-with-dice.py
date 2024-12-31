arr = list(map(int, input().split()))
count = [0]*6

for elem in arr:
    count[elem-1] += 1

for i in range(1, 7):
    print(f'{i} - {count[i-1]}')