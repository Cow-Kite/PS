s = input()
arr = list(input())

for elem in arr:
    if elem == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)