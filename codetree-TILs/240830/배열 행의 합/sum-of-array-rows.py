arr = []

for _ in range(5):
    arr.append(list(map(int, input().split())))

for i in range(5):
    hap = 0
    for j in arr[i]:
        hap += j
    print(hap)