n = int(input())
arr = list(map(int, (input().split())))
new_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for elem in arr:
    num = elem // 100 
    new_arr[num] = new_arr[num] + 1

for i in range(0, len(new_arr)):
    if new_arr[i] != 0:
        print(f'{i} - {new_arr[i]}')