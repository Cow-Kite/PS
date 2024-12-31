arr = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    hap = 0
    for j in range(3):
        hap += arr[i][j]
    print(f'{hap/3:.1f}', end=" ")
print()

for i in range(3):
    hap = 0
    for j in range(3):
        hap += arr[j][i]
    print(f'{hap/3:.1f}', end=" ")

hap = 0
for i in range(3):
    for j in range(3):
        hap += arr[i][j]

print()
print(f'{hap/9:.1f}')