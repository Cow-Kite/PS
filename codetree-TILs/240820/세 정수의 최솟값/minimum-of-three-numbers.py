# 변수 선언 및 입력
inp = input()
arr = inp.split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

# a가 가장 작은 경우
if a <= b and a <= c:
    print(a)
    
# b가 가장 작은 경우
elif b <= a and b <= c:
    print(b)

# c가 가장 작은 경우
else:
    print(c)