n = int(input())
arr = list(input().split())

for elem in arr:
    if int(elem) % 2 == 0:
        print(elem, end=" ")