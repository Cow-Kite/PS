n = int(input())
cnt = 2
for i in range(0, n):
    print("  "*i, end="")
    for j in range(1, n+1-i):
        print(cnt, end=" ")
        if cnt == 8:
            cnt = 2
        else:
            cnt += 2
    print()