str1 = list(input())
c = input()
cnt = 1 
for char in str1:
    if char == c:
        break
    cnt += 1
if cnt > len(str1):
    print('Not Found')
else:
    print(cnt)