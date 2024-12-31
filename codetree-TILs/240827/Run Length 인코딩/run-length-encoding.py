str1 = input()

c = str1[0]
cnt = 0
str2 = ""
for i in str1:
    if i == c:
        cnt += 1
    else:
        str2+=c
        str2+=str(cnt)
        c = i
        cnt = 1
str2+=c
str2+=str(cnt)
print(len(str2))
print(str2)