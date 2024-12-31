arr = list(map(int, input().split()))

if arr[1] > arr[0] and arr[1] > arr[2]:
    print(1, end=" ")
else:
    print(0, end=" ")

if arr[0] == arr[1] == arr[2]:
    print(1, end=" ")
else:
    print(0, end=" ")