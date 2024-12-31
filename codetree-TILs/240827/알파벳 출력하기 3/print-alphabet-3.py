n = int(input())
alpha = 65
for i in range(0, n):
    for j in range(0, n-i):
        if alpha == 91:
            alpha = 65
        print(chr(alpha), end="")
        alpha += 1
    print()