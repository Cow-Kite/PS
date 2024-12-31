string, n = input().split()
string = list(string)
n = int(n)

for _ in range(n):
    num = int(input())
    if num <= len(string):
        string.pop(num-1)
        print(''.join(string))