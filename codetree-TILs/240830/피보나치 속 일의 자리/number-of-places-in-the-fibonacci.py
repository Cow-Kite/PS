n = int(input())
arr = list(map(int, input().split()))

for i in range(2, n):
    arr.append((arr[i-2]+arr[i-1])%10)

for elem in arr:
    print(elem, end=" ")