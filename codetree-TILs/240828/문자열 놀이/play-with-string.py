s, q  = input().split()
s = list(s)

for i in range(int(q)):
    a, b, c = input().split()
    if int(a) == 1:
        b = int(b)
        c = int(c)
        temp = s[b-1]
        s[b-1] = s[c-1]
        s[c-1] = temp
    else:
        for j in range(0, len(s)):
            if s[j] == b:
                s[j] = c
    print(''.join(s))