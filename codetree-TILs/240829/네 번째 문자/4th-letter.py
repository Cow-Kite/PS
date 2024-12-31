n, c = input().split()
cnt = 0
dap = []
for _ in range(int(n)):
    s = input()
    if s[3] == c:
        cnt+=1
        dap.append(s)

print(cnt)
for elem in dap:
    print(elem)