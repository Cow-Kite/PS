n = int(input())
arr = list(map(int, input().split()))
ban = list(map(int, input().split()))
hap = arr[ban[0]-1] + arr[ban[1]-1]
print(f'{hap/2:.1f}')