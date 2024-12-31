arr1 = []
arr2 = []

for _ in range(4):
    arr1.append(list(map(int, input().split())))

input()

for _ in range(4):
    arr2.append(list(map(int, input().split())))

result = []
for i in range(4):
    result_row = []
    for j in range(2):
        result_row.append(arr1[i][j] * arr2[i][j])
    result.append(result_row)

for row in result:
    print(' '.join(map(str, row)))