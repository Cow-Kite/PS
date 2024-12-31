n = int(input())

arr = input().split()
str1 = ""
for elem in arr:
    str1 += elem


for i in range(0, len(str1)):
    if i != 0 and i % 5 == 0:
        print()
    print(str1[i], end="")