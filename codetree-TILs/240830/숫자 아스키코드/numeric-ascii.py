n = int(input())

for _ in range(n):
    s = input()
    if s.isalpha():
        print(s)
    else:
        print(ord(s))