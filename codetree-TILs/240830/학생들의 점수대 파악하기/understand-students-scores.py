n = int(input())

arr = [0] * 11
score = list(map(int, input().split()))

for i in score:
    arr[i // 10] += 1

for i in range(len(arr)-1, 0, -1):
    if arr[i] != 0:
        print(f'{i*10} - {arr[i]}')