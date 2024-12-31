a, b = input().split()
new_a = ""
new_b = ""
for i in a:
    if not i.isdigit():
        break
    new_a += i

for i in b:
    if not i.isdigit():
        break
    new_b += i

print(int(new_a)+int(new_b))