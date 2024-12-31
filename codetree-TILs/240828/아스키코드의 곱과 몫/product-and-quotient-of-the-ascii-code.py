a, b = input().split()

a = ord(a)
b = ord(b)

gob = a*b
na = a % b if b < a else b % a

print(gob, na)