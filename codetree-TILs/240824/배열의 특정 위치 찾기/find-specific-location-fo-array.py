arr = list(map(int, input().split()))

hap = arr[1]+arr[3]+arr[5]+arr[7]+arr[9]
avg = (arr[2]+arr[5]+arr[8])/3

print(f'{hap} {avg:.1f}')