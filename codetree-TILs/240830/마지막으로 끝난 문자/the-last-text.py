n = int(input())
string = []
for _ in range(n):
    string.append(input())

A = input()
dap = []

for elem in string:
    if elem.endswith(A):
        dap.append(elem)

print(len(dap))
for elem in dap:
    print(elem)