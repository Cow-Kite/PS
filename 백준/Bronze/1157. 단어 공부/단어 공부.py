line = input()
line = line.upper()

arr = [0] * 26
for i in line:
    arr[ord(i)-65] += 1

max_num = max(arr)
cnt = 0
for num in arr:
    if num == max_num:
        cnt +=1

if cnt > 1:
    print('?')
else:
    print(chr(arr.index(max_num)+65))