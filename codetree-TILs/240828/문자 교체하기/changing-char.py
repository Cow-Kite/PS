arr = input().split()

str0 = list(arr[0])
str1 = list(arr[1])

str1[:2] = str0[:2]
print("".join(str1))