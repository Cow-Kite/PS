string = input()
for elem in string:
    if elem.isalnum():
        print(elem.lower(), end="")