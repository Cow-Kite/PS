n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        break
    if num % 3 == 0:
       print(num//3) 
    else:
        print(num+2)