n = int(input())

for i in range(0, n):
    cnt1 = 2*(n-1) - 2*i
    cnt2 = 2*i + 1
    print('  '*cnt1, end="")
    print('* '*cnt2, end=" ")
    print()