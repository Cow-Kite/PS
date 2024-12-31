s = input()

for i in range(len(s)):
    if s[i] == 'e':
        s = s[:i] + s[i+1:]
        break

print(s)