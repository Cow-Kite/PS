n = int(input())
arr = list(input().split())

new_arr = ''.join(arr)

for i in range(0, len(new_arr), 5):
    print(new_arr[i:i+5])