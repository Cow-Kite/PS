n = int(input())

for i in range(1, n+1):
    print('@ '*i)

for i in range(0, n):
    print("  "*(i+1), end="")
    for j in range(n-1-i, 0, -1):
        print("@ ", end="")
    print()