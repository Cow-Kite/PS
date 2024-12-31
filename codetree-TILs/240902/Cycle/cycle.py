N, P = map(int, input().split())

dap = [N, ]
num = N

while True:
    num = (num*N)%P
    if num in dap:
        cycle = dap.index(num)
        break
    dap.append(num)

print(len(dap) - cycle)