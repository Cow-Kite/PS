a, b = input().split()

if len(a) > len(b):
    print(b, len(b))
elif len(b) > len(a):
    print(a, len(a))
elif len(a)==len(b):
    print('equal')