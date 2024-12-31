arr = input().split(" ")

if len(arr[0]) > len(arr[1]):
    print(f'{arr[0]} {len(arr[0])}')
elif len(arr[0]) < len(arr[1]):
    print(f'{arr[1]} {len(arr[1])}')
else:
    print('same')