input_string = input()
new_string =""
for char in input_string:
    if char.isalpha():
        new_string += char.lower()

print(new_string)