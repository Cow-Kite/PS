N = int(input())
number = sorted(list(map(int, input().split())))
count = 0

for i in range(N):
    num = number[i]
    left = 0
    right = N - 1

    while left < right:
        if left == i:
            left += 1
        elif right == i:
            right -= 1
        else:
            sum_value = number[left] + number[right]    

            if sum_value == num:
                count += 1
                break

            if sum_value > num:
                right -= 1
            else:
                left += 1

print(count)