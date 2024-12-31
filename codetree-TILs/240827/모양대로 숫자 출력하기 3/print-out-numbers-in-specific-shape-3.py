n = int(input())

for i in range(0, n):
    print("  "*i, end="")
    for j in range(1, n+1-i):
        print(j, end=" ")
    print()