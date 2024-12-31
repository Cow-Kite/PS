arr = []
while True:
    string = input()
    if string == '0':
        break
    arr.append(string)

print(len(arr))

for i in range(0, len(arr), 2):
    print(arr[i])