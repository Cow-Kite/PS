N = int(input())

liquid = list(map(int, input().split()))

number = float('inf')

left = 0
right = N - 1
num1 = 0
num2 = 0


while left < right:
    mix_value = liquid[left] + liquid[right]

    if abs(mix_value) < abs(number):
        number = mix_value
        num1 = liquid[left]
        num2 = liquid[right]

    if mix_value > 0:
        right -= 1
    else:
        left += 1

print(f"{num1} {num2}")