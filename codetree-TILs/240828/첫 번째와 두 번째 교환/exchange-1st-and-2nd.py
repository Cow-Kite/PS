str1 = list(input())
first = str1[0]
second = str1[1]

for i in range(0, len(str1)):
    if str1[i] == first:
        str1[i] = second
    elif str1[i] == second:
        str1[i] = first

print(''.join(str1))