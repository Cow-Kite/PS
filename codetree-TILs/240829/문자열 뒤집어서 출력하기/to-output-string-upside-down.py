string = []
for _ in range(4):
    string.append(input())

for elem in string[::-1]:
    print(elem[::-1])