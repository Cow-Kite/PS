for _ in range(1, 11):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    diag1 = 0
    diag2 = 0

    for i in range(100):
        row_sum = sum(arr[i])
        col_sum = sum(arr[j][i] for j in range(100))

        max_sum = max(max_sum, row_sum, col_sum)

        diag1 += arr[i][i]
        diag2 += arr[i][99 - i]

    max_sum = max(max_sum, diag1, diag2) 

    print(f'#{num} {max_sum}')