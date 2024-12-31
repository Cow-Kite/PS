string = input()

for i in string:
    if i>='a' and i<='z':
        print(i.upper(), end="")
    elif i>='A' and i<='Z':
        print(i.lower(), end="")