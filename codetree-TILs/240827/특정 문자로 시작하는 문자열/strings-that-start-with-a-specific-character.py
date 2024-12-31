n = int(input())
cnt = 0
hap = 0

arr = [
    input()
    for _ in range(n)
]

c = input()

for elem in arr:
    if elem[0] == c:
        hap += len(elem)
        cnt += 1

print(f'{cnt} {hap/cnt:.2f}')