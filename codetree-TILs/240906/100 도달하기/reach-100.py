n = int(input())
arr = [0, 0]
arr[0] = 1
arr[1] = n

i = 2
while True:
    num = arr[i-2] + arr[i-1]
    arr.append(num)
    if num > 100:
        break
    i += 1

print(' '.join(map(str, arr)))