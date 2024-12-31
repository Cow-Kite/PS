str1 = input()
str2 = ""

for i in range(1, len(str1), 2):
    str2 += str1[i]

print(str2[-1::-1])