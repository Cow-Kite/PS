n = int(input())
arr = list(map(int, input().split()))
new_arr = [0]*8

for i in arr:
    new_arr[i-1] += 1

cnt = 1
for elem in new_arr:
    print(f'{cnt} - {elem}')
    cnt += 1