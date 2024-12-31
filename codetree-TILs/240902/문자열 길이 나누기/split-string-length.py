n = int(input())
string = ""
for _ in range(n):
    str1 = input()
    string += str1

print(string[:len(string)//2])
print(string[len(string)//2:])