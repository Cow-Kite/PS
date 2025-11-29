y = int(input())

# 4의 배수이면서 100의 배수가 아닐 때
if y%4==0 and y%100!=0:
    print(1)
elif y%400==0:
    print(1)
else:
    print(0)