n = int(input())
arr = list(map(int, input().split()))
min_num = arr[0]

for elem in arr:
    if min_num > elem:
        min_num = elem
    
min_cnt = 0

for i in arr:
    if i == min_num:
        min_cnt+=1

print(f'{min_num} {min_cnt}')