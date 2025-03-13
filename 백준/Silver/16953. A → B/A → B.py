from collections import deque

a, b = input().split()

queue = deque([(a, 0)])

while queue:
    num, count = queue.popleft() # num은 문자열, count는 int형
    if num == b:
        print(count+1)
        exit()

    if int(num) > int(b):
        continue 
    
    queue.append((str(int(num)*2), count+1))
    queue.append((num+"1", count+1))

print(-1)