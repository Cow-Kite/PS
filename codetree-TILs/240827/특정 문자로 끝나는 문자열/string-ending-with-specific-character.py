arr = [
    input()
    for _ in range(10)
]

c = input()
ni = False
for elem in arr:
    if elem[-1] == c:
        print(elem)
        ni = True

if ni == False:
    print("None")