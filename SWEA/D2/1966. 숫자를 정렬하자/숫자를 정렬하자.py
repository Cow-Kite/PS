T = int(input())

for num in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    print(f'#{num}', *arr)