arr = list(map(int, input().split()))
max_num = arr[0]
min_num = arr[1]
for elem in arr:
    if elem == -999 or elem == 999:
        break
    if elem > max_num:
        max_num = elem
    if elem < min_num:
        min_num = elem


print(f'{max_num} {min_num}')