sex = int(input())
age = int(input())

if sex == 0:
    print('M') if age >= 19 else print('B')
else:
    print('W') if age >= 19 else print('G')