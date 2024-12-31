a = input()
b = input()
new_a = ""
new_b = ""
for i in a:
    if i.isdigit():
        new_a += i

for i in b:
    if i.isdigit():
        new_b += i

print(int(new_a) + int(new_b))