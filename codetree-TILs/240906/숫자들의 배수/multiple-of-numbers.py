n = int(input())
arr = []
num = n
cnt = 0
while True:
    arr.append(num)
    if num % 5 == 0:
        cnt += 1
    if cnt == 2:
        break 
    num += n

print(" ".join(map(str, arr)))