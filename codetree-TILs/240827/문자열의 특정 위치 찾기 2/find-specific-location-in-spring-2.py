arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
c = input()

for i in range(0, len(arr)):
    if arr[i][2] == c or arr[i][3] == c:
        print(arr[i])
        cnt += 1

print(cnt)