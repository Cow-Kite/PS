N, X = map(int, input().split())
arr = list(map(int, input().split()))

current_sum = sum(arr[:X])
max_sum = current_sum
count = 1

for i in range(X, N):
    current_sum += arr[i] - arr[i-X]

    if current_sum > max_sum:
        max_sum = current_sum
        count = 1
    elif current_sum == max_sum:
        count += 1

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(count)