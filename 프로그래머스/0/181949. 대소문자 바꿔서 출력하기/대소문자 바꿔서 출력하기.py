str = input()

for elem in str:
    if elem.isupper():
        print(elem.lower(), end="")
    else:
        print(elem.upper(), end="")