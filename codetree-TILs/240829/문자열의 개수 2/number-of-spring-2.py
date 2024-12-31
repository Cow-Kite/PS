string = []

while True:
    s = input()
    if s == '0':
        break
    string.append(s)

print(len(string))
for elem in string[1::2]:
    print(elem)