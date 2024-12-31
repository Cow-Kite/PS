s = list(input())

while True:
    if len(s) == 1:
        break
    n = int(input())
    if n >= len(s):
        s.pop(-1)
    else:
        s.pop(n)
    print(''.join(s))