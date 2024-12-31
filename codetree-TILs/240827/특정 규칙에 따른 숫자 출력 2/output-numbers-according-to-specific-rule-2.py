n = int(input())
cnt = 9

for i in range(0, n):
    for j in range(0, n):
        if cnt == -1:
            cnt = 9
        print(cnt, end=" ")
        cnt -= 2
    print()