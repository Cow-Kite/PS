num1, tem1 = input().split(" ")
num2, tem2 = input().split(" ")
num3, tem3 = input().split(" ")

count = 0

if num1 == 'Y' and int(tem1) >= 37:
    count += 1
if num2 == 'Y' and int(tem2) >= 37:
    count += 1
if num3 == 'Y' and int(tem3) >= 37:
    count += 1

if count >=2:
    print('E')
else:
    print('N')