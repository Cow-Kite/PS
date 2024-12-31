string = input()
hap = 0
for i in string:
    if i.isdigit():
        hap += int(i)

print(hap)