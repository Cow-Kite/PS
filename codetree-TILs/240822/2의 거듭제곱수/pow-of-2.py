N = int(input())

x = 1

while True:
    if N == 2 ** x:
        print(x)
        break
    x += 1